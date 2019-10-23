from app.db.setup import setup
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()

    USERNAME = os.getenv("DB_USERNAME")
    PASSWORD = os.getenv("DB_PASSWORD")
    HOST = os.getenv("DB_HOST")
    db = setup(USERNAME, PASSWORD, HOST)
    db.create()
