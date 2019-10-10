import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import *
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.chrome.options import Options
import HtmlTestRunner

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Olga/PycharmProjects/SeleniumIntroduction/POM/NewProject/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("http://www.newtours.demoaut.com/")
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys("mercury")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("mercury")
        self.driver.find_element_by_xpath("//input[@name='login']").click()
        self.driver.implicitly_wait(10)
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Find a Flight: Mercury Tours:")
        self.driver.get_screenshot_as_file("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/POM/NewProject/screenshots/Login.png")

    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner("C:/Users/Olga/PycharmProjects/SeleniumIntroduction/POM/NewProject/reports"),verbosity=2)