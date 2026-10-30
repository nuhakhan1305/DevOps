import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def setup_teardown():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Teardown: Close the browser after the test
    driver.quit()
def test_google_title(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.google.com")
    print("Page title is:", driver.title)
    assert "Google" in driver.title, "Title does not contain 'Google'"
    print("Test passed: Title contains 'Google'")