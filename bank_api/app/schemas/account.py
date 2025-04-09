from marshmallow import Schema, fields


class DepositSchema(Schema):
    amount = fields.Float(required=True)


class WithdrawSchema(Schema):
    amount = fields.Float(required=True)


class TransferSchema(Schema):
    username = fields.String(required=True)
    amount = fields.Float(required=True)


class AccountSchema(Schema):
    id = fields.Int()
    balance = fields.Float()
