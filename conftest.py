import pytest
import random
from selenium import webdriver
from src import helpers
from src.data import API_URL
from src.stellar_burger_api import StellarBurgerApi


def get_browser(browser):
    if browser == "chrome":
        return webdriver.Chrome()

    elif browser == "firefox":
        return webdriver.Firefox()

    else:
        raise ValueError("Указанный браузер не поддерживается")


@pytest.fixture(params=("chrome", "firefox"))
def driver(request):
    browser = get_browser(request.param)
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser

    browser.quit()


@pytest.fixture()
def stellar_burger_api():

    return StellarBurgerApi(API_URL)


@pytest.fixture()
def create_new_user(stellar_burger_api):
    user_data = helpers.generate_user_data()
    user = stellar_burger_api.create_user(user_data)
    token = user.json()["accessToken"]
    yield user_data, token

    stellar_burger_api.delete_user(token)


@pytest.fixture()
def get_ingredients(stellar_burger_api):
    ingredients_list = []
    response = stellar_burger_api.get_ingredients()

    for ingredient in response.json()["data"]:
        ingredients_list.append(ingredient["_id"])

    return ingredients_list


@pytest.fixture()
def create_new_order(stellar_burger_api, create_new_user, get_ingredients):
    user_data = create_new_user[0]
    token = create_new_user[1]
    ingredients = random.choices(get_ingredients, k=3)
    order_data = {
        "ingredients": ingredients
    }
    order = stellar_burger_api.create_order(token, order_data)

    return user_data, order.json()
