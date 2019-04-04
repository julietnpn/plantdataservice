# Import SQLAlchemy packages
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Initialize a declarative base class.
Base = declarative_base()


class Plant(Base):
    """Define the plan database model."""
    __tablename__ = 'plant'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), index=True, nullable=False)

    family_id = Column(Integer, ForeignKey('family.id'), nullable=False, index=True)
    family = relationship('Family')

    genus_id = Column(Integer, ForeignKey('genus.id'), nullable=False, index=True)
    genus = relationship('Genus')

    species_id = Column(Integer, ForeignKey('species.id'), nullable=False, index=True)
    species = relationship('Species')

    def __str__(self):
        return "{}".format(self.url)

    def __repr__(self):
        return '<Plant {}>'.format(self.__str__())


class Family(Base):
    """Define the family database model."""
    __tablename__ = 'family'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), index=True)

    def __str__(self):
        return "{}".format(self.url)

    def __repr__(self):
        return '<Family {}>'.format(self.__str__())


class Genus(Base):
    """Define the genus database model."""
    __tablename__ = 'genus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), index=True)

    def __str__(self):
        return "{}".format(self.url)

    def __repr__(self):
        return '<Genus {}>'.format(self.__str__())


class Species(Base):
    """Define the species database model."""
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), index=True)

    def __str__(self):
        return "{}".format(self.url)

    def __repr__(self):
        return '<Species {}>'.format(self.__str__())
