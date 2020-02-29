from selenium import webdriver
from time import sleep
import os


SCREENSHOTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'screenshots')
)

BASELINE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'screenshots', 'baseline')
)


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

    screenshots_dir = './screenshots/'

    if not os.path.exists(screenshots_dir):
        try:
            os.mkdir(screenshots_dir)
        except OSError:
            print("Failed to create screenshots directory. " +
                  f"Path to the directory: {screenshots_dir}"
                  )

    driver.find_element_by_tag_name('body').screenshot(
        screenshots_dir + file_name + ".png"
    )


if __name__ == '__main__':
    options = webdriver.chrome.options.Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    filename = './screenshots/test'

    driver.get(r'http://127.0.0.1:8000/')
    sleep(1)

    take_full_page_screenshot(driver, filename)
