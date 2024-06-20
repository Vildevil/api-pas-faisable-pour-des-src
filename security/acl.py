from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from models.coach import coaches

def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            user_id = get_jwt_identity()
            user = next((coach for coach in coaches if coach.id == user_id), None)
            if user and user.role == role:
                return fn(*args, **kwargs)
            return jsonify({"message": "Access forbidden"}), 403
        return decorator
    return wrapper
