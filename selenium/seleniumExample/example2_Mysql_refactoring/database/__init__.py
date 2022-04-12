import pymysql
from datetime import datetime
import os
class Mysql:
    VERSION = 1

    def __init__(self):
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))
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

    #############################
    # path에 있는 sql 파일 실행 #
    #############################
    def exeSqlFile(self, path:str):
        with open(self.BASE_DIR+path, 'r', encoding='UTF-8-sig') as f:
            # 쿼리문 나누기 및 반복
            for query in f.read().split(';'):
                try:
                    if query.strip() != '':
                        self.getCursor().execute(query)
                except Exception as msg:
                    print("Query Except : ", msg)

