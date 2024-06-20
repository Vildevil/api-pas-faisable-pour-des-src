from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.player import Player, players

class PlayerResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
    parser.add_argument('team_id', type=int, required=True, help='Team ID cannot be blank')

    @jwt_required()
    def get(self, player_id):
        player = next((player for player in players if player.id == player_id), None)
        if player:
            return {'id': player.id, 'name': player.name, 'team_id': player.team_id}, 200
        return {'message': 'Player not found'}, 404

    @jwt_required()
    def put(self, player_id):
        data = PlayerResource.parser.parse_args()
        player = next((player for player in players if player.id == player_id), None)
        if player:
            player.name = data['name']
            player.team_id = data['team_id']
            return {'message': 'Player updated', 'player': {'id': player.id, 'name': player.name, 'team_id': player.team_id}}, 200
        return {'message': 'Player not found'}, 404

    @jwt_required()
    def delete(self, player_id):
        global players
        players = [player for player in players if player.id != player_id]
        return {'message': 'Player deleted'}, 200

class PlayerListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
    parser.add_argument('team_id', type=int, required=True, help='Team ID cannot be blank')

    @jwt_required()
    def get(self):
        return {'players': [{'id': player.id, 'name': player.name, 'team_id': player.team_id} for player in players]}, 200

    @jwt_required()
    def post(self):
        data = PlayerListResource.parser.parse_args()
        player_id = len(players) + 1
        player = Player(id=player_id, name=data['name'], team_id=data['team_id'])
        players.append(player)
        return {'message': 'Player created', 'player': {'id': player.id, 'name': player.name, 'team_id': player.team_id}}, 201
