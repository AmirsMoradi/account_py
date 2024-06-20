from model.entity import *
from model.validator.validator import Validator


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
        self._name = Validator.name_validator( name , "Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validator.family_validator( family , "Invalid Family")


    @property
    def card_number(self):
       return self._card_number

    @card_number.setter
    def card_number(self, card_number):
            self._card_number = Validator.card_number_validator( card_number , "Invalid Card Number")

    @property
    def national_code(self):
        return self._national_code

    @national_code.setter
    def national_code(self, national_code):
        self._national_code = Validator.national_validator(national_code,"invalid national code")

    