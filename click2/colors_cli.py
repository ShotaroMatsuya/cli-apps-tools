import click


@click.command()
@click.option("--name", "-n")
def main(name):
    """A simple CLI"""
    click.echo(click.style("Hello {}".format(name), fg="blue", bg="white", bold=True))
    click.secho("Your name is {}".format(name), fg="yellow")

    click.echo("Your name is " + click.style(name, fg="red"))
