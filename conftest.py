import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    s = Service(r"\webdrivers\chromedriver.exe")
    chrome_options = Options()
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()
