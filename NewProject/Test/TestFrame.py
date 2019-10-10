import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.reports import reports

import HtmlTestRunner

from POM.NewProject.myPages.LoginPage import LoginPage
from POM.NewProject.myPages.HomePage import Homepage

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Olga/PycharmProjects/SeleniumIntroduction/POM/NewProject/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://www.newtours.demoaut.com/")

        login =LoginPage(driver)
        login.enter_username("mercury")
        login.enter_password("mercury")
        login.login()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Find a Flight: Mercury Tours:")
        self.driver.get_screenshot_as_file("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/POM/NewProject/screenshots/Login.png")

        homepage = homePage(driver)
        homepage.click_sign_off()

        #self.driver.implicitly_wait(10)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/OlgaPycharmProjectsSeleniumIntroduction/POM/NewProject/reports"), verbosity=2)