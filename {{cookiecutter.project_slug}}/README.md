# {{ cookiecutter.project_name }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }})](https://pypi.org/project/{{ cookiecutter.package_name }}/)
[![Downloads](https://static.pepy.tech/badge/{{ cookiecutter.package_name }}/month)](https://pepy.tech/project/{{ cookiecutter.package_name }})
[![Supported Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://pypi.org/project/{{ cookiecutter.package_name }}/)
[![Contributors](https://img.shields.io/github/contributors/will-wright-eng/{{ cookiecutter.project_slug }}.svg)](https://github.com/will-wright-eng/{{ cookiecutter.project_slug }}/graphs/contributors)
[![Tests](https://github.com/will-wright-eng/{{ cookiecutter.project_slug }}/workflows/Test/badge.svg)](https://github.com/will-wright-eng/{{ cookiecutter.project_slug }}/actions?query=workflow%3ATest)

## Summary

**{{ cookiecutter.project_short_description }}**

- generated using: [will-wright-eng/cookiecutter-typer-cli](https://github.com/will-wright-eng/cookiecutter-typer-cli)

## Installing `{{ cookiecutter.package_name }}` & Supported Versions

`{{ cookiecutter.package_name }}` is available on PyPI:

```bash
python -m pip install {{ cookiecutter.package_name }}
```

{{ cookiecutter.project_name }} Command Line Interface officially supports Python 3.8+.

## Quick Start

- setup global config file `~/.config/{{ cookiecutter.package_name }}/config`

```bash
{{ cookiecutter.package_name }} config
```

*fill out prompts*

```bash
{{ cookiecutter.package_name }} config
```

*check configs are correct*

```bash
{{ cookiecutter.package_name }} hello will
# Hello, Will!
```


## Supported Features & Usage

For help, run:

```bash
{{ cookiecutter.package_name }} --help
```

Commands:

```bash
➜ {{ cookiecutter.package_name }} --help

 Usage: {{ cookiecutter.package_name }} [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  config       Configures the application
  config-test  config test endpoint
  hello        first endpoint
```

## Development

To contribute to this tool, first checkout the code:

```bash
git clone https://github.com/will-wright-eng/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
```

Then create a new virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

To run the tests:

```bash
pytest
```

Install pre-commit before submitting a PR:

```bash
brew install pre-commit
pre-commit install
```

## References

- [PyPI Package](https://pypi.org/project/{{ cookiecutter.package_name }})
- Based on cookiecutter template [will-wright-eng/click-app](https://github.com/will-wright-eng/click-app)
