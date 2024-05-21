from setuptools import setup, find_packages

readme = open("README.md").read()
packages=find_packages(),
      
setup(
    name="customShopifyAPI",
    version="0.0.1",
    description="An simple library that help call shopify's API" ,
    long_description=readme,
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
        "json",
     ],
     keywords='shopify rest api'
)
