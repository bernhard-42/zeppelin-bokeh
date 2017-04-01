import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "zeppelin_bokeh",
    version = "0.9.0",
    author = "Bernhard Walter",
    author_email = "bwalter@gmail.com",
    description = ("Bokeh multiple state enabler for Apache Zeppelin"),
    license = "Apache License 2.0",
    keywords = "zeppelin bokeh",
    packages=find_packages(),
    long_description=read('Readme.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python'",
        "Programming Language :: Python :: 2'",
        "Programming Language :: Python :: 3'"
    ]
)