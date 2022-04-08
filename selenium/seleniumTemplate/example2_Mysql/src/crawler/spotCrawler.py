from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# wait를 위한 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

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
    def test(self):
        for name in self.travelList:
            print(name)
    def getSpotData(self, url):
        pass


if __name__ == '__main__':
    spot = spotCrawler()
    spot.test()