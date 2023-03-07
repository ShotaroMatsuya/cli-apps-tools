import click
# Purpose 
# Tracking Keeping records of jobs
import sqlite3
from terminaltables import AsciiTable

from click_didyoumean import DYMGroup
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from pkg_resources import iter_entry_points
from click_plugins import with_plugins

conn = sqlite3.connect('data.db')
c = conn.cursor()


# Table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS jobstable(name TEXT, address TEXT, email TEXT, title TEXT, jobtype TEXT, salary INTEGER, status TEXT)')


# Add Data
def add_data(name, address, email, title, jobtype, salary, status):
    c.execute('INSERT INTO jobstable (name, address, email, title, jobtype, salary, status) VALUES(?,?,?,?,?,?,?)', (name, address, email, title, jobtype, salary, status))
    conn.commit()


# View Data
def view_all_jobs():
    c.execute('SELECT * FROM jobstable')
    data = c.fetchall()
    return data


# Search/View
def get_single_job(title):
    c.execute('SELECT * FROM jobstable WHERE title="{}"'.format(title))
    data = c.fetchall()
    return data


def get_job_by_title(title):
    c.execute('SELECT * FROM jobstable WHERE title = "{}"'.format(title))
    data = c.fetchall()
    return data

    
def get_job_by_name(name):
    c.execute('SELECT * FROM jobstable WHERE name = "{}"'.format(name))
    data = c.fetchall()
    return data
    
    
def get_job_by_address(address):
    c.execute("SELECT * FROM jobstable WHERE address LIKE '%{}%'".format(address))
    data = c.fetchall()
    return data

    
def get_job_by_status(status):
    c.execute("SELECT * FROM jobstable WHERE status LIKE '%{}%'".format(status))
    data = c.fetchall()
    return data


def edit_job_by_name(name, new_name):
    c.execute('UPDATE jobstable SET name="{}" WHERE name="{}"'.format(new_name, name))
    conn.commit()
    data = c.fetchall()
    return data


def edit_job_by_status(status, new_status):
    c.execute('UPDATE jobstable SET status="{}" WHERE status="{}"'.format(new_status, status))
    conn.commit()
    data = c.fetchall()
    return data


def edit_job_by_title(title, new_title):
    c.execute('UPDATE jobstable SET title="{}" WHERE title="{}"'.format(new_title, title))
    conn.commit()
    data = c.fetchall()
    return data


def delete_data(title):
    c.execute('DELETE FROM jobstable WHERE title="{}"'.format(title))
    conn.commit()


# @click.group(cls=HelpColorsGroup, help_headers_color='yellow', help_options_color='cyan')
@with_plugins(iter_entry_points('click_command_tree'))
@click.group(cls=DYMGroup)
@click.version_option('0.0.1', prog_name='jobracker_cli')
def main():
    """Jobtracker CLI -Job tracking and record keeping CLI"""
    pass


# jobtracker add-job name/address/email/title/salary/status/jobtype
@main.command(cls=HelpColorsCommand, help_headers_color='yellow', help_options_color='cyan')
@click.option('--name', '-n', help='Name of Company', type=str, prompt=True)
@click.option('--address', '-a', help="Address of Company", type=str, prompt=True)
@click.option('--email', '-e', help="Email of Company", type=str, prompt=True)
@click.option('--title', '-t', help="Job Title for You", type=str, prompt=True)
@click.option('--jobtype', '-jt', help="Job Type", type=click.Choice(['Full-Time', 'Remote', 'Part-Time', 'Contract']), prompt=True)
@click.option('--salary', '-s', help="Salary of Company", type=float, prompt=True)
@click.option('--status', '-st', help="Job Search Status", type=click.Choice(['Pending', 'Cancelled', 'Success']), prompt=True)
def add_job(name, address, email, title, jobtype, salary, status):
    """Add Job"""
    click.echo("Adding Job")
    click.echo("Adding Job")
    click.secho("Adding {} to DB".format(name), fg='blue')
    click.echo("==============Summary=============")

    job_notes = [
        ['Job Info', 'Details'],
        ['Companay Name:', name],
        ['Companay Address:', address],
        ['Companay Email:', email],
        ['Job Title:', title],
        ['Job Type:', jobtype],
        ['Job Salary:', salary],
        ['Status:', status],
    ]
    create_table()
    add_data(name, address, email, title, jobtype, salary, status)
    table1 = AsciiTable(job_notes)
    click.echo(table1.table)
    click.secho("Saved job to DB", fg='white', bg='yellow')


# jobtracker show-all-job
@main.command()
def show_all():
    """Show All Jobs"""
    result = view_all_jobs()
    new_result = ['Company Name', 'Address', 'Email', 'Title', 'JobType', 'Salary', 'Status']
    result.insert(0, new_result)
    click.secho('{}'.format(new_result), bg='blue')
    table1 = AsciiTable(result, 'TableTitle')
    # table1.inner_footing_row_border = True
    # table1.justify_columns[0] = 'left'
    # table1.justify_columns[1] = 'center'
    # table1.justify_columns[2] = 'right'

    click.echo(table1.table)


# jobtracker view-job
@main.command()
@click.option('--title', '-t', prompt=True, help="View Job by Title")
def view_job(title):
    """View Job"""
    click.secho("Search For ::{}".format(title), fg='white', bg='cyan')
    result = get_single_job(title)
    new_result = ['Company Name', 'Address', 'Email', 'Title', 'JobType', 'Salary', 'Status']
    click.secho('{}'.format(new_result), bg='blue')
    table1 = AsciiTable(result)

    click.echo(table1.table)


# jobtracker search "job" --by name/title/status
@main.command()
@click.argument('text')
@click.option('--by', '-b', default='title', type=click.Choice(["name", "title", "status"]))
def search(text, by):
    """Search Jobs By [name/title/status]"""
    click.secho("Search For ::{}".format(text), fg='white', bg='cyan')
    if by == 'title':
        result = get_job_by_title(text)
        table1 = AsciiTable(result)
        click.echo(table1.table)
    elif by == 'name':
        result = get_job_by_name(text)
        table1 = AsciiTable(result)
        click.echo(table1.table)
    elif by == 'status':
        result = get_job_by_status(text)
        table1 = AsciiTable(result)
        click.echo(table1.table)
    else:
        click.secho("{} Not a Choice, Please Try Either of these [name/title/status]".format(by), fg='white', bh='red')


# jobtracker edit-job --field Title --old Developer --new Data Scientist
@main.command()
@click.option('--field', '-f')
@click.option('--old', '-o', help="Old Data To Edit")
@click.option('--new', '-n', help="New Data To Update")
def edit_job(field, old, new):
    """Edit Job
    jobtracker_cli edit-job --field Title --old Developer --new "Data Scientist"
    """
    click.secho("Editing Field:: {} with ::{} and updating ::{}".format(field, old, new), fg='white', bg='yellow')
    click.echo("================Previous===============")
    headers = ['Company Name', 'Address', 'Email', 'Title', 'JobType', 'Salary', 'Status']
    result1 = view_all_jobs()
    result1.insert(0, headers)
    table1 = AsciiTable(result1)
    click.echo(table1.table)
    
    if field == 'title':
        result2 = edit_job_by_title(old, new)
        result2.insert(0, headers)
    elif field == 'name':
        result2 = edit_job_by_name(old, new)
        result2.insert(0, headers)
    elif field == 'status':
        result2 = edit_job_by_status(old, new)
        result2.insert(0, headers)
    click.echo("================Updated===============")
    result1 = view_all_jobs()
    result1.insert(0, headers)
    table1 = AsciiTable(result1)
    click.echo(table1.table)
    
    
# jobtracker delete-job
@main.command()
@click.option('--title', '-t')
def delete_job(title):
    """Delete job"""
    click.secho("Deleting ::{}".format(title), fg='white', bg='red')
    click.echo("================Previous===============")
    headers = ['Company Name', 'Address', 'Email', 'Title', 'JobType', 'Salary', 'Status']
    result1 = view_all_jobs()
    result1.insert(0, headers)
    table1 = AsciiTable(result1)
    click.echo(table1.table)
    
    delete_data(title)
    click.secho("Deleted From DB", fg='white', bg='red')