import pytest # type: ignore
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("username, password, expected", [
    ("Admin", "admin123", "Dashboard"),  # Login Valid
    ("Admin", "admin321", "Invalid credentials"),  # Login Invalid
])
def test_login(setup_browser, username, password, expected):

    logger.info("🔄 Memulai pengujian login...")

    # Pengujian login dengan validasi hasil
    driver = setup_browser
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    # Menunggu elemen login muncul
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Menggunakan Action Chains untuk input data
    actions_login = ActionChains(driver)
    actions_login.send_keys_to_element(username_field, username).perform()
    actions_login.send_keys_to_element(password_field, password).perform()
    actions_login.click(login_button).perform()

    # Validasi hasil login
    if expected == "Dashboard":
        print("📲 Mengecek Dashboard...")
        assert wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
        logger.info("✅ Login berhasil!") 
    else:
        print("📲 Mengecek pesan error...")

        try:
            # Tunggu elemen alert login gagal nya muncul
            error_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='alert']")))

            # Ambil teks error
            error_message = error_element.text
            logger.info(f"❌ Login gagal! Pesan error: {error_message}")

            # Pastikan pesan error sesuai dengan yang diharapkan
            assert "Invalid credentials" in error_message, "Pesan error tidak sesuai!"

        except TimeoutException:
            logger.warning("⚠️ Tidak menemukan pesan error dalam waktu yang ditentukan.")

    logger.info("✅ Pengujian login selesai.")        