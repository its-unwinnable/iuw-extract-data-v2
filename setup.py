from setuptools import find_packages, setup


setup(
    name="iuw-extract-data",
    version="0.0.5",
    author="Mathias Gout",
    packages=find_packages(exclude=["tests"]),
    install_requires=["rito @ git+https://github.com/mathiasgout/rito.git@bca7496e8f156120854a04b9c5889d093ff8f686"],
    python_requires="==3.9.*",
)
