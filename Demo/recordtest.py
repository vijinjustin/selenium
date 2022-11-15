# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest2 , time, re


class CaptureScreenshots(unittest2.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../drive/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_capture_screenshots(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.save_screenshot('before-adding-comment.png')
        driver.find_element_by_id("comment").click()
        driver.find_element_by_id("comment").clear()
        driver.find_element_by_id("comment").send_keys("Added by Alex.")
        driver.save_screenshot('after-adding-comment.png')
        driver.find_element_by_xpath("//div[@id='rso']/div/div/div/div/div/a/div/cite").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("Admin")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin123")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
    #     driver.get(
    #         "https://www.udemy.com/course/selenium-python-step-by-step-for-beginners/learn/lecture/12021428#overview")
    #     driver.find_element_by_id("u154-playerId__14455518--36_html5_api").click()
    #
    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.driver.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest2.main()
