from selenium.webdriver.common.by import By

class LoginPageLoc:
    login_fill_loc = (By.ID, 'email')
    pass_fill_loc = (By.ID, 'pass')
    button_login_loc = (By.ID, 'send2')
    error_message_loc = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')

class SalePageLoc:
    sale_text_loc = (By.TAG_NAME, 'h1')

class SearchLoc:
    input_loc = (By.ID, 'search')
    result_text_loc = (By.TAG_NAME, 'h1')
