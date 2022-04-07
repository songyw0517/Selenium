# driver를 위한 라이브러리
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# wait를 위한 라이브러리
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time
class TestSelenium:
    def __init__(self, url, waitTime):
        # 시스템에 부착된 장치가 작동하지 않습니다. 에러 해결
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
        # 기다리는 시간설정
        self.waitTime=waitTime 
        # 드라이버 설정
        '''
        암묵적 대기 시간 : 3초
        '''
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(waitTime)

        # wait 설정
        self.wait = WebDriverWait(self.driver, waitTime)
    
        # url 설정
        self.url = url

    def dbInit():
        pass


    # 구현할 부분, ScrollDown
    def scrollDown(self):
        SCROLL_PAUSE_TIME = 1
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    self.driver.find_element(By.CLASS_NAME, "mye4qd").click()
                except:
                    print("끝")
                    break

            last_height = new_height


    # 구현할 부분, run
    def run(self):
        self.driver.get(self.url)
        elem = self.driver.find_element(By.NAME, "q")
        elem.send_keys('조코딩')
        elem.send_keys(Keys.RETURN)


        self.scrollDown()
        count = 1
        images = self.driver.find_elements(By.CLASS_NAME, "rg_i.Q4LuWd")
        for image in images:
            try:
                image.click()
                imgUrl = self.driver.find_element(
                    By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(imgUrl, "test{}.jpg".format(count))
                count+=1
            except:
                pass
            
        self.driver.close()
    
    
     
if __name__ == '__main__':
    url = "https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl"
    test = TestSelenium(url, 3)
    test.run()
