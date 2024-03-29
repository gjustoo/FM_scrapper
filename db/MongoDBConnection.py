import os

from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient


class MongoDBConnection:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MongoDBConnection.__instance == None:
            MongoDBConnection()
        return MongoDBConnection.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MongoDBConnection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            # Replace the values with your actual MongoDB connection string and database name
            load_dotenv(find_dotenv())
            # Replace the values with your actual MongoDB connection string and database name
            passwd = os.environ.get('MONGO_PWD')
            self.db_name = os.environ.get('MONGO_DB')
            self.username = os.environ.get('MONGO_USER')
            self.host = os.environ.get('MONGO_HOST')
            self.port = os.environ.get('MONGO_PORT')
            self.auth_src = os.environ.get('MONGO_AUTH_SOURCE')
            os_env_uri = os.environ.get('MONGO_URI')
            if os_env_uri:
                self.CONNECTION_STRING = os_env_uri
            else:
                self.CONNECTION_STRING = f"mongodb://admin:admin@localhost:27019/fbMarketplaceScrapper?authSource=admin"
                

            self.client = MongoClient(self.CONNECTION_STRING)
            self.db = self.client[self.db_name]
            MongoDBConnection.__instance = self

    def getDatabase(self):
        return self.db
