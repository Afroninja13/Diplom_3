import allure
from conftest import driver, user_model
from data import TestData
from pages.account_page import AccountPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage


class TestAccountPage:

    @allure.title('Тест перехода на вкладку "История заказов" в личном кабинете')
    def test_click_on_tab_order_history_redirects_on_history_page(self, driver, user_model):
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        header_page = HeaderPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        login_page.login_user_step(user_model['payload']['email'], user_model['payload']['password'])
        header_page.click_on_btn_personal_account()
        account_page.click_on_tab_order_history()
        assert account_page.check_tab_order_history_is_active()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('Тест выхода из аккаунта')
    def test_click_on_tab_exit_logs_out_user(self, driver, user_model):
        login_page = LoginPage(driver)
        account_page = AccountPage(driver)
        header_page = HeaderPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        login_page.login_user_step(user_model['payload']['email'], user_model['payload']['password'])
        header_page.click_on_btn_personal_account()
        account_page.click_on_tab_exit()
        assert login_page.check_logo_login_page_is_displayed()
