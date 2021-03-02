import typer
from fastapi_sqlalchemy import db

from app.db import db_session
from app.db.models.user import User

user_command = typer.Typer()


@user_command.command()
def users():
    with db():
        user = db_session.query(User).filter_by(ref_type='partner').all()
        print(user)
        typer.echo("Hello users and i am video")
