import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


driver = WebDriver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\pythonProject1\\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

#user_name = driver.find_element(By.ID,'user-name')  #ID
#user_name = driver.find_element(By.NAME,'user-name') #Name
time.sleep(1)
user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]') #Ввод логина
user_name.send_keys('standard_user')
time.sleep(1)
user_pass = driver.find_element(By.XPATH, '//*[@id="password"]') #Ввод пароля
user_pass.send_keys('secret_sauce')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()  #Клик по кнопке вход

time.sleep(1)


############___Эмитация Скролла__################
i = 1
while i < 100:
    driver.execute_script("window.scrollBy(0, 3);")

    time.sleep(0.001)
    i = i + 1
i = 1
while i < 150:
    driver.execute_script("window.scrollBy(0, -3);")
    time.sleep(0.001)
    i = i + 1

driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click() #Товар выбран
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()  #Переход в корзину
time.sleep(1)

###### Оформление заказа ###############
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Alex')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('Belsky')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('Test')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="finish"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
time.sleep(1)
driver.close()
