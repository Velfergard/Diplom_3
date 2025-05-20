import allure
from src import data
from src.pages.orders_list_page import OrdersListPage


class TestOrdersListPage:

    @allure.title("Проверка открытия окна с информацией о заказе")
    @allure.description("Проверяем, что после клика на заказ в 'Ленте заказов' открывается окно с информацией об этом заказе.")
    def test_order_details_window_is_opened_success(self, driver):
        page = OrdersListPage(driver)

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_orders_list_section()
        page.click_on_order_from_orders_list()
        page.check_order_details_is_opened()


    @allure.title("Проверка наличия заказа из 'Истории заказов' пользователя в 'Ленте заказов'")
    @allure.description("Проверяем, что заказ из 'Истории заказов' пользователя отображается в 'Ленте заказов'.")
    def test_order_from_personal_account_is_shown_in_orders_list(self, driver, create_new_order):
        page = OrdersListPage(driver)
        user = create_new_order[0]

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_sign_in_button()
        page.login(email=user["email"], password=user["password"])
        page.click_on_personal_account_button()
        page.click_order_history_section()
        order_id = page.collect_order_id()
        page.click_on_orders_list_section()
        page.check_order_from_pa_is_shown(order_id)


    @allure.title("Проверка работы счетчика всех выполненных заказов")
    @allure.description("Проверяем, что после создания заказа счетчик всех выполненных заказов увеличивается.")
    def test_check_orders_all_counter_raises(self, driver, create_new_user, get_ingredients, stellar_burger_api):
        page = OrdersListPage(driver)
        token = create_new_user[1]
        order_data = {
            "ingredients": get_ingredients[:3]
        }

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_orders_list_section()
        counter_before = page.collect_orders_all_counter_value_before_order()
        order = stellar_burger_api.create_order(token, order_data)
        page.check_orders_all_counter_value_after_order(counter_before)


    @allure.title("Проверка работы счетчика выполненных за сегодня заказов")
    @allure.description("Проверяем, что после создания заказа счетчик выполненных за сегодня заказов увеличивается.")
    def test_check_orders_today_counter_raises(self, driver, create_new_user, get_ingredients, stellar_burger_api):
        page = OrdersListPage(driver)
        token = create_new_user[1]
        order_data = {
            "ingredients": get_ingredients[3:5]
        }

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_orders_list_section()
        counter_before = page.collect_orders_today_counter_value_before_order()
        order = stellar_burger_api.create_order(token, order_data)
        page.check_orders_today_counter_value_after_order(counter_before)


    @allure.title("Проверка попадания нового заказа в раздел 'В работе'")
    @allure.description("Проверяем, что после создания заказ попадает в раздел 'В работе' в 'Ленте Заказов'.")
    def test_new_order_moves_to_orders_in_progress(self, driver, create_new_user, get_ingredients, stellar_burger_api):
        page = OrdersListPage(driver)
        token = create_new_user[1]
        order_data = {
            "ingredients": get_ingredients[:1]
        }

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_orders_list_section()
        order = stellar_burger_api.create_order(token, order_data)
        order_id = int(order.json()["order"]["number"])
        page.check_order_id_in_orders_in_progress(order_id)
