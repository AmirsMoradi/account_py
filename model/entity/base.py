from sqlalchemy.orm import DaclarativeBase


class Base(DaclarativeBase):
    def __repr__(self):
        return str({c.name: getattr(self, c.name) for c in self.__table__.columns})