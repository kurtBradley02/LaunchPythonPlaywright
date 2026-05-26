import pytest
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS, BROWSER
import time

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        driver = getattr(p, BROWSER).launch(headless=HEADLESS)
        yield driver
        driver.close()

@pytest.fixture
def context(browser):
    ctx = browser.new_context()
    yield ctx
    ctx.close()

@pytest.fixture
def page(context):
    pg = context.new_page()
    yield pg
    time.sleep(3)
    pg.close()