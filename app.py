from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from security.auth import authenticate, identity
from resources.coach import CoachResource
from resources.player import PlayerResource
from resources.teams import TeamResource

app = Flask(__name__)
app.config.from_object('config.Config')

api = Api(app)
jwt = JWTManager(app)

# Add resources to the API
api.add_resource(CoachResource, '/coaches/<int:id>', '/coaches')
api.add_resource(PlayerResource, '/players/<int:id>', '/players')
api.add_resource(TeamResource, '/teams/<int:id>', '/teams')

if __name__ == '__main__':
    app.run(debug=True)
