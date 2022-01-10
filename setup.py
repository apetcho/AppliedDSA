#!/usr/bin/env python3
from setuptools import setup
from appdsa.version import VERSION

with open("README.md", "r") as fd:
    LONG_DESCRCIPTION = fd.read()

major, minor, release = VERSION
APPDSA_VERSION = f"{major}.{minor}.{release}"

setup(
    name="appdsa",
    author="Eyram K. Apetcho",
    author_email="orion2dev@gmail.com",
    url="",
    version=f"{APPDSA_VERSION}",
    python_requires=">=3.6",
    license="MIT",
    description="Data Structures and Applications",
    long_description=LONG_DESCRCIPTION,
    long_description_content_type="text/markdown",
    platforms=["Windows", "Linux", "Mac OS X"],
    classifiers=[
        "Development Status:: Pre-Alpha",
        "Intended Audience :: Software Developmen",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development",],
    keywords=["Data Structures", "Interpreter", "Compiler"],
    tests_require=["pytest"],
    package_dir={"appdsa": "appdsa"},
    packages=["appdsa"],
    )
