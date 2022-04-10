if __name__ == "__main__":
    from __init__ import Mysql
    import pymysql
    import os
else:
    from DB import Mysql

class spotDB(Mysql):
    def __init__(self):
        super().__init__()
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    def initDB(self, path:str):
        '''
        DB 초기화
        - schema.sql 파일을 실행한다.
        '''
        with open(self.BASE_DIR+path, 'r', encoding='UTF-8-sig') as f:
            for query in f.read().split(';'):
                try:
                    if query.strip() != '':
                        self.getCursor().execute(query)
                except Exception as msg:
                    print("Command skipped: ", msg)

    def upsert_model(self, doucment:dict):
        pass

if __name__ == '__main__':
    test = spotDB()
    test.initDB('/schema.sql')