from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from models.user import User

def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = User.find_by_id(user_id)
            if user and user.role == role:
                return fn(*args, **kwargs)
            else:
                return {'message': 'Access forbidden'}, 403
        return decorator
    return wrapper
