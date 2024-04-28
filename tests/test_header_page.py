import allure
from conftest import driver, user_model
from data import TestData
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage


class TestHeaderPage:

    @allure.title('Тест перехода в личный кабинет по кнопке "Личный кабинет"')
    def test_click_on_btn_account_redirects_to_personal_account(self, driver, user_model):
        header_page = HeaderPage(driver)
        account_page = AccountPage(driver)
        login_page = LoginPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        login_page.login_user_step(user_model['payload']['email'], user_model['payload']['password'])
        header_page.click_on_btn_personal_account()
        assert account_page.check_account_logo_is_displayed()

    @allure.title('Тест перехода по кнопке "Конструктор"')
    def test_click_on_btn_constructor_redirects_to_constructor_page(self, driver):
        header_page = HeaderPage(driver)
        constructor_page = ConstructorPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        header_page.click_on_btn_constructor()
        assert constructor_page.check_constructor_logo_is_displayed()

    @allure.title('Тест перехода по кнопке "Лента заказов"')
    def test_click_on_btn_order_feed_redirects_to_order_feed_page(self, driver):
        header_page = HeaderPage(driver)
        feed_page = FeedPage(driver)
        driver.get(TestData.BASE_URL)
        header_page.click_on_btn_order_feed()
        assert feed_page.check_order_feed_logo_is_displayed()
