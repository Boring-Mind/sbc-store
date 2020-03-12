from selenium import webdriver
import os
import time

SCREENSHOTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'screenshots')
)

BASELINE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'screenshots', 'baseline')
)


class bcolors:
    """List of cli text colors."""

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class SeleniumService:
    """Get full page screenshot.
    
    Screenshots are saved in the same folder with script.
    Files have png format.
    """

    def get_images_folder(baseline: bool) -> str:
        if baseline is True:
            return BASELINE_DIR
        else:
            return SCREENSHOTS_DIR

    def __init__(
        self,
        driver: webdriver,
        url: str,
        img_name: str,
        page_width=1920,
        baseline=False,
        wait=None
    ):
        """Initialize class object.

        url - url of the tested page (http://your_site/page)
        img_name - name of screenshot file, that would be saved (without .png)
        page_width - browser screen width
        baseline - True to save images to baseline folder
        wait - function, which implements explicit wait for selenium
        """
        self.driver = driver
        self.url = url
        self.img_name = img_name
        self.page_width = page_width
        self.folder = SeleniumService.get_images_folder(baseline)
        self.wait = wait

    def get_full_page_screenshot(self):
        """Main function of the class.

        Describes recommended workflow with class.
        """
        self.create_images_directory()
        self.set_viewport()
        self.go_to_the_webpage()
        self.browser_set_fullscreen()
        self.wait_function()
        self.take_screenshot()

    def set_viewport(self):
        """Set default page size.

        Needed to set proper page size.
        """
        self.driver.set_window_size(
            self.page_width, int(self.page_width / (16 / 9))
        )

    def go_to_the_webpage(self):
        self.driver.get(self.url)

    def get_page_height(self) -> int:
        """Get full height of webpage."""
        return int(self.driver.execute_script(
            'return document.body.parentNode.scrollHeight'
        ))

    def browser_set_fullscreen(self):
        """Set browser to fullscreen mode."""
        page_height = self.get_page_height()
        self.driver.set_window_size(self.page_width, page_height)

    def create_images_directory(self):
        """Create screenshot or baseline folder if not present."""
        if not os.path.exists(self.folder):
            try:
                os.mkdir(self.folder)
            except OSError:
                print("Failed to create directory. "
                      f"Path to the directory: {self.folder}"
                      )

    def get_path_to_screenshot(self):
        return os.path.join(self.folder, f"{self.img_name}.png")

    def print_wait_error():
        print(f'{bcolors.FAIL}ERROR: {bcolors.ENDC}'
              'Failed to call wait function.\n'
              'Rolling back to default selenium wait.\n'
              'Some complicated pages with js or lazy load '
              'may not have time to load all content before '
              'screenshot is taken.'
              )

    # def print_wait_warning():
    #     print(f'{bcolors.WARNING}WARNING: {bcolors.ENDC}'
    #           'There is no wait function defined. '
    #           'Rolling back to default selenium wait.\n'
    #           'Some complicated pages with js or lazy load '
    #           'may not have time to load all content before '
    #           'screenshot is taken.\n'
    #           'Module: \"selenium_services\"\n'
    #           'Method: \"take_full_page_screenshot\"'
    #           )

    def wait_function(self):
        if self.wait is not None:
            try:
                self.wait(self.driver)
            except AttributeError as e:
                SeleniumService.print_wait_error()
                raise e
        # else:
        #     SeleniumService.print_wait_warning()

    def take_screenshot(self):
        screenshot_path = self.get_path_to_screenshot()
        body_element = self.driver.find_element_by_tag_name('body')
        body_element.screenshot(screenshot_path)


if __name__ == '__main__':
    time1 = time.perf_counter()

    options = webdriver.chrome.options.Options()
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get('http://127.0.0.1:8000/product/')

    try:
        ss = SeleniumService(driver, img_name='product')
        
        ss.get_full_page_screenshot()
        time2 = time.perf_counter()

        print(time2 - time1)
    finally:
        driver.quit()
