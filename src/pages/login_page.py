from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import locators
from src.pages.main_page import MainPage
import allure


class LoginPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Вводим email на форме авторизации пользователя")
    def input_email_for_auth(self, email):
        self.driver.find_element(*locators.INPUT_EMAIL).send_keys(email)


    @allure.step("Вводим пароль на форме авторизации пользователя")
    def input_password_for_auth(self, password):
        self.driver.find_element(*locators.INPUT_PASSWORD).send_keys(password)


    @allure.step("Нажимаем кнопку 'Войти'")
    def click_login_button(self):
        self.driver.find_element(*locators.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locators.CREATE_ORDER_BUTTON))


    @allure.step("Сценарий авторизации пользователя")
    def login(self, email, password):
        self.input_email_for_auth(email)
        self.input_password_for_auth(password)
        self.click_login_button()


    @allure.step("Нажимаем на гиперссылку 'Восстановить пароль'")
    def click_reset_password_link(self):
        self.driver.find_element(*locators.RESET_PASSWORD_LINK).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locators.RESET_PWD_HEADER))
