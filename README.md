# python-package-template

This is a template repository for projects that are Python packages.

## Getting started

After creating a new repository from this template, you need to:

1. Change the name of the `my_package` directory to the name you want.
2. Replace all mentions of `my_package` throughout this repository with the name you want.

    A quick way to find all mentions of `my_package` is:

    ```bash
    find . -type f -not -path './.git/*' -not -path ./README.md -not -path './docs/build/*' -not -path '*__pycache__*' | xargs grep 'my_package'
    ```

    There is also a one-liner to find and replace all mentions `my_package` with `actual_name_of_package`:

    ```bash
    find . -type f -not -path './.git/*' -not -path ./README.md -not -path './docs/build/*' -not -path '*__pycache__*' | xargs grep 'my_package'
    ```

3. Add repository secrets for `PYPI_USERNAME` and `PYPI_PASSWORD`.
