cd ..
virtualenv venv --python=python3.7
source venv\bin\activate
pip install -r requirements.txt
curl "https://raw.githubusercontent.com/agramfort/inria-aphp-assignment/master/data.db" -o data/data.db
curl "https://github.com/michalsn/australian-suburbs/blob/master/data/suburbs.csv" -o data/suburbs.csv