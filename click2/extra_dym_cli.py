import click
from click_didyoumean import DYMGroup


@click.group(cls=DYMGroup, max_suggestions=2)
def main():
    """A Simple CLI with Python"""
    pass

@main.command()
@click.argument("text")
def reverse(text):
    """Reverse A Text"""
    click.echo(text[::-1])


@main.command()
@click.argument('text')
def capitalize(text):
    """Capitalize A Text"""
    click.echo(text.upper())

