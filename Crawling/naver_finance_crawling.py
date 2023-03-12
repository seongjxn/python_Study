from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import re


chrome_options= Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_service = Service(executable_path= ChromeDriverManager().install())

driver = webdriver.Chrome(service= chrome_service, options= chrome_options)

targetStock = '000660'
targetYear = '2023'

getData = []

def getStock():
    page = 1

    while True:
        driver.get(f"https://finance.naver.com/item/sise_day.naver?code={targetStock}&page={page}")
        time.sleep(0.1)

        for i in [3, 4, 5, 6, 7, 11, 12, 13, 14, 15]:
            value = driver.find_element("xpath", f"/html/body/table[1]/tbody/tr[{i}]")
            if re.match(f'{targetYear}', value.text):
                diff = driver.find_element("xpath", f"/html/body/table[1]/tbody/tr[{i}]/td[3]/img").get_attribute('alt')
                diff = '+' if diff == "상승" else '-' if diff == '하락' else ''
                tmpData = value.text.split()
                tmpData[2] = diff + tmpData[2]
                getData.append(tmpData)
            else:
                return
        page+=1


def printStock():
    print("   날짜       종가     전일비     시가       고가       저가       거래량   ")

    for i in getData:
        print(f"{i[0]:10} {i[1]:>10} {i[2]:>8} {i[3]:>10} {i[4]:>10} {i[5]:>10} {i[6]:>12}")


def exportCSV():
    with open(file=f'{targetStock}.csv', mode='w', encoding='utf-8-sig', newline='') as f:
        csv_f = csv.writer(f)
        csv_f.writerow(['날짜', '종가', '전일비', '시가', '고가', '저가', '거래량'])
        for i in getData:
            csv_f.writerow(i)


if __name__ == '__main__':
    getStock()
    printStock()
    exportCSV()

