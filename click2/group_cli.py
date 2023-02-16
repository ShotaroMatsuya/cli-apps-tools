import click


# Parent Cmd
@click.group()
def main():
    """A Simple CLI with Group"""
    pass


# Child Cmd
@main.command()
@click.argument("text")
def reverse(text):
    """Reverse A text"""
    click.echo(text[::-1])


@main.command()
@click.argument("text")
def capitalize(text):
    """Capitalize A Text"""
    click.echo(text.upper())
