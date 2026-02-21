import pytest
import logging
from utils.event_listener import MyListener
from pages.login_page import LoginPage
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from config import TestUsers
from selenium.webdriver.support.events import EventFiringWebDriver

@pytest.fixture(scope="session")
def ios_caps():
    options = XCUITestOptions()
    options.platform_name = 'iOS'
    options.platform_version = '26.2' 
    options.device_name = 'iPhone 17'  # Имя устройства
    options.udid = '7F079710-01F6-4D4B-A4BC-CD7254C6284B' 
    options.app_path = '/Users/alex_luchkin/Code/Appium/iOS.Simulator.SauceLabs.Mobile.Sample.app.2.7.1.app' 
    options.automation_name = 'XCUITest'
    options.bundle_id = 'com.saucelabs.SwagLabsMobileApp'
    options.no_reset = True  # Не сбрасывать app между тестами
    options.full_reset = False
    options.should_terminate_app = True
    options.clear_system_files = True
    return options


# Фикстура для перезапуска приложения между тестами
@pytest.fixture(scope='function') 
def driver(ios_caps):
    base_drv = webdriver.Remote('http://127.0.0.1:4723', options=ios_caps)
    driver = EventFiringWebDriver(base_drv, MyListener())

    yield driver
    bundle_id = 'com.saucelabs.SwagLabsMobileApp'

    try:
        base_drv.terminate_app(bundle_id)
    except:
        pass

    base_drv.activate_app(bundle_id) 

    try:
        WebDriverWait(base_drv, 20).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))    
        )
    except Exception as e:
        print(f"Не дождались экрана логина после перезапуска: {e}")

    base_drv.quit()


@pytest.fixture
def auth(driver):
    login_page = LoginPage(driver)
    user = TestUsers.STANDARD_USER
    login_page.enter_username(user.login)   
    login_page.enter_password(user.password)
    login_page.click_login()
