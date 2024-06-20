from flask_restful import Resource, reqparse
from models.coach import Coach

class CoachResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
    parser.add_argument('team_id', type=int, required=True, help='Team ID cannot be blank')

    def get(self, id):
        coach = Coach.query.get(id)
        if not coach:
            return {'message': 'Coach not found'}, 404
        return coach.json()

    def post(self):
        data = CoachResource.parser.parse_args()
        coach = Coach(**data)
        coach.save_to_db()
        return coach.json(), 201

    def put(self, id):
        data = CoachResource.parser.parse_args()
        coach = Coach.query.get(id)
        if coach:
            coach.name = data['name']
            coach.team_id = data['team_id']
        else:
            coach = Coach(id=id, **data)
        coach.save_to_db()
        return coach.json()

    def delete(self, id):
        coach = Coach.query.get(id)
        if coach:
            coach.delete_from_db()
        return {'message': 'Coach deleted'}
