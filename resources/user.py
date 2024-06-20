
from flask_jwt_extended import create_access_token
from models.coach import coaches
from flask_restful import Resource, reqparse

sec_password = "password"

def authenticate(username, password):
    user = next((coach for coach in coaches if coach.username == username), None)
    if user and password == sec_password:  # Simplified authentication
        return create_access_token(identity=user.id)


class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        args = parser.parse_args()

        # if verify_user(args['username'], args['password']):
        #     session['username'] = args['username']
        #     return {'message': 'Logged in successfully'}, 200
        # else:
        #     return {'message': 'Invalid credentials'}, 401

        return authenticate(args["username"], args["password"])

# Définition de l'endpoint /login
