# calculator.py

import click


# multiple argument passing
@click.command()
@click.argument("xs", type=int, nargs=-1)
def add(xs):
    """Adds numbers."""
    click.echo(sum(xs))


# @click.command()
# @click.argument("x", type=int)
# @click.argument("y", type=int)
# def add(x, y):
#     """Adds numbers."""
#     click.echo(x + y)

# multiple argument passing
@click.command()
@click.argument("xs", type=int, nargs=-1)
def subtract(xs):
    """Subtracts numbers."""
    results = xs[0]
    for x in xs[1:]:
        results -= x
    click.echo(results)


# @click.command()
# @click.argument("x", type=int)
# @click.argument("y", type=int)
# def subtract(x, y):
#     """Subtracts numbers."""
#     click.echo(x - y)
