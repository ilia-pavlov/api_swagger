"""
RUN FLASK UP by CALEB CURRY

pwd
python3 -m venv .venv
source .venv/bin/activate
pip3 install flask
pip3 install flask-sqlalchemy

pip3 freeze > requirements.txt
touch application.py
export FLASK_APP=application.py
export FLASK_ENV=development
flask run

"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'
