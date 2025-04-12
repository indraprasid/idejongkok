import logging
from pages.login import LoginPage # type: ignore
from pages.inventory import InventoryPage # type: ignore
from pages.cart import CartPage # type: ignore
from pages.checkout_info import CheckoutInfoPage # type: ignore
from pages.checkout_overview import CheckoutOverviewPage # type: ignore
from pages.checkout_complete import CheckoutCompletePage # type: ignore

logger = logging.getLogger(__name__)


def test_endtoend_saucedemo(browser):
    """Test End to End Saucedemo: login, add to cart, checkout, verify complete"""

    login = LoginPage(browser)
    inventory = InventoryPage(browser)
    cart = CartPage(browser)
    checkout_info = CheckoutInfoPage(browser)
    overview = CheckoutOverviewPage(browser)
    complete = CheckoutCompletePage(browser)

    login.login("standard_user", "secret_sauce")
    logger.info(f"✅ Login berhasil")

    inventory.add_two_random_products()
    selected_items = inventory.selected_names
    inventory.go_to_cart()
    logger.info(f"✅ Produk berhasil ditambahkan ke cart: {selected_items}")

    cart.get_cart_item_names()
    cart.click_checkout()

    checkout_info.click_continue()
    checkout_info.get_error_message()
    checkout_info.input_firstname()
    checkout_info.input_lastname()
    checkout_info.input_postalcode()
    checkout_info.click_continue()

    overview.get_item_names()
    overview.click_finish()

    complete.get_success_message()
    logger.info(f"✅ Pengujian selesai! Order berhasil dilakukan.")