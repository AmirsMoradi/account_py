from model.entity import *
from model.validator.validator import Validator


class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _national_code = Column("national_code", String(10), nullable=False)
    email = Column(String(20), nullable=False)
    role = Column(String(10), nullable=True)

    def __init__(self, name, family, email, national_code, user_name, password, role="admin"):
        self.name = name
        self.family = family
        self.email = email
        self.national_code = national_code
        self.user_name = user_name
        self.password = password
        self.role = role


@property
def name(self):
    return self._name


@name.setter
def name(self, name):
    self._name = Validator.name_validator(name, "Invalid Name")


@property
def family(self):
    return self._family


@family.setter
def family(self, family):
    self._family = Validator.family_validator(family, "Invalid Family")


@property
def national_code(self):
    return self._national_code


@national_code.setter
def national_code(self, national_code):
    self._national_code = Validator.national_validator(national_code, "invalid national code")
