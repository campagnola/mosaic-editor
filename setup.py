import os
from setuptools import setup, find_packages

packages=find_packages('.')

setup(
    name = "mosaiceditor",
    version = "0.0.1",
    author = "Luke Campagnola",
    author_email = "lukec@alleninstitute.org",
    description = ("Interactive visualization and registration of image / spatial data"),
    license = "MIT",
    keywords = "",
    url = "",
    packages=packages,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
    ],
)


