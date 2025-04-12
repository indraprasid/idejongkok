import pytest # type: ignore
import logging
import re

from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore

@pytest.fixture(scope="function")
def browser():
    options = Options()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "Saucedemo Automation Test Report"

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Project: Saucedemo End to End Test"])

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