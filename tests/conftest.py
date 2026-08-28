import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from pages.login_page import LoginPage


load_dotenv()

CHROME_ARGS = (
    "--headless=new",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-extensions",
    "--disable-blink-features=AutomationControlled",
    "--blink-settings=imagesEnabled=false",
    "--window-size=1920,1080",
)


@pytest.fixture
def driver():
    options = Options()
    for arg in CHROME_ARGS:
        options.add_argument(arg)
    driver = webdriver.Chrome(options=options)

    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def base_url():
    return os.environ["APP_BASE_URL"]


@pytest.fixture
def authorized_user(driver, base_url):
    page = LoginPage(driver)
    page.open(base_url)
    page.login("user", "password")
    yield driver