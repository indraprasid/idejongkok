from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from pages.locators import CheckoutOverviewLocators

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_title(self):
        return self.wait.until(EC.visibility_of_element_located(CheckoutOverviewLocators.TITLE)).text

    def get_item_names(self):
        return [el.text for el in self.driver.find_elements(*CheckoutOverviewLocators.ITEM_NAMES)]

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(CheckoutOverviewLocators.FINISH_BTN)).click()