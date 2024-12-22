# test_web.py
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import os

@pytest.fixture(scope="module")
def driver():
    """Настройка и очистка браузера Edge для тестов."""
    driver_path = r"D:\ДЗ\Edge\msedgedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

def test_page_title(driver):
    """Тест проверки заголовка страницы."""
    driver.get("https://www.example.com")
    assert driver.title == "Example Domain"

def test_search_example(driver):
    """Тест поиска на example.com (если есть поле поиска)."""
    driver.get("https://www.example.com")
    # На example.com нет поля поиска, поэтому я просто проверяю, что страница загружается и
    # мы можем найти элемент с текстом "Example Domain"
    h1_element = driver.find_element(By.TAG_NAME, "h1")
    assert "Example Domain" in h1_element.text

def test_navigate_to_google(driver):
    """Тест открытия Google и проверки заголовка."""
    driver.get("https://www.google.com")
    assert "Google" in driver.title