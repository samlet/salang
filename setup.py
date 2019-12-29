import setuptools
from setuptools import find_packages, setup, Command

with open("README.md", "r") as fh:
    long_description = fh.read()

# What packages are required for this module to be executed?
REQUIRED = [
    "py4j",
    "simplejson"
]

setuptools.setup(
    name="salang",
    version="0.0.2",
    author="Samlet Wu",
    author_email="xiaofei.wu@gmail.com",
    description="A langpack package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samlet/salang",
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # $ setup.py publish support.
    # cmdclass={
    #     'upload': UploadCommand,
    # },
)

