import os
import re
import sys

from setuptools import find_packages, setup

long_description = ""

setup(
    name="minitrue",
    version="0.1",
    entry_points={
        'console_scripts': [
            'minitrued = minitrue.daemon:run',
        ]
    },
    packages=find_packages(),
    author="Paul Tagliamonte",
    author_email="tag@pault.ag",
    long_description=long_description,
    description='',
    license="Expat",
    url="http://pault.ag",
    platforms=['any'],
)
