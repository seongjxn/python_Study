from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyperclip

chrome_options= Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_service = Service(executable_path= ChromeDriverManager().install())

driver = webdriver.Chrome(service= chrome_service, options= chrome_options)
action = ActionChains(driver)



naver_id= 'eric267175'
naver_pw= 'Jangjin1057!'
blog_link= 'https://blog.naver.com/eric267175'



def naverLogin():
    driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=" + blog_link)
    time.sleep(5)

    id = driver.find_element(By.CSS_SELECTOR, '#id') #아이디 입력창
    time.sleep(0.1)
    pyperclip.copy(naver_id)
    time.sleep(0.1)
    id.send_keys(Keys.COMMAND, 'v')
    time.sleep(0.5)

    pw = driver.find_element(By.CSS_SELECTOR, '#pw') #비밀번호 입력창
    time.sleep(0.1)
    pyperclip.copy(naver_pw)
    time.sleep(0.1)
    pw.send_keys(Keys.COMMAND, 'v')
    time.sleep(0.5)

    driver.find_element(By.CSS_SELECTOR, '.btn_login').click()          # 로그인 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="new.dontsave"]').click()    # 자주 사용하는 기기 등록안함
    time.sleep(1)


def blogWrite():
    # driver.get(blog_link)
    driver.switch_to.frame("mainFrame")

    driver.find_element(By.XPATH, '//*[@id="post-admin"]/a[1]').click()
    time.sleep(10)

    #driver.find_element(By.XPATH, '//span[contains(text(), "취소")]').click()
    driver.find_element(By.CLASS_NAME, 'se-popup-button-cancel').click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//span[contains(text(), "제목")]').click()
    time.sleep(0.5)
    action.send_keys("Selenium 자동화 테스트").perform()
    time.sleep(0.5)

    
    driver.find_element(By.XPATH, '//span[contains(text(), "파일")]').click()
    time.sleep(0.5)
    # driver.find_element(By.XPATH, '//*[@id="SE-956a1fc5-2fe7-4153-b140-90828d5da725"]/div[1]/div/header/div[1]/ul/li[9]/button').click()
    
    file = driver.find_element(By.XPATH, '//span[contains(text(), "내 컴퓨터")]')
    file.send_keys('/Users/seongjxn/Documents/git/python_Study/Crawling/000660.csv')




    pass                                                                                            # Test Code



if __name__ == "__main__":
    naverLogin()
    blogWrite()

    pass                                                                                            # Test Code