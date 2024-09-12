from selenium.webdriver.common.by import By
from components.component import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    # Инициализация страницы с WebDriver и базовым URL
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    # Переход на базовый URL
    def visit(self):
        return self.driver.get(self.base_url)

    # Получение текущего URL
    def get_url(self):
        return self.driver.current_url

    # Сравнение текущего URL с базовым URL
    def equal_url(self):
        return self.get_url() == self.base_url

    # Получение заголовка страницы
    def get_title(self):
        return self.driver.title

    # Переход вперед по истории навигации
    def forward(self):
        self.driver.forward()

    # Обновление текущей страницы
    def refresh(self):
        self.driver.refresh()



    def get_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locator))
        )

