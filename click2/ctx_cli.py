import click


# Parent Cmd
@click.group(chain=True)
@click.option("--name")
@click.pass_context
def main(ctx, name):
    """A Simple CLI with Group"""
    ctx.ensure_object(dict)
    ctx.obj["name"] = name


# Child Cmd
@main.command()
@click.pass_context
def reverse(ctx):
    """Reverse A text"""
    new_name = ctx.obj["name"]
    click.echo("{}".format(new_name[::-1]))


@main.command()
@click.pass_context
def capitalize(ctx):
    """Capitalize A Text"""
    click.echo(ctx.obj["name"].upper())
