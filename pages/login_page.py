import re
import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from time import sleep


class LoginPage(BasePage):
    page_url = 'customer/account/login '


    @allure.step('Enter email')
    def enter_email(self, email):
        email_field = self.find_locator('#email')
        email_field.fill(email)


    @allure.step('Enter password')
    def enter_password(self, password):
        password_field = self.page.get_by_label('Password')
        password_field.fill(password) 

 
    @allure.step('Click submit button')
    def click_submit_button(self):
        self.page.get_by_role('button', name='Sign In').click()


    @allure.step('Check message')
    def check_message(self, message):
        expect(self.page).to_have_url(re.compile('login')) 
        alert_message = self.find_locator('[data-bind*="html: $parent"]').first
        expect(alert_message).to_have_text(message)