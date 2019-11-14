$ mkdir booking-backend
$ cd booking-backend

$ virtualenv -p python3 venv

# following command will activate virtual environment on macOs/Linux
$ source venv/bin/activate

# on Windows run next 
# (see here https://virtualenv.pypa.io/en/stable/userguide/)
# \venv\Scripts\activate

(venv) pip install flask flask-restful flask-jwt-extended passlib flask-sqlalchemy

(venv) pip install pip install psycopg2-binary

(venv) FLASK_APP=app.py FLASK_DEBUG=1 flask run