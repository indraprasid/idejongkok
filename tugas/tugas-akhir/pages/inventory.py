import random
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from pages.locators import InventoryLocators

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.selected_names = []

    def add_two_random_products(self):
        self.wait.until(EC.presence_of_all_elements_located(InventoryLocators.ADD_BUTTONS))
        items = self.driver.find_elements(*InventoryLocators.ADD_BUTTONS)
        names = self.driver.find_elements(*InventoryLocators.ITEM_NAMES)
        selected = random.sample(list(zip(items, names)), 2)
        for btn, name in selected:
            self.selected_names.append(name.text)
            btn.click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(InventoryLocators.CART_LINK)).click()