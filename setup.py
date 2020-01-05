from setuptools import setup, find_packages


setup(
	  name='sbc_store',
	  version='0.1',
	  packages=find_packages(),
	  include_package_data=True,
	  scripts=['scripts/manage.py'],
	  install_requires=[
	  	'docutils>=0.3',
	  	'django>=3.0',
	  	'python-decouple>=3.3',
		'psycopg2-binary>=2.8.0',
		'dj-database-url>=0.5.0',
		'uwsgi>=2.0',
		'selenium>=3.0',
	  ]
)
