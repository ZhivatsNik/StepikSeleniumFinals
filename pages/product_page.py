from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # method to click 'add to basket' button
    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    # method to compare product name with product name rendered in a message
    def should_add_correct_product_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_added_message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_BASKET_MESSAGE)
        assert product_name.text == product_added_message.text, "Incorrect product added to basket."
    
    # method to compare product price with price rendered in a message
    def compare_price_with_basket_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_message_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_INFO_MESSAGE)
        assert product_price.text == basket_message_price.text, "Basket value doesn't match product price"

    # method to check that message disappeares from the product page(using is_disappeared function)
    def should_not_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    # method to chedk user is authorized
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear"
            
