import allure
from playwright.sync_api import expect
from pages.base_page import BasePage


class ForgotPassPage(BasePage):

    page_url = 'customer/account/forgotpassword/'

    @allure.step('Enter email')
    def enter_email(self, email):
        email_field = self.find_locator('#email_address')
        email_field.press_sequentially(email)

    @allure.step('Click reset password button')
    def click_reset_button(self):
        self.find_locator('.action.submit').click()


        
    