from selene import be, have
from selene.support.shared import browser

def test_search(browser_max, clear_field):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
def test_search_negative(browser_max, clear_field):
    browser.element('[name="q"]').type('gjklsfdhgjksdghdskj').press_enter()
    browser.element('.card-section').should(have.text('По запросу gjklsfdhgjksdghdskj ничего не найдено. '))
