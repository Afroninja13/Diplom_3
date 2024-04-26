import allure
from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_btn_personal_account(self):
        self.click_on_element(HeaderPageLocators.BTN_PERSONAL_ACCOUNT)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_btn_constructor(self):
        self.click_on_element(HeaderPageLocators.BTN_CONSTRUCTOR)

    @allure.step('Клик по кнопке "Лента зказов"')
    def click_on_btn_order_feed(self):
        self.click_on_element(HeaderPageLocators.BTN_ORDER_FEED)
