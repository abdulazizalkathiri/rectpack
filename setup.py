from setuptools import setup, find_packages


setup(
    name='rectpack',
    version='0.2.2',
    description="In essence packing a set of rectangles into the smallest number of bins", 

    # Main homepage
    url='https://github.com/secnot/rectpack/',
    
    # Extra info and author details
    author='SecNot',

    keywords=['knapsack', 'rectangle', 'packing 2D', 'bin', 'binpacking'],

    license='Apache-2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        ],

    # package
    packages = ['rectpack'],
    zip_safe = False,

    # Tests
    test_suite='nose.collector',
    tests_require=['nose'],
)
