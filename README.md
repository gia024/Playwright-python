# Playwright with Python Setup and Test Execution Guide

## Steps to Set Up and Run Playwright Tests

### 1. Create a Folder
Create a new directory where you will set up your Playwright project.

### 2. Open Terminal
Navigate to the newly created folder using the terminal.

### 3. Create a Virtual Environment
Run the following command to create a virtual environment:
python3 -m venv venv

### 4. Activate the Virtual Environment
For macOS/Linux:
source venv/bin/activate

For Windows:
venv\Scripts\activate

### 5. Upgrade Pip
Upgrade pip globally:
python3 -m pip install --upgrade pip
Upgrade pip locally:
pip3 install --upgrade pip

### 6. Navigate to the File Path
Move to the directory where your test script is located:
cd path/to/file

### 7. Install Playwright
Install Playwright using pip:
pip3 install playwright

### 8. Write a Test Script
Create a Python script (e.g., `test_playwright.py`) and add the following code:
python
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

### 9.Run the Test
Execute the test script using:
python3 test_playwright.py

### Running Playwright Tests with Pytest and Generating Reports
Install Pytest and Pytest-Playwright
Install Pytest and Playwright integration for running tests:
pip3 install pytest pytest-playwright

### Install Pytest-HTML for Generating Reports
To generate an HTML report after test execution, install pytest-html:
pip3 install pytest-html

### Run Tests and Generate an HTML Report
Execute the following command to run the tests and generate an HTML report:
pytest --html=report.html --self-contained-html

This will generate a report.html file containing the test results in a structured format.

This guide walks through setting up Playwright, writing a test script, running tests, and generating an HTML report using Pytest. Following these steps ensures a smooth Playwright testing experience.









