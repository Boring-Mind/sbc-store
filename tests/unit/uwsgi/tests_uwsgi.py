from selenium import webdriver
import subprocess
import unittest

class UWSGITest(unittest.TestCase):

	def setUp(self):
		options = webdriver.firefox.options.Options()
		options.add_argument('--headless')

		self.browser = webdriver.Firefox(options=options)

		bash_command = 'uwsgi --http :8000 --wsgi-file uwsgi_start_for_tests.py'
		subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)

	def tearDown(self):
		self.browser.quit()
		bash_command = 'killall -s INT uwsgi'
		subprocess.Popen(bash_command, stdout=subprocess.PIPE, shell=True)
		# self.p.kill()

	def test_uwsgi_printed_hello_world(self):
		#uwsgi launches and sends Hello World as HTTP response
		self.browser.get('http://localhost:8000')

		self.assertIn(
			'Hello World',
			self.browser.page_source
		)


if __name__ == '__main__':
	unittest.main(warnings='ignore')
