##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""zope.browserpage setup
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

long_description = (read('README.rst') + '\n\n' + read('CHANGES.rst'))

def alltests():
    import os
    import sys
    import unittest
    # use the zope.testrunner machinery to find all the
    # test suites we've put under ourselves
    import zope.testrunner.find
    import zope.testrunner.options
    here = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
    args = sys.argv[:]
    defaults = ["--test-path", here]
    options = zope.testrunner.options.get_options(args, defaults)
    suites = list(zope.testrunner.find.find_suites(options))
    return unittest.TestSuite(suites)

setup(
    name='zope.browserpage',
    version='4.1.1.dev0',
    url='http://pypi.python.org/pypi/zope.browserpage/',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3',
        ],
    description='ZCML directives for configuring browser views for Zope.',
    long_description=long_description,
    license='ZPL 2.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope'],
    install_requires=[
        'setuptools',
        'zope.pagetemplate',
        'zope.component>=3.7',
        'zope.configuration',
        'zope.interface',
        'zope.publisher>=3.8',
        'zope.schema',
        'zope.security',
        'zope.traversing',
        ],
    extras_require={
        'menu': ['zope.browsermenu'],
        'test': [
          'zope.browsermenu',
          'zope.testing',
          'zope.testrunner',
          ],
        },
      tests_require = [
          'zope.browsermenu',
          'zope.testing',
          'zope.testrunner',
          ],
      test_suite = '__main__.alltests',
    include_package_data=True,
    zip_safe = False,
    )
