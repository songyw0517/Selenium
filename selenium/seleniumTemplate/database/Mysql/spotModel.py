import os
import json
from tqdm import tqdm

if __name__ == '__main__':
    from __init__ import Mysql
    
    # DTO 추가를 위한 경로 지정
    import sys
    sys.path.append(os.path.abspath(os.path.dirname(__file__))+'/../..')
    from DTO.spotDTO import spotDTO
    
else:
    from database import Mysql

class spotDB(Mysql):
    def __init__(self):
        super().__init__()
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    def insert_model(self, document:dict):
        table = spotDTO.__name__
        column = ', '.join(map(str, document.keys()))
        values = '\"'+'\", \"'.join(map(str, document.values()))+'\"'
        query = "INSERT INTO {} ({}) VALUES({})".format(table, column, values)
        self.getCursor().execute(query)

    def init(self):
        '''
        수집한 json파일을 mysql에 저장
        '''
        with open(self.BASE_DIR+'/../../data/spot.json', 'r', encoding='UTF-8-sig') as f:
            models = json.load(f)
            for model in models:
                for item in tqdm(model['items'], 
                                    bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}',
                                    desc="insert spot data"):
                    self.insert_model(item)
                self.getDB().commit()
if __name__ == '__main__':
    test = spotDB()
    test.exeSqlFile('/sql/schema.sql')
    test.init()
    