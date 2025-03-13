import allure
from pages.login_page import LoginPage 


@allure.feature('Login using valid credentials')
def test_valid_creds(login_page):
    login_page.open()