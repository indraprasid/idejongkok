from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from pages.locators import CartLocators

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_cart_title(self):
        return self.wait.until(EC.visibility_of_element_located(CartLocators.CART_TITLE)).text

    def get_cart_item_names(self):
        return [el.text for el in self.driver.find_elements(*CartLocators.ITEM_NAMES)]

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(CartLocators.CHECKOUT_BTN)).click()