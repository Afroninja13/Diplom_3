import allure
from conftest import driver
from data import TestData
from pages.account_page import AccountPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from api_methods.helpers import random_word, create_user, delete_user


class TestAccountPage:

    def setup_method(self):
        self.email = random_word()
        self.password = random_word()
        self.name = random_word()
        self.response_create = create_user(self.email, self.password, self.name)
        self.access_token = self.response_create.json()['accessToken']

    def teardown_method(self):
        delete_user(self.access_token)

    @allure.title('Тест перехода на вкладку "История заказов" в личном кабинете')
    def test_click_on_tab_order_history_redirects_on_history_page(self, driver):
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        header_page = HeaderPage(driver)
        driver.get(TestData.MAIN_URL + TestData.LOGIN_URL)
        login_page.login_user_step(self.email + '@ya.ru', self.password)
        header_page.click_on_btn_personal_account()
        account_page.click_on_tab_order_history()
        assert account_page.check_tab_order_history_is_active()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('Тест выхода из аккаунта')
    def test_click_on_tab_exit_logs_out_user(self, driver):
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        header_page = HeaderPage(driver)
        driver.get(TestData.MAIN_URL + TestData.LOGIN_URL)
        login_page.login_user_step(self.email + '@ya.ru', self.password)
        header_page.click_on_btn_personal_account()
        account_page.click_on_tab_exit()
        assert login_page.check_logo_login_page_is_displayed()
