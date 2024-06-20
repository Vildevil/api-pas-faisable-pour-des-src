from resources.coach import CoachResource, CoachListResource
from resources.player import PlayerResource, PlayerListResource
from resources.teams import TeamResource, TeamListResource
from resources.user import UserLogin
from resources.match import MatchResource, MatchListResource

def initialize_routes(api):
    # Teams routes
    api.add_resource(TeamListResource, '/api/teams')
    api.add_resource(TeamResource, '/api/teams/<int:team_id>')
    
    # Players routes
    api.add_resource(PlayerListResource, '/api/players')
    api.add_resource(PlayerResource, '/api/players/<int:player_id>')
    
    # Coaches routes
    api.add_resource(CoachListResource, '/api/coaches')
    api.add_resource(CoachResource, '/api/coaches/<int:coach_id>')


    #Matches routes
    api.add_resource(MatchListResource, '/api/matches')
    api.add_resource(MatchResource, '/api/matches/<int:match_id>')
    # Login
    api.add_resource(UserLogin, '/login')