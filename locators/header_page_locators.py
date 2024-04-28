from selenium.webdriver.common.by import By


class HeaderPageLocators:
    BTN_PERSONAL_ACCOUNT = By.XPATH, '//p[text()="Личный Кабинет"]'
    BTN_CONSTRUCTOR = By.XPATH, './/p[text()="Конструктор"]'
    BTN_ORDER_FEED = By.XPATH, './/p[text()="Лента Заказов"]'
