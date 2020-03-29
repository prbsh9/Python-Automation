from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def inFacebook(email, password, postMessage=None):
    driver = webdriver.Chrome('C:/Users/pk202/OneDrive/Desktop/chromedriver/chromedriver.exe')
    driver.get('https://www.facebook.com/')

    emailelement = driver.find_element(By.XPATH, './/*[@id="email"]')
    emailelement.send_keys(email)
    # time.sleep(2)

    passwordelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
    passwordelement.send_keys(password)
    # time.sleep(2)

    passwordelement.send_keys(Keys.RETURN)
    time.sleep(15)
    fbhtml = driver.get_screenshot_as_file('1111.png')

    if postMessage is not None:
        statuselement = driver.find_element(By.XPATH, '//*[@name="xhpc_message"]')
        statuselement.send_keys(postMessage)
        fbhtml = driver.get_screenshot_as_file('1111.png')
        time.sleep(2)
        button = driver.find_element_by_css_selector('._1mf7')
        button.click()
        time.sleep(4)
    return fbhtml


postMessage = '''Today is sunday. '''
# email =
# password
# inFacebook(email, password, postMessage)
