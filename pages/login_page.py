from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert (
            self.url.find("login") == -1
        ), "The 'login' substring is present in self.url"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "ТУТ НЕТ ФОРМЫ АВТОРИЗАЦИИ"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "ТУТ НЕТ ФОРМЫ РЕГИСТРАЦИИ"

    def register_new_user(self, email, password):
        self.browser.find_element(*BasePageLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*BasePageLocators.INPUT_PASS).send_keys(
            password
        )
        self.browser.find_element(*BasePageLocators.INPUT_PASS2).send_keys(
            password
        )
        self.browser.find_element(*BasePageLocators.BUTTON_REG).click()
