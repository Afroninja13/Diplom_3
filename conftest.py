from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Firefox, FirefoxOptions
import requests
import pytest
from api_methods.helpers import random_word
from api_methods.api_data import ApiData


@pytest.fixture(scope='function')
def user_model():
    """
    Создает юзера с рандомными email, password, name.
    Возвращает в вызывающую функцию response создания и словарь с email, password, name.
    Удаляет созданного юзера.
    """
    payload = {'email': random_word() + "@ya.ru", 'password': random_word(), 'name': random_word()}
    response_create = requests.post(ApiData.BASE_URL + ApiData.CREATE_USER_URL, data=payload)
    access_token = response_create.json()['accessToken']
    yield {'response_create': response_create, 'payload': payload}
    headers = {'Authorization': access_token}
    requests.delete(ApiData.BASE_URL + ApiData.BASE_USER_URL, headers=headers)


# Большинство тестов на firefox падают, куратор сказал сдавать работу как есть.
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = webdriver
    if request.param == 'chrome':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    if request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = Firefox(options=options)
    yield driver
    driver.quit()
