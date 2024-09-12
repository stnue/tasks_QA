import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.game_page import Game
from pages.game_page import Game
from selenium.webdriver.common.by import By
import re

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    #driver.set_window_size(width=1000, height=1000)
    yield driver
    driver.quit()


