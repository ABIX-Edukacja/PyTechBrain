# -*- coding: UTF-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTechBrain",
    version="0.8.1",
    author="Adam Jurkiewicz",
    python_requires=">=3.6",
    author_email="pytechbrain@abixedukacja.eu",
    description="PyTechBrain to nowa platforma wprowadzająca uczniów w dziedzinę IoT - Internet of Things (Internet Rzeczy). Działa z Python 3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pytechbrain.edu.pl",
    keywords="Arduino PyFirmata Laboratoriaprzyszłości",
    packages=setuptools.find_packages(),
    install_requires=[
          "pymata_aio",
          "snakemd",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
	"Intended Audience :: Education",
    ],
)
