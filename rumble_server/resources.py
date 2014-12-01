from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from api import rumble as server


class User(Resource):
    def post(self):
        parser = RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('handle', type=str, required=True)
        args = parser.parse_args()
        server.register(**args)