from setuptools import find_packages, setup


try:
    with open("requirements.txt", "r") as file:
        requirement = file.readline()
except FileNotFoundError:
    requirement = []

setup(
    name="data_feeder",
    version="1.0.0",
    author="Kanut Thummaruksa",
    author_email="",
    description="Data feeder module for neural network.",
    packages=find_packages(exclude=("tests",)),
    install_requires=requirement,
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
)
