from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

# Daftar website yang akan dikunjungi
websites = [
    "https://www.tiket.com",
    "https://www.tokopedia.com",
    "https://www.orangsiber.com",
    "https://www.idejongkok.com",
    "https://www.kelasotomesyen.com"
]

# Konfigurasi Chrome WebDriver
options = Options()
# options.add_argument("--headless")  # Menjalankan di background (opsional)
options.add_experimental_option("detach", True)

# Inisialisasi browser
driver = webdriver.Chrome(options=options)

# Minimize Window
driver.minimize_window()

# Looping melalui setiap website
for site in websites:
    driver.get(site)  # Akses website
    # time.sleep(3)  # Tunggu beberapa detik agar halaman termuat
    
    # Ambil Page Title
    page_title = driver.title
    
    # Cetak hasil
    print(f"{site.replace('https://www.', '')} - {page_title}")

# Tutup browser setelah selesai
driver.quit()