================
Wagtail AutoFixtures
================

This app is based on django-autofixture: https://github.com/gregmuellegger/django-autofixture

The wagtail-autofixtures application can be used to automatically generate pages with aleatory content.
The app main purpose is to load masses of randomly generated test data into your development database.
This application its smart enough to choose between foreign keys and dynamic add inlines to the parent page.

Features
========

- Generate pages with aleatory content.


Quick start
===========

1. Install :code:`wagtail-modeltranslation`::

    pip install wagtail-autofixtures

2. Add "wagtail_autofixtures" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = (
        ...
        'wagtail_autofixtures',
    )

3. Call the method that generates pages::

    from wagtail_autofixtures.models import GenericAutoFixture
    from core.models import HomePage

    GenericAutoFixture.generate_page(HomePage, 16, 5)

: ARGS:
 * HomePage - Class that you want to generate instances.
 * 16 - Parent page ID.
 * 5 - Number of instances that you want to create.

Project Home
------------
https://github.com/infoportugal/wagtail-autofixtures

