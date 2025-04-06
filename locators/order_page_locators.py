from selenium.webdriver.common.by import By

class LocatorsOrderPage:
    # Страница Для кого самокат
    # Форма Для кого самокат
    form_one = By.XPATH, ".//div[@class = 'Order_Content__bmtHS']"
    title_page_personal_info = By.XPATH, ".//div[text()='Для кого самокат']"
    # Поле Имя
    name_field = By.XPATH, ".//input[@placeholder = '* Имя']"
    # Поле Фамилия
    last_name_field = By.XPATH, ".//input[@placeholder = '* Фамилия']"
    # Поле Адрес
    address_field = By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"
    # Поле для выбора метро
    metro_field = By.XPATH, ".//input[@placeholder = '* Станция метро']"
    select_metro_in_dropdown = By.XPATH, ".//li[@class='select-search__row']"
    # Поле для ввода номера телефона
    phone_field = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    # Кнопка Далее
    next_button = By.XPATH, ".//button[text() = 'Далее']"

    # Страница Про аренду
    title_page_rent_info = By.XPATH, ".//div[text()='Про аренду']"
    #Поле Когда привезти самокат и всплывающий календарь
    date_field = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    calendar = By.XPATH, ".//div[@class = 'react-datepicker-popper']"
    calendar_item = By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]"
    # Поле Срок аренды
    rental_period_field = By.XPATH, ".//div[text()='* Срок аренды']"
    rental_period_dropdown_menu = By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='двое суток']"
    # Выбор цвета
    scooter_color_black = By.XPATH, ".//label[@for = 'black']"
    # Поле Комментарий для курьера
    comment_field = By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"
    # Кнопка Заказать и Назад
    order_button_order_page = By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()= 'Заказать']"
    back_button = By.XPATH, ".//button[text() = 'Назад']"
    # Окно подтверждения заказа
    order_confirmation_header = By.XPATH, ".//div[text() = 'Хотите оформить заказ?']"
    order_confirmation_yes_button = By.XPATH, ".//button[text() = 'Да']"
    order_confirmation_no_button = By.XPATH, ".//button[text() = 'Нет']"

    # Окно Заказ оформлен
    button_status_order = By.XPATH, ".//button[text() = 'Посмотреть статус']"
