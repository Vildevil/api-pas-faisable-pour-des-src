from flask_restful import Resource, reqparse
from models.teams import Team

class TeamResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank')

    def get(self, id):
        team = Team.query.get(id)
        if not team:
            return {'message': 'Team not found'}, 404
        return team.json()

    def post(self):
        data = TeamResource.parser.parse_args()
        team = Team(**data)
        team.save_to_db()
        return team.json(), 201

    def put(self, id):
        data = TeamResource.parser.parse_args()
        team = Team.query.get(id)
        if team:
            team.name = data['name']
        else:
            team = Team(id=id, **data)
        team.save_to_db()
        return team.json()

    def delete(self, id):
        team = Team.query.get(id)
        if team:
            team.delete_from_db()
        return {'message': 'Team deleted'}
