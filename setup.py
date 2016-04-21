from setuptools import setup

setup(
    name='exemel',
    version='0.1.0',
    description=(
        'Build XML documents easily and concisely using native Python data '
        'structures.'
    ),
    py_modules=[
        'exemel'
    ],
    install_requires=[
        'lxml>=3.0'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'xmlunittest>=0.2.0'
    ]
)
