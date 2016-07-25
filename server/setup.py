import sys
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

#with open('requirements.txt') as f:
#    required = f.read().splitlines()

#if required is None:
#    required = []

#if sys.version_info[0] == 2:
#    required.append('futures>=3.0.0')
rootdir = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(rootdir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()



setup(
    name='odin',
    version='0.1',
    description='ODIN detector server',
    long_description=long_description,
    url='https://github.com/timcnicholls/odin',
    author='Tim Nicholls',
    author_email='tim.nicholls@stfc.ac.uk',
    license='Apache Software License, Version 2.0',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='',

    # Specify the packages that this project provides (using find_packages() for automation)
    packages=find_packages(exclude=['docs','sandbox', 'tests*']),

#    install_requires=['nose>=1.3.7',
#                      'coverage==4.1b2',
#                      'codeclimate-test-reporter>=0.1.0',
#                      'pyzmq>=15.2.0',
#                      'requests>=2.9.1',
#                      'tornado>=4.3'],
    # run-time dependencies here. These will be installed by pip when the project is installed.
    install_requires=['numpy', 'h5py', 'future', 'enum34>=1.0'],

    # Additional groups of dependencies (e.g. development dependencies). 
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': ['nose>=1.3', 'coverage'],
    },

    entry_points={
        'console_scripts' : [
            'odin_server = odin.server:main',
        ],
    },
)

