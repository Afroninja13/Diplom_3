from selenium.webdriver.common.by import By


class FeedPageLocators:
    LOGO_ORDER_FEED = By.XPATH, './/h1[text()="Лента заказов"]'
    ORDER = By.XPATH, './/a[contains(@class, "OrderHistory_link")]'
    ORDER_DETAIL = By.XPATH, './/div[contains(@class, "Modal_orderBox")]'
    ORDER_NUMBER = By.XPATH, './/p[@class="text text_type_digits-default"]'
    ORDER_COUNT_ALL = By.XPATH, './/p[text() = "Выполнено за все время:"]/following-sibling::p[contains(@class, "OrderFeed_number")]'
    ORDER_COUNT_TODAY = By.XPATH, './/p[text() = "Выполнено за сегодня:"]/following-sibling::p[contains(@class, "OrderFeed_number")]'
    ORDER_NUMBER_INPROGRESS = By.XPATH, '//ul[contains(@class, "ListReady")]/li'
