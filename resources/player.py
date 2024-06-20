from flask_restful import Resource, reqparse
from models.player import Player

class PlayerResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
    parser.add_argument('team_id', type=int, required=True, help='Team ID cannot be blank')

    def get(self, id):
        player = Player.query.get(id)
        if not player:
            return {'message': 'Player not found'}, 404
        return player.json()

    def post(self):
        data = PlayerResource.parser.parse_args()
        player = Player(**data)
        player.save_to_db()
        return player.json(), 201

    def put(self, id):
        data = PlayerResource.parser.parse_args()
        player = Player.query.get(id)
        if player:
            player.name = data['name']
            player.team_id = data['team_id']
        else:
            player = Player(id=id, **data)
        player.save_to_db()
        return player.json()

    def delete(self, id):
        player = Player.query.get(id)
        if player:
            player.delete_from_db()
        return {'message': 'Player deleted'}
