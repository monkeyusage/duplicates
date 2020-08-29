cd ..
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
curl https://raw.githubusercontent.com/agramfort/inria-aphp-assignment/master/data.db --output data.db