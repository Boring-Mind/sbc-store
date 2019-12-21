from setuptools import setup, find_packages


setup(
	  name='sbc_store',
	  version='0.1',
	  packages=find_packages(),
	  include_package_data=True,
	  scripts=['scripts/manage.py'],
	  install_requires=[
	  	'docutils>=0.3',
	  	'django<3.1',
	  ]
)
