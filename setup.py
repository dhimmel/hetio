import pathlib
import re

import setuptools

directory = pathlib.Path(__file__).parent.absolute()

# version
init_path = directory.joinpath("hetnetpy", "__init__.py")
with init_path.open() as read_file:
    text = read_file.read()
pattern = re.compile(r"^__version__ = ['\"]([^'\"]*)['\"]", re.MULTILINE)
version = pattern.search(text).group(1)

# long_description
readme_path = directory.joinpath("README.md")
with readme_path.open() as read_file:
    long_description = read_file.read()

# Testing dependencies
tests_require = [
    "black ; python_version>='3.6'",
    "neo4j",
    "numpy",
    "pandas",
    "py2neo",
    "pytest",
    "scipy",
    "tqdm",
]

setuptools.setup(
    # Package details
    name="hetnetpy",
    version=version,
    url="https://github.com/hetio/hetnetpy",
    description="Hetnets in Python",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="CC0 1.0",
    # Author details
    author="Daniel Himmelstein",
    author_email="daniel.himmelstein@gmail.com",
    # Package topics
    keywords="hetnet graph heterogeneous network neo4j hetio hetnetpy",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    # should find hetnetpy (and hetio if symlink supported)
    packages=setuptools.find_packages(exclude=["test"]),
    # Specify python version
    python_requires=">=3.5",
    # Run-time dependencies
    install_requires=["regex"],
    # Testing dependencies
    tests_require=tests_require,
    # Additional groups of dependencies
    extras_require={
        "stats": ["pandas", "matplotlib", "seaborn"],
        "neo4j": ["pandas", "py2neo", "tqdm"],
        "matrix": ["numpy", "scipy"],
        "test": tests_require,
    },
)
