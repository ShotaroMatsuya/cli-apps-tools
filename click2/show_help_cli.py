import click


def recursive_help(cmd, parent=None):
    ctx = click.core.Context(cmd, info_name=cmd.name, parent=parent)
    print(cmd.get_help(ctx))
    print("-----------------")
    commands = getattr(cmd, "commands", {})
    for sub in commands.values():
        recursive_help(sub, ctx)


@click.group()
def main():
    """A Simple CLI with Python"""
    pass


@main.command()
@click.argument("text")
def reverse(text):
    """Reverse A Text"""
    click.echo(text[::-1])


@main.command()
@click.argument("text")
def capitalize(text):
    """Capitalize A Text"""
    click.echo(text.upper())


@main.command()
def show_help():
    recursive_help(main)
