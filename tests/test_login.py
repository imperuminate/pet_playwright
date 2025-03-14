import allure


message = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'

@allure.feature('Login using valid credentials')
def test_valid_creds(login_page, home_page):
    login_page.open()
    login_page.enter_email('rtfgrtfgrtfg0@gmail.com')
    login_page.enter_password('rtfgrtfgrtfg0!')
    login_page.click_submit_button()
    home_page.check_page_title('My Account')


@allure.feature('Login using invalid credentials')
def test_invalid_creds(login_page):
    login_page.open()
    login_page.enter_email('test@gmail.com')
    login_page.enter_password('123456qa')    
    login_page.click_submit_button()
    login_page.check_message(message)

