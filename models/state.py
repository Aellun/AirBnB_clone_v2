#!/usr/bin/python3
""" State Module for HBNB project"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """class State
    Attributes:
        name(str): state name
        cities (relationship): r/ship with the City class
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Getter method to retrieve cities related to the state.
        Returns:
            list_city: List of City objs related to state.
        """
        var = models.storage.all()
        list_city = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_city.append(var[key])
        for city in list_city:
            if (city.state_id == self.id):
                result.append(city)
        return (result)
