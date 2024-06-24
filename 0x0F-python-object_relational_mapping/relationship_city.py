#!/usr/bin/python3
"""
 contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    links to the MySQL table cities

    Attributes:

        id: represents a column of an auto-generated,
            unique integer, can't be null and is a primary key

        name: represents a column of a string of
            128 characters and can't be null

        state_id: represents a column of an integer,
                can't be null and is a foreign key to states.id
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
