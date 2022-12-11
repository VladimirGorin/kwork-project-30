from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from config.data import users_settings_dict
from config.data import sendText
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from login import login


class InstagramBot():

    def __init__(self, username, password):

        self.username = username
        self.password = password
        options = Options()
        self.browser = webdriver.Chrome("./chromedriver/chromedriver.exe", options=options)

    # метод для закрытия браузера
    def close_browser(self):

        self.browser.close()
        self.browser.quit()

    def check_xpath_exists(self, url):

        browser = self.browser
        try:
            browser.find_element(By.XPATH,url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def check_css_exists(self, css):

        browser = self.browser
        try:
            browser.find_element(By.CSS_SELECTOR,css)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    # метод для отправки сообщений в директ
    def send_direct_message(self, direct_users="", message=""):

        browser = self.browser
        
        browser.get("https://www.instagram.com/direct/inbox/")

        time.sleep(5)
        direct_notificationXPATH = '//*[@id="mount_0_0_v6"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]'
        print(self.check_xpath_exists(direct_notificationXPATH))
        if(self.check_xpath_exists(direct_notificationXPATH)):            
            direct_notification = browser.find_element(By.XPATH, direct_notificationXPATH)
            direct_notification.click()

            time.sleep(5)
        else:
            print("ok")

        direact_sendMessageXPATH = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[3]/div/button"
        direact_sendMessage = browser.find_element(By.XPATH, direact_sendMessageXPATH).click()
        time.sleep(5)

        direact_selectUsersXPATH = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input"
        direact_selectUsers = browser.find_element(By.XPATH, direact_selectUsersXPATH)
        direact_selectUsers.send_keys(direct_users)

        direct_selectUserXPATH = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/button"
        time.sleep(5) 
        if(self.check_xpath_exists(direct_selectUserXPATH) == True):
            direct_selectUser = browser.find_element(By.XPATH, direct_selectUserXPATH).click()
        else:
            print("Nothing")

        time.sleep(5)

        direct_nextButtonXPATH = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button"
        direct_nextButtonXPATH = browser.find_element(By.XPATH, direct_nextButtonXPATH).click()

        time.sleep(5)

        print(sendText)


        direct_inputMessageButtonXPATH = "textarea"
        direct_inputMessageButton = browser.find_element(By.TAG_NAME, direct_inputMessageButtonXPATH)
        for part in sendText.split('\n'):
            direct_inputMessageButton.send_keys(part)
            ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()


        time.sleep(15)
        direct_sendMessageButtonXPATH = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button"
        direct_sendMessageButton = browser.find_element(By.XPATH, direct_sendMessageButtonXPATH).click()

        time.sleep(5)
        

for user, user_data in users_settings_dict.items():
    username = user_data['login']
    password = user_data['password']
    direct_users = user_data['users']
    
    data = direct_users.__len__()
    i = 0

    my_bot = InstagramBot(username, password)
    print(sendText)
    login(my_bot.browser, username, password, my_bot.check_xpath_exists)
    while i < data:
        print(direct_users[i])
        my_bot.send_direct_message(direct_users[i], sendText)
        i = i + 1
    my_bot.close_browser()



