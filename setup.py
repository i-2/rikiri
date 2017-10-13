"""setup.py"""
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='rikiri',
    version='0.5',
    description='Make github presentations like a boss',
    long_description=README,
    author='Sourcepirate',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/sourcepirate/rikiri.git',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=[
        "jinja2",
        "yattag",
        "six"
    ],
    test_suite='tests',
    classifiers=[
          'License :: OSI Approved :: BSD License',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Environment :: Console'],
    scripts=['bin/rikiri']
)
