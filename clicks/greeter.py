# greeter.py

import click


@click.command()
@click.argument("name")
@click.option(
    "--lang", help="Specify language English (en) or Spanish (es)", default="en"
)
def greet(name, lang):
    """Displays a greeting to the user."""
    if lang == "es":
        greetings = "Hola"
    elif lang == "en":
        greetings = "Hello"
    else:
        raise click.BadOptionUsage("lang", "Unsupported language.")
    click.echo(f"{greetings} {name}")
