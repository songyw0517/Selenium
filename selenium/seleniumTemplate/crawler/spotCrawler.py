from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# wait를 위한 라이브러리
from tqdm import tqdm
import time
import os
import random
import json

# 단독 실행을 위한 환경 분리
if __name__ == "__main__":
    from __init__ import seleniumDriver
    # DTO 추가를 위한 경로 지정
    path = os.path.abspath(os.path.dirname(__file__))+'/..'
    import sys
    sys.path.append(path)
    from DTO.spotDTO import spotDTO

else:
    from crawler import seleniumDriver

# 크롤러 생성
class spotCrawler(seleniumDriver):
    def __init__(self):
        super(spotCrawler, self).__init__()

        # File path를 위한 기본 path
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))

        # 관광지 목록 가져오기
        with open(self.BASE_DIR+"/../spotList.txt", encoding='UTF-8') as f:
            self.travelList = list(map(lambda x:x.rstrip('\n'), f.readlines()))
            
    
    # 데이터 수집 메소드
    def collector(self, url):
        model = []
        self.getDriver().get(url)
        for spotName in tqdm(self.travelList[:3], bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}',
            desc="Spots"):
            time.sleep(random.randint(1, 2)) # 서버로 부터 벤 먹지않으려면..
            elem = self.getDriver().find_element(By.NAME, 'q')
            elem.send_keys(spotName)
            elem.send_keys(Keys.ENTER)

            # 상세보기 접근, 없을 경우 -> error 로그 표시
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
                # 검색창에 넣은 값 초기화
                self.getDriver().find_element(By.NAME, "q").clear()
                continue

            self.getDriver().get(src)
            address = self.getDriver().find_element(By.CLASS_NAME, "txt_address").text
            model.append(spotDTO(spotName, address)) # 객체 생성후 모델에 추가
            
        return model
    # 카테고리별로 반복시키는 부분
    def process(self):
        '''
        카테고리별
        '''
        spotData = []
        spotData.append(
            {
                'category':'spotData',
                'items':list(map(lambda x:x.__dict__, self.collector('https://map.kakao.com/')))
            }
        )
        print('s', spotData)
        self.save(spotData)

    # json형식으로 저장하는 부분
    @staticmethod
    def save(models, path="../data/spot.json"):
        dump = json.dumps(models, indent='\t', ensure_ascii=False)
        with open(path, 'w+', encoding='UTF-8-sig') as f:
            f.write(dump)

if __name__ == '__main__':
    spot = spotCrawler()
    spot.process()
