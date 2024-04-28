import allure
from locators.reset_page_locators import ResetPageLocators
from pages.base_page import BasePage


class ResetPage(BasePage):

    @allure.step('Проверка отображения заголовка страницы сохранения нового пароля')
    def check_reset_logo_text_is_displayed(self):
        return self.find_element_with_wait(ResetPageLocators.LOGO_TEXT).is_displayed()

    @allure.step('Клик по кнопке показать\скрыть пароль')
    def click_on_show_hide_btn(self):
        self.click_on_element(ResetPageLocators.BTN_SHOW_HIDE_PASS)

    @allure.step('Проверка поля Password на активность')
    def check_pass_field_is_active(self):
        element = self.find_element_with_wait(*ResetPageLocators.FIELD_PASSWORD)
        return element.get_attribute('class').__contains__('active')
