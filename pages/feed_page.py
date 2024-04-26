import allure
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Проверка отображения заголовка Лента заказов')
    def check_order_feed_logo_is_displayed(self):
        return self.find_element_with_wait(FeedPageLocators.LOGO_ORDER_FEED)

    @allure.step('Клик по заказу в Ленте заказов')
    def click_on_order(self):
        self.click_on_element(FeedPageLocators.ORDER)

    @allure.step('Проверка отображения окна деталей заказа')
    def check_order_detail_is_displayed(self):
        return self.find_element_with_wait(FeedPageLocators.ORDER_DETAIL)

    @allure.step('Получение номера заказа')
    def get_order_number_text(self):
        return self.find_element_with_wait(FeedPageLocators.ORDER_NUMBER).text

    @allure.step('Получение количества созданных заказов за все время')
    def get_order_count_all_text(self):
        return self.find_element_with_wait(FeedPageLocators.ORDER_COUNT_ALL).text

    @allure.step('Получение количества созданных заказов за сегодня')
    def get_order_count_today_text(self):
        return self.find_element_with_wait(FeedPageLocators.ORDER_COUNT_TODAY).text

    @allure.step('Получение текста номера заказа в секции "В работе"')
    def get_order_number_text_from_in_progress_section(self):
        self.find_element_with_wait(FeedPageLocators.ORDER_NUMBER_INPROGRESS)
        self.wait_for_text_not_template(FeedPageLocators.ORDER_NUMBER_INPROGRESS, 'Все текущие заказы готовы')
        return self.find_element_with_wait(FeedPageLocators.ORDER_NUMBER_INPROGRESS).text
