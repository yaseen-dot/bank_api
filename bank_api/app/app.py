from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from .config import Config
from .db import db
from .routes.auth_routes import blp as AuthBlueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt = JWTManager(app)
    api = Api(app)

    api.register_blueprint(AuthBlueprint)

    return app
