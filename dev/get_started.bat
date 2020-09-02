cd ..
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
curl "https://raw.githubusercontent.com/agramfort/inria-aphp-assignment/master/data.db" -o data/data.db
cd tests
python -m pytest test.py
cd ..
