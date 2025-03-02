from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Inisialisasi WebDriver Chrome
driver = webdriver.Chrome()

# Implicit Wait (Menunggu elemen hingga 10 detik sebelum error)
driver.implicitly_wait(10)

# Buka halaman demo alert
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

# Inisialisasi Explicit Wait
wait = WebDriverWait(driver, 10)

def wait_between_steps(seconds=5):
    # Menunggu beberapa detik sebelum lanjut ke langkah berikutnya
    try:
        WebDriverWait(driver, seconds).until(EC.alert_is_present())
    except TimeoutException:
        pass

# ===========================================================
# 1. Handle Basic Alert
print("\n🔹 Menguji Basic Alert...")
try:
    driver.find_element(By.ID, "alertButton").click()
    alert = wait.until(EC.alert_is_present())  # Beberapa detik hingga alert tampil
    print("✅ Basic Alert tampil dengan teks:", alert.text)
    
    wait_between_steps()  # Jeda sebelum klik OK
    alert.accept()
except TimeoutException:
    print("❌ Basic Alert tidak tampil!")

wait_between_steps()  # Jeda antar pengujian

# ===========================================================
# 2. Handle Confirm Alert
print("\n🔹 Menguji Confirm Alert...")
try:
    driver.find_element(By.ID, "confirmButton").click()
    alert = wait.until(EC.alert_is_present())
    print("✅ Confirm Alert tampil dengan teks:", alert.text)
    
    wait_between_steps()  # Jeda sebelum klik Cancel
    alert.dismiss()

    # Validasi apakah hasilnya "You selected Cancel"
    confirmResult = wait.until(EC.presence_of_element_located((By.ID, "confirmResult"))).text
    if confirmResult == "You selected Cancel":
        print("✅ Validasi sukses: Teks yang muncul adalah", confirmResult)
    else:
        print("❌ Validasi gagal: Teks yang muncul adalah", confirmResult)

except TimeoutException:
    print("❌ Confirm Alert tidak tampil!")

wait_between_steps()  # Jeda antar pengujian

# ===========================================================
# 3. Handle Prompt Alert
print("\n🔹 Menguji Prompt Alert...")
try:
    driver.find_element(By.ID, "promtButton").click()
    alert = wait.until(EC.alert_is_present())
    print("✅ Prompt Alert tampil dengan teks:", alert.text)
    
    alert.send_keys("Joane Indra Prasetyawan")  # Input teks ke prompt
    wait_between_steps()  # Jeda sebelum klik OK
    alert.accept()  # Klik OK

    # Validasi apakah hasilnya "You entered ..."
    promptResult = wait.until(EC.presence_of_element_located((By.ID, "promptResult"))).text
    if promptResult == "You entered Joane Indra Prasetyawan":
        print("✅ Validasi sukses: Teks yang muncul adalah", promptResult)
    else:
        print("❌ Validasi gagal: Teks yang muncul adalah", promptResult)

except TimeoutException:
    print("❌ Prompt Alert tidak tampil!")

wait_between_steps()  # Jeda antar pengujian

# ===========================================================
# 4. Handle Timer Alert (Delayed Alert)
print("\n🔹 Menguji Timer Alert...")
try:
    driver.find_element(By.ID, "timerAlertButton").click()
    alert = wait.until(EC.alert_is_present())
    print("✅ Timer Alert tampil dengan teks:", alert.text)
    
    wait_between_steps()  # Jeda sebelum klik OK
    alert.accept()
except TimeoutException:
    print("❌ Timer Alert tidak tampil!")

wait_between_steps()  # Jeda antar pengujian

# ===========================================================
# Tutup browser setelah semua pengujian selesai
driver.quit()