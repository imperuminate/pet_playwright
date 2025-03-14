import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.home_page import HomePage
from pages.forgot_password_page import ForgotPassPage


@pytest.fixture()
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture()
def registration_page(page: Page):
    return RegistrationPage(page)

@pytest.fixture()
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture()
def forgot_pass_page(page: Page):
    return ForgotPassPage(page)
