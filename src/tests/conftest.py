import random
import string

import pytest
from selenium import webdriver

from src.config import Config
from src.helpers.data import UserData
from src.pages.signin_page import SigninPage


@pytest.fixture(scope='function')
def driver():
    chrome = webdriver.Chrome()
    chrome.get(Config.BASE_URL)
    yield chrome
    chrome.quit()


def _rnd(n=5):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


@pytest.fixture
def name():
    return f"name_{_rnd()}"


@pytest.fixture
def lastname():
    return f"lastname_{_rnd()}"


@pytest.fixture
def username():
    return f"username_{_rnd()}"


@pytest.fixture
def email():
    return f"{_rnd()}@example.com"


@pytest.fixture
def password():
    return f"{_rnd()}987"


@pytest.fixture
def authorize(driver):
    signin_page = SigninPage(driver)
    signin_page.fill_email(UserData.USERNAME)
    signin_page.fill_password(UserData.PASSWORD)
    recipes_page = signin_page.click_auth()
    return recipes_page
