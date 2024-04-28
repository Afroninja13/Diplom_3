import allure
from data import TestData
from conftest import driver
from pages.recovery_page import RecoveryPage
from pages.reset_page import ResetPage


class TestResetPage:
    @allure.title('Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_on_show_hide_pass_activates_field(self, driver):
        reset_page = ResetPage(driver)
        recovery_page = RecoveryPage(driver)
        driver.get(TestData.BASE_URL + TestData.RECOVERY_PASS_URL)
        recovery_page.input_value_in_email_field('abc@ya.ru')
        recovery_page.click_on_recovery_btn()
        reset_page.click_on_show_hide_btn()
        assert reset_page.check_pass_field_is_active
