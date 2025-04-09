from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_smorest import Blueprint
from ..schemas.account import DepositSchema, WithdrawSchema, TransferSchema, AccountSchema
from ..services.account_service import AccountService

blp = Blueprint("Account", "account", url_prefix="/account", description="Bank Account Operations")

@blp.route("/deposit")
class Deposit(MethodView):
    @jwt_required()
    @blp.arguments(DepositSchema)
    @blp.response(200, AccountSchema)
    def post(self, data):
        user_id = int(get_jwt_identity())
        account = AccountService.deposit(user_id, data["amount"])
        return account

@blp.route("/withdraw")
class Withdraw(MethodView):
    @jwt_required()
    @blp.arguments(WithdrawSchema)
    @blp.response(200, AccountSchema)
    def post(self, data):
        user_id = int(get_jwt_identity())
        account = AccountService.withdraw(user_id, data["amount"])
        return account

@blp.route("/transfer")
class Transfer(MethodView):
    @jwt_required()
    @blp.arguments(TransferSchema)
    @blp.response(200)
    def post(self, data):
        user_id = int(get_jwt_identity())
        result = AccountService.transfer(user_id, data["username"], data["amount"])
        return result
