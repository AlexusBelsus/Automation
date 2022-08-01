import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

webDriver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\pythonProject1\\chromedriver.exe')
webDriver.get('https://www.saucedemo.com/')
webDriver.maximize_window()

def kartocka_korzina():
    return

webDriver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user') #Ввод логина

webDriver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce') #Ввод пароля


webDriver.find_element(By.XPATH, '//*[@id="login-button"]').click()  #Клик по кнопке вход

webDriver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()   #Клик по карточке товара

webDriver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()    #Клик добавить в корзину

webDriver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()     #Выход на главную