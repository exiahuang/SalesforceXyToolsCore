"""SalesforceXytools Core Package Setup"""

from setuptools import setup
import textwrap
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'SalesforceXytoolsCore', '__version__.py'),
          'r') as f:
    exec(f.read(), about)

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(name=about['__title__'],
      version=about['__version__'],
      author=about['__author__'],
      author_email=about['__author_email__'],
      maintainer=about['__maintainer__'],
      maintainer_email=about['__maintainer_email__'],
      packages=[
          'SalesforceXytoolsCore',
      ],
      url=about['__url__'],
      license=about['__license__'],
      description=about['__description__'],
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      install_requires=['requests[security]'],
      tests_require=[
          'nose>=1.3.0',
          'pytz>=2014.1.1',
          'responses>=0.5.1',
      ],
      test_suite='nose.collector',
      keywords=about['__keywords__'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: OS Independent', 'Topic :: Internet :: WWW/HTTP',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: PyPy'
      ])
