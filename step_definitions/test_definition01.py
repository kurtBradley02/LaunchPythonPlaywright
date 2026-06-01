import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def step_01(page):
    logger.info("Navigating to google.com")
    page.goto("https://www.google.com/?zx=1780322344236")
    page.get_by_role("combobox", name="Search").click()
    logger.info("Enter search term")
    page.get_by_role("combobox", name="Search").fill("Test")
    logger.info("Searching for test")


