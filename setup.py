# coding: utf-8
from setuptools import setup, find_packages


setup(
    name='pymetro',
    description='route planner for Moscow Metro',
    packages=find_packages(),
    install_requires=[
        'HeapDict==1.0.0',
    ],
)
