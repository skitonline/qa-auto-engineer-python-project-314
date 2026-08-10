import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv


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


@pytest.fixture(scope="function")
def driver():
    options = Options()
    for arg in CHROME_ARGS:
        options.add_argument(arg)
    driver = webdriver.Chrome(options=options)

    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture(scope="function")
def base_url():
    return os.environ["APP_BASE_URL"]