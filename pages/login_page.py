from pages.base_page import BasePage # импорт базовой страницы (
from pages.locators.locators import LoginPageLoc as Loc



class CustomerLogin(BasePage): # указываем что CustomerLogin дочерний класс от BasePage
                                # для того чтобы использовать методы и элементы которые характерны для все страниц
    page_url = '/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9nZWFyL3dhdGNoZXMuaHRtbA%2C%2C/'
    # при выозове метода open_page, который в BasePage, мы добавим к этой сслыке начало в виде https://magento.softwaretestingboard.com
    def login_user(self, login, password):
        login_fill = self.find(Loc.login_fill_loc) # в метод find описан в BasePage (просто заменяет self.driver.find_element)
        pass_fill = self.find(Loc.pass_fill_loc) # с помощью Loc, мы через импорт обращаемся к файлу, где собраны все локаторы для каждого элемента на странице
        button_login = self.find(Loc.button_login_loc)
        login_fill.send_keys(login) # login и password передаем при запуске теста
        pass_fill.send_keys(password)
        button_login.click()

    def check_error_msg(self,massage):
        error_message = self.find(Loc.error_message_loc)
        assert error_message.text == massage