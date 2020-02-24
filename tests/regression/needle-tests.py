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

    # Delete new screenshots after we pass all the tests
    cleanup_on_sucess = True

    @classmethod
    def get_web_driver(cls):
        """Set driver parameters.

        Set headless mode and return driver object
        """
        options = webdriver.FirefoxOptions()
        options.set_headless()
        return NeedleFirefox(options=options)

    def default_regr_test(self, pagename="index", url=""):
        """Regression test.
        
        Gets full page screenshot
        and compares it with reference screenshot
        """
        self.driver.get(r'http://127.0.0.1:8000/' + url)
        # Traversing through all the page down and up
        # We need to deal with lazy loading of scripts and images
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
        # Without that sleep script didn't recognize,
        # that we scroll the entire page
        sleep(0.5)
        # Return back to top
        # Otherwise our screenshots would be totally black
        self.driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
        # Wait for the images to load
        sleep(4)
        self.assertScreenshot('body', pagename + '_regr_fullhd')

    # def test_index(self):
        """Regression test for index page."""
        # self.default_regr_test()

    def test_login(self):
        """Regression test for login page."""
        self.default_regr_test('login', 'login/')

    def test_about(self):
        """Regression test for about page."""
        self.default_regr_test('about', 'about/')

    def test_cart(self):
        """Regression test for cart page."""
        self.default_regr_test('cart', 'cart/')

    def test_checkout(self):
        """Regression test for checkout page."""
        self.default_regr_test('checkout', 'checkout/')

    def test_contact(self):
        """Regression test for contact page."""
        self.default_regr_test('contact', 'contact/')

    def test_faq(self):
        """Regression test for faq page."""
        self.default_regr_test('faq', 'faq/')

    def test_restore_password(self):
        """Regression test for restore password page."""
        self.default_regr_test('restore_password', 'restore_password/')

    def test_account(self):
        """Regression test for account page."""
        self.default_regr_test('account', 'account/')

    def test_register(self):
        """Regression test for registration page."""
        self.default_regr_test('register', 'register/')

    def test_service(self):
        """Regression test for service page."""
        self.default_regr_test('service', 'service/')

    def test_shop(self):
        """Regression test for shop page."""
        self.default_regr_test('shop', 'shop/')

    def test_single_product(self):
        """Regression test for single product page."""
        self.default_regr_test('single_product', 'single_product/')

    def test_wishlist(self):
        """Regression test for wishlist page."""
        self.default_regr_test('wishlist', 'wishlist/')

    def test_404(self):
        """Regression test for error 404 page."""
        self.default_regr_test('404', '404/')
