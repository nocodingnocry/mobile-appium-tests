import logging
from .base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import allure

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'test-Username')   
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'test-Password')
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN')

    LOCKED_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, 'Sorry, this user has been locked out.')
    WRONG_PASSWORD_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, 'Username and password do not match any user in this service.')
    EMPTY_LOGIN_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, 'Username is required')
    EMPTY_PASSWORD_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, 'Password is required')

    @allure.step("Ввод логина пользователя")
    def enter_username(self, username):
        self.enter_text_slowly(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text_slowly(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def is_displayed_message_wrong_password(self):
        try:
            return self.find_element(self.WRONG_PASSWORD_MESSAGE)
        except NoSuchElementException:
            return False
    
    def is_displayed_message_empty_login(self):
        try:
            return self.find_element(self.EMPTY_LOGIN_MESSAGE)
        except NoSuchElementException:
            return False

    def is_displayed_message_empty_password(self):
        try:
            return self.find_element(self.EMPTY_PASSWORD_MESSAGE)
        except NoSuchElementException:
            return False
    
    def is_displayed_message_locked_user(self):
        try:
            return self.find_element(self.LOCKED_MESSAGE)
        except NoSuchElementException:
            return False