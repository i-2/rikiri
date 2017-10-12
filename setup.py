"""setup.py"""
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='gleam',
    version='0.5',
    description='Make github presentations like a boss',
    long_description=README,
    author='Sourcepirate',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/sourcepirate/gleam.git',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "jinja2",
        "yattag"
    ],
    test_suite='tests',
    scripts=['bin/gleam']
)
