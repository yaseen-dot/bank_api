from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from ..models.user import User
from ..db import db
from ..utils.error_handlers import conflict, unauthorized, not_found

class AuthService:

    @staticmethod
    def register(data):
        if User.query.filter_by(username=data["username"]).first():
            conflict("Username already exists")

        hashed_pw = generate_password_hash(data["password"])
        user = User(username=data["username"], password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login(data):
        user = User.query.filter_by(username=data["username"]).first()
        if user and check_password_hash(user.password, data["password"]):
            access_token = create_access_token(identity=str(user.id))
            return access_token
        unauthorized("Invalid credentials")

    @staticmethod
    def get_user(user_id):
        user = User.query.get(user_id)
        if not user:
            not_found("User not found")
        return user
