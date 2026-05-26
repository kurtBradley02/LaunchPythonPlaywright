import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def step_01(page):
    logger.info("Navigating to registration page")
    page.goto("https://codepen.io/kurtBradleyJocson/full/VYmMKjj")

    logger.info("Filling Full Name: test")
    page.locator("#result").content_frame.get_by_role("textbox", name="Full Name").click()
    page.locator("#result").content_frame.get_by_role("textbox", name="Full Name").fill("test")

    logger.info("Filling Email Address: test@mail.com")
    page.locator("#result").content_frame.get_by_role("textbox", name="Email Address").click()
    page.locator("#result").content_frame.get_by_role("textbox", name="Email Address").fill("test@mail.com")

    logger.info("Filling Password")
    page.locator("#result").content_frame.get_by_role("textbox", name="Password").click()
    page.locator("#result").content_frame.get_by_role("textbox", name="Password").fill("123456")

    logger.info("Selecting Gender: Male")
    page.locator("#result").content_frame.get_by_role("radio", name="Male", exact=True).check()

    logger.info("Selecting Nationality: Filipino")
    page.locator("#result").content_frame.get_by_label("Nationality").select_option("Filipino")

    logger.info("Clicking Updates span")
    page.locator("#result").content_frame.locator("span").nth(1).click()

    logger.info("Checking terms and conditions")
    page.locator("#result").content_frame.get_by_role("checkbox", name="I agree to the terms and").check()

    logger.info("Accepting privacy policy")
    page.locator("#result").content_frame.get_by_text("I accept the privacy policy").click()

    logger.info("Submitting registration")
    page.locator("#result").content_frame.get_by_role("button", name="Submit Registration").click()

    modal_banner = page.locator("#result").content_frame.get_by_text("Registration Submitted! Name").text_content()
    logger.info("Modal banner text: %s", modal_banner)

    return modal_banner