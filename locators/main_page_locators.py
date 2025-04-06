from selenium.webdriver.common.by import By

class LocatorsMainPage:
    # Кнопки в шапке страницы
    make_order_button_header = By.XPATH, "//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"
    status_order_button = By.XPATH, ".//div[@class = 'Header_Link__1TAG7']"
    # Кнопка заказа самоката в основной части страницы
    make_order_button_main = By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']/button[text() = 'Заказать']"
    # Секция с вопросами
    faq_section = By.XPATH, ".//div[@class = 'Home_FAQ__3uVm4']"
    faq_section_questions = {
        1: [By.XPATH, ".//div[@id = 'accordion__heading-0']"],
        2: [By.XPATH, ".//div[@id = 'accordion__heading-1']"],
        3: [By.XPATH, ".//div[@id = 'accordion__heading-2']"],
        4: [By.XPATH, ".//div[@id = 'accordion__heading-3']"],
        5: [By.XPATH, ".//div[@id = 'accordion__heading-4']"],
        6: [By.XPATH, ".//div[@id = 'accordion__heading-5']"],
        7: [By.XPATH, ".//div[@id = 'accordion__heading-6']"],
        8: [By.XPATH, ".//div[@id = 'accordion__heading-7']"]
    }
    faq_section_answers = {
        1: [By.XPATH, './/div[@id="accordion__panel-0"]'],
        2: [By.XPATH, './/div[@id="accordion__panel-1"]'],
        3: [By.XPATH, './/div[@id="accordion__panel-2"]'],
        4: [By.XPATH, './/div[@id="accordion__panel-3"]'],
        5: [By.XPATH, './/div[@id="accordion__panel-4"]'],
        6: [By.XPATH, './/div[@id="accordion__panel-5"]'],
        7: [By.XPATH, './/div[@id="accordion__panel-6"]'],
        8: [By.XPATH, './/div[@id="accordion__panel-7"]']
    }

    # Лого Самокат в шапке страницы
    logo_scooter_header = By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']"
    logo_yandex_header = By.XPATH, "//a[@href='//yandex.ru' and contains(@class, 'Header_LogoYandex__3TSOI')]"
    # Заголовок страницы Дзена
    title_page = By.TAG_NAME, 'title'

    # Заголовок главной страницы
    main_header = By.XPATH, ".//div[contains(@class, 'Home_Header__iJKdX')]"