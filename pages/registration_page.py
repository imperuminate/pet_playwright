import allure
from playwright.sync_api import expect
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    page_url = 'customer/account/create/'

    @allure.step('Enter first name')
    def enter_name(self, name):
        name_field = self.find_locator('#firstname')
        name_field.fill(name)

    @allure.step('Enter last name')
    def enter_last_name(self, last_name):
        last_name_field = self.find_locator('#lastname')
        last_name_field.fill(last_name)

    @allure.step('Enter email')
    def enter_email(self, email):
        email_field = self.find_locator('#email_address')
        email_field.fill(email)


    @allure.step('Enter password')
    def enter_password(self, password):
        password_field = self.find_locator('#password.input-text')
        password_field.fill(password)


    @allure.step('Confirm password')
    def confirm_password(self, password):
        confirm_password_field = self.find_locator('#password-confirmation')
        confirm_password_field.fill(password)


    @allure.step('Click create accoutn button')
    def click_create_acc_button(self):
        self.page.get_by_title('Create an Account').click()
        
    
    @allure.step('Check')
    def click_create_acc_button(self):
        self.page.get_by_title('Create an Account').click()

    
    @allure.step('Check message')
    def check_message(self, message):
        alert_message = self.find_locator('[data-bind*="html: $parent"]').first
        expect(alert_message).to_contain_text(message)

    
