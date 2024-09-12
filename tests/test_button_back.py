import time
import pytest
import allure
from pages.main_page import Main
from pages.game_page import Game
import random


@allure.title("Проверка возврата на главную страницу")
@allure.description("Проверка: проверяем,что кнопка 'Back to main' возвращает пользователя на главную страницу после перехода по клику на случайную карточку игры.")
def test_back_to_main_button_by_clicking_random_games(browser):
    main_page = Main(browser)
    main_page.visit()  # Переходим на главную страницу
    game_page = Game(browser)
    time.sleep(3)

    # Получаем список карточек игр и кликаем на случайную
    game_cards = main_page.get_game_cards()
    game_card = random.choice(game_cards)
    game_card.click()  # Кликаем по карточке игры
    time.sleep(3)

    # Нажимаем на кнопку "Back to main"
    game_page.back_to_main_button.click()

    # Ожидаемый результат: кнопка "Back to main" возвращает пользователя на главную страницу


    # Фактический результат: проверка успешности перехода на главную страницу
    main_page_name_text = main_page.name_main_page.get_text()
    assert main_page_name_text == "Main Page", f"Expected 'Main Page' text, but got '{main_page_name_text}'"     # Проверяем, что элемент с текстом "Main Page" отображается
