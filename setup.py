from setuptools import setup, find_packages

# Read the long description from the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Verify packages found
packages = find_packages()
print("Packages found:", packages)

setup(
    name="shopify_custom_api",
    version="0.1.1",
    description="A simple library that helps call Shopify's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bachnguyen2001/shopify_custom_api.git",
    author="Nguyen Ngoc Bach",
    author_email="bachnguyenfptu@gmail.com",
    license="MIT",
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        "requests",
    ],
    keywords='shopify rest api',
)
