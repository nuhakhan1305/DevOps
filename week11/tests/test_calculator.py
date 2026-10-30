import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://127.0.0.1:50011/"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

def test_addition(driver):
    driver.get(URL)
    time.sleep(5)
    driver.find_element(By.ID, "num1").send_keys("10")
    driver.find_element(By.ID, "num2").send_keys("5")
    driver.find_element(By.ID, "add").click()

    assert driver.find_element(By.ID, "result").text == "15"

def test_subtraction(driver):
    driver.get(URL)
    time.sleep(5)
    driver.find_element(By.ID, "num1").send_keys("10")
    driver.find_element(By.ID, "num2").send_keys("5")
    driver.find_element(By.ID, "sub").click()

    assert driver.find_element(By.ID, "result").text == "5"

def test_multiplication(driver):
    driver.get(URL)
    time.sleep(5)
    driver.find_element(By.ID, "num1").send_keys("10")
    driver.find_element(By.ID, "num2").send_keys("5")
    driver.find_element(By.ID, "mul").click()

    assert driver.find_element(By.ID, "result").text == "50"

def test_division(driver):
    driver.get(URL)
    time.sleep(5)
    driver.find_element(By.ID, "num1").send_keys("10")
    driver.find_element(By.ID, "num2").send_keys("5")
    driver.find_element(By.ID, "div").click()

    assert driver.find_element(By.ID, "result").text == "2"