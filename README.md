# cookiecutter-typer-cli

## summary


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
