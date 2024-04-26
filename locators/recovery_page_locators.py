from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    LOGO_TEXT = By.XPATH, './/div[contains(@class, "Auth_login")]/h2[text()="Восстановление пароля"]'
    FIELD_EMAIL = By.XPATH, './/input[@name="name"]'
    BTN_RECOVERY = By.XPATH, './/button[text()="Восстановить"]'
