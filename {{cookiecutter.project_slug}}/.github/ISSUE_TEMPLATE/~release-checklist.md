---
name: ✅  Release Checklist (Maintainers Only)
about: Checklist for core developers to complete as part of making a release

---
# Release Checklist

## Before Release

* [ ] Migrate any unresolved Issues or PRs from the [release GitHub project board](https://github.com/osl-incubator/cookiecutter-python/{{ cookiecutter.project_name }}) to a new project board.
* [ ] Verify that there is a release notes file for the release under [``docs/release-notes``](https://github.com/osl-incubator/cookiecutter-python/{{ cookiecutter.project_name }}#readme).
* [ ] Verify that the release notes files correctly summarize all development changes since the last release.
* [ ] Draft email to [``Cookiecutter-announcements`` mailing list] that summarizes the main points of the release notes and circulate it for development team approval.
* [ ] Update the checklist Issue template in the [``.github/ISSUE_TEMPLATE``](https://github.com/osl-incubator/cookiecutter-python/{{ cookiecutter.project_name }}/.github/ISSUE_TEMPLATE) directory if there are revisions.
* [ ] Make a release to [TestPyPI][TestPyPI_Cookiecutter] using the [workflow dispatch event trigger](https://github.com/osl-incubator/cookiecutter-python/{{ cookiecutter.project_name }}).
* [ ] Verify that the project README is displaying correctly on [TestPyPI][TestPyPI_Cookiecutter].
* [ ] Add any new use citations or published statistical models to the [Use and Citations page][citations_page].
* [ ] Verify that the citations on the [Use and Citations page][citations_page] are up to date with their current [INSPIRE](https://inspirehep.net/) record.
* [ ] Update the [pypa/gh-action-pypi-publish](https://github.com/osl-incubator/cookiecutter-python/{{ cookiecutter.project_name }}) GitHub Action used for deployment to TestPyPI and PyPI to the latest stable release.
* [ ] Update the ``codemeta.json`` file in the release PR if its requirements have updated.

[TestPyPI_Cookiecutter]: https://test.pypi.org/project/Cookiecutter/
[citations_page]: https://github.com/osl-incubator/cookiecutter-python

## Once Release PR is Merged

* [ ] Watch the CI to ensure that the deployment to [PyPI](https://github.com/osl-incubator/cookiecutter-python) is successful.
* [ ] Create a [GitHub release](https://github.com/osl-incubator/cookiecutter-python/{{ cookiecutter.project_name }}/releases) from the generated PR tag and copy the release notes published to the GitHub release page. The creation of the GitHub release triggers all other release related activities.
   - [ ] Before pasting in the release notes copy the changes that the GitHub bot has already queued up and pasted into the tag and place them in the "Changes" section of the release notes. If the release notes are published before these are copied then they will be overwritten and you'll have to add them back in by hand.
* [ ] Verify there is a new [Zenodo DOI](https://doi.org/10.5281/zenodo.1169739) minted for the release.
   - [ ] Verify that the new release archive metadata on Zenodo matches is being picked up as expected from [`CITATION.cff`](https://github.com/osl-incubator/cookiecutter-python/{{ cookiecutter.project_name }}/blob/main/CITATION.cff).
* [ ] Verify that a Binder has properly built for the new release.
* [ ] Watch for a GitHub notification that there is an automatic PR to the [Conda-forge feedstock](https://github.com/osl-incubator/cookiecutter-python/{{ cookiecutter.project_name }}). This may take multiple hours to happen. If there are any changes needed to the Conda-forge release make them **from a personal account** and not from an organization account to have workflows properly trigger.
   - [ ] Check if any requirements need to be updated by commenting "@conda-grayskull show requirements" on the PR.
   - [ ] Verify the requirements in the [Conda-forge feedstock](https://github.com/osl-incubator/cookiecutter-python/{{ cookiecutter.project_name }}) recipe `meta.yaml` match those in `pyproject.toml`.

## After Release

* [ ] Verify that the release is installable from both [PyPI](https://github.com/osl-incubator/cookiecutter-python) and [Conda-forge](https://github.com/conda-forge/Cookiecutter-feedstock/{{ cookiecutter.project_name }}).
* [ ] Send the drafted ``Cookiecutter-announcements`` email out from the ``Cookiecutter-announcements`` account email.
* [ ] Tweet the release out on both personal and team Twitter accounts.
* [ ] Announce the release on the [Scikit-HEP community Gitter](https://gitter.im/Cookiecutter/community).
* [ ] Make a release for the [`Cookiecutter` tutorial](https://github.com/osl-incubator/cookiecutter-python) corresponding to the **previous release** number. This release represents the last version of the tutorial that is guaranteed to work with previous release API.
* [ ] Update the [tutorial](https://github.com/osl-incubator/cookiecutter-python) to use the new release number and API.
* [ ] Make a PR to use the new release in the [CUDA enabled Docker images](https://github.com/osl-incubator/cookiecutter-python).
* [ ] Open a ticket on the CERN [Software Process and Infrastructure JIRA](https://sft.its.cern.ch/jira/browse/SPI) to update the version of `Cookiecutter` available in the next LCG release.
   - c.f. the [`v0.6.3` request ticket](https://sft.its.cern.ch/jira/browse/SPI-2086) as an example.
* [ ] If the release is a **major** or **minor** release, open a [GitHub Release Radar](https://github.com/github/release-radar) Issue for the release to potentially get featured on GitHub's [Release Radar blog](https://github.blog/?s=release+radar).
* [ ] Close the [release GitHub Project board](https://github.com/osl-incubator/cookiecutter-python).
