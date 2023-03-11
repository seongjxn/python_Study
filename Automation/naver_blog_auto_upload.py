from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyperclip

chrome_options= Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_service = Service(executable_path= ChromeDriverManager().install())

driver = webdriver.Chrome(service= chrome_service, options= chrome_options)



naver_id= 'eric267175'
naver_pw= 'Jangjin1057!'




def naverLogin():
    driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

    id = driver.find_element(By.CSS_SELECTOR, '#id') #아이디 입력창
    pyperclip.copy(naver_id)
    time.sleep(0.1)
    id.send_keys(Keys.COMMAND, 'v')
    time.sleep(2)

    pw = driver.find_element(By.CSS_SELECTOR, '#pw') #비밀번호 입력창
    pyperclip.copy(naver_pw)
    time.sleep(0.1)
    pw.send_keys(Keys.COMMAND, 'v')
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '.btn_login').click()          # 로그인 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="new.dontsave"]').click()    # 자주 사용하는 기기 등록안함


def blogWrite():
    pass                                                                                            # Test Code



if __name__ == "__main__":
    naverLogin()

    pass                                                                                            # Test Code