import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from cURL import main_page

# фикстура веб-драйвера
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    driver = webdriver.Firefox(options=options)
    driver.get(main_page)
    yield driver
    driver.quit()


