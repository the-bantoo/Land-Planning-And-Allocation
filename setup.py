# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in land_planning_and_allocation/__init__.py
from land_planning_and_allocation import __version__ as version

setup(
	name='land_planning_and_allocation',
	version=version,
	description='Planning and allocation of land',
	author='Bantoo Accounting',
	author_email='duncan@thebantoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
