#!/usr/bin/python3
"""
This script defines a City class
to work on MySQLAlchemy ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City Class

    Attributes:
        __tablename__ (str): The table name
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)