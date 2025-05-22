from src.locators import locators
from src.pages.base_page import BasePage
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Нажимаем кнопку 'Войти в аккаунт'")
    def click_on_sign_in_button(self):
        self.find_and_click(locators.SIGN_IN_BUTTON)
        self.wait_url_contains_text("login")


    @allure.step("Нажимаем кнопку 'Личный Кабинет'")
    def click_on_personal_account_button(self):
        self.find_and_click(locators.ACCOUNT_LINK)
        self.wait_url_contains_text("profile")


    @allure.step("Переходим на вкладку 'Лента Заказов'")
    def click_on_orders_list_section(self):
        self.find_and_click(locators.ORDERS_LIST)
        self.wait_for_element_located(locators.ORDERS_LIST_HEADER)


    @allure.step("Переходим на вкладку 'Конструктор'")
    def click_on_constructor_section(self):
        self.find_and_click(locators.CONSTRUCTOR)
        self.wait_for_element_located(locators.CONSTRUCTOR_HEADER)


    @allure.step("Кликаем на выбранный ингредиент")
    def click_on_ingredient(self, ingredient):
        if ingredient == "bun":
            self.find_and_click(locators.BUNS_INGREDIENT)

        elif ingredient == "sauce":
            self.find_and_click(locators.SAUCES_SECTION)
            self.wait_text_to_be_present_in_element_attribute(locators.SAUCES_IS_CURRENT,
                                                              "class", "current")
            self.find_and_click(locators.SAUCES_INGREDIENT)

        elif ingredient == "filling":
            self.find_and_click(locators.FILLINGS_SECTION)
            self.wait_text_to_be_present_in_element_attribute(locators.FILLINGS_IS_CURRENT,
                                                              "class", "current")
            self.find_and_click(locators.SAUCES_INGREDIENT)

        else:
            raise ValueError(f"Ингредиент {ingredient} не существует")


    @allure.step("Проверяем, что открылось окно с информацией об ингредиенте")
    def check_ingredient_details_window_is_opened(self):
        element = self.get_element_class(locators.INGREDIENT_DETAILS)

        assert "opened" in element, f"Окно с деталями заказа не было открыто"


    @allure.step("Закрываем окно с информацией об ингредиенте")
    def close_ingredient_details_window(self):
        self.find_and_click(locators.CLOSE_DETAILS_BUTTON)


    @allure.step("Проверяем, что окно с информацией об ингредиенте закрылось")
    def check_ingredient_details_window_is_closed(self):
        element = self.get_element_class(locators.INGREDIENT_DETAILS)

        assert "opened" not in element, f"Окно с деталями заказа не закрыто"


    @allure.step("Перетаскиваем булочки в конструктор")
    def add_buns_to_basket(self):
        bun = self.find_element(locators.BUNS_INGREDIENT)
        basket = self.find_element(locators.BURGER_BASKET)

        self.drag_and_drop(bun, basket)


    @allure.step("Перетаскиваем соусы в конструктор")
    def add_sauces_to_basket(self):
        self.find_and_click(locators.SAUCES_SECTION)
        sauce = self.find_element(locators.SAUCES_INGREDIENT)
        basket = self.find_element(locators.BURGER_BASKET)

        self.drag_and_drop(sauce, basket)


    @allure.step("Перетаскиваем начинки в конструктор")
    def add_fillings_to_basket(self):
        self.find_and_click(locators.FILLINGS_SECTION)
        filling = self.find_element(locators.FILLINGS_INGREDIENT)
        basket = self.find_element(locators.BURGER_BASKET)

        self.drag_and_drop(filling, basket)


    @allure.step("Собираем бургер")
    def construct_burger(self):
        self.add_buns_to_basket()
        self.add_sauces_to_basket()
        self.add_fillings_to_basket()


    @allure.step("Проверяем счетчик выбранного ингредиента")
    def check_ingredient_counter(self, ingredient):
        if ingredient == "bun":
            assert int(self.get_element_text(locators.BUNS_COUNTER)) == 2, f"Значение счетчика отлично от 2"

        elif ingredient == "sauce":
            assert int(self.get_element_text(locators.SAUCES_COUNTER)) == 1, f"Значение счетчика отлично от 1"

        elif ingredient == "filling":
            assert int(self.get_element_text(locators.FILLINGS_COUNTER)) == 1, f"Значение счетчика отлично от 1"

        else:
            raise ValueError(f"Ингредиент {ingredient} недоступен для выбора")


    @allure.step("Проверяем, что вкладка 'Конструктор' активна")
    def check_constructor_section_is_active(self):
        element = self.get_element_class(locators.CONSTRUCTOR)

        assert "link_active" in element, f"Вкладка 'Конструктор' не активна"


    @allure.step("Проверяем, что вкладка 'Лента Заказов' активна")
    def check_orders_list_section_is_active(self):
        element = self.get_element_class(locators.ORDERS_LIST)

        assert "link_active" in element, f"Вкладка 'Лента Заказов' не активна"


    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_on_create_order_button(self):
        self.find_and_click(locators.CREATE_ORDER_BUTTON)


    @allure.step("Проверяем, что заказ успешно создан,, и открылось соответствующее окно")
    def check_order_is_created(self):

        assert self.wait_text_to_be_present_in_element_attribute(locators.CREATED_ORDER_WINDOW,
                                                                 "class", "opened"),\
            f"Окно об успешном оформлении заказа не открылось"
