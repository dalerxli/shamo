from setuptools import setup, find_packages

# Load long description
long_description = open("README.md", "r").read()

# Define classifiers
CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering :: Medical Science Apps."
]

# Define setup settings
setup(
    name="shamo",
    version="v1.0.0",
    license="GPLv3",
    description="Forward modelling and sensitivity analysis.",
    long_description=long_description,
    author="Martin Grignard",
    author_email="mar.grignard@uliege.be",
    packages=find_packages(exclude=["tests"]),
    install_requires=["numpy", "nibabel", "scipy", "scikit-learn"],
    classifiers=CLASSIFIERS
)
