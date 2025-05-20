from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import locators
from src.pages.login_page import LoginPage
from src.data import STELLAR_BURGER_URL
import allure


class AccountPage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаем на вкладку 'История заказов'")
    def click_order_history_section(self):
        self.driver.find_element(*locators.ORDERS_HISTORY).click()
        WebDriverWait(self.driver, 5).until(EC.url_contains("order-history"))


    @allure.step("Получаем айди заказа на вкладке 'История заказов'")
    def collect_order_id(self):
        order_id = self.driver.find_element(*locators.ORDER_ID).text

        return order_id


    @allure.step("Нажимаем кнопку 'Выход'")
    def click_logout_button(self):
        self.driver.find_element(*locators.LOGOUT_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.url_changes(f"{STELLAR_BURGER_URL}/account/order-history"))

    @allure.step("Проверяем успешность логаута")
    def check_logout_is_successful(self):
        assert "login" in self.driver.current_url, f"Текущая страница: {self.driver.current_url}"
