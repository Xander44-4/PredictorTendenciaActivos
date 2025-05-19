import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME= os.getenv("MONGO_DB_NAME")


con = MongoClient(MONGO_URI)
db = con[MONGO_DB_NAME]