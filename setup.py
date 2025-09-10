### setup script

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name="PyPhy",
    version="0.1.0",
    author="Premanshu Bhagat",
    description="Python library for physics formulas.",
    long_description=description,
    url="https://github.com/cmd-cosmos/PyPhy",
    packages=find_packages(),
    classifiers=[]# to be filled
    python_requirement=">3.10",
    requires=pass
    tests="tests",
    include_package_data=True
)
