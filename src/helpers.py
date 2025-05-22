import random
import string
from src.data import email_domains


def gen_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))

    return random_string


def generate_email():
    email = gen_random_string(6) + random.choice(email_domains)

    return email


def generate_user_data():
    email = gen_random_string(6) + random.choice(email_domains)
    password = gen_random_string(10)
    name = gen_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload


def get_randint(a: int, b: int):
    num = random.randint(a, b)

    return num
