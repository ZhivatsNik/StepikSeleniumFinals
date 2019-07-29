from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.cart_page import CartPage
from .pages.product_page import ProductPage
import math
import pytest

class TestUserAddToCartFromProductPage(object):
    #@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        #                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        #                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

    #def test_user_can_add_product_to_cart(self, browser, link):
    #    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207" # link to the page
    #    page = ProductPage(browser, link) #initializing browser to use and link to open
    #    page.open() #opening the link
    #    page.click_add_to_basket() #click on 'add to basket' button
    #    page.solve_quiz_and_get_code() #quiz solving in alert
    #    page.should_add_correct_product_to_basket() #comparing product name with name rendered in message
    #    page.compare_price_with_basket_message() #comparign product price with price rendered in message

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207" # link to the page
        self.page = ProductPage(browser, link) # initializing browser to use and link to open
        self.page.open()  # opening the link
        self.page.should_not_be_success_message() # checking that element is not present

def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207" #link to the page
    page = ProductPage(browser, link)  # initializing browser to use and link to open
    page.open() #opening the link
    page.click_add_to_basket() #click on 'add to basket' button
    page.should_not_be_success_message() #check if element is present on the page





def test_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207" # link to the page
    page = ProductPage(browser, link)  # initializing browser to use and link to open
    page.open() #opening the link
    page.click_add_to_basket() #click on 'add to basket' button
    page.should_disappear_success_message() #check if element disappears on the page

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# method to check is really basket empty
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = CartPage(browser, link)
    page.open()
    page.should_click_on_view_basket_button()
    page.should_not_see_products_in_basket()
    page.should_see_empty_basket_message()