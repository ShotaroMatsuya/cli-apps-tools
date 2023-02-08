# greeter.py

import click


@click.command()
@click.argument("name")
def greet():
    """Displays a greeting to the user."""
    click.echo("Hello")
