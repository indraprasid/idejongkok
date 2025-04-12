from selenium.webdriver.common.by import By # type: ignore

class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

class InventoryLocators:
    ADD_BUTTONS = (By.CSS_SELECTOR, ".inventory_item button")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

class CartLocators:
    CART_TITLE = (By.CLASS_NAME, "title")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BTN = (By.ID, "checkout")

class CheckoutInfoLocators:
    TITLE = (By.CLASS_NAME, "title")
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    POSTALCODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    ERROR_MSG = (By.CLASS_NAME, "error-message-container")

class CheckoutOverviewLocators:
    TITLE = (By.CLASS_NAME, "title")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    FINISH_BTN = (By.ID, "finish")

class CheckoutCompleteLocators:
    COMPLETE_TITLE = (By.CLASS_NAME, "title")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-text")