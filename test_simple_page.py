import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os

@pytest.fixture(scope="module")
def driver():
    driver_path = r"D:\ДЗ\Edge\msedgedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_page_title(driver):
    driver.get("https://www.example.com")
    assert driver.title == "Example Domain"