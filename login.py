
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(browser, username, password, check_xpath_exists):
    browser.get("https://www.instagram.com/direct/inbox/")
    time.sleep(5)

    direct_notificationXPATH = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]"
    if(check_xpath_exists(direct_notificationXPATH)):            
        browser.find_element(By.XPATH, direct_notificationXPATH).click()
        time.sleep(5)
    else:
        print("ok")
    time.sleep(2)
    browser.find_element(By.NAME, 'username').send_keys(username)
    browser.find_element(By.NAME, 'password').send_keys(password)
    browser.find_element(By.NAME, 'password').send_keys(Keys.ENTER)

    time.sleep(10)
