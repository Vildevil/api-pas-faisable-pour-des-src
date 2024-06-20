from flask_jwt_extended import create_access_token
from models.coach import coaches

def authenticate(username, password):
    user = next((coach for coach in coaches if coach.name == username), None)
    if user and password == "password":  # Simplified authentication
        return create_access_token(identity=user.id)

def identity(payload):
    user_id = payload['identity']
    return next((coach for coach in coaches if coach.id == user_id), None)
