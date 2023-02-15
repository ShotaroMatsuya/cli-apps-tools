import click


# Variadic Argument/ multiple Argument
@click.command()
@click.argument("source", nargs=-1)  # accept unlimited number of values
@click.argument("destination")
def main(source, destination):
    """A Simple CLI with varidadic Argument"""
    for f in source:
        click.echo("Moving {} to folder {}".format(f, destination))
