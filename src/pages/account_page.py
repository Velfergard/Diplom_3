from src.locators import locators
from src.pages.base_page import BasePage
from src.data import STELLAR_BURGER_URL
import allure


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Нажимаем на вкладку 'История заказов'")
    def click_order_history_section(self):
        self.find_and_click(locators.ORDERS_HISTORY)
        self.wait_url_contains_text("order-history")


    @allure.step("Получаем айди заказа на вкладке 'История заказов'")
    def collect_order_id(self):
        order_id = self.get_element_text(locators.ORDER_ID)

        return order_id


    @allure.step("Нажимаем кнопку 'Выход'")
    def click_logout_button(self):
        self.find_and_click(locators.LOGOUT_BUTTON)
        self.wait_url_changes(f"{STELLAR_BURGER_URL}/account/order-history")


    @allure.step("Проверяем успешность логаута")
    def check_logout_is_successful(self):
        assert "login" in self.driver.current_url, f"Текущая страница: {self.driver.current_url}"
