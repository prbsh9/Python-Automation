from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def Twitter(email, password, tweetPost=None):
    driver = webdriver.Chrome('C:/Users/pk202/OneDrive/Desktop/chromedriver/chromedriver.exe')
    driver.get('https://twitter.com/login')
    time.sleep(6)
    emailelement = driver.find_element_by_name("session[username_or_email]")
    emailelement.send_keys(email)

    passwordelement = driver.find_element_by_name("session[password]")
    passwordelement.send_keys(password)

    passwordelement.send_keys(Keys.RETURN)
    time.sleep(5)
    if tweetPost is not None:
        tweetelem = driver.find_element_by_class_name("notranslate")
        tweetelem.send_keys(tweetPost)
        time.sleep(2)
        tweetButton = driver.find_element_by_css_selector('div.r-urgr8i:nth-child(4)')
        tweetButton.click()
    global twitterHtml
    twitterHtml = driver.page_source
    return driver.close()


# postMessage = ''' Finally  '''
# email_or_username =
# password =
# Twitter(email_or_username, password, postMessage)
