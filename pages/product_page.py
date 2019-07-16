from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_add_correct_product_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_added_message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_BASKET_MESSAGE)
        assert product_name.text == product_added_message.text, "Incorrect product added to basket."
