from model.entity import *


class Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    card_number = Column(Integer, nullable=False)
    national_code = Column(String(10), nullable=False)




    def __init__(self, id, name, family, card_number,national_code):
        self.id = None
        self.name = name
        self.family = family
        self.card_number = card_number
        self.national_code = national_code
