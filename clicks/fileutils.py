# fileutils.py
import typing

import click
import requests
from pyfiglet import Figlet


@click.command()
@click.argument("fo", type=click.File("a"))  # file open (append mode)
def note(fo: typing.IO):
    """Write notes input to given file."""
    click.echo("Enter lines of text below and CTRL+C to exit.")
    f = Figlet(font="slant")
    click.echo(f.renderText("text to render"))
    try:
        while True:
            value = click.prompt("", prompt_suffix=">")
            fo.write(f"{value}\n")
    except click.Abort:
        click.echo(f"\noutput written to file {fo.name}")


@click.command()
@click.argument("inputs", type=click.File("r"), nargs=-1)  # input file (read mode)
@click.argument("output", type=click.File("w"))  # final argument (write mode)
def concat(inputs: typing.Collection[typing.IO], output: typing.IO):
    """Concatenates the contents of one or more files into an output file."""
    for f in inputs:
        for line in f:
            output.write(line)
        click.echo(f"{f.name} written to {output.name}")


@click.command()
@click.argument("inputs", nargs=-1)
def download(inputs):
    """Downloads web resource from (url, filename) input pairs.

    Example:
        download http://xyz.com/p1.txt,page1.txt http://xyz.com/p2.txt,page2.txt

        this fetches web resources by url and saves them locally to filename.
    """

    with click.progressbar(
        length=len(inputs),
        show_eta=False,
        item_show_func=lambda fname: f"Downloading {fname}",
    ) as bar:
        for i, item in enumerate(inputs):
            url, file_name = item.split(",")
            response = requests.get(url)
            with open(file_name, "w") as fo:
                fo.write(response.text)
            bar.update(i, file_name)  # updateされるたびにitem_show_funcが実行される

    click.echo("Download complete.")
