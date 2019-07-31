import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуем проверку на корректный url адрес
        self.check_current_url = self.browser.current_url
        assert 'login' in self.check_current_url

    def should_be_login_form(self):
        # реализуем проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуем проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

        # method to register new user
    def register_new_user(self, email, password):
        new_user_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        new_user_email.send_keys(email)
        new_user_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        new_user_password.send_keys(password)
        new_user_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        new_user_password_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
