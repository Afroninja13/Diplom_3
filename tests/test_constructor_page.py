import allure
from conftest import driver, user_model
from data import TestData
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


class TestConstructorPage:

    @allure.title('Тест отображения окна деталей ингредиента')
    def test_click_on_btn_ingredient_shows_logo_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        driver.get(TestData.BASE_URL)
        constructor_page.click_on_btn_ingredient()
        assert constructor_page.check_logo_ingredient_is_displayed()

    @allure.title('Тест закрытия окна деталей ингредиента нажатием на крестик')
    def test_click_on_btn_close_closes_logo_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        driver.get(TestData.BASE_URL)
        constructor_page.click_on_btn_ingredient()
        constructor_page.click_on_btn_close_ingredient()
        assert not constructor_page.check_logo_ingredient_is_not_displayed()

    @allure.title('Тест увеличения счетчика ингредиента в заказе при добавлении ингредиента в заказ')
    def test_add_ingredient_to_order_increases_counter_of_ingredients(self, driver):
        constructor_page = ConstructorPage(driver)
        driver.get(TestData.BASE_URL)
        constructor_page.move_sause_to_order()
        assert int(constructor_page.check_ingredient_counter()) == 1

    @allure.title('Тест создания заказа залогиненным пользователем')
    def test_authorized_user_can_create_order(self, driver, user_model):
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        login_page.login_user_step(user_model['payload']['email'], user_model['payload']['password'])
        constructor_page.move_sause_to_order()
        constructor_page.click_on_btn_create_order()
        assert constructor_page.check_logo_order_id_is_displayed()
