from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    LOGO_CONSTRUCTOR = By.XPATH, './/h1[text()="Соберите бургер"]'
    DETAIL_INGREDIENT = By.XPATH, './/h2[text()="Детали ингредиента"]'
    SECTION_DETAIL_INGREDIENT = By.XPATH, './/section[contains(@class, "Modal_modal")]'
    BASKET = By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket__list")]'
    INGREDIENT_COUNTER = By.XPATH, './/a[@href = "/ingredient/61c0c5a71d1f82001bdaaa73"]//p[contains(@class, "counter_counter__num")]'
    LOGO_ORDER_ID = By.XPATH, './/p[text()="идентификатор заказа"]'
    ORDER_NUMBER_FINAL = By.XPATH, './/h2[contains(@class, "Modal_modal__title")]'
    BTN_LOGIN_ACCOUNT = By.XPATH, './/button[text()="Войти в аккаунт"]'
    BTN_CREATE_ORDER = By.XPATH, './/button[text()="Оформить заказ"]'
    BUN = By.XPATH, './/a[contains(@href, "61c0c5a71d1f82001bdaaa6d")]'
    BTN_CLOSE_ORDER_FINAL = By.XPATH, './/button[contains(@class, "Modal_modal__close_modified")]'
    SAUSE = By.XPATH, './/a[contains(@href, "61c0c5a71d1f82001bdaaa73")]'
    BTN_CLOSE_INGREDIENT = By.XPATH, './/button[contains(@class, "Modal_modal__close_modified")]'
    ORDER_LOADING_FINAL = By.XPATH, './/*/div/img[contains(@class, "Modal_modal__loading__3534A")]'
