import os
import json
from tqdm import tqdm

if __name__ == '__main__':
    from __init__ import MongoDB    
else:
    from database import MongoDB

class spotDB(MongoDB):

    def upsert_model(self, document: dict):
        self.col.update_one(
            {'name':document['name']},
            {'$set':self.schemize(document)},
            upsert=True
        )

    def init(self):
        '''
        수집한 json파일을 mysql에 저장
        '''
        with open('../../data/spot.json', 'r', encoding='UTF-8-sig') as f:
            models = json.load(f)
            for model in models:
                for i, item in enumerate(tqdm(model['items'], 
                                    bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}',
                                    desc="insert spot data")):
                    self.upsert_model(item)
                    print('upset complete ', i)

if __name__ == '__main__':
    test = spotDB()
    test.init()
    