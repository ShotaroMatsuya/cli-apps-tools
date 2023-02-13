
import pytest
from click.testing import CliRunner

from calculator import add


def test_add():
    runner = CliRunner()
    result = runner.invoke(add, ['10', '20'])
    assert result.exit_code == 0
    assert result.output == '30\n'


def test_add_verbose():
    runner = CliRunner()
    result = runner.invoke(add, ['10', '20', '-v'])
    assert result.exit_code == 0
    assert result.output == '10 + 20 = 30\n'


def test_add_multiple():
    runner = CliRunner()
    result = runner.invoke(add, ['10', '20', '30', '-v'])
    assert result.exit_code == 0
    assert result.output == '10 + 20 + 30 = 60\n'


def test_add_multiples():
    runner = CliRunner()
    result = runner.invoke(add, ['10', '20', '30', '-vv'])
    assert result.exit_code == 0
    
    expected_output = ''.join([
        '10 = 10\n'
        '10 + 20 = 30\n',
        '10 + 20 + 30 = 60\n'
    ])
    assert result.output == expected_output