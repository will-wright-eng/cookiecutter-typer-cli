import pytest
from typer.testing import CliRunner
from {{cookiecutter.package_name}}.app import app

runner = CliRunner()


@pytest.mark.parametrize("name", ["Alice", "Bob"])
def test_hello_command(name):
    result = runner.invoke(app, ["hello", name])
    assert result.exit_code == 0
    assert f"Hello, {name.title()}!" in result.output
