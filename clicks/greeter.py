# greeter.py

import click


@click.command()
@click.argument("name")
@click.option(
    "-l",
    "--lang",
    help="Specify language English (en) or Spanish (es)",
    default="en",
    type=click.Choice(["es", "en"]),
)
def greet(name, lang):
    """Displays a greeting to the user."""
    greetings = "Hello " if lang == "en" else "Hola"
    click.echo(f"{greetings} {name}")
