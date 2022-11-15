from selenium import webdriver

driver =webdriver.Chrome("../drive/chromedriver")
driver.get("https:google.com")
print(driver.title)
driver.close()
driver.quit()
print("completed")