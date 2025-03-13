from playwright.sync_api import Page, Locator
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None


    def __init__(self, page: Page):
        self.page = page


    @allure.step('Open the page')
    def open(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened by URL')
        

    @allure.step('Find element by locator')
    def find(self, locator) -> Locator:
        return self.page.locator(locator)