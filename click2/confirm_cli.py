import click

# Method 1
# @click.command()
# @click.argument("file_name", required=True)
# def download(file_name):
#     """Download Files"""
#     click.confirm("Do you want to continue downloading ", abort=True, default=True)
#     click.echo("Downloading {}".format(file_name))


# Method 2
@click.command()
@click.argument("file_name", required=True)
@click.confirmation_option(prompt="Do you want to continue downloading?")
def download(file_name):
    """Download Files"""
    click.echo("Downloading {}".format(file_name))
