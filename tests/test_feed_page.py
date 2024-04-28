import allure
from conftest import driver, user_model
from data import TestData
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage


class TestFeedPage:

    @allure.title('Тест отображения окна с деталями заказа при клике на заказ')
    def test_click_on_order_opens_order_details(self, driver):
        feed_page = FeedPage(driver)
        driver.get(TestData.BASE_URL + TestData.FEED_URL)
        feed_page.click_on_order()
        assert feed_page.check_order_detail_is_displayed()

    @allure.title('Тест отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов»')
    def test_orders_from_history_shown_on_order_feed_page(self, driver, user_model):
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)
        header_page = HeaderPage(driver)
        constructor_page = ConstructorPage(driver)
        account_page = AccountPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        login_page.login_user_step(user_model['payload']['email'], user_model['payload']['password'])
        constructor_page.create_order_step()
        header_page.click_on_btn_personal_account()
        account_page.click_on_tab_order_history()
        history_order_number = account_page.get_order_number_text()
        header_page.click_on_btn_order_feed()
        feed_order_number = feed_page.get_order_number_text()
        assert history_order_number == feed_order_number

    @allure.title('Тест увеличения значения общего счетчика заказов при создании нового заказа')
    def test_create_order_increases_common_order_counter_value(self, driver, user_model):
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        header_page = HeaderPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        login_page.login_user_step(user_model['payload']['email'], user_model['payload']['password'])
        header_page.click_on_btn_order_feed()
        order_count_before = feed_page.get_order_count_all_text()
        header_page.click_on_btn_constructor()
        constructor_page.create_order_step()
        header_page.click_on_btn_order_feed()
        order_count_after = feed_page.get_order_count_all_text()
        assert int(order_count_after) == int(order_count_before) + 1

    @allure.title('Тест увеличения значения дневного счетчика заказов при создании нового заказа')
    def test_create_order_increases_daily_order_counter_value(self, driver, user_model):
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        header_page = HeaderPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        login_page.login_user_step(user_model['payload']['email'], user_model['payload']['password'])
        header_page.click_on_btn_order_feed()
        order_count_before = feed_page.get_order_count_today_text()
        header_page.click_on_btn_constructor()
        constructor_page.create_order_step()
        header_page.click_on_btn_order_feed()
        order_count_after = feed_page.get_order_count_today_text()
        assert int(order_count_after) == int(order_count_before) + 1

    @allure.title('Тест отображения номера заказа в разделе "В работе" после его создания')
    def test_created_order_displayed_on_in_progress_section(self, driver, user_model):
        """
        Тест падает без явных ожиданий номера заказа
        - в окне подтверждения заказа
        - в списке заказов которые в работе
        """
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        header_page = HeaderPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        login_page.login_user_step(user_model['payload']['email'], user_model['payload']['password'])
        constructor_page.move_bun_to_order()
        constructor_page.click_on_btn_create_order()
        order_number_create = constructor_page.get_order_number_text_from_final()
        constructor_page.click_on_btn_close_order_final()
        header_page.click_on_btn_order_feed()
        order_number_in_progress = feed_page.get_order_number_text_from_in_progress_section()
        assert '0' + order_number_create == order_number_in_progress
