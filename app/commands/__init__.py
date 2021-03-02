import typer

from app.commands.users import user_command
from app.db.models import *

commands: typer.Typer = typer.Typer(help="Fast Api Command Line")


@commands.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@commands.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


commands.add_typer(user_command, name='user', help="All User Commands")
