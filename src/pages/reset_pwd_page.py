from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import locators
from src.pages.login_page import LoginPage
import allure


class ResetPasswordPage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Вводим email")
    def input_email(self, email):
        self.driver.find_element(*locators.RESET_PWD_EMAIL).send_keys(email)


    @allure.step("Жмем на кнопку 'Восстановить пароль'")
    def click_reset_button(self):
        self.driver.find_element(*locators.RESET_PWD_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.url_contains("reset")
                                            and EC.presence_of_element_located(locators.RESET_PWD_HEADER))


    @allure.step("Восстанавливаем пароль")
    def reset_password(self, email):
        self.input_email(email)
        self.click_reset_button()


    @allure.step("Нажимаем на иконку для показа/сокрытия пароля")
    def click_show_password_icon(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locators.SHOW_PASSWORD_ICON))
        self.driver.find_element(*locators.SHOW_PASSWORD_ICON).click()


    @allure.step("Проверяем, что контейнер с паролем активен, и пароль раскрыт")
    def check_password_container_is_active(self):
        element = self.driver.find_element(*locators.RESET_PWD_CONTAINER).get_attribute("class")

        assert "input_status_active" in element, f"Значение пароля не раскрыто"
