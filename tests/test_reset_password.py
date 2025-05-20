import allure
from src import data
from src import helpers
from src.pages.reset_pwd_page import ResetPasswordPage


class TestResetPasswordPage:

    @allure.title("Проверка сценария по восстановлению пароля")
    @allure.description("Проверяем, что после восстановления пароля можно узнать значение нового пароля.")
    def test_password_container_is_active_true(self, driver):
        email = helpers.generate_email()
        reset_pwd_page = ResetPasswordPage(driver)

        reset_pwd_page.go_to_site(data.STELLAR_BURGER_URL)
        reset_pwd_page.click_on_sign_in_button()
        reset_pwd_page.click_reset_password_link()
        reset_pwd_page.reset_password(email)
        reset_pwd_page.click_show_password_icon()
        reset_pwd_page.check_password_container_is_active()
