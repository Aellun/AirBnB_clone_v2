#!/usr/bin/python3
"""Module for class sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental that
    manages SQLAlchemy database interactions
    """
    __engine = None
    __session = None

    # Retrieve database connection details from environment variables
    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        # Creates the SQLAlchemy engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dict of objects in the database.
        Args:
            cls: (Optional) class filter. If specified, only objects of the
                 specified class are included in the dict.

        Returns:
            dict of objects in the database.
        """
        dic = {}
        # Convert string class names to actual class objects
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """Adds new element to the database.
        Args:
            obj: Object to be added to the database.
        """
        self.__session.add(obj)

    def save(self):
        """saves changes to DB
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        obj: the object to be deleted
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Configures the database session and creates all tables
        """

        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
            closes the DB session
        """
        self.__session.close()
