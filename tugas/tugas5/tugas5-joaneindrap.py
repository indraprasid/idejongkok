from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 🔹 Inisialisasi WebDriver (Pastikan ChromeDriver sudah ada di PATH)
driver = webdriver.Chrome()

# 🔹 Atur Implicit Wait (Menunggu elemen hingga 10 detik sebelum error)
driver.implicitly_wait(10)

# 🔹 Buka halaman demo alert
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

# 🔹 Inisialisasi Explicit Wait
wait = WebDriverWait(driver, 10)

# ===========================================================
# 📌 1. Handle Basic Alert
print("\n🔹 Menguji Basic Alert...")
try:
    driver.find_element(By.ID, "alertButton").click()
    alert = wait.until(EC.alert_is_present())  # Tunggu hingga alert muncul
    print("✅ Basic Alert muncul dengan teks:", alert.text)
    alert.accept()
except TimeoutException:
    print("❌ Basic Alert tidak muncul!")

# ===========================================================
# 📌 2. Handle Confirm Alert
print("\n🔹 Menguji Confirm Alert...")
try:
    driver.find_element(By.ID, "confirmButton").click()
    alert = wait.until(EC.alert_is_present())
    print("✅ Confirm Alert muncul dengan teks:", alert.text)
    alert.dismiss()  # Bisa pakai alert.accept() untuk "OK"
except TimeoutException:
    print("❌ Confirm Alert tidak muncul!")

# ===========================================================
# 📌 3. Handle Prompt Alert
print("\n🔹 Menguji Prompt Alert...")
try:
    driver.find_element(By.ID, "promtButton").click()
    alert = wait.until(EC.alert_is_present())
    print("✅ Prompt Alert muncul dengan teks:", alert.text)
    alert.send_keys("ChatGPT")  # Input teks ke prompt
    alert.accept()  # Klik OK
except TimeoutException:
    print("❌ Prompt Alert tidak muncul!")

# ===========================================================
# 📌 4. Handle Timer Alert (Delayed Alert)
print("\n🔹 Menguji Timer Alert...")
try:
    driver.find_element(By.ID, "timerAlertButton").click()
    alert = wait.until(EC.alert_is_present())
    print("✅ Timer Alert muncul dengan teks:", alert.text)
    alert.accept()
except TimeoutException:
    print("❌ Timer Alert tidak muncul!")

# ===========================================================
# 🔹 Tutup browser setelah semua pengujian selesai
print("\n✅ Semua pengujian selesai! Menutup browser...")
driver.quit()