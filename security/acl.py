from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from models.user import User

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.find_by_id(user_id)
        if user and user.is_admin():
            return fn(*args, **kwargs)
        return {'message': 'Admins only!'}, 403
    return wrapper
