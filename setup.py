#!/usr/bin/env python
from setuptools import setup

setup(
    name='wagtail-autofixtures',
    version='0.1.0',
    description='Automatically generate pages with aleatory content.',
    long_description=(
        'The wagtail-autofixtures application can be used to automatically generate pages with aleatory content.'
        'The app main purpose is to load masses of randomly generated test data into your development database.'
        'This application its smart enough to choose between foreign keys and dynamic add inlines to the parent page.'),
    author='InfoPortugal, S.A.',
    author_email='efnogueira@infoportugal.impresa.pt',
    maintainer='Eduardo Nogueira',
    maintainer_email='eduardo.nogueira.externo@infoportugal.pt',
    url='https://github.com/infoportugal/wagtail-autofixtures',
    packages=['wagtail_autofixtures'],
    package_data={},
    install_requires=['django>=1.8', 'wagtail>=1.0', 'django-autofixture>=0.11.0'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License'],
    license='New BSD')
