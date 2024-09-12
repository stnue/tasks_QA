from selenium import webdriver
from pages.main_page import Main
from conftest import browser
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure


@pytest.mark.parametrize("category_name, expected_genre", [
    ("MMORPG", "MMORPG"),
    ("shooter", "Shooter"),
    ("strategy", "Strategy"),
    ("moba", "MOBA"),
    ("racing", "Racing"),
    ("sports", "Sports"),
    ("social", "Social")
])
@allure.title("Проверка фильтрации игр по категории")
@allure.description("Проверка: проверяем, что фильтрация по выбранной категории правильно отображает игры соответствующего жанра.")
def test_filter_category(browser, category_name, expected_genre):
    main_page = Main(browser)
    main_page.visit()  # Переходим на главную страницу
    time.sleep(3)  # Ожидание для загрузки страницы (можно уменьшить при необходимости)
    main_page.select_category.scroll_to_element()  # Прокручиваем и кликаем по категории
    main_page.select_category.click()
    main_page.select_category_by_name(category_name) # Выбираем категорию

    # Ожидаемый результат: все игры на странице после выбора категории должны иметь жанр `expected_genre`

    # Фактический результат: игры на странице после выбора категории

    # Проверяем все страницы на наличие игр с неправильным жанром
    all_invalid_games = main_page.verify_all_games(expected_genre)

    # Если есть игры с неправильным жанром, выводим их в требуемом формате
    if all_invalid_games:
        formatted_invalid_games = "\n".join(all_invalid_games)
        # Отчет о неправильных играх в формате Allure
        allure.attach("Invalid Games Report", formatted_invalid_games, allure.attachment_type.TEXT)

        # Тест не проходит, если есть игры, которые не соответствуют ожидаемому жанру
        assert False, f"Игры, которые не соответствуют выбранной категории:\n{formatted_invalid_games}"


@pytest.mark.parametrize("category_name, reset_category", [
    ("MMORPG", "not_chosen"),
    ("shooter", "not_chosen"),
    ("strategy", "not_chosen"),
    ("moba", "not_chosen"),
    ("racing", "not_chosen"),
    ("sports", "not_chosen"),
    ("social", "not_chosen"),
])
@allure.title("Проверка сброса фильтрации после обновления страницы")
@allure.description("Проверка: проверяем, что после обновления страницы фильтр сбрасывается на категорию 'not chosen'.")
def test_filter_reset_after_refresh(browser, category_name, reset_category):
    main_page = Main(browser)
    main_page.visit()  # Переходим на главную страницу

    # Выбираем категорию фильтра
    main_page.select_category.scroll_to_element()  # Прокручиваем и кликаем по категории
    main_page.select_category.click()
    main_page.select_category_by_name(category_name)  # Выбираем категорию

    # Ожидаемый результат: фильтр должен быть сброшен на "not chosen" после обновления страницы

    browser.refresh()  # Обновляем страницу
    time.sleep(3)  # Ожидание для загрузки страницы после обновления

    # Фактический результат: проверяем состояние фильтра после обновления страницы

    main_page.select_category.click()  # Кликаем по категории, чтобы обновить отображение

    # Проверяем, что фильтр сбросился на категорию "not chosen"
    filter_element = main_page.get_filter_element("not chosen")
    selected_text = filter_element.text

    # Ожидание: фильтр должен быть сброшен на "not chosen"
    assert selected_text == "not chosen", f"Expected category to be 'not chosen', but found '{selected_text}'"

