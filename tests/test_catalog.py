import pytest
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from config import TestUsers

@pytest.fixture
def catalog_page(driver):
    page = CatalogPage(driver)
    return page

def test_add_prodruct_to_cart(catalog_page, auth):
    catalog_page.click_to_add_product()

    assert catalog_page.is_product_added_in_cart, 'Product is added successful'

def test_remove_produt_from_cart(catalog_page, auth):
    catalog_page.click_to_add_product()
    catalog_page.click_to_remove_button()

    assert catalog_page.is_shown_button_add, 'Product revomeved from cart'

def test_of_filter_name_desc(catalog_page, auth):
    catalog_page.click_on_filtres()
    catalog_page.click_on_name_desc()

    assert  catalog_page.is_sort_name_desc, 'Sortred by name desc'

def test_change_view_cards(catalog_page, auth):
    catalog_page.click_to_change_view_cards()

    assert catalog_page.is_shown_button_plus, 'Veiw is changed'

def test_logout(driver, catalog_page, auth):
    catalog_page.click_on_menu()
    catalog_page.click_on_logout()

    login_page = LoginPage(driver)

    assert login_page.is_displayed_login, 'Logout is completed'