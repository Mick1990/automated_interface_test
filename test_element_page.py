from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.URL_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_the_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.URL_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.URL_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_the_basket()
    page.should_not_be_success_message_v2()
