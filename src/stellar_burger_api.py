import requests
import allure
from src.data import API_URL


class StellarBurgerApi:

    def __init__(self, url):
        self.url = url


    @allure.step("Создаем пользователя по API")
    def create_user(self, payload):
        response = requests.post(f'{API_URL}/auth/register', json=payload)

        return response


    @allure.step("Удаляем пользователя по API")
    def delete_user(self, token):
        response = requests.delete(f'{API_URL}/auth/user', headers={"Authorization": f'{token}'})

        return response


    @allure.step("Получаем список ингредиентов по API")
    def get_ingredients(self):
        response = requests.get(f'{API_URL}/ingredients')

        return response


    @allure.step("Создаем заказ по API")
    def create_order(self, token, payload):
        response = requests.post(f'{API_URL}/orders', headers={"Authorization": f'{token}'}, json=payload)

        return response
