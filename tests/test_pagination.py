from selenium import webdriver
from pages.main_page import Main
from components.component import WebElement
from conftest import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure


@allure.title("Проверка работы пагинации на главной странице")
@allure.description("Проверка: проверяем, что пагинация позволяет корректно переходить между страницами, и кнопки 'Предыдущая' и ''Следующая' правильно отображаются.")
def test_pagination(browser):
    main_page = Main(browser)
    main_page.visit()  # Переходим на главную страницу

    current_page_number = main_page.get_current_page_number() # Проверяем, что мы на первой странице
    assert current_page_number == 1, "Не на первой странице при загрузке."

    prev_button = main_page.previous_button.get_element() # Проверяем, что кнопка "Предыдущая" отключена на первой странице
    assert prev_button.get_attribute("disabled") or "disabled" in prev_button.get_attribute(
        "class"), "Кнопка 'Предыдущая' должна быть отключена на первой странице."

    next_button = main_page.get_next_button()  # Находим кнопку "Следующая страница"

    # Переходим по страницам и проверяем результаты
    current_page = 1
    while next_button:
        # Проверяем результаты на текущей странице
        results = main_page.get_search_results()
        assert results, "No results found on the page."

        # Ожидаем обновления страницы и наличие новой кнопки "Следующая"
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(next_button)
        )

        next_button = main_page.get_next_button() # Находим кнопку "Следующая страница"

        # Проверяем, если кнопка больше не существует или отключена, то это последняя страница
        if not next_button or next_button.get_attribute("disabled") or "disabled" in next_button.get_attribute("class"):
            break

        next_button.click() # Переходим на следующую страницу
        current_page += 1

    # Ожидаемый результат: после перехода по всем страницам, номер последней страницы должен совпадать с текущим значением
    last_page_number = main_page.get_current_page_number()

    # Фактический результат: проверяем, что текущий номер страницы соответствует ожидаемому
    assert last_page_number == current_page, f"Expected page number to be {current_page}, but found {last_page_number}."
