from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def test_google_title():
    # Set up the Chrome WebDriver
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    print("Page title is:", driver.title)
    assert "Google" in driver.title, "Title does not contain 'Google'"
    print("Test passed: Title contains 'Google'")
    driver.quit()
if __name__ == "__main__":
    test_google_title()