from model.entity import *


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column("name",String(20), nullable=False)
    _family = Column("family",String(20), nullable=False)
    _card_number = Column("card_number",Integer, nullable=False)

    customer_id = Column(Integer, ForeignKey("customer.customer_id"))
    customer = relationship("Customer")

    def __init__(self, name, family, card_number):
        self.id = None
        self.name = name
        self.family = family
        self.card_number = card_number
