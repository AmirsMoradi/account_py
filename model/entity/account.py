from model.entity import *

class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    card_number = Column(Integer, nullable=False)

    person_id = Column(Integer, ForeignKey("customer.id"))
    person = relationship("Customer")

    def __init__(self, id, name, family, card_number):
        self.id = None
        self.name = name
        self.family = family
        self.card_number = card_number