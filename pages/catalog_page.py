from .base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import logging

logger = logging.getLogger(__name__)

class CatalogPage(BasePage):
    
    PRODUCTS_ZONE = AppiumBy.ACCESSIBILITY_ID, 'test-Cart drop zone'
    PRODUCT_CARD = AppiumBy.ACCESSIBILITY_ID, '//XCUIElementTypeStaticText[string-length(@name) = 1])[1]'
    BUTTON_ADD_PRODUCT = AppiumBy.XPATH, '(//XCUIElementTypeOther[@name="test-ADD TO CART"])[1]'
    BUTTON_REMOVE = AppiumBy.ACCESSIBILITY_ID, 'test-REMOVE'
    LABEL_ON_CART_ICON = AppiumBy.XPATH, '//XCUIElementTypeOther[@name="1"])[4]'

    def click_to_add_product(self):
        self.find_element(self.BUTTON_ADD_PRODUCT).click()

    
    def click_to_remove_button(self):
        self.find_element(self.BUTTON_REMOVE).click()

    def open_to_product_card(self):
        self.find_element(self.PRODUCT_CARD).click()

    def is_login_successful(self) -> bool:
        try:
            return self.find_element(self.PRODUCTS_ZONE).is_displayed()
        except NoSuchElementException:
            return False
        
    def is_product_added_in_cart(self) -> bool:
        try:
            return self.find_element(self.LABEL_ON_CART_ICON).is_displayed()
        except NoSuchElementException:
            return False
        
    def is_shown_button_add(self) -> bool:
        try:
            return self.find_element(self.BUTTON_ADD_PRODUCT).is_displayed()
        except:
            False
    