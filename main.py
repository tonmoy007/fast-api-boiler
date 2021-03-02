from app import create_app
from app.commands import commands

app = create_app()

if __name__ == '__main__':
    commands()
