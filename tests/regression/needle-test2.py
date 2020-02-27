from needle.cases import NeedleTestCase
# from needle.driver import NeedleFirefox
from needle.driver import NeedleChrome
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from time import perf_counter


class element_is_not_visible(object):
    """An expectation for checking that an element has a particular css class.

    locator - used to find the element
    returns the WebElement once it has the particular css class
    """

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if element.is_displayed():
            return False
        else:
            return element

        # options = webdriver.chrome.options.Options()
        # options.add_argument("--headless")
        # return NeedleChrome(chrome_options=options)

def default_regr_test_timing(pagename="index", url=""):
    # print('Enter test')
    time1 = perf_counter()

    options = webdriver.chrome.options.Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    max_height = driver.execute_script(
        'return document.body.parentNode.scrollHeight'
    )
    driver.set_window_size(1920, max_height)
    # print('Driver is set')
    driver.get(r'http://127.0.0.1:8000/' + url)
    delay = 3
    try:
        # print('enter try block')
        element_invisible = element_is_not_visible(
            (By.CLASS_NAME, 'menu-hidden')
        )
        WebDriverWait(driver, delay).until(
            element_invisible
        )
        # print('Element is loaded successfully')
    except TimeoutException:
        print('Page loading took too much time')

    time2 = perf_counter()
    print(time2 - time1)
    # print('Test is done')


default_regr_test_timing('login', 'login/')