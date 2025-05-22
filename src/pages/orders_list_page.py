from src.locators import locators
from src.pages.base_page import BasePage
import allure


class OrdersListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Кликаем на заказ на вкладке 'Лента заказов'")
    def click_on_order_from_orders_list(self):
        self.find_and_click(locators.ORDER_ELEMENTS)


    @allure.step("Проверяем, что открылось окно с информацией о заказе")
    def check_order_details_is_opened(self):
        order_window = self.get_element_class(locators.ORDER_WINDOW)

        assert "opened" in order_window, f"Окно с деталями заказа не было открыто"


    @allure.step("Проверяем, что в 'Ленте заказов' отображается заказ из 'Истории заказов' пользователя")
    def check_order_from_pa_is_shown(self, order_id):
        orders = self.find_elements(locators.ORDERS_IDS)
        ids = []

        for order in orders:
            ids.append(order.text)

        assert order_id in ids, f"Заказ {order_id} не был найден в списке заказов"


    @allure.step("Получаем значение счетчика всех заказов до оформления заказа")
    def collect_orders_all_counter_value_before_order(self):
        counter = self.get_element_text(locators.ORDERS_ALL_COUNTER)

        return counter


    @allure.step("Получаем значение счетчика всех заказов после оформления заказа")
    def check_orders_all_counter_value_after_order(self, counter):
        counter_before = counter
        counter_after = self.get_element_text(locators.ORDERS_ALL_COUNTER)

        assert int(counter_after) > int(counter_before), \
            f"Счетчик до заказа: {counter_before}, счетчик после: {counter_after}"


    @allure.step("Получаем значение счетчика сегодняшних заказов до оформления заказа")
    def collect_orders_today_counter_value_before_order(self):
        counter = self.get_element_text(locators.ORDERS_TODAY_COUNTER)

        return counter


    @allure.step("Получаем значение счетчика сегодняшних заказов после оформления заказа")
    def check_orders_today_counter_value_after_order(self, counter):
        counter_before = counter
        counter_after = self.get_element_text(locators.ORDERS_TODAY_COUNTER)

        assert int(counter_after) > int(counter_before), \
            f"Счетчик до заказа: {counter_before}, счетчик после: {counter_after}"


    @allure.step("Проверяем, что созданный заказ попал в раздел 'В работе'")
    def check_order_id_in_orders_in_progress(self, order_id):
        orders = self.find_elements(locators.ORDER_IN_PROGRESS)
        ids = []

        for order in orders:
            ids.append(int(order.text))

        assert order_id in ids, f"Заказ {order_id} не был найден в списке заказов 'В работе'"
