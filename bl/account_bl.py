from exceptoins.exceptoins import Accountnotfound
from model.da.db  import DataAccess
from model.entity import  account

account_da = DataAccess(account)


class AccountBl:
    @staticmethod
    def save(account):
        return account_da.save(account)

    @staticmethod
    def edit(account):
        if account_da.find_by_account_id(account.account_id):
            return account_da.edit(account)
        else:
            raise Accountnotfound()

    @staticmethod
    def remove(account_id):
        customer = account_da.find_by_account_id(account_id)
        if customer:
            return account_da.remove(account)
        else:
            raise Accountnotfound()

    @staticmethod
    def find_all():
        account_list = account_da.find_all()
        if account_list:
            return account_list
        else:
            raise Accountnotfound()

    @staticmethod
    def find_by_id(account_id):
        customer = account_da.find_by_account_id(account_id)
        if customer:
            return customer
        else:
            raise Accountnotfound()

