class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        # These are the 3 locators on this page.
        self.username_textbox_xpath = "//input[@name='userName']"
        self.password_textbox_xpath = "//input[@name='password']"
        self.signin_button_xpath = "//input[@name='login']"
        self.destinations_link_xpath ="//a[contains(text(),'your destination')]"
        self.featured_vacations_destinations_link_xpath = "//a[contains(text(),'featured vacation destinations')]"
        self.registerhere_link_xpath = "//a[contains(text(),'Register')]"
        self.signon_link_xpath = "//a[contains(text(),'SIGN-ON')]"
        self.register_link_xpath = "//a[contains(text(),'REGISTER')]"
        self.support_link_xpath = "//a[contains(text(),'SUPPORT')]"
        self.contact_link_xpath = "//a[contains(text(),'CONTACT')]"
        self.home_link_xpath = "//a[contains(text(),'Home')]"
        self.flights_link_xpath = "//a[contains(text(),'Flights')]"
        self.carrentals_link_xpath = "//a[contains(text(),'Car Rentals')]"
        self.cruises_link_xpath = "//a[contains(text(),'Cruises')]"
        self.destinations_link_xpath = "//a[contains(text(),'Destinations')]"
        self.vacations_link_xpath ="//a[contains(text(),'Vacations')]"
        self.business_traval_link_xpath = "//a[contains(text(),'Business')]"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)
        #self.driver.implicity_wait(10)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)
        #self.driver.implicity_wait(10)

    def login(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()
        #self.driver.implicity_wait