from selenium import webdriver
import unittest2
import HtmlTestRunner


class GoogleSearch(unittest2.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drive/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_Automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name", "q").send_keys("Automation Step by Step")
        self.driver.find_element("name", "btnK").click()

    def test_search_vijinjustin(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name", "q").send_keys("vijinjustin")
        self.driver.find_element("name", "btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    print("Test Completed")


if __name__ == '__main__':
    unittest2.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/justin/PycharmProjects/selenium/report'))
