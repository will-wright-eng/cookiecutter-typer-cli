import os
import json
from typing import Optional
from pathlib import Path

import toml
import typer
from typer import echo

from {{ cookiecutter.package_name }}.config import Config

app = typer.Typer(add_completion=False)


def get_version():
    pyproject = toml.load("pyproject.toml")
    return pyproject["tool"]["poetry"]["version"]


def version_callback(value: bool):
    if value:
        print(f"{{ cookiecutter.package_name_upper }} CLI Version: {get_version()}")
        raise typer.Exit()


@app.callback()
def common(
    ctx: typer.Context,
    version: bool = typer.Option(
        None, "--version", callback=version_callback, help="Show the version and exit.", is_eager=True
    ),
):
    pass


@app.command()
def hello(name: str) -> None:
    """
    first endpoint
    """
    print(f"Hello, {name.title()}!")
    return

@app.command()
def config_test() -> None:
    """
    config test endpoint
    """

    configs = Config().get_configs()
    print(f"configs:\n{json.dumps(configs, indent=2)}")
    return


def write_config(config):
    config.dotenv_path.unlink(missing_ok=True)
    config.dotenv_path.touch()
    echo()
    env_vars = {}
    config_dict = config.configs

    for _, val in config.keys_dict.items():
        key = val.get("name")

        if config_dict:
            res_default = config_dict.get(key)
        else:
            res_default = None

        res = typer.prompt(f"{key} ({val.get('note')})", type=str, default=res_default)
        env_vars[key] = res

    config.write_env_vars(env_vars)
    config.print_current_config()


@app.command()
def config() -> None:
    """
    Configures the application
    """
    config = Config()

    if config.check_exists():
        config.load_env()
        config.print_current_config()

        if typer.confirm("Would you like to overwrite these settings?", default=False):
            echo("Overwriting")
            write_config(config)
    else:
        write_config(config)

    echo("Configuration complete.")


def entry_point() -> None:
    app()


if __name__ == "__main__":
    entry_point()
