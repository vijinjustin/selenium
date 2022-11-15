import time

from selenium import webdriver
path="../drive/geckodriver-v0.31.0-linux64.tar.gz"
driver=webdriver.Firefox(executable_path= path)
driver.get("https://google.com")
time.sleep(2)
driver.close()
driver.quit()
