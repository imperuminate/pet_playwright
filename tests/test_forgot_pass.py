import allure
from time import sleep


invalid_email = 'test123456qa@gmail.com'
success_message = f'If there is an account associated with {invalid_email} you will receive an email with a link to reset your password.'

@allure.feature('Recover password for existing user')
def test_valid_user_pass_recover(forgot_pass_page):
    forgot_pass_page.open()
    forgot_pass_page.enter_email('rtfgrtfgrtfg0@gmail.com')
    forgot_pass_page.click_reset_button()
    

@allure.feature('Recover password for not existing user')
def test_invalid_user_pass_recover(forgot_pass_page, login_page):
    forgot_pass_page.open()
    forgot_pass_page.enter_email('test123456qa@gmail.com')
    forgot_pass_page.click_reset_button()
    login_page.check_message(success_message)

