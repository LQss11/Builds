## Python Library
Build test and publish a **Python Library**, with simple code and commands explained through this `README.md`.

You can follow through the steps in the instructions in order to get a better idea about this project, how it's created, and how to run it and test it on your host machine.

## Quick Start
To run this project you will need follow through these steps:
- first we are going to create a file `tar.gz` format:
```sh
python3 <path-to-setup.py> sdist
```
This will generate a package of the piece of code that we got
>Python3 was used in this example you can check by running `python3 --version` or `py --version`

- Now that we have our package a dist directory will be generated can then run:
```sh
pip install <path-to-package-file>
```
### Additional Information and links
Build a python application [full example (must read and watch video!!!)](https://simonwillison.net/2021/Nov/4/publish-open-source-python-library/) --- [VIDEO](https://www.youtube.com/watch?v=VMnLXynUqys)