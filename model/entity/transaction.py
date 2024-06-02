from sqlalchemy.orm import backref

from model.entity import *



class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    dateTime = Column(DateTime, nullable=False)
    transaction_type = Column(String(20), nullable=False)
    description = Column(String(20), nullable=False)

    sender_id = Column(Integer, ForeignKey("account.id"))
    sender = relationship("Account",foreign_keys=[sender_id])

    receiver_id = Column(Integer, ForeignKey("account.id"))
    receiver = relationship("Account",foreign_keys=[receiver_id])
    #todo -> problem with sender and reciver

    def __init__(self, id, card_number, transaction_type, description):
        self.id = id
        self.dateTime = None
        self.transaction_type = transaction_type
        self.card_number = card_number
        self.description = description

    def get_transaction_type(self):
        return self._transaction_type

    def set_transaction_type(self, transaction_type):
        if isinstance(transaction_type, str) and transaction_type.lower() in ("income", "outcome"):
            self._transaction_type = transaction_type.lower()
        elif isinstance(transaction_type, int) and transaction_type in (1, -1):
            self._transaction_type = "income" if transaction_type == 1 else "outcome"
        else:
            raise ValueError("invalid:transaction_type")
