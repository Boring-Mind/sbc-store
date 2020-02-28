from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from time import perf_counter
from time import sleep


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


def wait_for_menu(driver: webdriver, delay=3):
    """Wait until categories menu is closed.

    delay - max time to wait, in seconds
    """
    try:
        element_invisible = element_is_not_visible(
            (By.CLASS_NAME, 'menu-hidden')
        )
        WebDriverWait(driver, delay).until(
            element_invisible
        )
    except TimeoutException:
        print('Page loading took too much time')


def get_page_height(driver: webdriver) -> int:
    """Get full height of webpage."""
    return int(driver.execute_script(
        'return document.body.parentNode.scrollHeight'
    ))


def take_full_page_screenshot(
    driver: webdriver,
    file_name="screenshot",
    wait_func=None,
    page_width=1920
):
    """Get full page screenshot.

    file_name - name of output screenshot file, without .jpg or .png extension
    wait_func - function, which implements explicit wait for selenium
    page_width - browser screen width

    Screenshots are saved in the same folder with script.
    Files have png format.
    """
    page_height = get_page_height(driver)
    driver.set_window_size(page_width, page_height)

    if wait_func is not None:
        wait_func(driver)

    driver.find_element_by_tag_name('body').screenshot(file_name + ".png")


def get_chrome_driver() -> webdriver:
    """Set chrome driver to headless mode and return instance."""
    options = webdriver.chrome.options.Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def get_firefox_driver() -> webdriver:
    """Set firefox driver to headless mode and return instance."""
    options = webdriver.FirefoxOptions()
    options.set_headless()
    return webdriver.Firefox(options=options)


def benchmark(function, *params):
    """Decorator. Benchmarks function and prints elapsed time.

    function - function to be benchmarked
    *params - parameters, passed to wrapped function
    """
    def wrapper(*params):
        time1 = perf_counter()
        function(*params)
        time2 = perf_counter()
        print(time2 - time1)
    return wrapper


@benchmark
def regression_test(pagename="index", url=""):
    try:
        driver = get_chrome_driver()
        driver.get(r'http://127.0.0.1:8000/' + url)
        sleep(1)
        take_full_page_screenshot(driver=driver, file_name=pagename)
    except Exception as e:
        raise e
    finally:
        driver.quit()


if __name__ == '__main__':
    # regression_test('login', 'login/')
    regression_test()
