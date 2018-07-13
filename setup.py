from __future__ import absolute_import
from setuptools import setup, find_packages
from setuptools.command.install import install

setup(name='talin',
      version='10.0.0',
      description=("Library to extract message quotations, based on Mailgun's Talon but without signatures and ML."),
      long_description=open("README.rst").read(),
      author='Wesley Willian Schleumer de Góes',
      author_email='wesley.schleumer@gmail.com',
      url='https://github.com/schleumer/talin',
      license='APACHE2',
      packages=find_packages(exclude=['tests', 'tests.*']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "lxml>=2.3.3",
          "regex>=1",
          'chardet>=1.0.1',
          'cchardet>=0.3.5',
          'cssselect',
          'six>=1.10.0',
          'html5lib'
          ],
      tests_require=[
          "mock",
          "nose>=1.2.1",
          "coverage"
          ]
      )
