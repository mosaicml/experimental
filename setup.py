# Copyright 2021 MosaicML. All Rights Reserved.

import setuptools
from setuptools import setup

install_requires = [
    "mosaicml==0.6.0"
]

setup(name="staging",
      version="0.0.1",
      author="MosaicML",
      author_email="team@mosaicml.com",
      description="Staging repo for algorithms",
      url="https://github.com/mosaicml/staging",
      include_package_data=True,
      packages=setuptools.find_packages(exclude=["tests*"]),
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
      ],
      install_requires=install_requires,
      python_requires=">=3.7",
)
