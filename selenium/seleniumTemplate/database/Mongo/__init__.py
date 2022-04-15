from pymongo import MongoClient
from datetime import datetime
class MongoDB:
    VERSION = 1

    def __init__(self):
        self.db_name = 'seleniumTest'

        # 방법1
        self.client = MongoClient("mongodb://localhost:27017/")
        
        # 방법2
        # self.host = 'localhost'
        # self.port = 27017
        # self.client = MongoClient(host=self.host, port=self.port)


        self.col = self.client[self.db_name][self.__class__.__name__]

    @property
    def schema(self) -> dict:
        """Get default document format"""
        return {
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            '__version__': self.VERSION,
        }

    def schemize(self, document: dict) -> dict:
        """Generate JSON scheme"""
        return {**self.schema, **document}