import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_recovery_pass_btn(self):
        self.click_on_element(LoginPageLocators.BTN_RECOVERY_PASS)

    @allure.step('Ввод значения в поле "email"')
    def input_value_in_email_field(self, email):
        self.input_value_in_field(LoginPageLocators.FIELD_EMAIL, email)

    @allure.step('Ввод значения в поле "password"')
    def input_value_in_password_field(self, password):
        self.input_value_in_field(LoginPageLocators.FIELD_PASSWORD, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_on_btn_login(self):
        self.click_on_element(LoginPageLocators.BTN_LOGIN)

    @allure.step('Шаг авторизации с логином {email} и паролем {password}')
    def login_user_step(self, email, password):
        self.input_value_in_email_field(email)
        self.input_value_in_password_field(password)
        self.click_on_btn_login()

    @allure.step('Проверка отображения логотипа "Вход" на странице логина')
    def check_logo_login_page_is_displayed(self):
        return self.find_element_with_wait(LoginPageLocators.LOGO_LOGIN_PAGE).is_displayed()
