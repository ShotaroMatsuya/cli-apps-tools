from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.table import Column, Table

console = Console()
# console.print()
# console.log()  # Time


# Text/Color
console.print("Hello world", style="bold red")
console.print("[u]Hello[/u] [bold cyan]Jesse[/bold cyan]")

print("Hello [bold magenta]Jesse[/bold magenta]")

# Emoji
console.print("I :heart: coding :smiley:")

# Markdown
with open("README.md") as md:
    markdown = Markdown(md.read())
    console.print(markdown)

my_code = """
def hello(name):
    return "Hello {}".format(name)
"""
# Syntax
synt = Syntax(my_code, "python", theme="monokai", line_numbers=True)
console.print(synt)

# Tables
table = Table(show_header=True, header_style="bold cyan")

table.add_column("Title", style="dim", width=12)
table.add_column("Author", style="dim", width=12)

table.add_row("Python Handbook", "Wes Micn")

console.print(table)
