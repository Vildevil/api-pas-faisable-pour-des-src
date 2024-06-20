from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from routes import initialize_routes

app = Flask(__name__)
app.config.from_object('config.Config')

api = Api(app)
jwt = JWTManager(app)

initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)