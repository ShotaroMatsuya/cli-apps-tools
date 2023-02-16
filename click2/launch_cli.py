import click


@click.group()
def main():
    """A simple CLI Launcher"""
    pass


@main.command()
@click.argument("url")
def open_url(url):
    """Open Url"""
    click.echo("Opening Url")
    click.launch(url)


@main.command()
@click.argument("file")
@click.option("--locate", "-l")
def open_file(file, locate):
    """Open File"""
    click.echo("Opening File")
    click.launch(file, locate=locate)
