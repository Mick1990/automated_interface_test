from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def transition_to_the_basket_of_the_head(self):
        basket_btn = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_btn.click()


    def should_be_are_no_items_in_the_basket(self):
        assert self.is_not_element_present(
            *BasePageLocators.BASKET_ITEMS
        ), "В корзине есть товар, но не должно быть"


    def should_be_text_that_the_basket_is_empty(self):
        basket_is_empty = self.browser.find_element(*BasePageLocators.BACKET_CLEAR)
        basket_is_empty_text = basket_is_empty.text
        assert "Ваша корзина пуста" in basket_is_empty_text, f"{basket_is_empty_text}"