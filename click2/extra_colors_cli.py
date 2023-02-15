import click
from click_help_colors import HelpColorsCommand, HelpColorsGroup


@click.group(cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="magenta")
def main():
    """A Click Extra CLI"""
    pass


@main.command(cls=HelpColorsCommand, help_options_color='blue')
@click.option('--name', '-n', help="Specify Name")
def sayhello(name):
    """Say Hello"""
    click.echo("Hello {}".format(name))
