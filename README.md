[![build](https://github.com/masaaldosey/python-template/actions/workflows/tests.yml/badge.svg)](https://github.com/masaaldosey/python-template/actions/workflows/tests.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/masaaldosey/python-template/main.svg)](https://results.pre-commit.ci/latest/github/masaaldosey/python-template/main)
[![codecov](https://codecov.io/gh/masaaldosey/python-template/branch/main/graph/badge.svg?token=WMM2Wzcjm8)](https://codecov.io/gh/masaaldosey/python-template)

# python-template
A very minimal Python project template.

## Features
- **Static analysis** using [pre-commit](https://pre-commit.com/).
- **CI** workflows (via *GitHub Actions*) for Linux and Windows.
- **Code coverage** enabled with *Codecov* integration.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Pre-requisites
This project can be changed to better suit the needs of the developer(s). If you wish to use the template as-is, then you will need the following to be installed on your system:
- `python3` (recommend python3.9 or higher) ([here](https://www.python.org/downloads/))
- `virtualenv` ([here](https://virtualenv.pypa.io/en/latest/installation.html))
- `tox` ([here](https://tox.wiki/en/latest/installation.html))

### Building
Provided that all the pre-requisites are installed, the project can be built as below:

```shell
$ virtualenv venv                      # create the virtual environment
$ source venv/bin/activate             # activate the virtual environment
$ python -m pip install --upgrade pip  # upgrade pip
$ pip install -r requirements-dev.txt  # install the dev requirements
$ pytest -v                            # run pytest
```

You should see an output where the two tests pass.


### Verify with `tox`
It is easier to verify the build with `tox`. You can simply type `tox` in the terminal.

```shell
$ tox
```
