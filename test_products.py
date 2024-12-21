import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service
import os

@pytest.fixture(scope="module")
def driver():
    driver_path = r"D:\ДЗ\Edge\msedgedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()

def test_product_list(driver):
     # Открыть веб-страницу
    driver.get("https://testpages.herokuapp.com/styled/index.html")
    
    # Ожидание перехода на нужную страницу
    WebDriverWait(driver, 20).until(
       EC.url_contains("index.html")
    )

    # Переход на страницу с товарами
    link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Fake Products Page"))
    )

    actions = ActionChains(driver)
    actions.move_to_element(link).click().perform()

    # Ожидание загрузки страницы
    WebDriverWait(driver, 20).until(
          EC.url_contains("fake-products-page.html")
    )
        
    # Ожидание появления списка товаров
    product_list = WebDriverWait(driver, 20).until(
          EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products li"))
    )
        
      # Проверка, что список товаров не пуст
    assert len(product_list) > 0
        
      # Проверка, что у каждого товара есть имя и цена
    for product in product_list:
      name = product.find_element(By.CSS_SELECTOR, ".name").text
      price = product.find_element(By.CSS_SELECTOR, ".price").text
      assert name != ""
      assert price != ""
        
     # Дополнительная проверка, что есть хотя бы один товар с названием "Socks"
    socks_present = any("Socks" in item.text for item in product_list)
    assert socks_present