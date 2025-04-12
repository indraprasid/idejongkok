from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from pages.locators import CheckoutInfoLocators
import random, string

class CheckoutInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_title(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutInfoLocators.TITLE)).text

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(CheckoutInfoLocators.CONTINUE_BTN)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutInfoLocators.ERROR_MSG)).text

    def input_firstname(self):
        firstname = random.choice(string.ascii_uppercase) + ''.join(random.choices(string.ascii_lowercase, k=9))
        self.driver.find_element(*CheckoutInfoLocators.FIRSTNAME).send_keys(firstname)

    def input_lastname(self):
        lastname = random.choice(string.ascii_uppercase) + ''.join(random.choices(string.ascii_lowercase, k=9))
        self.driver.find_element(*CheckoutInfoLocators.LASTNAME).send_keys(lastname)

    def input_postalcode(self):
        codes = ['10110', '40123', '60293', '70126', '80361']
        self.driver.find_element(*CheckoutInfoLocators.POSTALCODE).send_keys(random.choice(codes))
    
    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(CheckoutInfoLocators.CONTINUE_BTN)).click()