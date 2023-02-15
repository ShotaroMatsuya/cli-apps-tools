import click


@click.group()
def main():
    """"""
    pass


# Child
@main.group()
def reverse():
    """Reverse A Text"""


# Grandchild/Subcommand
@reverse.command("upper")
@click.argument("name")
def reverse_upper(name):
    """Reverse and Convert to Uppercase"""
    click.echo(name[::-1].upper())


# Grandchild/Subcommand
@reverse.command("lower")
@click.argument("name")
def reverse_lower(name):
    """Reverse and Convert to Lowercase"""
    click.echo(name[::-1].lower())


@main.group()
def capitalize():
    """Capitalize A text"""


@capitalize.command("upper")
@click.argument("name")
def capitalize_upper(name):
    """Capitalize and Convert to Uppercase"""
    click.echo(name.upper())
