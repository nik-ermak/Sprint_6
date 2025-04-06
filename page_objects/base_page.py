import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import LocatorsMainPage


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Скролл до нужного элемента')
    def scroll_for_element(self, locator, timeout = 10):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout = 10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Проверить отображение элемента на дисплее')
    def checking_display_an_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить заголовок страницы')
    def get_page_title(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(LocatorsMainPage.title_page))
        return self.driver.title
