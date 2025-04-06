import allure

from locators.main_page_locators import LocatorsMainPage as LPM
from page_objects.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Клик по кнопке Заказать в шапке')
    def click_on_order_button_header(self):
        self.click_on_element(LPM.make_order_button_header)

    @allure.step('Ожидание кнопки Заказать в шапке')
    def wait_order_button_header(self):
        self.wait_for_element(LPM.make_order_button_header)

    @allure.step('Клик по лого Самокат')
    def click_on_logo_scooter_header(self):
        self.click_on_element(LPM.logo_scooter_header)

    @allure.step('Клик по лого Яндекс')
    def click_on_logo_yandex_header(self):
        self.click_on_element(LPM.logo_yandex_header)

    @allure.step('Ожидание лого Самокат')
    def wait_on_logo_scooter_header(self):
        self.wait_for_element(LPM.logo_scooter_header)

    @allure.step('Ожидание появления лого Самокат')
    def visibility_logo_scooter_header(self):
        self.wait_for_element(LPM.logo_scooter_header)

    @allure.step('Ожидание лого Яндекс')
    def wait_on_logo_yandex_header(self):
        self.wait_for_element(LPM.logo_yandex_header)

    @allure.step('Скролл до Вопросов о важном')
    def scroll_to_faq_section(self):
        self.scroll_for_element(LPM.faq_section)

    @allure.step('Получение текста ответа на вопрос в секции Вопросы о важном')
    def get_text_faq_section_answer(self, test_data):
        return self.get_text_on_element(LPM.faq_section_answers[test_data])

    @allure.step('Кликнуть на нужный вопрос в секции Вопросы о важном')
    def click_on_faq_section_question(self, test_data):
        self.click_on_element(LPM.faq_section_questions[test_data])

    @allure.step('Ожидание загрузки нужного ответа в секции Вопросы о важном')
    def wait_answer_faq_section(self, test_data):
        self.wait_for_element(LPM.faq_section_answers[test_data])

    @allure.step('Ожидание загрузки нужного вопроса в секции Вопросы о важном')
    def wait_question_faq_section(self, test_data):
        self.wait_for_element(LPM.faq_section_questions[test_data])

    @allure.step('Ожидание появления кнопки Заказать в основной части сайта')
    def wait_order_button_main(self):
        self.wait_for_element(LPM.make_order_button_main)

    @allure.step('Клик по кнопке Заказать в основной части сайта')
    def clik_on_order_button_main(self):
        self.click_on_element(LPM.make_order_button_main)

    @allure.step('Ожидание появления заголовка главной страницы')
    def waiting_for_the_main_page_title(self):
        self.wait_for_element(LPM.main_header)

    @allure.step('Проверка отображения заголовка главной страницы')
    def checking_display_of_main_header(self):
        return self.checking_display_an_element(LPM.main_header)