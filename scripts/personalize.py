"""
Run this script once after first creating your project from this template repo to personalize
it for own project.

This script is interactive and will prompt you for various inputs.
"""

FILES_TO_REMOVE = {
    ".github/workflows/setup.yml",
    "setup-requirements.txt",
}

BASE_URL_TO_REPLACE = "https://github.com/allenai/python-package-template"

import click
from click_help_colors import HelpColorsCommand
from rich import print
from rich.prompt import Confirm
from rich.traceback import install

install(show_locals=True, suppress=[click])


@click.command(
    cls=HelpColorsCommand,
    help_options_color="green",
    help_headers_color="yellow",
    context_settings={"max_content_width": 115},
)
@click.option(
    "--github-org",
    prompt="GitHub organization or user (e.g. 'allenai')",
    help="The name of your GitHub organization or user.",
)
@click.option(
    "--github-repo",
    prompt="GitHub repository (e.g. 'python-package-template')",
    help="The name of your GitHub repository.",
)
@click.option(
    "--package-name",
    prompt="Python package name (e.g. 'my_package')",
    help="The name of your Python package.",
)
@click.option(
    "-y",
    "--yes",
    is_flag=True,
    help="Run the script without prompting for a confirmation.",
    default=False,
)
def main(github_org: str, github_repo: str, package_name: str, yes: bool = False):
    if not yes:
        yes = Confirm.ask("Is this correct?")
    if not yes:
        raise click.ClickException("Aborted, please run script again")


if __name__ == "__main__":
    main()
