#!/usr/bin/python3
"""City Module for HBNB project"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


Base = declarative_base()


class City(BaseModel, Base):
    """the class city
    Attributes:
        state_id (str): The state id
        name (str): City name
        places (relationship): Relationship with the Place class
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
