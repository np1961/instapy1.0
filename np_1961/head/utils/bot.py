import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings as message
from random import randint as random
from time import sleep
from info import username, password 
message('ignore')


browser=webdriver.Firefox(executable_path='/home/np_1961/utils/geckodriver/geckodriver')
sleep(random(1,3))
browser.get('https://instagram.com/')
sleep(random(7,10))

_login_=browser.find_element(by=By.NAME, value='username')
_login_.send_keys(username)
sleep(random(1,3))

_password_=browser.find_element(by=By.NAME, value='password')
_password_.send_keys(password+Keys.ENTER)
sleep(random(7,10))


mouse=browser.find_element(by=By.CSS_SELECTOR, value='button._acan:nth-child(1)')
mouse.click()
sleep(2)

mouse=browser.find_element(by=By.CSS_SELECTOR, value='button._a9--:nth-child(2)')
mouse.click()
sleep(2)
