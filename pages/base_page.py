from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим элемент на странице')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Вводим значение в поле')
    def input_value_in_field(self, locator, value):
        self.find_element_with_wait(locator).send_keys(value)

    @allure.step('Находим неотображаемый элемент на странице')
    def find_hidden_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Перетаскивание элемента из одной точки в другую')
    def move_element_from_to(self, source_element, dest_element):
        ActionChains(self.driver).drag_and_drop(self.find_element_with_wait(source_element),
                                                self.find_element_with_wait(dest_element)).perform()

    @allure.step('Ожидание пока не изменится текст в элементе')
    def wait_for_text_not_template(self, locator, template, time=10):
        WebDriverWait(self.driver, time).until_not(expected_conditions.text_to_be_present_in_element(locator, template))
        return self.driver.find_element(*locator)
