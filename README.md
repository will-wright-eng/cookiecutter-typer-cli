# cookiecutter-typer-cli

## summary

- based on tiangolo's Typer and [tiangolo/full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql)

`test`

```bash
cookiecutter cookiecutter-typer-cli/ -o test -f --no-input

conda env remove -n test
conda create -n test python=3.8 -y
python -m pip install -e .
```
