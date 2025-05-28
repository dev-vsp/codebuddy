
import click

from .modules import *


@click.command(help="Script for git repository analysis and reporting.")
@click.argument("api", type=str)
@click.argument("repository", type=click.Path(exists=True, file_okay=False))
def review(api, repository):
    pass


if __name__ == "__main__":
    review()
