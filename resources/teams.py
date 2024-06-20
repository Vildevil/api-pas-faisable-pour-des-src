from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.teams import Team, teams

class TeamResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank')

    @jwt_required()
    def get(self, team_id):
        team = next((team for team in teams if team.id == team_id), None)
        if team:
            return team.__dict__, 200
        return {'message': 'Team not found'}, 404

    @jwt_required()
    def put(self, team_id):
        data = TeamResource.parser.parse_args()
        team = next((team for team in teams if team.id == team_id), None)
        if team:
            team.name = data['name']
            return {'message': 'Team updated', 'team': {'id': team.id, 'name': team.name}}, 200
        return {'message': 'Team not found'}, 404

    @jwt_required()
    def delete(self, team_id):
        global teams
        teams = [team for team in teams if team.id != team_id]
        return {'message': 'Team deleted'}, 200

class TeamListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
    parser.add_argument('coach_id', type=str, required=True, help='Name cannot be blank')
    parser.add_argument('players_id', action='append')


    @jwt_required()
    def get(self):
        return {'teams': [team.__dict__ for team in teams]}, 200

    @jwt_required()
    def post(self):
        data = TeamListResource.parser.parse_args()
        team_id = len(teams) + 1
        team = Team(id=team_id, name=data['name'], coach_id=data["coach_id"], players_id=data["players_id"])
        teams.append(team)
        return {'message': 'Team created', 'team': {'id': team.id, 'name': team.name}}, 201
