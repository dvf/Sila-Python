
from setuptools import setup, find_packages

from codecs import open
from os import path



setup(
    name='sila_api',


    version='0.1.1',

    description='Sila Python library for message signing and api wrapper',

    url='https://github.com/Sila-Money/Sila-Python',

    author='Sila',
    author_email='support@silamoney.com',

    license='MIT',

    classifiers=[
        
        # How stable is your project? 
        #   3 - Alpha, 4 - Beta,5 - Production/Stable

        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6'

    ],

    keywords='Sila v0.1.1 Rest API',

    packages=["sila_api.wallets","sila_api.api"],

   
    install_requires=['requests'],

    zip_safe=False,
    
    include_package_data=True,

    extras_require={},

   
    package_data={},

  
    entry_points={}
)