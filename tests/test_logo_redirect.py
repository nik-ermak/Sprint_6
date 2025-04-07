import allure
import pytest

from curl import main_page
from page_objects.main_page import MainPage
from test_data import TestData as TD

class TestLogoRedirect:
    @allure.title('Проверка перехода на страницу Дзена при клике на лого Яндекс')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_on_logo_yandex_header()
        main_page.click_on_logo_yandex_header()
        main_page.switch_to_next_tab()
        assert main_page.get_title_page_dzen() == TD.dzen_title_page

    @allure.title('Проверка перехода на главную страницу по клику на лого Самокат')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_on_logo_scooter_header()
        main_page.click_on_order_button_header()
        main_page.wait_on_logo_scooter_header()
        main_page.click_on_logo_scooter_header()
        main_page.waiting_for_the_main_page_title()
        assert main_page.checking_display_of_main_header()
