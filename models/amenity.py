#!/usr/bin/python3
"""This is the amenity class module"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Class represention of Amenity class.
    Attributes:
        name (str):amenity Name.
        place_amenities (relationship): r/ship with the Place class
            through the place_amenity related table.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
