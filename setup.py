""""lambdata- collaction of data science functions"""""

import setuptools #available with standard library

REQUIRED = [
    "numpy",
    "pandas"
]

with open("readme.md", "r") as fh:
        LONG_DESCRIPTION = fh.read()


setuptools.setup(
    name='lambdata-bobbriksz',
    version='0.0.3',
    author='bobbriksz',
    description=LONG_DESCRIPTION,
    long_description_content='text/markdown',
    url ="https://github.com/BobBriksz/lambdata-bobbriksz",
    packages= setuptools.find_packages(), #how we want to find our require packages
    python_requires=">=3.6", #what versions of python we are compatible with
    install_requires=REQUIRED,
    classifiers=[
        "Programming language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
            ]
)
