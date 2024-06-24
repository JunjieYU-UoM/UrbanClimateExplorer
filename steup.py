from setuptools import setup, find_packages, Extension
import os

classifiers = [
    "Development Status :: 1 - Pre-Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering :: Earth and Environmental Sciences"
    ]

with open("README.rst", "r") as fp:
    long_description = fp.read()
    
def get_requires():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        file_content = f.read()
        lines = [line.strip() for line in file_content.strip().split("\n") if not line.startswith("#")]
        return lines

setup(
    name="UrbanCimateExplorer",
    version="0.0.0",
    #author="Junjie Yu",
    #author_email="yjj1997@live.cn",
    #url="https://github.com/JunjieYU-UoM/pyclmuapp",
    long_description=long_description,
    license="MIT",
    classifiers=classifiers,
    install_requires=get_requires(),
    packages=find_packages()
    )