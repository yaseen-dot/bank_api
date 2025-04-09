from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from .config import Config
from flask_migrate import Migrate
from .db import db
from .routes.auth_routes import blp as AuthBlueprint
from .routes.account_routes import blp as AccountBlueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    migrate = Migrate(app, db)

    db.init_app(app)
    jwt = JWTManager(app)
    api = Api(app)





    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(AccountBlueprint)

    return app
