import allure
from src import data
from src.pages.account_page import AccountPage


class TestPersonalAccount:

    @allure.title("Проверка раздела 'Личный Кабинет'")
    @allure.description("Проверяем, работу раздела 'Личный Кабинет':"
                        "Логин - переход в ЛК - переход в 'Историю заказов' - Логаут")
    def test_personal_account_page(self, driver, create_new_user):
        user = create_new_user
        account_page =  AccountPage(driver)

        account_page.go_to_site(data.STELLAR_BURGER_URL)
        account_page.click_on_sign_in_button()
        account_page.login(email=user[0]["email"], password=user[0]["password"])
        account_page.click_on_personal_account_button()
        account_page.click_order_history_section()
        account_page.click_logout_button()
        account_page.check_logout_is_successful()
