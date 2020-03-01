import unittest
import os
import time
import sys

from selenium import webdriver

import selenium_services
from imagemagick_services import screenshots_equal


class PageLayoutTest(unittest.TestCase):

    SAVE_BASELINE = False

    @classmethod
    def setUpClass(self):
        """Set chrome driver to headless mode and return instance."""
        options = webdriver.chrome.options.Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

        if not os.path.exists(selenium_services.BASELINE_DIR):
            try:
                os.mkdir(selenium_services.BASELINE_DIR)
            except OSError:
                print("Creation of the baseline directory failed. "
                      "Path to the directory: "
                      f"{selenium_services.BASELINE_DIR}"
                      )

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def default_page_layout_test(
            self, img_name: str, url=''
    ):
        """Test equality of test and reference images.

        img_name - name of the image file.
                   Must be same for baseline and test images.
        url: str - relative url to the tested page (http://domain_name/url/)
        """
        self.driver.get(f'http://127.0.0.1:8000/{url}')
        selenium_services.take_screenshot(
            driver=self.driver,
            file_name=img_name,
            baseline=self.SAVE_BASELINE
        )
        if not self.SAVE_BASELINE:
            self.assertTrue(
                screenshots_equal(
                    base_img=img_name,
                    test_img=img_name
                ),
                f"Layout of {img_name} page differs from the reference layout.\n"
                "Check the diff file to see a difference."
            )

    def test_index_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='index', url='')

    # def test_about_page_has_valid_page_layout(self):
    #     self.driver.get(r'http://127.0.0.1:8000/about')
    #     selenium_services.take_full_page_screenshot(
    #         self.driver, 'about', baseline=self.SAVE_BASELINE
    #     )

    def test_about_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='about', url='about')

    def test_cart_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='cart', url='cart')

    def test_checkout_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='checkout', url='checkout')

    def test_contact_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='contact', url='contact')

    def test_faq_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='faq', url='faq')

    def test_password_restore_page_has_valid_page_layout(self):
        self.default_page_layout_test(
            img_name='password', url='restore_password'
        )

    def test_account_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='account', url='account')

    def test_login_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='login', url='login')

    def test_register_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='register', url='register')

    def test_shop_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='shop', url='shop')

    def test_shop_list_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='shop_list', url='shop_list')

    def test_product_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='product', url='product')

    def test_wishlist_page_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='wishlist', url='wishlist')

    def test_page_404_has_valid_page_layout(self):
        self.default_page_layout_test(img_name='404', url='404')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        argument = sys.argv.pop()
        if argument == '--with-save-baseline':
            print('Save baseline mode activated')
            PageLayoutTest.SAVE_BASELINE = True
            unittest.main()
        elif argument == '-h':
            print('List of arguments:')
            print('----------------------')
            print('--with-save-baseline: Generate reference images '
                  'and save it to the baseline folder'
                  )
        elif argument[:14] == 'PageLayoutTest':
            unittest.main()
        else:
            print(f'Unknown argument: {argument}')
            print('Please, try again')
    else:
        unittest.main()
