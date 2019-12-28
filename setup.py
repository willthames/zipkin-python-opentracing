from setuptools import setup, find_packages

setup(
    name='zipkin-python-opentracing',
    version='1.0.1',
    description='OpenZipkin Python OpenTracing Implementation',
    long_description='',
    author='OpenZipkin',
    license='',
    install_requires=['thrift==0.13.0',
                      'jsonpickle',
                      'pytest',
                      'thriftpy2',
                      'requests',
                      'opentracing==2.2.0',
                      'basictracer',
                      'mock'],
    tests_require=['sphinx',
                   'sphinx-epytext'
                   ],

    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        ],

    keywords=[ 'opentracing', 'openzipkin', 'traceguide', 'tracing', 'microservices', 'distributed' ],
    packages=find_packages(exclude=['docs*', 'tests*', 'sample*']),
    package_data={'': ['*.thrift']},
)
