import click


@click.command()
# option (non mandatory, --)
@click.option(
    "--firstname", "-f", help="Firstname Description", type=str, default="Friend"
)
@click.option("--age", "-a", help="Your Age", type=int)
# multiple value for an option
# salary 200 2003 040045 00
@click.option("--salary", "-s", help="Your Salary", nargs=2, type=int)

# multiple options
# -f Jesse -f David -f
@click.option("--city", "-c", help="Your Cities", multiple=True)
@click.version_option("0.01", prog_name="basic_cli")
def main(firstname, age, salary, city):
    """A Simple CLI"""
    click.echo("Hello CLI builders")
    click.echo("Hello {} your age is {}".format(firstname, age))
    year_by_now = 1 + age
    click.echo("You will be this {} a year by now".format(year_by_now))
    click.echo("Your salary is {}".format(sum(salary)))
    click.echo("Your visited {}".format(city))


if __name__ == "__main__":
    main()
