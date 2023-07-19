from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
from .pages.locators import ProductPageLocators


@pytest.mark.guest
class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.URL_PROMO
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = ProductPageLocators.URL_PRODUCT_PAGE
        page = ProductPage(
            browser, link
        )
        page.open()
        page.should_be_added_to_the_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = ProductPageLocators.URL_PRODUCT_PAGE
        page = ProductPage(
            browser, link
        )
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = ProductPageLocators.URL_PRODUCT_PAGE
        page = ProductPage(
            browser, link
        )
        page.open()
        page.should_be_added_to_the_basket()
        page.should_not_be_success_message_v2()

    @pytest.mark.smoke
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = ProductPageLocators.URL_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = ProductPageLocators.URL_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = ProductPageLocators.URL_PRODUCT_PAGE
        page = BasketPage(browser, link)
        page.open()
        page.transition_to_the_basket_of_the_head()
        page.should_be_are_no_items_in_the_basket()
        page.should_be_text_that_the_basket_is_empty()


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:
     # перенёс setup в фикстуру user
    def test_user_cant_see_success_message(self, browser, user):
        link = ProductPageLocators.URL_PRODUCT_PAGE
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


    def test_user_can_add_product_to_basket(self, browser, user):
        link = ProductPageLocators.URL_PROMO
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
