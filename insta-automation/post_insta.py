from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

username = 'armando7.lorenz'
password = 'CEOhelpmillions1@'


def loginInsta(username, password):
    option = Options()

    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })
    # option.set_headless()
    driver = webdriver.Chrome(chrome_options=option)
    driver.get('https://www.instagram.com/')
    time.sleep(4)
    emailemem = driver.find_element_by_name('username')
    emailemem.send_keys(username)

    passelem = driver.find_element_by_name('password')
    print(passelem)
    passelem.send_keys(password)

    passelem.send_keys(Keys.RETURN)
    time.sleep(10)
    upload = driver.find_element(By.XPATH, './/*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]')
    upload.click()
    # ActionChains(driver) \
    #     .key_down(Keys.CONTROL) \
    #     .key_down(Keys.SHIFT) \
    #     .send_keys('i') \
    #     .key_up(Keys.CONTROL) \
    #     .key_up(Keys.SHIFT) \
    #     .perform()
    time.sleep(20)


def postInsta(picturePath, whatToWrite):
    '''We suppose that it is already logged in and you just want to post. '''
    pass


loginInsta(username, password)
