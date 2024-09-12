from pages.base_page import BasePage
from components.component import WebElement


class Game(BasePage):
    def __init__(self, driver):
        self.base_url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment/"
        #  локаторы
        self.back_to_main_button = WebElement(driver, locator="button[type='button']")

        super().__init__(driver, base_url=None)  # Не передаем base_url, так как он не используется в этом классе

    def get_back_to_main_button(self):
        return self.back_to_main_button.get_element()
