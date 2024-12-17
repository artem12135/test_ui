import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import CustomerLogin
from pages.sale_page import Sale
from pages.search import Search


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture()
def sale_page(driver):
    return Sale(driver)

@pytest.fixture()
def search(driver):
    return Search(driver)