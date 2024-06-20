from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from resources.coach import CoachResource
from resources.player import PlayerResource
from resources.teams import TeamResource

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

# Ajouter les ressources à l'API
api.add_resource(CoachResource, '/coaches/<int:id>', '/coaches')
api.add_resource(PlayerResource, '/players/<int:id>', '/players')
api.add_resource(TeamResource, '/teams/<int:id>', '/teams')

if __name__ == '__main__':
    from models.coach import Coach
    from models.player import Player
    from models.teams import Team

    with app.app_context():
        db.create_all()
    app.run(debug=True)
