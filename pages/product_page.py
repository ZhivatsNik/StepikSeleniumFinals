from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    #функция должна тыкать кнопку "add to basket"
    def add_to_basket_button_click(self):
        self.add_to_basket_button = self.browser.find_element_by(*ProductPageLocators, ADD_TO_BASKET_BUTTON)
        self.add_to_basket_button.click()

    #функция должна проверить что мы на нужной URL
    def should_be_product_page(self):
        self.current_url = self.browser.getCurrentUrl()
        assert "?promo=newYear" in self.current_url
    
    #функция должна 