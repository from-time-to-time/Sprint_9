import os
import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.config import Config
from src.helpers.data import UserData
from src.pages.signin_page import SigninPage


@pytest.fixture(scope="function")
def driver():
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    if selenoid_url:
        # Работа через Selenoid
        options.set_capability("browserName", "chrome")
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": False,
            },
        )

        browser = webdriver.Remote(
            command_executor=selenoid_url,
            options=options,
        )
    else:
        # Локальный запуск
        browser = webdriver.Chrome(options=options)
        browser.get(Config.BASE_URL)

    yield browser
    browser.quit()



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
    signin_page = SigninPage(driver).open()
    signin_page.fill_email(UserData.USERNAME)
    signin_page.fill_password(UserData.PASSWORD)
    recipes_page = signin_page.click_auth()
    return recipes_page
