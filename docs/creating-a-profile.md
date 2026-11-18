# Creating a SciCookie Profile

SciCookie profiles let you customize the settings used when generating a
project. For example, the `osl` profile contains settings recommended by Open
Science Labs.

## 1. Understand Existing Profiles

SciCookie stores its built-in profiles in `src/scicookie/profiles/`.

- `base.yaml` defines the default configuration.
- `osl.yaml` overrides selected settings for the Open Science Labs profile.

Review these files before creating a new profile so you can understand the
available settings and their structure.

## 2. Create a Profile

Create a YAML file in `src/scicookie/profiles/` with a descriptive name, such as
`community.yaml`.

A profile can override selected properties from `base.yaml`. For example, a
profile can change default values or control which questions are visible. Use
`osl.yaml` as a reference for the expected structure.

Only include settings you need to customize, and make sure the property names
match those in `base.yaml`.

## 3. Use Your Profile

Once the profile file is available in SciCookie's profiles directory, select it
by its filename without the `.yaml` extension:

```bash
scicookie --profile community
```

To use the default profile instead, run:

```bash
scicookie
```

## 4. Test Your Profile

Review the existing CLI profile tests in `tests/test_cli.py` and the sample
profiles in `tests/profiles/`. These show how SciCookie tests profile behavior.

The CLI profile tests are currently marked as Linux-only, so they are skipped on
Windows. Run them in a supported Linux environment when validating CLI behavior.

Before contributing a profile, check that its YAML is valid, that its property
names match those in `src/scicookie/profiles/base.yaml`, and that the profile
can be loaded by SciCookie.

## 5. Build the Documentation

To check the documentation locally, run:

```bash
poetry run mkdocs build
```

## 6. Contribute Your Profile

If your profile could be useful to other SciCookie users, consider contributing
it:

1. Fork the SciCookie repository and create a branch for your changes.
2. Add your profile and any relevant tests or documentation.
3. Run the appropriate checks.
4. Commit and push your branch to your fork.
5. Open a pull request explaining the profile and the settings it changes.

See the [Contributing Guide](contributing.md) for details about the development
workflow and pull requests.
