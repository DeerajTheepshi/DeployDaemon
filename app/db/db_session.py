from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


class session:

    def __init__(self, setup):
        load_dotenv()
        username = os.getenv("DB_USERNAME")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        db = os.getenv("DB_NAME")
        Setup = setup(username, password, host, db)
        self.engine = Setup.create()

    def create(self):
        session = sessionmaker(bind=self.engine)
        self.Session = session()
        return session()

    def close(self):
        self.Session.close()
