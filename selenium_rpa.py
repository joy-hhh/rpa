import selenium
from selenium import webdriver


driver = webdriver.Chrome('c:\\R_selenium\\chromedriver.exe')

## Chrome 브라우저를 최대화 하기 위하여는
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximizeed")
# driver = webdriver.Chrome('c:\\R_selenium\\chromedriver.exe', chrome_options=options)

import time
time.sleep(1)

driver.get('https://www.naver.com')

# DevTools listening on ws://127.0.0.1:63507/devtools/browser/4229d9c8-4b8b-4e58-9659-13be3766baf4 
# 웹드라이버의 버젼이 최신이 아닌 경우 발생하는 오류 - 웹드라이버를 최신으로 다운로드


