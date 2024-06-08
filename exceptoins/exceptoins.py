class CustomerNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Customer not found")


class AccountNotFoundError(Exception):
    def __init__(self):
        Exception.__init__(self, "Account not found")


class Trancaction(Exception):
    def __init__(self):
        Exception.__init__(self, "Trancaction not found")
