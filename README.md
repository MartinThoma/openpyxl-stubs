[![PyPI version](https://badge.fury.io/py/Flask-HTTPAuth-stubs.svg)](https://pypi.org/project/openpyxl-stubs)
[![Code on Github](https://img.shields.io/badge/Code-GitHub-brightgreen)](https://github.com/MartinThoma/openpyxl-stubs)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub last commit](https://img.shields.io/github/last-commit/MartinThoma/openpyxl-stubs)

# openpyxl-stubs

Add types for [openpyxl](https://pypi.org/project/openpyxl/) for mypy.

## Installation

```
$ pip install openpyxl-stubs
```

## Usage

Mypy will automatically use the type annotations in this package, once it is
installed. You just need to annotate your code:

```python
from typing import Optional
from flask_httpauth import HTTPAuth, Authorization


def foo(bar: HTTPAuth) -> Optional[Authorization]:
    return bar.get_auth()
```

For general hints how to use type annotations, please read [Type Annotations in Python 3.8](https://medium.com/analytics-vidhya/type-annotations-in-python-3-8-3b401384403d)
