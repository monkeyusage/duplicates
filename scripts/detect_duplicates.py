import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from typing import List

engine = create_engine('sqlite:///../data/data.db', echo=False)
con = engine.connect()
df = pd.read_sql('select * from patient', con=con)
con.close()

def detect_duplicates(df:pd.DataFrame) -> pd.DataFrame:
    # remove the patients with duplicated id
    df = df[~df.patient_id.duplicated()]
    # remove the patients with null names
    df['name'] = df['given_name'] + ' ' + df['surname']
    df = df[~df.name.isnull()]
    
    
    # Using phone number to detect duplicates
    # first remove the rows with phone numbers being None
    df = df.dropna(subset=["phone_number"])
    # then remove patient ids corresponding to duplicated phone numbers
    df = df[~df.patient_id.isin(set(df[df.phone_number.duplicated()].patient_id.values))]
    
    def rm_gb(cols:List[str], data:pd.DataFrame) -> pd.DataFrame:
        '''groups by columns and removes rows where groupby count resulted in more than 1 example
        
        if there are more than 1 occurences of "name" == "Gerard" and "state"=="nsw" then 
        rm_gb(['name', 'state']) => should remove it
        '''
        gb_cols = data.groupby(cols).count()
        gb_cols = gb_cols[gb_cols.patient_id > 1].reset_index()
        dup = data[data[cols[0]].isin(gb_cols[cols[0]])]
        for col in cols[1:]:
            dup = dup[df[col].isin(gb_cols[col])]
        data = data[~data.patient_id.isin(dup[dup.name.duplicated()].patient_id.values)]
        return data
    
    df = rm_gb(['name', 'postcode'], df)
    df = rm_gb(['name', 'address_1'], df)
    df = rm_gb(['name', 'suburb'], df)
    return df

df = detect_duplicates(df)