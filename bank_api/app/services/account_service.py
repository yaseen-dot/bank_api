from ..models.account import BankAccount
from ..models.user import User
from ..db import db
from ..utils.error_handlers import not_found, bad_request

class AccountService:

    @staticmethod
    def get_or_create_account(user_id):
        account = BankAccount.query.filter_by(user_id=user_id).first()
        if not account:
            account = BankAccount(user_id=user_id, balance=0.0)
            db.session.add(account)
            db.session.commit()
        return account

    @staticmethod
    def deposit(user_id, amount):
        if amount <= 0:
            bad_request("Amount must be greater than 0")

        account = AccountService.get_or_create_account(user_id)
        account.balance += amount
        db.session.commit()
        return account

    @staticmethod
    def withdraw(user_id, amount):
        if amount <= 0:
            bad_request("Amount must be greater than 0")

        account = AccountService.get_or_create_account(user_id)

        if account.balance < amount:
            bad_request("Insufficient funds")

        account.balance -= amount
        db.session.commit()
        return account

    @staticmethod
    def transfer(from_user_id, to_username, amount):
        if amount <= 0:
            bad_request("Amount must be greater than 0")

        sender = AccountService.get_or_create_account(from_user_id)

        if sender.balance < amount:
            bad_request("Insufficient funds")

        receiver_user = User.query.filter_by(username=to_username).first()
        if not receiver_user:
            not_found("Receiver user not found")

        receiver = AccountService.get_or_create_account(receiver_user.id)

        # Process transaction
        sender.balance -= amount
        receiver.balance += amount
        db.session.commit()

        return {
            "from": sender.user.username,
            "to": receiver_user.username,
            "amount": amount,
            "sender_balance": sender.balance
        }
