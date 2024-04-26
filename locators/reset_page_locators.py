from selenium.webdriver.common.by import By


class ResetPageLocators:
    LOGO_TEXT = By.XPATH, './/div[contains(@class, "Auth_login")]/h2[text()="Восстановление пароля"]'
    FIELD_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div'
    BTN_SHOW_HIDE_PASS = By.XPATH, './/div[@class="input__icon input__icon-action"]/*'
