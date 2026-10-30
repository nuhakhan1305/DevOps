
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


def test_google_search_button_exist(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed(), "Google search field not visible"

    search_buttons = driver.find_elements(
        By.XPATH,
        "//input[@name='btnK'] | //button[@aria-label='Google Search']"
    )

    assert any(button.is_displayed() for button in search_buttons), \
        "Google search button not visible"

    print("Google search field and button are visible")
