from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# driver를 위한 라이브러리
from selenium import webdriver

class seleniumDriver:
    def __init__(self):
        # option 설정 #
        # 시스템에 부착된 장치가 작동하지 않습니다. 에러 해결
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.waitTime = 10
        
        # 드라이버 생성
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        
        # 암묵적 대기 시간 설정
        self.driver.implicitly_wait(self.waitTime)
    
    def getDriver(self):
        return self.driver
    
    def __del__(self):
        if "driver" in self.__dict__:
            self.driver.close()

    def setWaitTime(self, waitTime):
        self.waitTime = waitTime
        self.driver.implicitly_wait(self.waitTime)