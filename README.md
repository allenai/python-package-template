# python-package-template

This is a template repository for Python package projects.

## In this README :point_down:

- [Features](#features)
- [Usage](#usage)
  - [Initial setup](#initial-setup)
  - [Creating releases](#creating-releases)
- [Projects using this template](#projects-using-this-template)
- [FAQ](#faq)
- [Contributing](#contributing)

## Features

This template repository comes with all of the boilerplate needed for:

⚙️ Robust (and free) CI with [GitHub Actions](https://github.com/features/actions):
  - Unit tests ran with [PyTest](https://docs.pytest.org) against multiple Python versions and operating systems.
  - Type checking with [mypy](https://github.com/python/mypy).
  - Linting with [ruff](https://astral.sh/ruff).
  - Formatting with [isort](https://pycqa.github.io/isort/) and [black](https://black.readthedocs.io/en/stable/).

🤖 [Dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/) configuration to keep your dependencies up-to-date.

📄 Great looking API documentation built using [Sphinx](https://www.sphinx-doc.org/en/master/) (run `make docs` to preview).

🚀 Automatic GitHub and PyPI releases. Just follow the steps in [`RELEASE_PROCESS.md`](./RELEASE_PROCESS.md) to trigger a new release.

## Usage

### Initial setup

1. [Create a new repository](https://github.com/allenai/python-package-template/generate) from this template with the desired name of your project.

    *Your project name (i.e. the name of the repository) and the name of the corresponding Python package don't necessarily need to match, but you might want to check on [PyPI](https://pypi.org/) first to see if the package name you want is already taken.*

2. Create a Python 3.8 or newer virtual environment.

    *If you're not sure how to create a suitable Python environment, the easiest way is using [Miniconda](https://docs.conda.io/en/latest/miniconda.html). On a Mac, for example, you can install Miniconda using [Homebrew](https://brew.sh/):*

    ```
    brew install miniconda
    ```

    *Then you can create and activate a new Python environment by running:*

    ```
    conda create -n my-package python=3.9
    conda activate my-package
    ```

3. Now that you have a suitable Python environment, you're ready to personalize this repository. Just run:

    ```
    pip install -r setup-requirements.txt
    python scripts/personalize.py
    ```

    And then follow the prompts.

    :pencil: *NOTE: This script will overwrite the README in your repository.*

4. Commit and push your changes, then make sure all GitHub Actions jobs pass.

5. (Optional) If you plan on publishing your package to PyPI, add repository secrets for `PYPI_USERNAME` and `PYPI_PASSWORD`. To add these, go to "Settings" > "Secrets" > "Actions", and then click "New repository secret".

    *If you don't have PyPI account yet, you can [create one for free](https://pypi.org/account/register/).*

6. (Optional) If you want to deploy your API docs to [readthedocs.org](https://readthedocs.org), go to the [readthedocs dashboard](https://readthedocs.org/dashboard/import/?) and import your new project.

    Then click on the "Admin" button, navigate to "Automation Rules" in the sidebar, click "Add Rule", and then enter the following fields:

    - **Description:** Publish new versions from tags
    - **Match:** Custom Match
    - **Custom match:** v[vV]
    - **Version:** Tag
    - **Action:** Activate version

    Then hit "Save".

    *After your first release, the docs will automatically be published to [your-project-name.readthedocs.io](https://your-project-name.readthedocs.io/).*

### Creating releases

Creating new GitHub and PyPI releases is easy. The GitHub Actions workflow that comes with this repository will handle all of that for you.
All you need to do is follow the instructions in [RELEASE_PROCESS.md](./RELEASE_PROCESS.md).

## Projects using this template

Here is an incomplete list of some projects that started off with this template:

- [ai2-tango](https://github.com/allenai/tango)
- [cached-path](https://github.com/allenai/cached_path)
- [beaker-py](https://github.com/allenai/beaker-py)
- [gantry](https://github.com/allenai/beaker-gantry)
- [ip-bot](https://github.com/abe-101/ip-bot)
- [atty](https://github.com/mstuttgart/atty)

☝️ *Want your work featured here? Just open a pull request that adds the link.*

## FAQ

#### Should I use this template even if I don't want to publish my package?

Absolutely! If you don't want to publish your package, just delete the `docs/` directory and the `release` job in [`.github/workflows/main.yml`](https://github.com/allenai/python-package-template/blob/main/.github/workflows/main.yml).

## Contributing

If you find a bug :bug:, please open a [bug report](https://github.com/allenai/python-package-template/issues/new?assignees=&labels=bug&template=bug_report.md&title=).
If you have an idea for an improvement or new feature :rocket:, please open a [feature request](https://github.com/allenai/python-package-template/issues/new?assignees=&labels=Feature+request&template=feature_request.md&title=).
