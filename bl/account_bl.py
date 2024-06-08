from exceptoins.exceptoins import AccountNotFoundError
from model.da.db import *
from model.entity import account, Transaction

account_da = DataAccess(account)
transaction_da = DataAccess(Transaction)


class AccountBl:
    @staticmethod
    def save(account):
        return account_da.save(account)

    @staticmethod
    def edit(account):
        if account_da.find_by_id(account.account_id):
            return account_da.edit(account)
        else:
            raise AccountNotFoundError()

    @staticmethod
    def remove(account_id):
        customer = account_da.find_by_account_id(account_id)
        if customer:
            return account_da.remove(account)
        else:
            raise AccountNotFoundError()

    @staticmethod
    def find_all():
        account_list = account_da.find_all()
        if account_list:
            return account_list
        else:
            raise AccountNotFoundError()

    @staticmethod
    def find_by_id(account_id):
        customer = account_da.find_by_id(account_id)
        if customer:
            return customer
        else:
            raise AccountNotFoundError()

    @staticmethod
    def find_all_transactions_by_account_id(account_id):
        transactions = transaction_da.find_by(
            or_(Transaction.sender_id == account_id, Transaction.receiver_id == account_id))

    @staticmethod
    def find_by_sender_id(account_id):
        transactions = transaction_da.find_by(
            (Transaction.sender_id == account_id))

    @staticmethod
    def find_by_receiver_id(account_id):
        transactions = transaction_da.find_by(
            (Transaction.receiver_id == account_id))






