# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='dhcplib',
    version='0.1.0',
    packages=find_packages(),
    description='Pure-Python, spec-compliant DHCP-packet-processing library',
    long_description=(
        'dhcplib is a fork of staticDHCPd\'s libpydhcpserver aiming to provide '
        'Python 3 compatility and dropping decoupling it from a network API '
        'so you can use it with either sync or async networking libs.'
    ),
    author='Jan Segre',
    author_email='jan@ispflex.com',
    license='GPLv3',
    url='https://github.com/jansegre/dhcplib/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
    ],
)
