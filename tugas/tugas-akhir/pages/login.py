from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from pages.locators import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(LoginLocators.USERNAME)).send_keys(username)
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginLocators.LOGIN_BTN).click()
