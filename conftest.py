import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture()
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture()
def registration_page(page):
    return RegistrationPage()