import pytest # type: ignore
import logging
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # type: ignore

@pytest.fixture
def setup_browser(): # Setup browser untuk setiap test case
    options = Options()
    # options.add_argument("--headless")  # Uncomment jika ingin jalankan tanpa UI
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(20)  # Implicit Wait 10 detik
    driver.maximize_window()
    
    yield driver  # Return driver untuk digunakan di test
    
    driver.quit()  # Tutup browser setelah pengujian selesai

@pytest.fixture(autouse=True)
def log_test_output(request): # Setup Log Output pada Report HTML di Pytest
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    
    # Pencegahan penamaan file yang dianggap berkarakter ilegal di Windows
    safe_node_id = re.sub(r'[<>:"/\\|?*]', '_', request.node.nodeid)

    # Gunakan nama file yang valid
    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(safe_node_id)
    
    logger.addHandler(handler)

    return logger