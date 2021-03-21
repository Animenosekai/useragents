# `useragents`

### A Python module which does one thing: giving you a random User-Agent Header
***Do not worry about sticking with a single user-agent for you HTTP requests ever again!***

[![PyPI version](https://badge.fury.io/py/useragents.svg)](https://pypi.org/project/useragents/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/useragents)](https://pypistats.org/packages/useragents)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/useragents)](https://pypi.org/project/useragents/)
[![PyPI - Status](https://img.shields.io/pypi/status/useragents)](https://pypi.org/project/useragents/)
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

According to Vermin, Python 3.0 or higher is needed to use `useragents` even if it does work on Python 2.

Always check if your Python version works with `useragents` before using it in production

*Tested manually on `Python 2.7` and `Python 3.9`*

*Tested automatically (CI) with Pytest on `Python 2.7`, `Python 3.0` and `Python 3.9`*

### Installing

You can install it from PyPI with:

```bash
pip install useragents
```

You can check if you successfully installed it by printing out its version:

```bash
python -c "import useragents; print(useragents.__version__)"
# output:
useragents v1.0
```

## List of User-Agents

The list of User-Agents headers has been crawled from various sources.

They are all available in the `useragents/data/list.py` file.

> The list being in a python module means that it will be preloaded by Python in memory for performance reasons.

## Usage
```python
>>> import useragents
>>> headers = {
    "User-Agent": useragents.random(),
    "Content-Type": "application/json",
    "and so on..."
}
>>> useragents.random()
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
