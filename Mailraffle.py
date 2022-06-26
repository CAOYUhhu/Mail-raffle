# 两个函数，分别实现推特登录和抓取指定账户最新推文（除去置顶推文）
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import re


class Mailraffle:

    def __init__(self):
        self.s = Service('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        self.chrome_options = Options()
        #self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=self.s)
        #self.driver = webdriver.Chrome(service=self.s, chrome_options=self.chrome_options)

    def mailinput(self, accountpage, mailaddr):
        self.driver.get(accountpage)
        sleep(3)
        cards = self.driver.find_element(
            by=By.XPATH,
            value='//input[@placeholder="Enter Your Email address"]')
        cards.send_keys(mailaddr)
        botton = self.driver.find_element(
            by=By.XPATH,
            value='//button[@class="ant-btn ant-btn-primary ant-btn-lg ant-input-search-button"]')
        botton.click()
        sleep(3)





