# Installation

Follow the steps below to install `scicookie` locally.

## Install scicookie

`scicookie` uses modern `Python` packaging and can be installed using `pip` -

```
python -m pip install scicookie
```

## Setting Up for Local Development

To contribute to `scicookie`, follow these steps to set up your development
environment:

- **Fork the Repository**: Begin by forking the `scicookie` repository on GitHub
  to your own account.

- **Clone Your Fork Locally**: Clone the forked repository to your local machine
  and navigate into the project directory.

  ```bash
  $ git clone git@github.com:your_username/scicookie.git
  $ cd scicookie
  ```

- **Install Dependencies**: Use `mamba` to create a Conda environment and
  `poetry` for managing Python dependencies.

  ```bash
  $ mamba env create --file conda/dev.yaml --yes
  $ conda activate scicookie
  $ poetry config virtualenvs.create false
  $ poetry install
  ```

- **Create a Development Branch**: Make a dedicated branch for your bugfix or
  feature.

  ```bash
  $ git checkout -b name-of-your-bugfix-or-feature
  ```

- **Make Changes Locally**: You are now ready to implement your changes or
  improvements.

- **Install and Use Pre-commit Hooks**: `scicookie` utilizes `pre-commit` hooks
  to ensure code quality. Install them locally and they will automatically run
  on each commit.

  ```bash
  $ pre-commit install
  $ pre-commit run --all-files
  ```

  To bypass the hooks temporarily, use `git commit` with `--no-verify`.

- **Run Smoke Tests**: Quickly validate the functionality of your changes with
  smoke tests.

  ```bash
  $ makim tests.smoke
  ```

  Always complement smoke tests with thorough unit testing to ensure code
  integrity.

- **Unit Testing with `pytest`**: `scicookie` leverages `pytest` for unit
  testing, along with `pytest-cov` for coverage analysis. Run unit tests using:

  ```bash
  $ python -m pytest
  ```

  or

  ```bash
  $ makim tests.unit
  ```

- **Commit and Push Changes**: Stage, commit, and push your changes to GitHub.
  After setting the upstream branch once, subsequent pushes only require
  `git push`.

  ```bash
  $ git add .
  $ git commit -m "Detailed description of your changes."
  $ git push --set-upstream origin <branch name>
  ```

- **Submit a Pull Request**: Once your changes are pushed, go to the GitHub
  website to submit a pull request for review.

Feel free to read our
[Contributing Guide](https://osl-incubator.github.io/scicookie/contributing/)
for more information on developing `scicookie`.
