
def identity(payload):
    user_id = payload['identity']
    return next((coach for coach in coaches if coach.id == user_id), None)
