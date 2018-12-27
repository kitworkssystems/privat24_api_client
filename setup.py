#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='privat24_api_client',
    version='1.0.1',
    description='Privat24 Python SDK',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests', 'kws_date_ext', ],
)
