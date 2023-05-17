import pytest
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    options = Options()
    # options.add_argument('--headless')
    chrome = Chrome(chrome_options=options)
    chrome.implicitly_wait(3)
    chrome.maximize_window()
    chrome.get('http://127.0.0.1:5000/')
    yield chrome
    chrome.quit()


def environment_not_ready():
    try:
        r = requests.head("http://127.0.0.1:5000")
        if r.status_code == 200:
            return False
    except requests.ConnectionError:
        pass

    return True


@pytest.mark.skipif(environment_not_ready(),
                reason="requires app running")
def test_login_form_invalid_username_and_password(browser):
    browser.find_element(By.LINK_TEXT, 'Log in').click()
    WebDriverWait(browser, timeout=3).until(
        lambda d: d.find_element(By.ID, "username")
    )

    browser.find_element(By.ID, "username").send_keys("dummy-user")
    browser.find_element(By.ID, "password").send_keys("dummy-user")
    button = browser.find_element(By.ID, 'submit')
    button.click()

    assert WebDriverWait(browser, timeout=3).until(
        lambda d: d.find_element(By.CLASS_NAME, 'invalid-feedback-username')
    ).text == 'Invalid username'
    assert WebDriverWait(browser, timeout=3).until(
        lambda d: d.find_element(By.CLASS_NAME, 'invalid-feedback-password')
    ).text == 'Invalid password'
