from setuptools import setup, find_packages

setup(
    name='ez-api',
    version='1.0.2',
    description='A simple API wrapper for e-z.host (Includes: Files, Pastes & Link Shortener). Must have an account on e-z.host to use.',
    long_description=open("pypi-README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)