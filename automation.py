from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get('https://sakshingp.github.io/assignment/login.html')

time.sleep(2)

UserName = 'TapanNaik'
name= driver.find_element(By.XPATH , '//*[@id="username"]')
name.send_keys(UserName)
time.sleep(2)
Password = "TapanST77777"
password = driver.find_element(By.XPATH ,'//*[@id="password"]')
password.send_keys(Password)
time.sleep(2)
LoginBouuton = driver.find_element(By.XPATH,'//*[@id="log-in"]')
LoginBouuton.click()
time.sleep(2)
Amount= driver.find_element(By.XPATH,'//*[@id="amount"]')
Amount.click()