from selenium import webdriver

import pytest


@pytest.fixture()
def test_setUp():
    # global driver
    driver = webdriver.Chrome(executable_path="../../drive/chromedriver")
    driver.implicitly_wait(10)
    driver.maximize_window()


# def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    yield
    driver.close()
    driver.quit()
    print("test completed")

# def test_login(test_setUp):
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     driver.find_element_by_id("txtUsername").send_keys("Admin")
#     driver.find_element_by_id("txtPassword").send_keys("admin123")
#     driver.find_element_by_id("btnLogin").click()


# def test_teardown():
#     driver.close()
#     driver.quit()
#     print("test completed")
