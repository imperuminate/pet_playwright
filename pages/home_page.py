import allure
from playwright.sync_api import expect
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Check page title')
    def check_page_title(self, title):
        page_title = self.find_locator('.base')
        expect(page_title).to_have_text(title)