#!/usr/bin/python3
"""Define class Db-Storage"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

args_obj = {"BaseModel": BaseModel, "City": City, "State": State,
            "Amenity": Amenity, "User": User, "Place": Place, "Review": Review}


class DBStorage():
    """DBStorage class"""
    __engine = None
    __session = None


def __init__(self):
    """This is the constructor"""

    self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                  .format(getenv(HBNB_MYSQL_USER),
                                          getenv(HBNB_MYSQL_PWD),
                                          getenv(HBNB_MYSQL_HOST),
                                          getenv(HBNB_MYSQL_DB)),
                                  pool_pre_ping=True)
    if getenv('HNB_ENV') == 'test':
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"query on the current database session """
        temp = {}
        for a in args_obj:
            if cls is None or cls is args_obj[a]:
                burger = session.query(args_obj[a]).all()
                for bu in burger:
                    key = "{}.{}".format(bu.__class__.__name__, bu.id)
                    temp[key] = bu
        return (temp)

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload data"""
        Base.metadata.create_all(self.__engine)
        Session_m = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session_m)
        self.__session = session

    def close(self):
        """session closed"""
        self.__session.close()
