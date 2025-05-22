from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from src.locators import locators
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем ресурс {url}")
    def go_to_site(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locators.ACCOUNT_LINK))

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locator))

    def drag_and_drop(self, elem_from, elem_to):
        return ActionChains(self.driver, 2).drag_and_drop(elem_from, elem_to).perform()

    def find_and_click(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()

    def get_element_class(self, locator):
        return self.find_element(locator).get_attribute("class")

    def get_element_text(self, locator):
        return self.find_element(locator).text

    def send_keys(self, locator, text):
        return self.find_element(locator).send_keys(text)

    def wait_text_to_be_present_in_element_attribute(self, locator, attribute, text):
        return WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element_attribute(locator, attribute, text))

    def wait_url_contains_text(self, text):
        return WebDriverWait(self.driver, 5).until(EC.url_contains(text))

    def wait_for_element_located(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def wait_url_changes(self, url):
        return WebDriverWait(self.driver, 5).until(EC.url_changes(url))
