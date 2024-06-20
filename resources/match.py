from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.match import Match, matches


class MatchResource(Resource):

    @jwt_required()
    def get(self, match_id):
        match = next((match for match in matches if id == match.id), None)
        
        if match: return match.__dict__

        return {'message': 'Match not found'}, 404
    
    @jwt_required()
    def delete(self, match_id):
        global matches
        matches = [player for player in matches if player.id != match_id]
        return {'message': 'Match deleted'}, 200


class MatchListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('team_a', type=int, required=True, help='Team ID cannot be blank')
    parser.add_argument('team_b', type=int, required=True, help='Team ID cannot be blank')
    parser.add_argument("score_a", type=int)
    parser.add_argument("score_b", type=int)

    @jwt_required()
    def get(self):
        return {'matches': [match.__dict__ for match in matches]}, 200

    @jwt_required()
    def post(self):
        data = MatchListResource.parser.parse_args()
        match_id = len(matches) + 1
        match = Match(
            id=match_id, 
            teams_a=data["team_a"], 
            teams_b=data["team_b"],
            score_a=data["score_a"],
            score_b=data["score_b"]
        )
        matches.append(match)
        return match.__dict__, 201
