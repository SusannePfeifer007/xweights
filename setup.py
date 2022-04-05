#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('xweights/__init__.py') as init_file:
    lines = init_file.read().strip().replace(" ","").split('\n')
    for line in lines:
        if '__version__' in line:
            __version__ = line.split('=')[-1]
            break
    
requirements = open("ci/requirements/requirements.txt").read().strip().split("\n")

#requirements = [
#    'numpy>=1.21.2',
#    'dask>=2021.9.1',
#    'geopandas>=0.10.0',
#    'intake-esm>=2021.8.17',
#    'nc-time-axis>=1.3.1',
#    'numpy>=1.21.2',
#    'pandas>=1.3.3',
#    'xarray>=0.19.0',
#    'py-cordex>=0.3.1',
#    'xesmf @ git+https://github.com/pangeo-data/xesmf'
#   ]


setup_requirements = open("ci/requirements/requirements_dev.txt").read().strip().split("\n")

test_requirements = [ ]

setup(
    author="Ludwig Lierhammer",
    author_email='ludwig.lierhammer@hereon.de',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python xweights contains all the functions to create grid weighted area means",
    entry_points={
        'console_scripts': [
            'xweights=xweights.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='xweights',
    name='xweights',
    packages=find_packages(include=['xweights', 'xweights.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ludwiglierhammer/xweights',
    version=__version__,
    zip_safe=False,
)
