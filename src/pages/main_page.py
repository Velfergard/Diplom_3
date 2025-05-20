from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from src.locators import locators
from src.pages.base_page import BasePage
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Нажимаем кнопку 'Войти в аккаунт'")
    def click_on_sign_in_button(self):
        self.driver.find_element(*locators.SIGN_IN_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.url_contains("login"))

    @allure.step("Нажимаем кнопку 'Личный Кабинет'")
    def click_on_personal_account_button(self):
        self.driver.find_element(*locators.ACCOUNT_LINK).click()
        WebDriverWait(self.driver, 5).until(EC.url_contains("profile"))

    @allure.step("Переходим на вкладку 'Лента Заказов'")
    def click_on_orders_list_section(self):
        self.driver.find_element(*locators.ORDERS_LIST).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locators.ORDERS_LIST_HEADER))

    @allure.step("Переходим на вкладку 'Конструктор'")
    def click_on_constructor_section(self):
        self.driver.find_element(*locators.CONSTRUCTOR).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locators.CONSTRUCTOR_HEADER))

    @allure.step("Кликаем на выбранный ингредиент")
    def click_on_ingredient(self, ingredient):
        if ingredient == "bun":
            self.driver.find_element(*locators.BUNS_INGREDIENT).click()

        elif ingredient == "sauce":
            self.driver.find_element(*locators.SAUCES_SECTION).click()
            WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element_attribute(locators.SAUCES_IS_CURRENT, "class", "current"))
            self.driver.find_element(*locators.SAUCES_INGREDIENT).click()

        elif ingredient == "filling":
            self.driver.find_element(*locators.FILLINGS_SECTION).click()
            WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element_attribute(locators.FILLINGS_IS_CURRENT, "class", "current"))
            self.driver.find_element(*locators.SAUCES_INGREDIENT).click()

        else:
            raise ValueError(f"Ингредиент {ingredient} не существует")

    @allure.step("Проверяем, что открылось окно с информацией об ингредиенте")
    def check_ingredient_details_window_is_opened(self):
        element = self.driver.find_element(*locators.INGREDIENT_DETAILS).get_attribute("class")

        assert "opened" in element, f"Окно с деталями заказа не было открыто"


    @allure.step("Закрываем окно с информацией об ингредиенте")
    def close_ingredient_details_window(self):
        self.driver.find_element(*locators.CLOSE_DETAILS_BUTTON).click()


    @allure.step("Проверяем, что окно с информацией об ингредиенте закрылось")
    def check_ingredient_details_window_is_closed(self):
        element = self.driver.find_element(*locators.INGREDIENT_DETAILS).get_attribute("class")

        assert "opened" not in element, f"Окно с деталями заказа не закрыто"


    @allure.step("Перетаскиваем булочки в конструктор")
    def add_buns_to_basket(self):
        bun = self.driver.find_element(*locators.BUNS_INGREDIENT)
        basket = self.driver.find_element(*locators.BURGER_BASKET)

        ActionChains(self.driver).drag_and_drop(bun, basket).perform()

    @allure.step("Перетаскиваем соусы в конструктор")
    def add_sauces_to_basket(self):
        self.driver.find_element(*locators.SAUCES_SECTION).click()
        sauce = self.driver.find_element(*locators.SAUCES_INGREDIENT)
        basket = self.driver.find_element(*locators.BURGER_BASKET)

        ActionChains(self.driver).drag_and_drop(sauce, basket).perform()

    @allure.step("Перетаскиваем начинки в конструктор")
    def add_fillings_to_basket(self):
        self.driver.find_element(*locators.FILLINGS_SECTION).click()
        filling = self.driver.find_element(*locators.FILLINGS_INGREDIENT)
        basket = self.driver.find_element(*locators.BURGER_BASKET)

        ActionChains(self.driver).drag_and_drop(filling, basket).perform()

    @allure.step("Собираем бургер")
    def construct_burger(self):
        self.add_buns_to_basket()
        self.add_sauces_to_basket()
        self.add_fillings_to_basket()

    @allure.step("Проверяем счетчик выбранного ингредиента")
    def check_ingredient_counter(self, ingredient):
        if ingredient == "bun":
            assert int(self.driver.find_element(*locators.BUNS_COUNTER).text) == 2, f"Значение счетчика отлично от 2"

        elif ingredient == "sauce":
            assert int(self.driver.find_element(*locators.SAUCES_COUNTER).text) == 1, f"Значение счетчика отлично от 1"

        elif ingredient == "filling":
            assert int(self.driver.find_element(*locators.FILLINGS_COUNTER).text) == 1, f"Значение счетчика отлично от 1"

        else:
            raise ValueError(f"Ингредиент {ingredient} недоступен для выбора")


    @allure.step("Проверяем, что вкладка 'Конструктор' активна")
    def check_constructor_section_is_active(self):
        element = self.driver.find_element(*locators.CONSTRUCTOR).get_attribute("class")

        assert "link_active" in element, f"Вкладка 'Конструктор' не активна"


    @allure.step("Проверяем, что вкладка 'Лента Заказов' активна")
    def check_orders_list_section_is_active(self):
        element = self.driver.find_element(*locators.ORDERS_LIST).get_attribute("class")

        assert "link_active" in element, f"Вкладка 'Лента Заказов' не активна"


    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_on_create_order_button(self):
        self.driver.find_element(*locators.CREATE_ORDER_BUTTON).click()


    @allure.step("Проверяем, что заказ успешно создан и открылось соответствующее окно")
    def check_order_is_created(self):

        assert WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element_attribute(locators.CREATED_ORDER_WINDOW, "class", "opened")),\
            f"Окно об успешном оформлении заказа не открылось"
