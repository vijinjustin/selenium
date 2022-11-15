import unittest2
from selenium import webdriver


class MyTestCase(unittest2.TestCase):
    # @classmethod
    def setUp(self):
       self.driver= webdriver.Chrome(executable_path="../drive/chromedriver")  # add assertion here
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

if __name__ == '__main__':
    unittest2.main()
