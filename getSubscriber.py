from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from config.data import username, password, user_search, user_sub_counter
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

    def get_subscriber(self, user_search, user_sub_counter,):
        browser = self.browser 

        browser.get(f'https://www.instagram.com/{user_search}/followers/')
        time.sleep(6)
        i = 1
        while i < user_sub_counter: 
            
            get_profile = f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div/div/div/span/a'
            if(self.check_xpath_exists(get_profile)):

                get_profile = browser.find_element(By.XPATH, get_profile)
                profile_link = get_profile.get_attribute('href')

                scrolling_element_xpath = "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
                scrolling_element = browser.find_element(By.XPATH, scrolling_element_xpath)

                link = profile_link.split("https://www.instagram.com/")[1]
                print(link)

                with open("./info/subscribers.txt", "a", encoding="utf8") as file:
                    file.write(f"{link} \n")
                    file.close()

                browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrolling_element)

            else:
                print('SUB NON')
            i = i + 1  



        


my_bot = InstagramBot(username, password)
login(my_bot.browser, username, password, my_bot.check_xpath_exists)
my_bot.get_subscriber(user_search, user_sub_counter)
my_bot.close_browser()



