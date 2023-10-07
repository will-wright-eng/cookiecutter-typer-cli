# cookiecutter-typer-cli

## summary

generates boilerplate code for typer command line interface application

## features

- pyproject
- codeowner
- typer app
	- config module for gloally awareness
	- log module for debugging
- `.github/`
	- github actions
		- pypi publishing
		- codespell
		- test
	- md templates
		- pull request
		- bug report
		- feature request
		- question
	- dependabot

## json

```js
{
    "project_name": "Typer Project",
    "project_slug": "{{ cookiecutter.project_name|lower|replace(' ', '-') }}",
    "package_name": "{{ cookiecutter.project_slug|lower|replace('-', '_') }}",
    "package_name_upper": "{{ cookiecutter.package_name|upper }}",
    "project_short_description": "a short description",
    "full_name": "John Smith",
    "github_username": "jsmith",
    "email": "john@example.com",
    "open_source_license": "GNU GPL v3.0",
    "_copy_without_render": [
        ".github/workflows/*.yml"
    ]
}
```

## test

```bash
cookiecutter cookiecutter-typer-cli/ -o test --no-input

conda env remove -n test
conda create -n test python=3.8 -y

cd test/typer-project/
python -m pip install -e .
```

## references

- [tiangolo/full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [will-wright-eng/cookiecutter-click-cli](https://github.com/will-wright-eng/cookiecutter-click-cli)
