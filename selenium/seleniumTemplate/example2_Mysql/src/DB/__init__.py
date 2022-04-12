import pymysql
from datetime import datetime
class Mysql:
    VERSION = 1

    def __init__(self):
        self.__user = 'test'
        self.__host = 'localhost'
        self.__password = 'test'
        self.__database = 'test'
        self.__port = 3306
        self.__charset = 'utf8'

        self.__db = pymysql.connect(host = self.__host,
                                    port = self.__port,
                                    user=self.__user,
                                    password=self.__password,
                                    database=self.__database,
                                    charset=self.__charset)
        self.__cursor = self.__db.cursor()
    def getCursor(self):
        return self.__cursor

    def getDB(self):
        return self.__db
    