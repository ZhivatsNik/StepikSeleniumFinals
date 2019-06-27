from .product_page import ProductPage
from .main_page import MainPage

def user_can_click_login_button(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.add_to_basket_button_click()
