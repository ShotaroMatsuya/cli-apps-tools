import click
import click_config_file


@click.command()
@click.option('--name', '-n', help="Specify Name")
@click.option('--location', '-l', help="Specify Location")
@click_config_file.configuration_option()
def main(name, location):
    """A Simple CLI Extra CLI"""
    click.echo("Hello {}".format(name))
    click.echo("Your location is {}".format(location))
