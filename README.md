# python-package-template

This is a template repository for Python package projects.

## Features

This template repo comes with all of the boiler plate for:

- Robust CI with GitHub Actions.
- Dependabot configuration.
- Great looking API documentation built using [Sphinx](https://www.sphinx-doc.org/en/master/) (run `make docs` to preview).
- Automatic GitHub and PyPI releases. Just follow the steps in [`RELEASE_PROCESS.md`](./RELEASE_PROCESS.md) to trigger a new release.

## Setup

1. [Create a new repository](https://github.com/allenai/python-package-template/generate) from this template with the desired name of your project.

    Your project name (i.e. the name of the repository) and the name of the corresponding Python package don't necessarily need to match, but you might want to check on [PyPI](https://pypi.org/) first to see if the package name you want is already taken.

2. Create a Python 3.7 or newer virtual environment.

    If you're not sure how to create a suitable Python environment, the easiest way is using [Miniconda](https://docs.conda.io/en/latest/miniconda.html). On a Mac, for example, you can install Miniconda using [Homebrew](https://brew.sh/):

    ```
    brew install miniconda
    ```

    Then you can create and activate a new Python environment by running:

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

4. Commit and push your changes, then make sure all GitHub Actions jobs pass.

5. (Optional) If you plan on publishing your package to PyPI, add repository secrets for `PYPI_USERNAME` and `PYPI_PASSWORD`. To add these, go to "Settings" > "Secrets" > "Actions", and then click "New repository secret".

    If you don't have PyPI account yet, you can create one for free. Or, if you'd like to publish your package under the AllenNLP PyPI account, just ask someone on the AllenNLP team for the credentials.

6. (Optional) If you want to deploy your API docs to [readthedocs.org](https://readthedocs.org), go to the [readthedocs dashboard](https://readthedocs.org/dashboard/import/?) and import your new project.

    Then click on the "Admin" button, navigate to "Automation Rules" in the sidebar, click "Add Rule", and then enter the following fields:

    - **Description:** Publish new versions from tags
    - **Match:** Custom Match
    - **Custom match:** v[vV]
    - **Version:** Tag
    - **Action:** Activate version

    Then hit "Save".

    After your first release, the docs will automatically be published to [your-project-name.readthedocs.io](https://your-project-name.readthedocs.io/).

## Creating a new release

Creating new GitHub and PyPI releases is easy. The GitHub Actions workflow that comes with this repository will handle all of that for you.
All you need to do is follow the instructions in [RELEASE_PROCESS.md](./RELEASE_PROCESS.md).
