from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from password import password1, user1 #the password and user name for facebook
import os
lk = os.path.join(os.getcwd(), "chromedriver",)
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(lk, options=chrome_options)
driver.get('https://www.instagram.com/')
sleep(3)
facebook=driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]')
facebook.click()
sleep(3)
username=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input')
username.send_keys(user1)
password=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input')
password.send_keys(password1,Keys.ENTER)
sleep(8)
driver.get("https://www.instagram.com/bar.schwartz.9/")
sleep(5)
message=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]')
message.click()
sleep(2)
messg=driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
counter=1
while True:
    lol="bulbul number: "+str(counter)+" 8============}"
    #lol=random.choice(lst)
    try:
        messg = driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        messg.send_keys(lol,Keys.ENTER)
    except:
        continue

    counter+=1
    print(counter-1)
    sleep(5)