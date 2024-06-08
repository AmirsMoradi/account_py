from exceptoins.exceptoins import DuplicateUsernameError
from model.entity import *


class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    card_number = Column(Integer, nullable=False)
    national_code = Column(String(10), nullable=False)
    role = Column(String(20), nullable=True)

    def __init__(self, name, family, card_number, national_code, user_name, password, role="customer"):
        self.id = None
        self.name = name
        self.family = family
        self.card_number = card_number
        self.national_code = national_code
        self.user_name = user_name
        self.password = password
        self.role = role

    @property
    def Name(self):
        return self.name

    @Name.setter
    def Name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self.name = value

    @property
    def Family(self):
        return self.name

    @Family.setter
    def Family(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self.name = value

    @classmethod
    def find_by_username(cls, username):
        pass


    