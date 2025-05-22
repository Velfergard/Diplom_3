from src.locators import locators
from src.pages.base_page import BasePage
import allure


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Вводим email")
    def input_email(self, email):
        self.send_keys(locators.RESET_PWD_EMAIL, email)


    @allure.step("Жмем на кнопку 'Восстановить пароль'")
    def click_reset_button(self):
        self.find_and_click(locators.RESET_PWD_BUTTON)
        self.wait_url_contains_text("reset")
        self.wait_for_element_located(locators.RESET_PWD_HEADER)


    @allure.step("Восстанавливаем пароль")
    def reset_password(self, email):
        self.input_email(email)
        self.click_reset_button()


    @allure.step("Нажимаем на иконку для показа/сокрытия пароля")
    def click_show_password_icon(self):
        self.find_and_click(locators.SHOW_PASSWORD_ICON)


    @allure.step("Проверяем, что контейнер с паролем активен, и пароль раскрыт")
    def check_password_container_is_active(self):
        element = self.get_element_class(locators.RESET_PWD_CONTAINER)

        assert "input_status_active" in element, f"Значение пароля не раскрыто"
