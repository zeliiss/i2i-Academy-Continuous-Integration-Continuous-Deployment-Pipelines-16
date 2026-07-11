from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_homepage_title():
    """Örnek web sitesinin başlığını headless modda doğrular."""
    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://example.com")
        assert "Example Domain" in driver.title
    finally:
        driver.quit()