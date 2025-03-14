import allure
from time import sleep

message = 'There is already an account with this email address.'

@allure.feature('Create an account with existed user data')
def test_create_acc_used_data(registration_page, login_page):
    registration_page.open()
    registration_page.enter_name('Yur')
    registration_page.enter_last_name('And')
    registration_page.enter_email('qaw@gmail.com')
    registration_page.enter_password('1234qwerty!')
    registration_page.confirm_password('1234qwerty!')
    registration_page.click_create_acc_button()
    registration_page.check_message(message)
