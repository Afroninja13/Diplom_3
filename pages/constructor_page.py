import allure
from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step('Проверка отображения заголовка Конструктора')
    def check_constructor_logo_is_displayed(self):
        return self.find_element_with_wait(ConstructorPageLocators.LOGO_CONSTRUCTOR)

    @allure.step('Клик на ингредиент')
    def click_on_btn_ingredient(self):
        self.click_on_element(ConstructorPageLocators.BUN)

    @allure.step('Проверка отображения окна деталей ингредиента')
    def check_logo_ingredient_is_displayed(self):
        return self.find_element_with_wait(ConstructorPageLocators.DETAIL_INGREDIENT).is_displayed()

    @allure.step('Клик на крестик закрытия окна деталей ингредиента')
    def click_on_btn_close_ingredient(self):
        self.click_on_element(ConstructorPageLocators.BTN_CLOSE_INGREDIENT)

    @allure.step('Проверка не отображения окна деталей ингредиента')
    def check_logo_ingredient_is_not_displayed(self):
        return self.find_hidden_element_with_wait(
            ConstructorPageLocators.SECTION_DETAIL_INGREDIENT).get_attribute('class').__contains__('opened')

    @allure.step('Перетаскивание соуса в заказ')
    def move_sause_to_order(self):
        self.move_element_from_to(ConstructorPageLocators.SAUSE, ConstructorPageLocators.BASKET)

    @allure.step('Перетаскивание булки в заказ')
    def move_bun_to_order(self):
        self.move_element_from_to(ConstructorPageLocators.BUN, ConstructorPageLocators.BASKET)

    @allure.step('Проверка увеличения счетчика соуса в заказе')
    def check_ingredient_counter(self):
        return self.find_element_with_wait(ConstructorPageLocators.INGREDIENT_COUNTER).text

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_btn_create_order(self):
        self.click_on_element(ConstructorPageLocators.BTN_CREATE_ORDER)

    @allure.step('Проверка отображения окна с идентификатором заказа')
    def check_logo_order_id_is_displayed(self):
        return self.find_element_with_wait(ConstructorPageLocators.LOGO_ORDER_ID)

    @allure.step('Клик на крестик закрытия окна подтверждения заказа')
    def click_on_btn_close_order_final(self):
        self.click_on_element(ConstructorPageLocators.BTN_CLOSE_ORDER_FINAL)

    @allure.step('Шаг создания заказа с булкой')
    def create_order_step(self):
        self.move_bun_to_order()
        self.click_on_btn_create_order()
        self.click_on_btn_close_order_final()

    @allure.step('Получение номера заказа из окна подтверждения заказа')
    def get_order_number_text_from_final(self):
        self.find_element_with_wait(ConstructorPageLocators.ORDER_NUMBER_FINAL)
        self.wait_for_text_not_template(ConstructorPageLocators.ORDER_NUMBER_FINAL, '9999')
        return self.find_element_with_wait(ConstructorPageLocators.ORDER_NUMBER_FINAL).text
