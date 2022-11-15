import unittest2
from selenium import webdriver
import HtmlTestRunner

class MyTestCase(unittest2.TestCase):
    # @classmethod
    def setUp(self):
       self.driver= webdriver.Chrome("../drive/chromedriver")  # add assertion here
       self.driver.implicitly_wait(10)
       self.driver.maximize_window()
    def test_search(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name","q").send_keys("Automation step by step")
        self.driver.find_element("name","btnK").click()
        x=self.driver.title
        print(x)
        # self.assertEqual(x,"justin cletus-googlesearch")
    # @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    # def main():
    #     unittest_main()
if __name__ == '__main__':
    unittest2.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/justin/PycharmProjects/selenium/report'),verbosity=2)

