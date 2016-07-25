import sys
from setuptools import setup, find_packages

#with open('requirements.txt') as f:
#    required = f.read().splitlines()

#if required is None:
#    required = []

#if sys.version_info[0] == 2:
#    required.append('futures>=3.0.0')


setup(
    name="odin",
    version='0.1',
    description='ODIN detector server',
    url='https://github.com/timcnicholls/odin',
    author='Tim Nicholls',
    author_email='tim.nicholls@stfc.ac.uk',
    packages=find_packages(),
    install_requires=['nose>=1.3.7',
                      'coverage==4.1b2',
                      'codeclimate-test-reporter>=0.1.0',
                      'pyzmq>=15.2.0',
                      'requests>=2.9.1',
                      'tornado>=4.3'],
#    entry_points={
#        'console_scripts' : [
#            'odin_server = odin.server:main',
#        ],
#    },
)

