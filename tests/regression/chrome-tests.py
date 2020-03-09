import unittest
import os
import time
import sys

from selenium import webdriver

from selenium_services import SeleniumService
from imagemagick_services import screenshots_equal


class PageLayoutTest(unittest.TestCase):

    SAVE_BASELINE = False

    @classmethod
    def setUpClass(self):
        """Set chrome driver to headless mode and return instance."""
        options = webdriver.chrome.options.Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def default_page_layout_test(
            self, img_name: str, url=''
    ):
        """Test equality of test and reference images.

        img_name - name of the image file.
                   Must be same for baseline and test images.
        url: str - relative url to the tested page (http://domain_name/{url}/)
        """
        selenium_service = SeleniumService(
            driver=self.driver,
            img_name=img_name,
            baseline=self.SAVE_BASELINE,
            url=f'http://127.0.0.1:8000/{url}'
        )
        selenium_service.get_full_page_screenshot()
        if not self.SAVE_BASELINE:
            self.assertTrue(
                screenshots_equal(img_name=img_name),
                f"Layout of {img_name} page differs from the reference layout."
                "\nCheck the diff file to see a difference."
            )

    def test_index_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='index', url='')

    def test_about_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='about', url='about')

    def test_cart_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='cart', url='cart')

    def test_checkout_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='checkout', url='checkout')

    def test_contact_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='contact', url='contact')

    def test_faq_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='faq', url='faq')

    def test_password_restore_page_has_valid_layout(self):
        self.default_page_layout_test(
            img_name='password', url='restore_password'
        )

    def test_account_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='account', url='account')

    def test_login_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='login', url='login')

    def test_register_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='register', url='register')

    def test_shop_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='shop', url='shop')

    def test_shop_list_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='shop_list', url='shop_list')

    def test_product_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='product', url='product')

    def test_wishlist_page_has_valid_layout(self):
        self.default_page_layout_test(img_name='wishlist', url='wishlist')

    def test_page_404_has_valid_layout(self):
        self.default_page_layout_test(img_name='404', url='404')


if __name__ == '__main__':
    arg_list = sys.argv
    if '-h' in arg_list:
        sys.argv.remove('-h')
        print('List of arguments:')
        print('----------------------')
        print('--with-save-baseline: Generate reference images '
              'and save it to the baseline folder'
              )
    elif '--with-save-baseline' in arg_list:
        # Remove baseline argument, because it cannot be recognized
        # by unittest framework
        sys.argv.remove('--with-save-baseline')
        print('Save baseline mode activated')
        PageLayoutTest.SAVE_BASELINE = True
        unittest.main()
    else:
        unittest.main()
