from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn")
    BASKET_TOTAL_INFO_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_ADDED_TO_BASKET_MESSAGE = (
        By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
