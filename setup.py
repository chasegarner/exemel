from setuptools import setup

setup(
    name='exemel',
    version='0.1.2',
    description=(
        'Build XML documents easily and concisely using native Python data '
        'structures.'
    ),
    url='https://github.com/aptbosox/exemel',
    author='Alexander Thompson',
    author_email='aptbosox@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    py_modules=[
        'exemel'
    ],
    install_requires=[
        'future>=0.15.2',
        'lxml>=3.0'
    ]
)
