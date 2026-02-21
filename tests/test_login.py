import pytest
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from config import TestUsers

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    return page

def test_successful_login(driver, login_page):
    user = TestUsers.STANDARD_USER
    login_page.enter_username(user.login)   
    login_page.enter_password(user.password)
    login_page.click_login()
    
    catalog_page = CatalogPage(driver)
    assert catalog_page.is_login_successful(), "Authorization is successful"


def test_login_wrong_password(login_page):  #ToDO Сделай перезапуск приложения после выполнения теста
    user = TestUsers.STANDARD_USER
    login_page.enter_username(user.login)
    login_page.enter_password('password1')
    login_page.click_login()

    assert login_page.is_displayed_message_wrong_password(), "Correct message about wrong password"

def test_login_empty_error_message(login_page):
    login_page.enter_username('')
    login_page.enter_password('password1')
    login_page.click_login()

    assert login_page.is_displayed_message_empty_login(), 'Correct message about empty login`s field'

def test_password_empty_error_message(login_page):
    login_page.enter_username('test')
    login_page.enter_password('')
    login_page.click_login()

    assert login_page.is_displayed_message_empty_password(), 'Correct message about empty password`s field'

def test_login_locked_user(login_page):
    user = TestUsers.LOCKED_USER
    login_page.enter_username(user.login)
    login_page.enter_password(user.password)
    login_page.click_login()

    assert login_page.is_displayed_message_locked_user(), 'Correct message about login locked user'

def test_login_problem_user(driver, login_page):
    user = TestUsers.PROBLEM_USER
    login_page.enter_username(user.login)
    login_page.enter_password(user.password)
    login_page.click_login()

    catalog_page = CatalogPage(driver)
    assert catalog_page.is_login_successful(), "Authorization is successful"