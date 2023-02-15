import click


# Method 1
@click.command()
@click.option("--firstname", "-f", prompt=True)
@click.option(
    "--password", "-p", prompt=True, hide_input=True, confirmation_prompt=True
)
def main(firstname, password):
    """A Simple CLI"""
    click.echo("Your firstname is {}".format(firstname))
    click.echo("Your password is {}".format(password))


# Method2
# @click.command()
# @click.option("--firstname", "-f", prompt="Enter your first name")
# def main(firstname):
#     """A Simple CLI"""
#     click.echo("Your firstname is {}".format(firstname))


# Method 3
# @click.command()
# def main():
#     """A Simple CLI"""
#     fname = click.prompt("Enter your firstname")
#     click.echo("Your firstname is {}".format(fname))
