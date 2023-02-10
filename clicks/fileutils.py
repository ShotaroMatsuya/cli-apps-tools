# fileutils.py
import typing

import click


@click.command()
@click.argument('fo', type=click.File('a'))  # file open (append mode)
def note(fo: typing.IO):
    """Write notes input to given file."""
    click.echo('Enter lines of text below and CTRL+C to exit.')
    try:
        while True:
            value = click.prompt('', prompt_suffix='>')
            fo.write(f'{value}\n')
    except click.Abort:
        click.echo(f'\noutput written to file {fo.name}')
