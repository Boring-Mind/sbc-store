from needle.cases import NeedleTestCase
from needle.driver import NeedleFirefox
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class RegressionTests(NeedleTestCase):
    """Regression test for all pages on site."""
    
    engine_class = 'needle.engines.imagemagick_engine.Engine'
    # Set dispay size to fullhd
    viewport_width = 1920
    viewport_height = 1080

    cleanup_on_sucess = True

    @classmethod
    def get_web_driver(cls):
        """Set driver parameters.

        Set headless mode and return driver object
        """
        options = webdriver.FirefoxOptions()
        options.set_headless()
        return NeedleFirefox(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_index(self):
        """Regression test for index page.
        
        Gets full screenshot of index page
        and compares it with reference screenshot
        """
        self.driver.get(r'http://127.0.0.1:8000/')
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(0.5)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
        sleep(3)
        self.assertScreenshot('body', 'index_regression_fullhd')
