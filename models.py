"""
The module for creating a database structure.
"""

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship  # this + foreign key will allow to make connections between tables
from database import Base


class Users(Base):
    # creating Users class which extends our Base from database module, giving it a structure

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # creating indexes, which speed up a search, but cost memory
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    todos = relationship("Todos", back_populates="owner")  # creating a relationship, pointing at class and its object
    # with relationship function


class Todos(Base):
    # creating Todos class which extends our Base from database module, giving it a structure

    __tablename__ = "todos"  # defining the table name

    # defining columns
    id = Column(Integer, primary_key=True, index=True)  # giving a type to the column, setting a primary key
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)  # when a new task is created, it will be False, so not complete
    owner_id = Column(Integer, ForeignKey("users.id"))  # creating a foreign key with id column from users table

    owner = relationship("Users", back_populates="todos")  # creating an opposite relationship
