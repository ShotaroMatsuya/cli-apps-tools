import click
import random
import data

from termcolor import cprint


@click.command()
@click.option("--recommend", "-r", help="Randomly Recommend", type=click.Choice(["books", "movies", "datascience"]))
@click.option("--limit", "-l", help="Set Limit", default=2, type=int)
@click.version_option("0.01", prog_name="randomix_click")
def main(recommend, limit):
    """A Simple Recommendation CLI"""
    if recommend == 'books':
        cprint("Recommended {}".format(recommend), 'white', 'on_blue')
        results = random.choices(data.books_list, k=limit)
        for result in results:
            click.echo(result)
    elif recommend == 'movies':
        cprint("Recommended {}".format(recommend), 'white', 'on_blue')
        results = random.choices(data.movies_list, k=limit)
        for result in results:
            click.echo(result)
    elif recommend == 'datascience':
        cprint("Recommended {}".format(recommend), 'white', 'on_blue')
        results = random.choices(data.datascience_blogs, k=limit)
        for result in results:
            click.echo(result)
    else:
        cprint("Recommended {}".format('books'), 'white', 'on_blue')
        results = random.choices(data.books_list, k=limit)
        for result in results:
            click.echo(result)        