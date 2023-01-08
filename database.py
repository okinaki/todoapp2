"""
The module for creating an engine, session and base.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# here we will be storing the data for our application
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Bajabongo2022!@127.0.0.1:3307/todoapp"
# for PostgreSQL -> "postgresql://postgres:Bajabongo2022!@localhost/TodoApplicationDatabase"
# for MySQL -> "mysql+pymysql://root:Bajabongo2022!@127.0.0.1:3307/todoapp"
# for sqlite -> "sqlite:///./todos.db"

# creating SQL Alchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# connect_args={"check_same_thread": False} - this is a specific argument for sqlite
# no need for additional argument for PostgreSQL or MySQL


# creating a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # no automatic commits

# creating a base
Base = declarative_base()
