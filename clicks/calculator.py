# calculator.py

import click


# multiple argument passing
@click.command()
@click.argument("xs", type=int, nargs=-1)
# @click.option("-v", "--verbose", help="Show additional output.", is_flag=True)
@click.option("-v", "--verbose", help="Show additional output.", count=True)
def add(xs, verbose):
    """Adds numbers."""
    if verbose > 1:  # vの数が入る(countの場合)
        steps = []
        results = 0
        for x in xs:
            steps.append(x)
            results += x
            click.echo(f"{' + '.join(str(s) for s in steps)} = {sum(steps)}")
    elif verbose == 1:
        click.echo(f"{' + '.join(str(x) for x in xs)} = {sum(xs)}")
    else:
        click.echo(sum(xs))

    # if verbose: # booleanが入る(is_flagの場合)
    #     click.echo(f"{' + '.join(str(s) for s in steps)} = {sum(steps)}")
    # else:
    #     click.echo(sum(xs))


# @click.command()
# @click.argument("x", type=int)
# @click.argument("y", type=int)
# def add(x, y):
#     """Adds numbers."""
#     click.echo(x + y)

# multiple argument passing
@click.command()
@click.argument("xs", type=int, nargs=-1)
# @click.option("-v", "--verbose", help="Show additional output.", is_flag=True)
@click.option("-v", "--verbose", help="Show additional output.", count=True)
def subtract(xs, verbose):
    """Subtracts numbers."""
    if verbose > 1:  # vの数が入る(countの場合)
        z = xs[0]
        steps = [z]
        for x in xs[1:]:
            steps.append(x)
            z -= x
            click.echo(f"{' - '.join(str(s) for s in steps)} = {z}")
    else:
        results = xs[0]
        for x in xs[1:]:
            results -= x

        if verbose == 1:
            click.echo(f"{' - '.join(str(x) for x in xs)} = {results}")
        else:
            click.echo(results)

    # results = xs[0]
    # for x in xs[1:]:
    #     results -= x

    # if verbose:# booleanが入る(is_flagの場合)
    #     click.echo(f"{' - '.join(str(x) for x in xs)} = {results}")
    # else:
    #     click.echo(results)


# @click.command()
# @click.argument("x", type=int)
# @click.argument("y", type=int)
# def subtract(x, y):
#     """Subtracts numbers."""
#     click.echo(x - y)
