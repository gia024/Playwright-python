# test_playwright.py
from playwright.sync_api import sync_playwright

def test_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch Chromium in headed mode
        page = browser.new_page()
        page.goto("https://www.google.com")
        print("Page title:", page.title())
        browser.close()

if __name__ == "__main__":
    test_playwright()
