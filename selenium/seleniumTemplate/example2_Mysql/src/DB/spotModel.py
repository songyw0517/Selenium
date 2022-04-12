import pymysql
import os
import json
from tqdm import tqdm
if __name__ == "__main__":
    from __init__ import Mysql
    
else:
    from DB import Mysql

class spotDB(Mysql):
    def __init__(self):
        super().__init__()
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))

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

    def insert_model(self, document:dict):
        '''
        DB 설계 미스로 인한 임시 구현, id 중복처리 불가
        '''
        table = "traveltest" # DTO.__name__로 대체 가능
        column = ', '.join(map(str, document.keys()))
        values = '\"'+'\", \"'.join(map(str, document.values()))+'\"'
        query = "INSERT INTO {} ({}) VALUES({})".format(table, column, values)
        self.getCursor().execute(query)

    def init(self):
        '''
        수집한 json파일을 mysql에 저장
        '''
        with open(self.BASE_DIR+'/../data/spot.json', 'r', encoding='UTF-8-sig') as f:
            models = json.load(f)
            for model in models:
                for item in tqdm(model['items'], 
                                    bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}',
                                    desc="insert spot data"):
                    self.insert_model(item)
                self.getDB().commit()

if __name__ == '__main__':
    test = spotDB()
    test.init()