from setuptools import setup, find_packages


setup(
    name="statscollection",
    version="0.0.1",
    description="A collection of statistical functions.",
    long_description="A collection of statistical functions.",
    author="tommyod",
    author_email="tod001@uib.no",
    license="MIT",
    packages=find_packages(exclude=[]),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["statistics"],
)
