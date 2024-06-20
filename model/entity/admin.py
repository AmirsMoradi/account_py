from model.entity import *

class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name",String(20), nullable=False)
    _family = Column("family",String(20), nullable=False)
    _national_code = Column("national_code",String(10), nullable=False)
    email = Column(String(20), nullable=False)
    role = Column(String(10), nullable=True)

    def __init__(self, name, family, email, national_code, user_name, password,role="admin"):
        self.name = name
        self.family = family
        self.email = email
        self.national_code = national_code
        self.user_name = user_name
        self.password = password
        self.role = role
