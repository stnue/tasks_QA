from pages.base_page import BasePage
from components.component import WebElement
from conftest import browser
from components.component import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main(BasePage):

    def __init__(self, driver):
        self.base_url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment/"

        self.select_category = WebElement(driver,
                                          locator="#root > div > div:nth-child(3) > div > div:nth-child(2) > div.ant-select.css-17a39f8")
        self.select_not_chosen = WebElement(driver,
                                            locator="div[title='not chosen'] div[class='ant-select-item-option-content']")
        self.select_mmorpg = WebElement(driver,
                                        locator="div[title='mmorpg'] div[class='ant-select-item-option-content']")
        self.select_shooter = WebElement(driver,
                                         locator="div[title='shooter'] div[class='ant-select-item-option-content']")
        self.select_strategy = WebElement(driver,
                                          locator="div[title='strategy'] div[class='ant-select-item-option-content']")
        self.select_moba = WebElement(driver, locator="div[title='moba'] div[class='ant-select-item-option-content']")
        self.select_racing = WebElement(driver,
                                        locator="div[title='racing'] div[class='ant-select-item-option-content']")
        self.select_sports = WebElement(driver,
                                        locator="div[title='sports'] div[class='ant-select-item-option-content']")
        self.select_social = WebElement(driver,
                                        locator="div[title='social'] div[class='ant-select-item-option-content']")
        self.next_button = WebElement(driver, locator="li.ant-pagination-next")
        self.previous_button = WebElement(driver,
                                    locator="li.ant-pagination-prev")
        self.name_main_page = WebElement(driver,
                                         locator="div[class ='ant-col css-17a39f8'] h1[class ='ant-typography css-17a39f8']")
        self.game_card = WebElement(driver, locator=".ant-card-body")
        # Локаторы для текущей страницы и результатов поиска
        self.current_page_locator = WebElement(driver, "li.ant-pagination-item-active", "css")
        self.search_results_locator = "#root > div > div.ant-list.ant-list-split.ant-list-something-after-last-item.css-17a39f8 > div.ant-spin-nested-loading.css-17a39f8 > div > ul > li"

        super().__init__(driver, self.base_url)

    def verify_all_games(self, expected_genre):  # Проверяет игры на текущей странице и всех последующих страницах на соответствие ожидаемому жанру.

        all_invalid_games = []  # создаем список для всех игр с неправильными жанрами

        while True:
            try:
                # Находим все игры на текущей странице
                games = self.get_game_cards()

                # Проверяем каждую игру на соответствие жанру
                for game in games:
                    game_text = game.text

                    try:
                        # Предполагаем, что информация представлена как "Title: <название игры>\nGenre: <жанр>"
                        game_lines = game_text.split('\n')
                        title = game_lines[0]
                        genre_line = game_lines[3]
                        genre = genre_line.split(': ')[1]  # Извлекаем жанр

                        # Если жанр не соответствует ожидаемому, добавляем в список
                        if genre.lower() != expected_genre.lower():
                            all_invalid_games.append(f"Game: {title}, Genre: {genre}")

                    except Exception as e:
                        print(f"Error processing game text: {game_text}, error: {e}")

                # Проверяем, есть ли кнопка "Следующая" и активна ли она
                next_button = self.get_next_button()

                if next_button.get_attribute("disabled") or "disabled" in next_button.get_attribute("class"):
                    print("Последняя страница достигнута")
                    break  # Если это последняя страница, выходим из цикла

                # Переходим на следующую страницу
                next_button.click()

            except Exception as e:
                print(f"No more pages or an error occurred: {e}")
                break  # Если произошла ошибка или больше нет страниц

        return all_invalid_games  # Возвращаем список всех игр с неправильными жанрами

    def select_category_by_name(self, category_name):  # Выбирает категорию по ее имени.

        category_selector_name = f"select_{category_name.lower()}"

        if hasattr(self, category_selector_name):
            category_selector = getattr(self, category_selector_name)
            category_selector.click_force()
        else:
            raise AttributeError(f"'Main' object has no attribute '{category_selector_name}'")

    # Получает элемент кнопки "Следующая страница" на текущей странице.
    def get_next_button(self):
        return self.next_button.get_element()

    # Ожидание загрузки карточек игр на главной странице
    def get_game_cards(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.game_card.locator)

    # Возвращает элемент фильтра по имени категории. может пригодиться для проверки состояния фильтра
    def get_filter_element(self, category_name):

        filter_locator = f"div.ant-select span[title='{category_name}']"
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, filter_locator))
        )

    # Получение номера текущей страницы.
    def get_current_page_number(self):
        current_page = self.current_page_locator.get_element()
        return int(current_page.text)

    # Ожидает появления всех элементов результатов поиска и возвращает их текст в виде списка
    def get_search_results(self):
        # Ожидаем, пока все элементы списка результатов поиска появятся на странице
        results = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.search_results_locator))
        )
        # Извлекаем и возвращаем текст всех найденных элементов списка результатов
        return [result.text for result in results]
