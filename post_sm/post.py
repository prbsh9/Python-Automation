from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from secrets import fbmail, twittermail, fbpass, twitterpass


def postInFacebook(email, password, postMessage=None):
    from selenium.webdriver.chrome.options import Options

    option = Options()

    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })

    driver = webdriver.Chrome(chrome_options = option, executable_path='C:/Users/pk202/OneDrive/Desktop/prakash/chromedriver/chromedriver.exe')
    driver.get('https://www.facebook.com/')

    emailelement = driver.find_element(By.XPATH, './/*[@id="email"]')
    emailelement.send_keys(email)
    # time.sleep(2)

    passwordelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
    passwordelement.send_keys(password)
    # time.sleep(2)

    passwordelement.send_keys(Keys.RETURN)
    time.sleep(3)
    if postMessage is not None:
        statuselement = driver.find_element(By.XPATH, '//*[@name="xhpc_message"]')
        statuselement.send_keys(postMessage)
        time.sleep(4)
        button = driver.find_element_by_css_selector('._1mf7')
        button.click()
        time.sleep(2)
    return driver.close()


def postInTwitter(email, password, tweetPost=None):
    driver = webdriver.Chrome('C:/Users/pk202/OneDrive/Desktop/prakash/chromedriver/chromedriver.exe')
    driver.get('https://twitter.com/login')
    time.sleep(2)
    emailelement = driver.find_element_by_name("session[username_or_email]")
    emailelement.send_keys(email)

    passwordelement = driver.find_element_by_name("session[password]")
    passwordelement.send_keys(password)

    passwordelement.send_keys(Keys.RETURN)
    time.sleep(3)
    if tweetPost is not None:
        tweetelem = driver.find_element_by_class_name("notranslate")
        tweetelem.send_keys(tweetPost)
        time.sleep(2)
        tweetButton = driver.find_element_by_css_selector('div.r-urgr8i:nth-child(4)')
        tweetButton.click()
        time.sleep(3)
    return driver.close()


def whereToPost(postMessage, num=1):
    '''Chose where you want to post. '''
    if num == 1:
        postInFacebook(fbmail, fbpass, postMessage)
        postInTwitter(twittermail, twitterpass, postMessage)
    elif num == 2:
        postInFacebook(fbmail, fbpass, postMessage)
    elif num == 3:
        postInTwitter(twittermail, twitterpass, postMessage)
    else:
        print("Invalid command")

message = input('What do you want to post? ')
num = int(input("Where to post? \n 1 - both fb and twitter(default) \n 2 - only facebook \n 3 - only twitter \n"))
try:
    whereToPost(message, num)
except Exception as e:
    print(f'Error {e}')
