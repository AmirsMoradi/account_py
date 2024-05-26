from model.entity import *

class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    national_code = Column(String(10), nullable=False)
    email = Column(String(20), nullable=False)

    def __init__(self, name, family, email, national_code, user_name, password):
        self.name = name
        self.family = family
        self.email = email
        self.national_code = national_code
        self.user_name = user_name
        self.password = password
