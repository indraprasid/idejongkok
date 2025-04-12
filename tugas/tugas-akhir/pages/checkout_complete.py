from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from pages.locators import CheckoutCompleteLocators

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_complete_title(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutCompleteLocators.COMPLETE_TITLE)).text

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutCompleteLocators.SUCCESS_MSG)).text