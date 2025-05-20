import allure
import pytest
from src import data
from src.pages.main_page import MainPage
from src.pages.login_page import LoginPage


class TestMainFunctions:

    @allure.title("Проверка успешного перехода на вкладку 'Лента Заказов'")
    @allure.description("Проверяем, что после клика на 'Лента Заказов' происходит переход на соответствующую страницу.")
    def test_move_to_orders_list_section_success(self, driver):
        page = MainPage(driver)

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_orders_list_section()
        page.check_orders_list_section_is_active()


    @allure.title("Проверка успешного перехода на вкладку 'Конструктор'")
    @allure.description("Проверяем, что после клика на 'Конструктор' происходит переход на соответствующую страницу.")
    def test_move_to_constructor_section_success(self, driver):
        page = MainPage(driver)

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_orders_list_section()
        page.click_on_constructor_section()
        page.check_constructor_section_is_active()


    @allure.title("Проверка успешного открытия окна с информацией об ингредиенте")
    @allure.description("Проверяем, что после клика на ингредиент открывается окно с информацией о нем.")

    @pytest.mark.parametrize('ingredient', ['bun', 'sauce', 'filling'])
    def test_open_ingredient_details_success(self, driver, ingredient):
        page = MainPage(driver)

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_ingredient(ingredient)
        page.check_ingredient_details_window_is_opened()


    @allure.title("Проверка успешного закрытия окна с информацией об ингредиенте")
    @allure.description("Проверяем, что после клика на Х происходит закрытие окна с информацией об ингредиенте.")
    def test_close_ingredient_details_by_x_button_success(self, driver):
        page = MainPage(driver)

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_ingredient("bun")
        page.close_ingredient_details_window()
        page.check_ingredient_details_window_is_closed()


    @allure.title("Проверка работы счетчика для булочек")
    @allure.description("Проверяем, что после перетаскивания булочки в конструктор изменяется значение счетчика.")
    def test_buns_counter_is_working(self, driver):
        page = MainPage(driver)

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.add_buns_to_basket()
        page.check_ingredient_counter("bun")


    @allure.title("Проверка работы счетчика для соусов")
    @allure.description("Проверяем, что после перетаскивания соуса в конструктор изменяется значение счетчика.")
    def test_sauces_counter_is_working(self, driver):
        page = MainPage(driver)

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.add_sauces_to_basket()
        page.check_ingredient_counter("sauce")


    @allure.title("Проверка работы счетчика для начинок")
    @allure.description("Проверяем, что после перетаскивания начинки в конструктор изменяется значение счетчика.")
    def test_fillings_counter_is_working(self, driver):
        page = MainPage(driver)

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.add_fillings_to_basket()
        page.check_ingredient_counter("filling")


    @allure.title("Проверка создания заказа под авторизованным пользователем через UI")
    @allure.description("Проверяем, что, собрав бургер в конструкторе, можно оформить заказ под авторизованным юзером")
    def test_create_order_by_authorized_user_order_created(self, driver, create_new_user):
        user = create_new_user
        page = LoginPage(driver)

        page.go_to_site(data.STELLAR_BURGER_URL)
        page.click_on_sign_in_button()
        page.login(email=user[0]["email"], password=user[0]["password"])
        page.construct_burger()
        page.click_on_create_order_button()
        page.check_order_is_created()
