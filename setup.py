# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PyScrumTrello',
    version='1.0.0',
    description='Python codes to get Scrum metrics from the Trello.',
    long_description=readme,
    author='Leonardo Nascimento',
    author_email='lnascimento.mail@gmail.com',
    url='https://github.com/leofontesnascimento/py-scrum-trello',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
