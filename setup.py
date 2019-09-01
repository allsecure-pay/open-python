# coding=utf-8
__author__ = 'ALLSECURE'
import sys

if sys.version_info < (3, 4):
    install_requires = ['requests >= 2.5.3', 'six >= 1.9.0', 'pyopenssl', 'ndg-httpsclient', 'pyasn1']
else:
    install_requires = ['requests >= 2.5.3', 'six >= 1.9.0']

from setuptools import setup

setup(
    name='opp',
    version='1.3.1',
    description='Python wrapper for OPP',
    author='ALLSECURE',
    author_email='support@allsecpay.com',
    url='https://github.com/allsecure-pay/open-python',
    license='MIT',
    packages=['opp'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=install_requires,
    download_url='https://github.com/allsecure-pay/open-python.git'
)
