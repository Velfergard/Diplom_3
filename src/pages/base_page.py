from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import locators
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    @allure.step("Открываем ресурс {url}")
    def go_to_site(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locators.ACCOUNT_LINK))
