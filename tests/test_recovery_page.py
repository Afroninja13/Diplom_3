import allure
from data import TestData
from pages.login_page import LoginPage
from conftest import driver
from pages.recovery_page import RecoveryPage
from pages.reset_page import ResetPage


class TestRecoveryPage:

    @allure.title('Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_on_recovery_pass_btn_redirects_to_recovery_page(self, driver):
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        driver.get(TestData.BASE_URL + TestData.LOGIN_URL)
        login_page.click_on_recovery_pass_btn()
        assert recovery_page.check_recovery_logo_text_is_displayed()

    @allure.title('Тест ввода почты и клика по кнопке «Восстановить»')
    def test_enter_email_value_and_click_on_recovery_btn(self, driver):
        reset_page = ResetPage(driver)
        recovery_page = RecoveryPage(driver)
        driver.get(TestData.BASE_URL + TestData.RECOVERY_PASS_URL)
        recovery_page.input_value_in_email_field('abc@ya.ru')
        recovery_page.click_on_recovery_btn()
        assert reset_page.check_reset_logo_text_is_displayed()
