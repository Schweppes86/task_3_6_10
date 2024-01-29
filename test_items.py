from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_good_to_cart(browser):
    browser.get(link)
    assert WebDriverWait(browser, 10) \
        .until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form button"))), \
        "Button is not displayed on page"
