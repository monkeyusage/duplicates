cd ..
virtualenv venv --python=python3.7
source venv\bin\activate
pip install -r requirements.txt
curl https://raw.githubusercontent.com/agramfort/inria-aphp-assignment/master/data.db --output data.db