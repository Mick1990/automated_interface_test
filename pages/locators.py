from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    ITEMS_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")
    PRICE_BASKET = (
        By.XPATH,
        "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//p",
    )
    PRICE_ITEM = (By.XPATH, "//div[@class='col-sm-6 product_main']//p")
    URL_PRODUCT_PAGE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    URL_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"


class BasePageLocators:
    URL_START_PAGE = "http://selenium1py.pythonanywhere.com/"
    BACKET_CLEAR = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    INPUT_EMAIL = (By.ID, "id_registration-email")
    INPUT_PASS = (By.ID, "id_registration-password1")
    INPUT_PASS2 = (By.ID, "id_registration-password2")
    BUTTON_REG = (By.NAME, "registration_submit")
