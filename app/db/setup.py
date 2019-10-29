from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import urllib
Base = declarative_base()

# Connect to db --------------------------------------


class setup:
    username = ""
    password = ""
    host = ""
    db = ""

    def __init__(self, username, password, host, db):
        self.username = username
        self.password = password
        self.host = host
        self.db = db

    def create(self):
        engine = create_engine("mysql://%s:%s@%s/%s"
                               % (urllib.parse.quote_plus(self.username),
                                  urllib.parse.quote_plus(self.password),
                                  urllib.parse.quote_plus(self.host),
                                  urllib.parse.quote_plus(self.db)), echo=True)
        Base.metadata.create_all(engine)
        return engine

# Declare Tables Schemas here------------------------------------------


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(32))  # probably a hash of 16/32 char
    authLevel = Column(Integer)


class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    projectName = Column(String(50))
    location = Column(String(50))
    apache_file = Column(String(50))
    stack = Column(String(50))
    githubLink = Column(String(100))
