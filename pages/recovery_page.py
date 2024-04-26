import allure
from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):

    @allure.step('Проверка отображения заголовка страницы восстановления пароля')
    def check_recovery_logo_text_is_displayed(self):
        return self.find_element_with_wait(RecoveryPageLocators.LOGO_TEXT).is_displayed()

    @allure.step('Ввод значения в поле email')
    def input_value_in_email_field(self, email):
        self.input_value_in_field(RecoveryPageLocators.FIELD_EMAIL, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_on_recovery_btn(self):
        self.click_on_element(RecoveryPageLocators.BTN_RECOVERY)
