#!/usr/bin/python3
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name  = "cloudflare",
    version = "0.1",
    description = "A Basic Cloudflare REST API client to update DNS records",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/marknet15/cloudflare-client',
    author='Mark Woolley',
    author_email='mw@marknet15.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages = find_packages(),
    install_requires = [
        "requests"
    ],
)