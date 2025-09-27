from setuptools import setup, find_packages

setup(
    name="shape_library",
    version="0.1.0",
    packages=find_packages(),
    description="A simple geometry library for calculating areas of shapes like circles and triangles.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="IgorAmashukeli",
    author_email="amashukeliim1150@gmail.com",
    license="MIT",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
