from random import Random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# wait를 위한 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tqdm import tqdm
import time
import os
import random
import json

# 단독 실행을 위한 환경 분리
if __name__ == "__main__":
    from __init__ import seleniumDriver
else:
    from example2_Mysql.src.crawler import seleniumDriver

class spotCrawler(seleniumDriver):
    def __init__(self):
        super(spotCrawler, self).__init__()

        # File path를 위한 기본 path
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))

        # 관광지 목록 가져오기
        with open(self.BASE_DIR+"/../refData/ref.txt", encoding='UTF-8') as f:
            travelList = f.readlines()
            self.travelList = list(map(lambda x:x.rstrip('\n'), travelList))
            
    
    def getSpotData(self, url):
        model = []
        self.getDriver().get(url)
        for spotName in tqdm(self.travelList, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}',
            desc="Spots"):
            time.sleep(random.randint(1, 2))
            elem = self.getDriver().find_element(By.NAME, 'q')
            elem.send_keys(spotName)
            elem.send_keys(Keys.ENTER)

            try:                
                src = self.getDriver().find_element(By.CLASS_NAME, "moreview").get_attribute('href')
            except:
                with open('../data/error.json', 'w', encoding='UTF-8-sig') as f:
                    error = {
                                'error spot':'상세보기',
                                'spot Name' : spotName
                            }
                    dump = json.dumps(error, indent='\t', ensure_ascii=False)
                    f.write(dump)
                self.getDriver().find_element(By.NAME, "q").clear()
                continue

            self.getDriver().get(src)
            address = self.getDriver().find_element(By.CLASS_NAME, "txt_address").text
            model.append(
                {
                    'name':spotName,
                    'address':address
                }
            )
        print('model = ', model)
        
        return model
    def process(self):
        spotData = []
        spotData.append(
            {
                'category':'spotData',
                'items':self.getSpotData('https://map.kakao.com/')
            }
        )
        print(spotData)
        self.save(spotData)

    @staticmethod
    def save(models, path="../data/spot.json"):
        dump = json.dumps(models, indent='\t', ensure_ascii=False)
        with open(path, 'w', encoding='UTF-8-sig') as f:
            f.write(dump)

if __name__ == '__main__':
    spot = spotCrawler()
    spot.process()
