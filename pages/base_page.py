from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)
        logger.info(f'Opening url {url}')

    def click(self, *locator):
        self.driver.find_element(*locator).click()
        logger.info(f'Clicking on {locator}')

    def find_element(self, *locator):
        logger.info(f'Searching for element {locator}')
        return self.driver.find_element(*locator)

    def input(self, text, *locator):
        logger.info(f"Inputting text '{text}' for element {locator}")
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'Expected {expected_partial_url} not in url'
        )

    def verify_url(self, expected_url):
        self.wait.until(
            EC.url_to_be(expected_url),
            message=f'Expected {expected_url} not in url'
        )
