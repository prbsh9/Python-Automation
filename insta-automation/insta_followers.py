from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



# def inInsta():
driver = webdriver.Chrome('C:/Users/pk202/OneDrive/Desktop/prakash/chromedriver/chromedriver.exe')
driver.get('https://www.instagram.com/')
time.sleep(4)
emailemem = driver.find_element_by_name('username')
emailemem.send_keys(email)

passelem = driver.find_element_by_name('password')
print(passelem)
passelem.send_keys(password)
time.sleep(2)
passelem.send_keys(Keys.RETURN)
time.sleep(20)

# notifelem = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
notifelem = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notifelem.click()
time.sleep(2)

# driver.execute_script("window.scrollTo(0, 100)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

myelem = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
myelem.click()

time.sleep(2)

followingelem = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
followingelem.click()
time.sleep(2)
# driver.execute_script("window.scrollTo(0, 5)")
driver.execute_script('''var popup = document.getElementsByClassName('isgrP');
                        popup[0].scrollTop = 5000; ''')
print('executed1')
driver.execute_script('''var popup = document.getElementsByClassName('isgrP');
                        popup[0].scrollTop = 5000; ''')
print('executed2')
driver.execute_script('''var popup = document.getElementsByClassName('isgrP');
                        popup[0].scrollTop = 5000; ''')
print('executed3')
driver.execute_script('''var popup = document.getElementsByClassName('isgrP');
                        popup[0].scrollTop = 5000; ''')
print('executed4')
driver.execute_script('''var popup = document.getElementsByClassName('isgrP');
                        popup[0].scrollTop = 5000; ''')



for x in range(20, 30):
    css_selector = '.PZuss > li:nth-child({}) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)'.format(x)
    unfollowelem = driver.find_element_by_css_selector(css_selector)
    unfollowelem.click()
    time.sleep(4)
    unfollowelem1 = driver.find_element_by_css_selector('button.aOOlW:nth-child(1)')
    unfollowelem1.click()
    time.sleep(6)

print('Finished!')
