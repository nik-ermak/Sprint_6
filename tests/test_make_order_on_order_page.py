import allure
import pytest

from conftest import driver
from test_data import TestData as TD

from page_objects.order_page import OrderPage
from locators.main_page_locators import LocatorsMainPage as LPM


class TestMakeOrder:
    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Использование двух точек входа и 2 набора тестовых данных')
    @pytest.mark.parametrize('enter_button, test_data', [(LPM.make_order_button_header, TD.test_data_1), (LPM.make_order_button_main, TD.test_data_2)])
    def test_make_order_success(self, driver, enter_button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_for_element(enter_button)
        order_page.wait_for_element(enter_button)
        order_page.click_on_element(enter_button)
        order_page.filling_first_form(test_data)
        order_page.filling_second_form(test_data)
        assert order_page.check_button_check_status_of_order()

