import pytest
from selenium import webdriver
from .pages.login_page import LoginPage
import time


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="ru",
        help="Choose browser: chrome or firefox",
    )


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def user(browser):
    """
    фикстура для авторегистрации
    """
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    email = str(time.time()) + "@fakemail.org"
    page.register_new_user(email, "I1daTYsd1sdTGaJJH")
    page.should_be_authorized_user()
