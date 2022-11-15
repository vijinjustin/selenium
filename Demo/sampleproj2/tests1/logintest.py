# import unittest2
# import by
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path="../home/justin/PycharmProjects/selenium/drive/chromedriver")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element("name", "username").send_keys("Admin")
driver.find_element("name", "password").send_keys("admin123")
#driver.find_element(by.xpath("//body/div[@id='app']/div[")).click()
driver.find_element("submit").click()
driver.find_elements("Logout").click()
# driver.find_element("by.id", "welcome").click()
# driver.find_element_by_link_text("Logout").click()
driver.close()
driver.quit()
print("test completed")
#
# if __name__ == '__main__':
#     unittest2.main()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element("name", "username").send_keys("Admin")
# driver.find_element("name", "password").send_keys("admin123")
# driver.find_element("type", "submit").click()

