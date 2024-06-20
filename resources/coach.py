from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.coach import Coach, coaches

class CoachResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank')

    @jwt_required()
    def get(self, coach_id):
        coach = next((coach for coach in coaches if coach.id == coach_id), None)
        if coach:
            return {'id': coach.id, 'name': coach.name}, 200
        return {'message': 'Coach not found'}, 404

    @jwt_required()
    def put(self, coach_id):
        data = CoachResource.parser.parse_args()
        coach = next((coach for coach in coaches if coach.id == coach_id), None)
        if coach:
            coach.name = data['name']
            return {'message': 'Coach updated', 'coach': {'id': coach.id, 'name': coach.name}}, 200
        return {'message': 'Coach not found'}, 404

    @jwt_required()
    def delete(self, coach_id):
        global coaches
        coaches = [coach for coach in coaches if coach.id != coach_id]
        return {'message': 'Coach deleted'}, 200

class CoachListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank')

    @jwt_required()
    def get(self):
        return {'coaches': [{'id': coach.id, 'name': coach.name} for coach in coaches]}, 200

    @jwt_required()
    def post(self):
        data = CoachListResource.parser.parse_args()
        coach_id = len(coaches) + 1
        coach = Coach(id=coach_id, name=data['name'])
        coaches.append(coach)
        return {'message': 'Coach created', 'coach': {'id': coach.id, 'name': coach.name}}, 201
