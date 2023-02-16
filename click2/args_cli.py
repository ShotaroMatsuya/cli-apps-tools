# Position Arg
# Position is essential
# must

import click


@click.command()
@click.argument("number1", type=int)
@click.argument("number2", type=int)
@click.argument("operator")
def main(number1, number2, operator):
    """A Simple CLI with Pos Arg"""
    click.echo("A Simple Calculator")
    if operator == "add":
        result = number1 + number2
    if operator == "subtract":
        result = number1 - number2
    if operator == "multiply":
        result = number1 * number2
    if operator == "divide":
        result = number1 / number2
    click.echo("Result {}".format(result))


if __name__ == "__name__":
    main()
