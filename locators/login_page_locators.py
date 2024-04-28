from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGO_LOGIN_PAGE = By.XPATH, './/h2[text()="Вход"]'
    BTN_LOGIN = By.XPATH, './/button[text()="Войти"]'
    BTN_RECOVERY_PASS = By.XPATH, './/a[text()="Восстановить пароль"]'
    FIELD_EMAIL = By.XPATH, './/input[@type="text"]'
    FIELD_PASSWORD = By.XPATH, './/input[@type="password"]'
