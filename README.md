# `useragents`

### A Python module which does one thing: giving you a random User-Agent Header
***Do not worry about sticking with a single user-agent for you HTTP requests ever again!***

[![PyPI version](https://badge.fury.io/py/pyuseragents.svg)](https://pypi.org/project/pyuseragents/)
[![PyPI — Total Downloads](https://static.pepy.tech/badge/pyuseragents)](https://pepy.tech/project/pyuseragents)
[![PyPI - Monthly Downloads](https://img.shields.io/pypi/dm/pyuseragents)](https://pypistats.org/packages/pyuseragents)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyuseragents)](https://pypi.org/project/pyuseragents/)
[![PyPI - Status](https://img.shields.io/pypi/status/pyuseragents)](https://pypi.org/project/pyuseragents/)
[![GitHub - License](https://img.shields.io/github/license/Animenosekai/useragents)](https://github.com/Animenosekai/useragents/blob/master/LICENSE)
[![GitHub Top language](https://img.shields.io/github/languages/top/Animenosekai/useragents)](https://github.com/Animenosekai/useragents)
[![CodeQL Checks Badge](https://github.com/Animenosekai/useragents/workflows/CodeQL%20Python%20Analysis/badge.svg)](https://github.com/Animenosekai/useragents/actions?query=workflow%3ACodeQL)
[![Pytest](https://github.com/Animenosekai/useragents/actions/workflows/pytest.yml/badge.svg)](https://github.com/Animenosekai/useragents/actions/workflows/pytest.yml)
![Code Size](https://img.shields.io/github/languages/code-size/Animenosekai/useragents)
![Repo Size](https://img.shields.io/github/repo-size/Animenosekai/useragents)
![Issues](https://img.shields.io/github/issues/Animenosekai/useragents)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to have Python installed on your computer to use this software

According to Vermin, Python 3.0 or higher is needed to use `pyuseragents` even if it **does work** on Python 2.

Always check if your Python version works with `pyuseragents` before using it in production

*Tested manually on `Python 2.7` and `Python 3.9` and `Python 3.12.2`*

*Tested automatically (CI) with Pytest on CPython `3.7.17`, `3.8.18`, `3.9.19`, `3.10.14`, `3.11.9`, `3.12.3`, `3.13.0-beta.1`, on PyPy `3.9` and on GraalPy `24.0`*

### Installing

You can install it from PyPI with:

```bash
pip install --upgrade pyuseragents
```

You can check if you successfully installed it by printing out its version:

```bash
python -c "import pyuseragents; print(pyuseragents.__version__)"
# output:
pyuseragents v1.0.5
```

## List of User-Agents

The list of User-Agents headers has been crawled from various sources.

They are all available in the `pyuseragents/data/list.py` file.

> The list being in a python module means that it will be preloaded by Python in memory for performance reasons.

## Usage
```python
>>> import pyuseragents
>>> headers = {
    "User-Agent": pyuseragents.random(),
    "Content-Type": "application/json",
    "and so on..."
}
>>> pyuseragents.random()
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
```

## Deployment

This module should be stable but might contain bugs with edge-cases.

Feel free to use it in production if you feel like it is suitable for your production and report any issue under the "Issues" section of the [GitHub repository](https://github.com/Animenosekai/useragents).

## Built With
No dependency is needed for this module

## Authors

* **Anime no Sekai** - *Initial work* - [Animenosekai](https://github.com/Animenosekai)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
