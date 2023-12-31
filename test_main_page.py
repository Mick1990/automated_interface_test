from .pages.locators import BasePageLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = BasePageLocators.URL_START_PAGE
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = BasePageLocators.URL_START_PAGE
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = BasePageLocators.URL_START_PAGE
    page = BasketPage(browser, link)
    page.open()
    page.transition_to_the_basket_of_the_head()
    page.should_be_are_no_items_in_the_basket()
    page.should_be_text_that_the_basket_is_empty()
