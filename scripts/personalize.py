"""
Run this script once after first creating your project from this template repo to personalize
it for own project.

This script is interactive and will prompt you for various inputs.
"""

import sys
from pathlib import Path
from typing import Generator, List, Tuple

import click
from click_help_colors import HelpColorsCommand
from rich import print
from rich.markdown import Markdown
from rich.prompt import Confirm
from rich.syntax import Syntax
from rich.traceback import install

install(show_locals=True, suppress=[click])

REPO_BASE = (Path(__file__).parent / "..").resolve()

FILES_TO_REMOVE = {
    REPO_BASE / ".github" / "workflows" / "setup.yml",
    REPO_BASE / "setup-requirements.txt",
    REPO_BASE / "scripts" / "personalize.py",
}

PATHS_TO_IGNORE = {
    REPO_BASE / "README.md",
    REPO_BASE / ".git",
    REPO_BASE / "docs" / "source" / "_static" / "favicon.ico",
}

GITIGNORE_LIST = [
    line.strip()
    for line in (REPO_BASE / ".gitignore").open(encoding="utf-8").readlines()
    if line.strip() and not line.startswith("#")
]

REPO_NAME_TO_REPLACE = "python-package-template"
BASE_URL_TO_REPLACE = "https://github.com/allenai/python-package-template"


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
    prompt="Python package name (e.g. 'my-package')",
    help="The name of your Python package.",
)
@click.option(
    "-y",
    "--yes",
    is_flag=True,
    help="Run the script without prompting for a confirmation.",
    default=False,
)
@click.option(
    "--dry-run",
    is_flag=True,
    hidden=True,
    default=False,
)
def main(
    github_org: str, github_repo: str, package_name: str, yes: bool = False, dry_run: bool = False
):
    repo_url = f"https://github.com/{github_org}/{github_repo}"
    package_actual_name = package_name.replace("_", "-")
    package_dir_name = package_name.replace("-", "_")

    # Confirm before continuing.
    print(f"Repository URL set to: [link={repo_url}]{repo_url}[/]")
    print(f"Package name set to: [cyan]{package_actual_name}[/]")
    if not yes:
        yes = Confirm.ask("Is this correct?")
    if not yes:
        raise click.ClickException("Aborted, please run script again")

    # Personalize files.
    replacements = [
        (BASE_URL_TO_REPLACE, repo_url),
        (REPO_NAME_TO_REPLACE, github_repo),
        ("my-package", package_actual_name),
        ("my_package", package_dir_name),
    ]
    if dry_run:
        for old, new in replacements:
            print(f"Replacing '{old}' with '{new}'")
    for path in iterfiles(REPO_BASE):
        if path.resolve() not in FILES_TO_REMOVE:
            personalize_file(path, dry_run, replacements)

    # Rename 'my_package' directory to `package_dir_name`.
    if not dry_run:
        (REPO_BASE / "my_package").replace(REPO_BASE / package_dir_name)
    else:
        print(f"Renaming 'my_package' directory to '{package_dir_name}'")

    # Start with a fresh README.
    readme_contents = f"""# {package_actual_name}\n"""
    if not dry_run:
        with open(REPO_BASE / "README.md", mode="w+t", encoding="utf-8") as readme_file:
            readme_file.write(readme_contents)
    else:
        print("Replacing README.md contents with:\n", Markdown(readme_contents))

    install_example = Syntax("pip install -e '.[dev]'", "bash")
    print(
        "[green]\N{check mark} Success![/] You can now install your package locally in development mode with:\n",
        install_example,
    )

    # Lastly, remove that we don't need.
    for path in FILES_TO_REMOVE:
        assert path.is_file(), path
        if not dry_run:
            if path.name == "personalize.py" and sys.platform.startswith("win"):
                # We can't unlink/remove an open file on Windows.
                print("You can remove the 'scripts/personalize.py' file now")
            else:
                path.unlink()


def iterfiles(dir: Path) -> Generator[Path, None, None]:
    assert dir.is_dir()
    for path in dir.iterdir():
        if path in PATHS_TO_IGNORE:
            continue

        is_ignored_file = False
        for gitignore_entry in GITIGNORE_LIST:
            if path.relative_to(REPO_BASE).match(gitignore_entry):
                is_ignored_file = True
                break
        if is_ignored_file:
            continue

        if path.is_dir():
            yield from iterfiles(path)
        else:
            yield path


def personalize_file(path: Path, dry_run: bool, replacements: List[Tuple[str, str]]):
    with path.open(mode="r+t", encoding="utf-8") as file:
        filedata = file.read()

    should_update: bool = False
    for old, new in replacements:
        if filedata.count(old):
            should_update = True
            filedata = filedata.replace(old, new)

    if should_update:
        if not dry_run:
            with path.open(mode="w+t", encoding="utf-8") as file:
                file.write(filedata)
        else:
            print(f"Updating {path}")


if __name__ == "__main__":
    main()
