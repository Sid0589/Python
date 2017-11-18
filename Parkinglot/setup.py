# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ParkingLot',
    version='1.0.0',
    description='GoJEK Problem',
    long_description=readme,
    author='Soupam Mandal',
    author_email='sooupam@gmail.com',
    url='https://github.com/Sid0589/ParkingLot',
    license=license,
    packages=['ParkingLot'],
    entry_points={
    'console_scripts': [
              'parking_lot = ParkingLot.__main__:main'
              ]
    },
    test_suite='tests.test_parkinglot'
)