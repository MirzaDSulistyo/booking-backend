# main script to start the server
from flask import Flask, request, json
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

ENV = 'dev'

if ENV == 'dev' :
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/bookingbackend'
else :
	app.debug = False
	app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return UserModel.RevokedToken.is_jti_blacklisted(jti)

from resources import index
from resources import users
from models import user as UserModel

api.add_resource(index.Index, '/')

api.add_resource(users.UserRegistration, '/registration')
api.add_resource(users.UserLogin, '/login')
api.add_resource(users.UserLogoutAccess, '/logout/access')
api.add_resource(users.UserLogoutRefresh, '/logout/refresh')
api.add_resource(users.TokenRefresh, '/token/refresh')
api.add_resource(users.AllUsers, '/users')
api.add_resource(users.SecretResource, '/secret')

if __name__ == "__main__":
    app.run()