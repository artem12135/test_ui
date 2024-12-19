import allure
import pytest


@pytest.mark.smoke
@allure.title('тест неудачного логина')
def test_login(login_page):
    login_page.open_page()
    with allure.step('вводим логин и пароль'):
        login_page.login_user('hdfsdhaf@wqe.es', 'dbfsdnf')
    login_page.check_error_msg( 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.')

