from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

driver = webdriver.Chrome(r"D:\Пары\chromedriver.exe")
driver.get("https://www.python.org")


WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.NAME, "q"))
)
elem = driver.find_element(By.NAME, 'q')
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
sleep(3)

driver.close()



