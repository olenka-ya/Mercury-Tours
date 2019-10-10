import unittest
from selenium import webdriver
import HtmlTestRunner

class Homepage():

    def __init__(self, driver):
        self.driver = driver

        self.sign_off_link_xpath = "//a[contains(text(),'SIGN-OFF')]"
        self.round_trip_box_xpath = "//body//b//input[1]"
        self.one_trip_box_xpath = "//body//b//input[2]"
        self.passengers_box_xpath = "//select[@name='passCount']"
        self.departure_box_xpath = "//select[@name='fromPort']"
        self.on_month_box_xpath = "//select[@name='passCount']"
        self.day_box_xpath = "//select[@name='fromDay']"
        self.arriving_box_xpath = "//select[@name='toPort']"
        self.returning_month_box_xpath = "//select[@name='toMonth']"
        self.returning_day_box_xpath = "//select[@name='toDay']"
        self.contunue_box_xpath = "//input[@name='findFlights']"


    def click_sign_off(self):
        self.driver.find_element_by_xpath(self.sign_off_link_xpath).click()