from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..schemas.user import UserRegisterSchema, UserLoginSchema, UserOutSchema
from ..services.auth_service import AuthService
from ..utils.response import success_response

blp = Blueprint("Auth", "auth", url_prefix="/auth", description="Authentication")

@blp.route("/register")
class Register(MethodView):
    @blp.arguments(UserRegisterSchema)
    @blp.response(201, UserOutSchema)
    def post(self, data):
        user = AuthService.register(data)
        return user

@blp.route("/login")
class Login(MethodView):
    @blp.arguments(UserLoginSchema)
    def post(self, data):
        token = AuthService.login(data)
        return success_response("Login successful", {"access_token": token})

@blp.route("/me")
class Me(MethodView):
    @jwt_required()
    @blp.response(200, UserOutSchema)
    def get(self):
        current_user_id = int(get_jwt_identity())
        user = AuthService.get_user(current_user_id)
        return user
