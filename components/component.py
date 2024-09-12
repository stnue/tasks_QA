from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest

class WebElement:
    def __init__(self, driver, locator='', locator_type="css"):
        self.locator = locator
        self.driver = driver
        self.locator_type = locator_type

    # Ожидает и возвращает элемент, найденный по CSS-селектору
    def get_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.get_by_type(), self.locator))
        )

    # Выполняет клик по элементу
    def click(self):
        self.find_element().click()

    # Находит элемент по заданному локатору
    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    # Находит несколько элементов по заданному локатору
    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    # Возвращает тип локатора (например, по id, name, xpath, css и т.д.)
    def get_by_type(self):
        if self.locator_type == "id":
            return By.ID
        if self.locator_type == "name":
            return By.NAME
        if self.locator_type == "xpath":
            return By.XPATH
        if self.locator_type == "css":
            return By.CSS_SELECTOR
        if self.locator_type == "class":
            return By.CLASS_NAME
        if self.locator_type == "linc":
            return By.LINK_TEXT
        else:
            print("locator type " + self.locator_type + " not correct")
            return False

    # Проверяет, совпадает ли значение указанного CSS-стиля с ожидаемым
    def check_css(self, style, value=""):  # стиль элемента
        return self.find_element().value_of_css_property(style) == value

    # Проверяет существование элемента на странице
    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    # Возвращает текст элемента
    def get_text(self):
        return str(self.find_element().text)

    # Проверяет, виден ли элемент на странице
    def visible(self):
        return self.find_element().is_displayed()

    # Проверяет, соответствует ли количество найденных элементов заданному числу
    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    # Отправляет текст в элемент (например, в поле ввода)
    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    # Выполняет принудительный клик
    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    # Очищает содержимое поля ввода (через выделение и удаление)
    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + "a")
        self.find_element().send_keys(Keys.DELETE)

    # Возвращает значение атрибута элемента, если он существует
    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)
        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    # Прокручивает страницу до элемента
    def scroll_to_element(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);", self.find_element())

    # Получение элемента по его CSS селектору
    def get_element_by_css(self, css_selector):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

    # Возвращает кнопку по её CSS селектору
    def get_button_by_css(self, css_selector):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

    # Проверяет текст элемента по объекту WebElement
    def check_element_text_by_web_element(self, web_element, expected_text):
        try:
            actual_text = web_element.get_text()
            assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
        except TimeoutException:
            pytest.fail(f"Element not found or text mismatch. Current URL: {self.get_url()}")
