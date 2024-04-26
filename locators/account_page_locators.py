from selenium.webdriver.common.by import By


class AccountPageLocators:
    TAB_PROFILE = By.XPATH, './/a[text()="Профиль"]'
    TAB_ORDDER_HISTORY = By.XPATH, './/a[text()="История заказов"]'
    TAB_EXIT = By.XPATH, './/button[text()="Выход"]'
    LOGO_MAIN = By.XPATH, './/p[text()="В этом разделе вы можете изменить свои персональные данные"]'
    ORDER_NUMBER = By.XPATH, './/p[@class="text text_type_digits-default"]'
