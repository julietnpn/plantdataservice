# Import SQLAlchemy packages
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Initialize a declarative base class.
Base = declarative_base()


class Plant(Base):
    """Define the plan database model."""
    __tablename__ = 'plant'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), index=True, nullable=False)

    def __str__(self):
        return "{}".format(self.url)

    def __repr__(self):
        return '<Plant {}>'.format(self.__str__())
