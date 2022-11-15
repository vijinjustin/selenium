from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver =webdriver.Chrome("../drive/chromedriver")
#implicit waits
# driver.implicitly_wait(10)

driver.get("https:google.com")
driver.find_element("name","q").send_keys("Automation")
# explicit waits
# wait =  WebDriverWait(driver, 10)
element = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.NAME, "btnK"))).click()
# driver.find_element("name","btnK").click()
print("test completed")
# driver.close()
driver.quit()


