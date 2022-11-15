from selenium import webdriver
import time
import unittest2
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", " .."))
from Demo.POMDemo.pages.LoginPage import LoginPage
from Demo.POMDemo.pages.homepage import HomePage
import HtmlTestRunner

class LoginTests(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drive/chromedriver")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click()
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element("name",  "username").send_keys("Admin")
        # self.driver.find_element("name",  "password").send_keys("admin123")
        # self.driver.find_element("name", "btnLogin").click()
        # self.driver.find_elements("class", "Logout").click()

    time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest2.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/justin/PycharmProjects/selenium/report'))

# driver = webdriver.Chrome(executable_path="/home/justin/PycharmProjects/selenium/drive/chromedriver")
# driver.implicitly_wait(10)
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element("name", "username").send_keys("Admin")
# driver.find_element("name", "password").send_keys("admin123")
# driver.find_element("submit").click()
# driver.find_elements("Logout").click()
# time.sleep(2)
# driver.close()
# driver.quit()
# print("test completed")
