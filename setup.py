from importlib.metadata import entry_points
from setuptools import setup
import os


setup(
   name="aoc",
   version="1.0.0",
   description="Advent of Code helpers",
   long_description="foo",
   author="Kristian Rother",
   author_email="kristian.rother@posteo.de",
   packages=["aoc"],
   url="https://github.com/krother/advent_of_code",
   license="MIT",
   classifiers=[
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Programming Language :: Python :: 3.11",
   ],
)
    
