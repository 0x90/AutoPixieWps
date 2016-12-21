#!/usr/bin/env python
from setuptools import setup

setup(
    name = "AutoPixieWps",
    version = "0.1",
    author = "nxxxu",
    description = "Automated pixieWps python script",
    keywords = "WiFi 802.11 WPS pixiewps",
    url = "https://github.com/nxxxu/AutoPixieWps",
    scripts=['autopixie'],
    # py_modules=['wifijammer'],
    #install_requires=['scapy'],
    long_description="AutoPixieWps is a script to automate the pixiewps attack",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
