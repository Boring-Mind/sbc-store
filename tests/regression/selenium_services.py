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


def take_screenshot(
    driver: webdriver,
    file_name: str,
    wait_func=None,
    page_width=1920,
    baseline=False
):
    """Create path for saving screenshots and call take_full_page_screenshot.
    
    file_name - name of screenshot file, that would be saved (without .png)
    wait_func - function, which implements explicit wait for selenium
    page_width - browser screen width
    baseline - True to save images to baseline folder
    
    Main goal of this function - reduce complexity
    of the take_full_page_screenshot function.
    """
    folder = SCREENSHOTS_DIR
    if baseline is True:
        folder = BASELINE_DIR

    if not os.path.exists(folder):
        try:
            os.mkdir(folder)
        except OSError:
            print("Failed to create directory. "
                  f"Path to the directory: {folder}"
                  )

    path_to_screenshot = os.path.join(folder, f"{file_name}.png")

    take_full_page_screenshot(
        driver=driver,
        file_path=path_to_screenshot,
        wait_func=wait_func,
        page_width=page_width
    )


def take_full_page_screenshot(
    driver: webdriver,
    file_path: str,
    wait_func: callable,
    page_width: int,
):
    """Get full page screenshot.

    file_path - full path to the screenshot file,
                that would be saved (with .png)
    wait_func - function, which implements explicit wait for selenium
    page_width - browser screen width
    
    Screenshots are saved in the same folder with script.
    Files have png format.
    """
    page_height = get_page_height(driver)
    driver.set_window_size(page_width, page_height)

    if wait_func is not None:
        wait_func(driver)

    driver.find_element_by_tag_name('body').screenshot(file_path)


if __name__ == '__main__':
    options = webdriver.chrome.options.Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get('http://127.0.0.1:8000/login/')
    sleep(1)

    try:
        take_screenshot(driver, file_name='login', baseline=True)
    finally:
        driver.quit()
