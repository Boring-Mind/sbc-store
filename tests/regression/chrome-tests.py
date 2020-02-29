import unittest
import os
import time

from selenium import webdriver

import selenium_services
from imagemagick_services import screenshots_equal


class PageLayoutTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """Set chrome driver to headless mode and return instance."""
        options = webdriver.chrome.options.Options()
        options.add_argument("--headless")
        # options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

        if not os.path.exists(selenium_services.BASELINE_DIR):
            try:
                os.mkdir(selenium_services.BASELINE_DIR)
            except OSError:
                print("Creation of the baseline directory failed. " +
                      "Path to the directory: " +
                      selenium_services.BASELINE_DIR
                      )

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_index_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/')
        selenium_services.take_full_page_screenshot(self.driver, 'index')

    def test_about_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/about')
        selenium_services.take_full_page_screenshot(self.driver, 'about')

    def test_cart_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/cart')
        selenium_services.take_full_page_screenshot(self.driver, 'cart')

    def test_checkout_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/checkout')
        selenium_services.take_full_page_screenshot(self.driver, 'checkout')

    def test_contact_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/contact')
        time.sleep(3)
        selenium_services.take_full_page_screenshot(self.driver, 'contact')

    def test_faq_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/faq')
        selenium_services.take_full_page_screenshot(self.driver, 'faq')

    def test_password_restore_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/restore_password')
        selenium_services.take_full_page_screenshot(
            self.driver, 'restore_password'
        )

    def test_account_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/account')
        selenium_services.take_full_page_screenshot(self.driver, 'account')

    def test_login_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/login')
        selenium_services.take_full_page_screenshot(self.driver, 'login')
        self.assertTrue(screenshots_equal('login_regr_fullhd', 'login'))

    def test_register_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/register')
        selenium_services.take_full_page_screenshot(self.driver, 'register')

    def test_shop_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/shop')
        selenium_services.take_full_page_screenshot(self.driver, 'shop')

    def test_shop_list_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/shop_list')
        selenium_services.take_full_page_screenshot(self.driver, 'shop_list')

    def test_product_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/product')
        selenium_services.take_full_page_screenshot(self.driver, 'product')

    def test_wishlist_page_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/wishlist')
        selenium_services.take_full_page_screenshot(self.driver, 'wishlist')

    def test_page_404_has_valid_page_layout(self):
        self.driver.get(r'http://127.0.0.1:8000/404')
        selenium_services.take_full_page_screenshot(self.driver, '404')


if __name__ == '__main__':
    unittest.main()
