import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from time import sleep


class LoginPage(BasePage):
    page_url = '/customer/account/login '


    @allure.step('Enter email')
    def enter_email(self, email):
        email_field = self.find_locator('#email')
        email_field.fill(email)


    @allure.step('Enter password')
    def enter_password(self, password):
        password_field = self.find_locator('#pass')
        password_field.fill(password) 

 
    @allure.step('Click submit button')
    def click_submit_button(self):
        self.find_locator('#send2').click()

    
    @allure.step('Check error message')
    def check_error_message(self, message):
        error_message = self.find_locator('.message-error')
        expect(error_message).to_have_text(message)