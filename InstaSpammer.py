# instagram Dm spam bot by stiizzy cat
# not ment for malicious purposes
# this was made for edu peropses only
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
browser = webdriver.Firefox()


username = input("Enter instagram username: ")
spam = input("message to spam: ")

browser.implicitly_wait(5)

print("[+]logging in ")
browser.get('https://www.instagram.com/')



sleep(2)
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("your alt username") # your spam bots username
password_input.send_keys("your alt password ") # your  spam bots password

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(5)
Save_password = browser.find_element_by_xpath("//button[@type='button']")
Save_password.click()

sleep(4)
# removes notification
Notif_button = browser.find_element_by_xpath('//button[text()="Not Now"]')
Notif_button.click()
browser.get("https://www.instagram.com/" + username)
sleep(2)  
message_user = browser.find_element_by_class_name('sqdOP ')
message_user.click()
sleep(4)
# removes notification  if it pops up again
Notif_button = browser.find_element_by_xpath('//button[text()="Not Now"]')
Notif_button.click()
sleep(2)
x = 1   # spams forever untill you stop the script or close the browser
while True:
 cum = browser.find_element_by_tag_name('textarea')
 cum.send_keys(spam)
 Comment_input = browser.find_element_by_xpath('//button[text()="Send"]')
 Comment_input.click()
 x = 1

