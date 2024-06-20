from exceptoins.exceptoins import DuplicateUsernameError
from model.entity import *


class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name",String(20), nullable=False)
    _family = Column("family",String(20), nullable=False)
    _card_number = Column("card_number",Integer, nullable=False)
    _national_code = Column("national_code",String(10), nullable=False)
    role = Column(String(20), nullable=True)

    def __init__(self, name, family, card_number, national_code, user_name, password, role="customer"):
        self.customer_id = None
        self.name = name
        self.family = family
        self.card_number = card_number
        self.national_code = national_code
        self.user_name = user_name
        self.password = password
        self.role = role

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if not isinstance(family, str):
            raise ValueError("Name must be a string")
        self._family = family


    @property
    def card_number(self):
        return self._card_number

    