from src.helpers import get_randint
from selenium.webdriver.common.by import By


# Локаторы главной страницы
ACCOUNT_LINK = [By.LINK_TEXT, "Личный Кабинет"]  # кнопка "Личный кабинет" на главной странице
SIGN_IN_BUTTON = [By.XPATH, "//button[text() = 'Войти в аккаунт']"]  # Кнопка "Войти в аккаунт"
CONSTRUCTOR = [By.XPATH, "//p[text() = 'Конструктор']/parent::a[@href = '/']"]  # Раздел "Конструктор" в хедере страницы
ORDERS_LIST = [By.XPATH, "//p[text() = 'Лента Заказов']/parent::a[@href = '/feed']"]  # Раздел "Лента заказов" в хедере страницы
CREATE_ORDER_BUTTON = [By.XPATH, "//button[text() = 'Оформить заказ']"]  # Кнопка "Оформить заказ"
BUNS_SECTION = [By.XPATH, "//span[text() = 'Булки']"]  # Кнопка "Булки" в ингредиентах
BUNS_IS_CURRENT = [By.XPATH, f"{BUNS_SECTION[1]}/.."]  # Название вкладки "Булки" в ингредиентах
SAUCES_SECTION = [By.XPATH, "//span[text() = 'Соусы']"]  # Кнопка "Соусы" в ингредиентах
SAUCES_IS_CURRENT = [By.XPATH, f"{SAUCES_SECTION[1]}/.."]  # Название вкладки "Соусы" в ингредиентах
FILLINGS_SECTION = [By.XPATH, "//span[text() = 'Начинки']"]  # Кнопка "Начинки" в ингредиентах
FILLINGS_IS_CURRENT = [By.XPATH, f"{FILLINGS_SECTION[1]}/.."]  # Название вкладки "Начинки" в ингредиентах
BUNS_HEADER = [By.XPATH, "//h2[text() = 'Булки']"]  # Заголовок "Булки" в ингредиентах
SAUCES_HEADER = [By.XPATH, "//h2[text() = 'Соусы']"]  # Заголовок "Соусы" в ингредиентах
FILLINGS_HEADER = [By.XPATH, "//h2[text() = 'Начинки']"]  # Заголовок "Начинки" в ингредиентах
BUNS_INGREDIENT = [By.XPATH, f"{BUNS_HEADER[1]}/following-sibling::ul[1]/a[{get_randint(1, 2)}]"]  # Выбор булки
SAUCES_INGREDIENT = [By.XPATH, f"{SAUCES_HEADER[1]}/following-sibling::ul[1]/a[{get_randint(1, 4)}]"]  # Выбор соуса
FILLINGS_INGREDIENT = [By.XPATH, f"{FILLINGS_HEADER[1]}/following-sibling::ul[1]/a[{get_randint(1, 9)}]"]  # Выбор начинки
INGREDIENT_DETAILS = [By. XPATH, "//section[contains(@class, 'modal')][1]"]  # Окно с информацией об ингредиенте
CLOSE_DETAILS_BUTTON = [By.XPATH, "//button[contains(@class, 'modal__close')][1]"]  # Кнопка для закрытия окна с инф-ей об ингредиенте
BURGER_BASKET = [By.XPATH, "//ul[contains(@class, 'basket')]"]  # Корзина заказа бургера
BUNS_COUNTER = [By.XPATH, f"{BUNS_INGREDIENT[1]}/div/p[contains(@class, 'counter')]"]  # Счетчик для выбранной булочки
SAUCES_COUNTER = [By.XPATH, f"{SAUCES_INGREDIENT[1]}/div/p[contains(@class, 'counter')]"]  # Счетчик для выбранного соуса
FILLINGS_COUNTER = [By.XPATH, f"{FILLINGS_INGREDIENT[1]}/div/p[contains(@class, 'counter')]"]  # Счетчик для выбранной начинки
CREATED_ORDER_WINDOW = [By.XPATH, "//section[contains(@class, 'modal')]"]  # Окно с ИД оформленного заказа


# Локаторы для разделов главной страницы
CONSTRUCTOR_HEADER = [By.XPATH, "//h1[text() = 'Соберите бургер']"]  # Заголовок раздела "Конструктор"
ORDERS_LIST_HEADER = [By.XPATH, "//h1[text() = 'Лента заказов']"]  # Заголовок раздела "Лента Заказов"


# Локаторы для формы авторизации
INPUT_EMAIL = [By.XPATH, "//input[@name = 'name']"]  # Поле ввода "Email"
INPUT_PASSWORD = [By.XPATH, "//input[@name = 'Пароль']"]  # Поле ввода "Пароль"
LOGIN_BUTTON = [By.XPATH, "//button[text() = 'Войти']"]  # Кнопка "Войти"
RESET_PASSWORD_LINK = [By.LINK_TEXT, "Восстановить пароль"]  # Гиперссылка "Восстановить пароль" на форме авторизации


# Локаторы для восстановления пароля
RESET_PWD_HEADER = [By.XPATH, "//h2[text() = 'Восстановление пароля']"]  # Заголовок раздела "Восстановление пароля"
RESET_PWD_EMAIL = [By.XPATH, "//input[contains(@class, 'textfield')]"]  # Поле ввода "Email"
RESET_PWD_BUTTON = [By.XPATH, "//button[text() = 'Восстановить']"]  # Кнопка "Восстановить"
RESET_PWD_PASSWORD = [By. XPATH, "//input[@name = 'Введите новый пароль']"]  # Поле ввода "Пароль"
RESET_PWD_CONTAINER = [By.XPATH, f"{RESET_PWD_PASSWORD[1]}/parent::div"]  # Контейнер "Пароль"
SHOW_PASSWORD_ICON = [By.CSS_SELECTOR, "div.input > div > svg"]  # Иконка для отображения/сокрытия пароля


# Локаторы для личного кабинета авторизованного юзера
ORDERS_HISTORY = [By.LINK_TEXT, "История заказов"]  # Вкладка "История заказов"
ORDER_INFO = [By.XPATH, "//div[contains(@class, 'OrderHistory')]"]  # Плашка с информацией о заказе
ORDER_ID = [By.XPATH, "//div[contains(@class, 'textBox')]/p[1]"]  # Идентификатор первого заказа
LOGOUT_BUTTON = [By.XPATH, "//button[text() = 'Выход']"]  # Кнопка "Выход"


# Локаторы для вкладки "Лента заказов"
ORDERS_BOX = [By.XPATH, "//div[contains(@class, 'OrderFeed_contentBox')]"]  # Контейнер со списком заказов
ORDER_ELEMENTS = [By.XPATH, f"{ORDERS_BOX[1]}/ul/li"]  # Заказ в списке заказов
ORDERS_IDS = [By.XPATH, "//div[contains(@class, 'textBox')]/p[contains(@class, 'digits')]"]  # Идентификаторы заказов
ORDER_WINDOW = [By.XPATH, "//section[2]"]  # Окно с деталями заказа
ORDERS_ALL = [By.XPATH, "//p[text() = 'Выполнено за все время:']"]  # Блок с выполненными заказами за все время
ORDERS_TODAY = [By.XPATH, "//p[text() = 'Выполнено за сегодня:']"]  # Блок с выполненными заказами за сегодня
ORDERS_ALL_COUNTER = [By.XPATH, f"{ORDERS_ALL[1]}/following-sibling::p"]  # Счетчик выполненных заказов за все время
ORDERS_TODAY_COUNTER = [By.XPATH, f"{ORDERS_TODAY[1]}/following-sibling::p"]  # Счетчик выполненных заказов за сегодня
ORDERS_STATUS = [By.XPATH, "//div[contains(@class, 'orderStatusBox')]"]  # Блок со статусами заказов
ORDER_IN_PROGRESS = [By.XPATH, f"{ORDERS_STATUS[1]}/ul[contains(@class, 'Ready')]/li"]  # Заказы в работе
