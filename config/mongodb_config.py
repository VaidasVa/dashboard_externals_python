import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('DBUSER')
password = os.getenv('PASSWORD')
URL = os.getenv('URL')
database = os.getenv('DB')
collection = os.getenv('COLLECTION')

con_str = f"mongodb+srv://{user}:{password}@{URL}/{database}"
client = MongoClient(con_str)
db = client[database]
col = db[collection]


def connect_to_db():
    return col
