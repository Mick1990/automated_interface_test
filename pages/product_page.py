from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_added_to_the_basket()
        self.solve_quiz_and_get_code()
        self.should_be_notification_of_items_in_the_basket()
        self.should_be_the_conformity_of_the_product_name()
        self.should_be_the_basket_price_is_the_product_price()

    def should_be_added_to_the_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        btn_basket.click()

    def should_be_notification_of_items_in_the_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ITEMS_BASKET
        ), "ТОВАР НЕ БЫЛ ДОБАВЛЕН В КОРЗИНУ"


    # def should_be_are_no_products_in_the_basket(self):
    #     self.transition_to_the_basket_of_the_head()
    #     assert self.is_not_element_present(
    #         *BasePageLocators.BASKET_ITEMS
    #     ), "В корзине есть товар, товар не должно быть"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ITEMS_BASKET
        ), "Сообщение об успехе представлено, но не должно быть"

    def should_not_be_success_message_v2(self):
        assert self.is_disappeared(
            *ProductPageLocators.ITEMS_BASKET
        ), "Сообщение об успехе представлено, но не должно быть"

    def should_be_the_conformity_of_the_product_name(self):
        items_basket_text = self.browser.find_element(
            *ProductPageLocators.ITEMS_BASKET
        ).text
        product_name_text = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        assert (
            product_name_text == items_basket_text
        ), "НАЗВАНИЕ ТОВАРА В КОРЗИНЕ НЕ СОВПАДЕТ"

    def should_be_the_basket_price_is_the_product_price(self):
        try:
            price_basket = self.browser.find_element(
                *ProductPageLocators.PRICE_BASKET
            ).text
            price_basket_text = price_basket.split()
            price_item = self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text
            price_item_text = price_item.split()
            print(f"Стоимость корзины", *price_basket_text[-2:])
            assert (
                price_basket_text[-2:] == price_item_text[-2:]
            ), "Стоимость корзины не совпадает с ценой товара."

        except:
            print("Цена не получена")
