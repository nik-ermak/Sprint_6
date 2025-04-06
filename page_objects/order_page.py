import allure

from locators.order_page_locators import LocatorsOrderPage as LOP
from page_objects.base_page import BasePage

class OrderPage(BasePage):
    @allure.step('Заполнение первой формы заказа самоката')
    def filling_first_form(self, test_data):
        self.wait_for_element(LOP.title_page_personal_info)
        self.click_on_element(LOP.name_field)
        self.send_keys_to_input(LOP.name_field, test_data[0])
        # Заполнение поля Фамилия
        self.click_on_element(LOP.last_name_field)
        self.send_keys_to_input(LOP.last_name_field, test_data[1])
        # Заполнение поля Адрес
        self.click_on_element(LOP.address_field)
        self.send_keys_to_input(LOP.address_field, test_data[2])
        # Ввод станции метро
        self.click_on_element(LOP.metro_field)
        self.send_keys_to_input(LOP.metro_field, test_data[3])
        # Выбор станции в селекторе
        self.click_on_element(LOP.select_metro_in_dropdown)
        # Ввод номера телефона
        self.click_on_element(LOP.phone_field)
        self.send_keys_to_input(LOP.phone_field, test_data[4])
        # Переход ко второй форме
        self.click_on_element(LOP.next_button)

    @allure.step('Заполнение второй формы заказа самоката')
    def filling_second_form(self, test_data):
        # Ожидание поля для даты и ввод даты доставки
        self.wait_for_element(LOP.date_field)
        self.click_on_element(LOP.date_field)
        self.send_keys_to_input(LOP.date_field, test_data[5])
        # Выбор цвета самоката
        self.click_on_element(LOP.scooter_color_black)
        # Выбор срока аренды
        self.click_on_element(LOP.rental_period_field)
        self.click_on_element(LOP.rental_period_dropdown_menu)
        # Написание комментария для курьера
        self.click_on_element(LOP.comment_field)
        self.send_keys_to_input(LOP.comment_field, test_data[6])
        # Нажатие на кнопку Заказать в форме
        self.click_on_element(LOP.order_button_order_page)
        # Подтверждение заказа
        self.wait_for_element(LOP.order_confirmation_header)
        self.click_on_element(LOP.order_confirmation_yes_button)

    @allure.step('Ввод даты через всплывающий календарь')
    def click_date_in_calendar(self):
        self.click_on_element(LOP.calendar_item)

    @allure.step('Отображение кнопки Просмотра заказа при его подтверждении')
    def check_button_check_status_of_order(self):
        return self.checking_display_an_element(LOP.button_status_order)