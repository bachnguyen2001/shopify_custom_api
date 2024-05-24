# Shopify Custom API Library

A custom Shopify API library that make shopify api call more easy.

## Table of Contents

- [Shopify Custom API Library](#shopify-custom-api-library)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Getting started](#getting-started)
    - [setup](#setup)
    - [get](#get)
    - [post](#post)
    - [put](#put)
    - [delete](#delete)
## Features

- Easy authentication with Shopify.
- Simplified methods for common API operations.
- Support for additional Shopify API endpoints not covered by the official library.

## Installation

To install the package, you can use `pip`:

```sh
pip install -U shopify_custom_api
```
## Getting started
- Generate access token for your store by following instruction
  (https://help.plytix.com/en/getting-api-credentials-from-your-shopify-store)

- checkout shopify api document
  (https://shopify.dev/docs/api/admin-rest)

### setup
```py
from cshopify import API

shop = API('xxxxx', 'shpat_xxxxxxxxxxxxxxxxxxxxxxx', '2024-01')
```
### get
```py
.get(endpoint, params)
```
### post
```py
.post(endpoint, data)
```
### put
```py
.put(endpoint, data)
```
### delete
```py
.delete(endpoint)
```


