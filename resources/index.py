# API endpoints
from flask import request, jsonify, json
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class Index(Resource):
    def get(self):
        return "Hello world!!"