import random
import string
import allure
import requests
from api_methods.api_data import ApiData


@allure.step('Создаем рандомное слово из 6 символов')
def random_word():
    return str(''.join(random.choice(string.ascii_letters) for x in range(6))).lower()


@allure.step('Создаем пользователя')
def create_user(email, password, name):
    payload = {'email': email + '@ya.ru', 'password': password, 'name': name}
    response_create = requests.post(ApiData.BASE_URL + ApiData.CREATE_USER_URL, data=payload)
    return response_create


@allure.step('Удаляем пользователем')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    response_delete = requests.delete(ApiData.BASE_URL + ApiData.BASE_USER_URL, headers=headers)
    return response_delete
