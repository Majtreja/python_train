# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import unittest
from data import Data


class TestLoginBO(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#        webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)

    def open_page(self):
        driver = self.driver
        driver.get("https://bo-qa-03.icecat.biz/home/login/")

    def fill_form(self, data):
        driver = self.driver
        driver.find_element_by_name("Login").click()
        driver.find_element_by_name("Login").clear()
        driver.find_element_by_name("Login").send_keys(data.user)
        driver.find_element_by_name("Password").click()
        driver.find_element_by_name("Password").clear()
        driver.find_element_by_name("Password").send_keys(data.password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='REGISTER (FREE)'])[1]/preceding::button[1]").click()

    def test_login(self):
        self.open_page()
        self.fill_form(Data(user="QA_DB_superuser", password="roo6Piv2"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
