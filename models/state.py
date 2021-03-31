#!/usr/bin/python
"""Contains class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """The state class"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref='state', cascade="all, delete")
    else:
        @property
        def cities(self):
            """to list the cities"""
            from models import storage
            citiesList = []
            for key, obj in storage.all(City).items():
                if self.id == obj.state_id:
                    citiesList.append(obj)
            return citiesList
