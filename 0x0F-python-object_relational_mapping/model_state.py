#!/usr/bin/python3
"""
Defines a State class and Base class
to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State Class

    Attributes:
        __tablename__ (str): The table name of class
        id (int): The State id of class
        name (str): The State name of class

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)