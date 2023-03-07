import click
import sqlite3
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


def show_idea_on_table(result: list):
    title, detail, status = result[0]
    return [
        ["Idea Info", "Details"],
        ["Title", title],
        ["Detail", detail],
        ["Status", status],
    ]


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
    c.execute('SELECT * FROM ideatable WHERE detail="{}"'.format(details))
    data = c.fetchall()
    return data


def get_idea_by_status(status):
    c.execute("SELECT * FROM ideatable WHERE status like '%{}%'".format(status))
    data = c.fetchall()
    return data


# update
def update_title(title, idea_title):
    results = get_idea_by_title(idea_title)
    if len(results) != 0:
        c.execute(
            'UPDATE ideatable SET (title) = (?) WHERE title ="{}"'.format(idea_title),
            [title],
        )
        conn.commit()
        return get_single_idea(title)
    else:
        return []


def update_details(details, idea_title) -> list:
    results = get_idea_by_title(idea_title)
    if len(results) != 0:
        c.execute(
            'UPDATE ideatable SET (detail) = (?) WHERE title ="{}"'.format(idea_title),
            [details],
        )
        conn.commit()
        return get_single_idea(idea_title)
    else:
        return []


def update_status(status, idea_title):
    results = get_idea_by_title(idea_title)
    if len(results) != 0:
        c.execute(
            'UPDATE ideatable SET (status) = (?) WHERE title ="{}"'.format(idea_title),
            [status],
        )
        conn.commit()
        return get_single_idea(idea_title)
    else:
        return []


# delete
def delete_idea_by(title):
    c.execute('DELETE FROM ideatable WHERE title="{}"'.format(title))
    conn.commit()


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
    # table
    create_table()
    add_data(title, detail, status)
    from terminaltables import AsciiTable

    click.echo("=====Summary=====")
    user_idea = show_idea_on_table(get_single_idea(title))
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
    """Search By Option [Title/Details/Status]"""
    click.secho("Searched For {}".format(text), fg="blue")
    from terminaltables import AsciiTable

    if by == "title":
        result = get_idea_by_title(text)
        table1 = AsciiTable(result)
        click.echo(table1.table)

    elif by == "detail":
        result = get_idea_by_details(text)
        table1 = AsciiTable(result)
        click.echo(table1.table)

    elif by == "status":
        result = get_idea_by_status(text)
        table1 = AsciiTable(result)
        click.echo(table1.table)

    else:
        click.secho(
            "{} Not found [title/status/details]".format(by), fg="white", bg="red"
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


@main.command()
@click.option("--title", "-t", prompt=True, help="Idea Title to be updated", type=str)
@click.option(
    "--on",
    "-o",
    help="Column to be Updated",
    prompt=True,
    type=click.Choice(["title", "details", "status"]),
)
@click.option("--value", "-v", help="Set New Value", prompt=True, type=str)
def update(title, on, value):
    """Update by Option [Title/Details/Status]"""
    click.secho("Updated {} on DB".format(title), fg="blue")
    click.echo("=====Summary=====")
    from terminaltables import AsciiTable

    if on == "title":
        result = update_title(value, title)
        if len(result) == 0:
            click.secho("{} is Not found [title]".format(title), fg="white", bg="red")
        else:
            table1 = AsciiTable(result)
            click.echo(table1.table)
    elif on == "details":
        result = update_details(value, title)
        if len(result) == 0:
            click.secho("{} is Not found [title]".format(title), fg="white", bg="red")
        else:
            table1 = AsciiTable(result)
            click.echo(table1.table)
    elif on == "status":
        result = update_status(value, title)
        if len(result) == 0:
            click.secho("{} is Not found [title]".format(title), fg="white", bg="red")
        else:
            table1 = AsciiTable(result)
            click.echo(table1.table)


@main.command()
@click.option("--title", "-t", prompt=True, help="Idea Title to be deleted", type=str)
def delete(title):
    """Delete by title"""
    click.secho("Deleted {} from DB".format(title), fg="blue")
    delete_idea_by(title)
