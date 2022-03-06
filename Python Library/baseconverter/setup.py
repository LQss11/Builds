from setuptools import setup

setup(
    name="pids",
    version="0.1",
    description="A tiny Python library for generating public IDs from integers",
    author="Simon Willison",
    url="https://github.com/simonw/...",
    license="Apache License, Version 2.0",    
    py_modules=["baseconverter"], # This is the what the setup will package (filename.py must exist within the working dir where you executed)
)