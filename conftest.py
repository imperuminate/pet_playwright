import pytest
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture()
def login_page(page):
    return LoginPage(page)

@pytest.fixture()
def registration_page(page):
    return RegistrationPage()