import allure
import pytest

from conftest import driver
from page_objects.main_page import MainPage
from test_data import TestData

class TestMainPageFaq:
    @allure.title('Проверка раздела Вопросы о важном')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_answer_faq)
    def test_correctness_of_the_answers_faq(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_question_faq_section(question_number)
        main_page.click_on_faq_section_question(question_number)
        main_page.wait_answer_faq_section(question_number)
        assert main_page.get_text_faq_section_answer(question_number) == expected_answer