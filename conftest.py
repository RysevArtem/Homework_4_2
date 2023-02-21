import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def browser_max():
    browser.config.window_height = 1600
    browser.config.window_width = 1600
    browser.open('https://google.com')
    yield browser_max


@pytest.fixture(scope="function")
def clear_field():
    yield
    browser.element('[name="q"]').clear()
