from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import locators
from src.pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Вводим email на форме авторизации пользователя")
    def input_email_for_auth(self, email):
        self.send_keys(locators.INPUT_EMAIL, email)


    @allure.step("Вводим пароль на форме авторизации пользователя")
    def input_password_for_auth(self, password):
        self.send_keys(locators.INPUT_PASSWORD, password)


    @allure.step("Нажимаем кнопку 'Войти'")
    def click_login_button(self):
        self.find_and_click(locators.LOGIN_BUTTON)
        self.wait_element_to_be_clickable(locators.CREATE_ORDER_BUTTON)


    @allure.step("Сценарий авторизации пользователя")
    def login(self, email, password):
        self.input_email_for_auth(email)
        self.input_password_for_auth(password)
        self.click_login_button()


    @allure.step("Нажимаем на гиперссылку 'Восстановить пароль'")
    def click_reset_password_link(self):
        self.find_and_click(locators.RESET_PASSWORD_LINK)
        self.wait_for_element_located(locators.RESET_PWD_HEADER)
