from .base_page import BasePage
from .locators import CartPageLocators
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    # method to check if products are in the basket while user never added any
    def should_not_see_products_in_basket(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS), \
            "Should be no items in basket, but there are some."

# method to check if "empty basket" message is rendered with no products added to basket
    def should_see_empty_basket_message(self):
        assert self.is_element_preset(*CartPageLocators.YOUR_BASKET_IS_EMPTY_MESSAGE), \
            "User should see 'Empty basket' message, but it is not rendered"
