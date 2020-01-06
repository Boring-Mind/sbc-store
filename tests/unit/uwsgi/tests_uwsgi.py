from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOpts
from selenium.webdriver.firefox.options import Options as FirefoxOpts
from os import path
import subprocess
import unittest


class UWSGITestFirefox(unittest.TestCase):

    def setUp(self):
        options = FirefoxOpts()
        options.add_argument('--headless')

        self.browser = webdriver.Firefox(options=options)

        bash_command = "uwsgi --http :8000 --wsgi-file "
        # uwsgi needs an absolute path to wsgi-file
        bash_command += path.join(
            path.abspath(path.dirname(__file__)),
            'uwsgi_start_for_tests.py'
        )
        subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)

    def test_uwsgi_printed_hello_world(self):
        """ uwsgi launches and sends Hello World as HTTP response """
        self.browser.get('http://localhost:8000')

        self.assertIn(
            'Hello World',
            self.browser.page_source
        )

    def tearDown(self):
        self.browser.quit()
        bash_command = 'killall -s INT uwsgi'
        subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)


class UWSGITestChrome(unittest.TestCase):

    def setUp(self):
        options = ChromeOpts()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')

        self.browser = webdriver.Chrome(
            r'/usr/bin/chromewdriver',
            options=options
        )

        bash_command = "uwsgi --http :8000 --wsgi-file "
        # uwsgi needs an absolute path to wsgi-file
        bash_command += path.join(
            path.abspath(path.dirname(__file__)),
            'uwsgi_start_for_tests.py'
        )
        subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)

    def test_uwsgi_printed_hello_world(self):
        """ uwsgi launches and sends Hello World as HTTP response """
        self.browser.get('http://localhost:8000')

        self.assertIn(
            'Hello World',
            self.browser.page_source
        )

    def tearDown(self):
        self.browser.quit()
        bash_command = 'killall -s INT uwsgi'
        subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
