import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Firefox, FirefoxOptions


# Большинство тестов на firefox падают, куратор сказал сдавать работу как есть.
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = webdriver
    if request.param == 'chrome':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    if request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = Firefox(options=options)
    yield driver
    driver.quit()
