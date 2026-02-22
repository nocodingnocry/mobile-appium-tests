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
    TOGGLE_VEIW_CARDS = AppiumBy.ACCESSIBILITY_ID, 'test-Toggle' 
    BUTTON_MENU = AppiumBy.ACCESSIBILITY_ID, 'test-Menu'
    BUTTON_LIST_FILTERS = AppiumBy.XPATH, '//XCUIElementTypeOther[@name="test-Modal Selector Button"]/XCUIElementTypeOther/XCUIElementTypeOther'
    BUTTON_LOGOUT = AppiumBy.ACCESSIBILITY_ID, 'test-LOGOUT'
    BUTTON_FILTER_NAME_DESC = AppiumBy.ACCESSIBILITY_ID, 'Name (Z to A)'
    CARD_PRODUCT_NAME_DESC = AppiumBy.ACCESSIBILITY_ID, 'Test.allTheThings() T-Shirt (Red)'
    BUTTON_PLUS = AppiumBy.XPATH, '(//XCUIElementTypeOther[@name="+"])[2]'


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
        except NoSuchElementException:
            False
    
    def click_to_change_view_cards(self):
        self.find_element(self.TOGGLE_VEIW_CARDS).click()
 
    def click_on_logout(self):
        self.find_element(self.BUTTON_LOGOUT).click()

    def click_on_filtres(self):
        self.find_element(self.BUTTON_LIST_FILTERS).click()

    def click_on_name_desc(self):
        self.find_element(self.BUTTON_FILTER_NAME_DESC).click()

    def is_sort_name_desc(self) -> bool:
        try:
            return self.find_element(self.CARD_PRODUCT_NAME_DESC).is_displayed()
        except NoSuchElementException:
            False 
    
    def is_shown_button_plus(self) -> bool:
        try:
            return self.find_element(self.BUTTON_PLUS).is_displayed()
        except NoSuchElementException:
            False
    
    def click_on_menu(self):
        self.find_element(self.BUTTON_MENU).click()
