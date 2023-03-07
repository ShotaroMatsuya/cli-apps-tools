import sqlite3

import click
from click_help_colors import HelpColorsGroup

# Database
conn = sqlite3.connect("ideabank.db")
c = conn.cursor()


# Create Table
def create_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS ideatable(title TEXT,detail TEXT,status TEXT)"
    )


# Add Data
def add_data(title, detail, status):
    c.execute(
        "INSERT  INTO ideatable(title,detail,status) VALUES (?,?,?)",
        (title, detail, status),
    )
    conn.commit()


# View Data
def view_all_ideas():
    c.execute("SELECT * FROM ideatable")
    data = c.fetchall()
    return data


# Search
def get_single_idea(title):
    c.execute('SELECT * FROM ideatable WHERE title="{}"'.format(title))
    data = c.fetchall()
    return data


def get_idea_by_title(title):
    c.execute('SELECT * FROM ideatable WHERE title="{}"'.format(title))
    data = c.fetchall()
    return data


def get_idea_by_details(details):
    c.execute('SELECT * FROM ideatable WHERE details="{}"'.format(details))
    data = c.fetchall()
    return data


def get_idea_by_status(status):
    c.execute("SELECT * FROM ideatable WHERE status like '%{}%'".format(status))
    data = c.fetchall()
    return data


@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="green"
)
@click.version_option(prog_name="idealist", version="0.01")
def main():
    """Idealist CLI - Idea Notes Keeping CLI"""
    pass


@main.command()
@click.option("--title", "-t", help="Title of Idea", prompt=True, type=str)
@click.option("--detail", "-d", help="Details of Idea", prompt=True, type=str)
@click.option(
    "--status",
    "-s",
    help="Status of Idea",
    prompt=True,
    type=click.Choice(["ToDo", "Doing", "Done"]),
)
def add_idea(title, detail, status):
    """Add Idea To Database"""
    click.echo("Add A New Idea")
    click.secho("Added {} to DB".format(title), fg="blue")
    click.echo("=====Summary=====")
    # table
    create_table()
    add_data(title, detail, status)
    from terminaltables import AsciiTable

    user_idea = [
        ["Idea Info", "Details"],
        ["Title", title],
        ["Detail", detail],
        ["Status", status],
    ]
    table1 = AsciiTable(user_idea)
    click.echo(table1.table)


@main.command()
@click.option("--title", "-t", prompt=True)
def view_idea(title):
    """View Idea By Title"""
    click.secho("Searched For {}".format(title), fg="blue")
    from terminaltables import AsciiTable

    result = get_single_idea(title)
    table1 = AsciiTable(result)
    click.echo(table1.table)


@main.command()
@click.argument("text")
@click.option(
    "--by",
    "-b",
    default="title",
    help="Option to Search By",
    type=click.Choice(["title", "details", "status"]),
)
def search(text, by):
    """Search By Option [Title/Details/Status]

    idealist search "Your Term" --by "title"

    """
    click.secho("Searched For {}".format(text), fg="blue")
    from terminaltables import AsciiTable

    if by == "title":
        result = get_idea_by_title(text)
        table1 = AsciiTable(result)
        click.echo(table1.table)
    elif by == "details":
        result = get_idea_by_details(text)
        table1 = AsciiTable(result)
        click.echo(table1.table)
    elif by == "status":
        result = get_idea_by_status(text)
        table1 = AsciiTable(result)
        click.echo(table1.table)
    else:
        click.secho(
            "{} Not found Try [title/status/details]".format(by), fg="white", bg="red"
        )


@main.command()
def show_all():
    """Show All Idea"""
    click.echo("Showing All Idea")
    click.echo("===================")
    from terminaltables import AsciiTable

    result = view_all_ideas()
    new_result_header = ["Title", "Details", "Status"]
    click.secho("{}".format(new_result_header))
    table1 = AsciiTable(result)
    click.echo(table1.table)


# Add Ideas
# View idea by title
# Search Idea by title
# Show All the Ideas

# Structure
# idealist add-idea
# idealist add-idea --title /details/status

# idealist view-idea
# idealist search
# idealist show-all
