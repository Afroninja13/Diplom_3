import allure
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step('Проверка отображения заголовка страницы "Личный кабинет"')
    def check_account_logo_is_displayed(self):
        return self.find_element_with_wait(AccountPageLocators.LOGO_MAIN).is_displayed()

    @allure.step('Клик по вкладке "История заказов"')
    def click_on_tab_order_history(self):
        self.click_on_element(AccountPageLocators.TAB_ORDDER_HISTORY)

    @allure.step('Проверка активности вкладки "История заказов"')
    def check_tab_order_history_is_active(self):
        return self.find_element_with_wait(
            AccountPageLocators.TAB_ORDDER_HISTORY).get_attribute('class').__contains__('Account_link_active')

    @allure.step('Клик по вкладке "Выход"')
    def click_on_tab_exit(self):
        self.click_on_element(AccountPageLocators.TAB_EXIT)

    @allure.step('Получение номера заказа')
    def get_order_number_text(self):
        return self.find_element_with_wait(AccountPageLocators.ORDER_NUMBER).text
