import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.login_page import CustomerLogin
from pages.sale_page import Sale
from pages.search import Search


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('window-size=1920,1080')
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
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