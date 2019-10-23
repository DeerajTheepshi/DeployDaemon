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

    def __init__(self, username, password, host):
        self.username = username
        self.password = password
        self.host = host

    def create(self):
        engine = create_engine("mysql://%s:%s@%s/deployD"
                               % (urllib.parse.quote_plus(self.username),
                                  urllib.parse.quote_plus(self.password),
                                  urllib.parse.quote_plus(self.host)), echo=True)
        Base.metadata.create_all(engine)

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
