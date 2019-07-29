from .pages.base_page import BasePage
from .pages.locators import CartPageLocators
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

# method to check if products are in the basket while user never added any
    def should_not_see_products_in_basket(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS), \
            "Should be no items in basket, but there are some."

# method to check if "empty basket" message is rendered with no products added to basket
    def should_see_empty_basket_message(self):
        assert self.is_element_preset(*CartPageLocators.YOUR_BASKET_IS_EMPTY_MESSAGE), \
            "User should see 'Empty basket' message, but it is not rendered"
