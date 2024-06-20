from flask_jwt_extended import get_jwt_identity
from models.coach import coaches

def get_user_role():
    user_id = get_jwt_identity()
    user = next((coach for coach in coaches if coach.id == user_id), None)
    if user:
        return 'coach'  # Simplified role management
    return None
