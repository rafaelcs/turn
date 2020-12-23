from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from locators.information_page_locators import InformationPageLocators

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def visit(self, url='https://partners.turning.io/apply/Turn%20Technologies/P5444771180?do_checks=false'):
        self.driver.get(url)
        self.wait_visibility_of(*InformationPageLocators.FIRST_NAME_TEXT_FIELD)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_visibility_of(self, *locator, timeout=30, custom_message=None):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=custom_message
        )

    def click(self, locator):
        self.find_element(*locator).click()

    def send_keys(self, locator, text: str):
        self.find_element(*locator).send_keys(text)

    def select_value_from_dropdown(self, locator, expected_value: str):
        self.click(locator)
        self.wait_visibility_of(*InformationPageLocators.OPTIONS_FROM_DROPDOWN)

        for option in self.find_elements(*InformationPageLocators.OPTIONS_FROM_DROPDOWN):
            if option.text.lower() == expected_value.lower():
                option.click()
                break
        else:
            raise ValueError(f'The value {expected_value} does not exist')