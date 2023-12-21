#!/usr/bin/python3
"""This module define the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """user class representation
    Attributes:
        email (str):user Email address
        password (str):user Password
        first_name (str):user First name
        last_name (str):user Last name
        places (relationship): r/ship with the Place class.
        reviews (relationship): r/ship with the Review class.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
