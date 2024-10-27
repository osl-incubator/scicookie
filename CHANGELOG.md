# Release Notes
---

# [0.11.0](https://github.com/osl-incubator/scicookie/compare/0.10.0...0.11.0) (2024-10-27)


### Bug Fixes

* Split build system config by tools, fix typos, and fix the `default` attribute in profile ([#323](https://github.com/osl-incubator/scicookie/issues/323)) ([010a0dd](https://github.com/osl-incubator/scicookie/commit/010a0dd2cb866027ac06483a954edf2f21a27438))


### Features

* Add gitlab ci to the template ([#316](https://github.com/osl-incubator/scicookie/issues/316)) ([8a058f6](https://github.com/osl-incubator/scicookie/commit/8a058f6632963decf86063fa14965b0cfdcb1de2))
* **template:** Adding azure-pipelines to template ([#317](https://github.com/osl-incubator/scicookie/issues/317)) ([d8c990a](https://github.com/osl-incubator/scicookie/commit/d8c990a61f4ba1f398f83cc3c4285931bda127fa))

# [0.10.0](https://github.com/osl-incubator/scicookie/compare/0.9.0...0.10.0) (2024-10-15)


### Bug Fixes

* Fix development dependencies issues with distlib and move from conda pkg build to python-build ([#314](https://github.com/osl-incubator/scicookie/issues/314)) ([e524f2e](https://github.com/osl-incubator/scicookie/commit/e524f2e232a413ca3fd9ebbf1ca6902b0cd5fb85))
* Remove griffe from dependencies ([#312](https://github.com/osl-incubator/scicookie/issues/312)) ([37c65c4](https://github.com/osl-incubator/scicookie/commit/37c65c46531bd541949efd9e03c11ccfbd34b5cf))
* Remove support for python >3.12,<3.9 ([#318](https://github.com/osl-incubator/scicookie/issues/318)) ([9b425f1](https://github.com/osl-incubator/scicookie/commit/9b425f1f30be8cd41f2f59b05b801a8d1f1ca3ab))
* **template:** Updating quarto-cli and quartodoc versions and pin griffe version ([#310](https://github.com/osl-incubator/scicookie/issues/310)) ([e0ccc0c](https://github.com/osl-incubator/scicookie/commit/e0ccc0cab5a5e65d625ebbe49b30272528de1045))


### Features

* Add Circle Ci to the template ([#306](https://github.com/osl-incubator/scicookie/issues/306)) ([ecf5b1c](https://github.com/osl-incubator/scicookie/commit/ecf5b1c2353bdc7c063c59bd1945e651c08c22e2))
* Add pixi as a build system option to the template ([#305](https://github.com/osl-incubator/scicookie/issues/305)) ([f07e14c](https://github.com/osl-incubator/scicookie/commit/f07e14c742dc3f632e54f633c17951b567a4baec))
* Autogeneration api documentation files for mkdocs ([#311](https://github.com/osl-incubator/scicookie/issues/311)) ([10ceb0e](https://github.com/osl-incubator/scicookie/commit/10ceb0eab83a6adc686c60e9e0bc7b58cd3d71fc))

# [0.9.0](https://github.com/osl-incubator/scicookie/compare/0.8.3...0.9.0) (2024-08-16)


### Bug Fixes

* add section build-system for poetry ([#308](https://github.com/osl-incubator/scicookie/issues/308)) ([b7777bd](https://github.com/osl-incubator/scicookie/commit/b7777bd67d4e6ebc48e93be171dd82f65852f5d9))
* Fix comment about semantic-release ([#303](https://github.com/osl-incubator/scicookie/issues/303)) ([32980bf](https://github.com/osl-incubator/scicookie/commit/32980bf05ec409484c580ce229b20457d8e256ff))
* Fix template issue for mkdocs ([#299](https://github.com/osl-incubator/scicookie/issues/299)) ([2160f4f](https://github.com/osl-incubator/scicookie/commit/2160f4f9c548ad9d36328475b9addaea114aaab6))


### Features

* Add initial mechanism for conditional question ([#291](https://github.com/osl-incubator/scicookie/issues/291)) ([3591c9e](https://github.com/osl-incubator/scicookie/commit/3591c9e66d29bf908b774664231b6891abc36cdb))
* Add support for jinja2 template in the visibility attribute ([#296](https://github.com/osl-incubator/scicookie/issues/296)) ([54c6a2e](https://github.com/osl-incubator/scicookie/commit/54c6a2e34ec77ef79d8fb3caa85b0e26f05e80e8))
* Add support for OR and AND for depends_on ([#295](https://github.com/osl-incubator/scicookie/issues/295)) ([a2ff8c7](https://github.com/osl-incubator/scicookie/commit/a2ff8c7b67e438cc9b7685ccfa686109e5b28635))
* **caching:** add cache for conda environment in template ci and update ruff linter commands ([#301](https://github.com/osl-incubator/scicookie/issues/301)) ([4018593](https://github.com/osl-incubator/scicookie/commit/4018593d34ddf81719f9b1d34d9a1f0e1619ca47))
* **doc-template:** adding options for documentation themes ([#292](https://github.com/osl-incubator/scicookie/issues/292)) ([428785d](https://github.com/osl-incubator/scicookie/commit/428785d48d95fa04d17463dd144b5508ab9c77f5))
* **ruff:** add option for ruff as linter and auto-formatter ([#298](https://github.com/osl-incubator/scicookie/issues/298)) ([549bd67](https://github.com/osl-incubator/scicookie/commit/549bd67432f385f23643940156bae370156aaac5))
* **template:** Improve support for sphinx RST and MyST ([#289](https://github.com/osl-incubator/scicookie/issues/289)) ([ac6c36b](https://github.com/osl-incubator/scicookie/commit/ac6c36bc7730cec10d09d2d28eae8a45705e8f50))

## [0.8.3](https://github.com/osl-incubator/scicookie/compare/0.8.2...0.8.3) (2024-05-13)


### Bug Fixes

* Fix support for pipx ([#286](https://github.com/osl-incubator/scicookie/issues/286)) ([0e5b125](https://github.com/osl-incubator/scicookie/commit/0e5b1251becf4cec319fb74ceb3a11dc4f704212))

## [0.8.2](https://github.com/osl-incubator/scicookie/compare/0.8.1...0.8.2) (2024-05-11)


### Bug Fixes

* Fix generation for maturin build-system ([#279](https://github.com/osl-incubator/scicookie/issues/279)) ([9aecb55](https://github.com/osl-incubator/scicookie/commit/9aecb554f260b65f5df3b472d23bc67e820f1fbc))
* Fix the project generation for mesonpy build-system ([#278](https://github.com/osl-incubator/scicookie/issues/278)) ([2a1102c](https://github.com/osl-incubator/scicookie/commit/2a1102c1c4f0574e5cc8a041d6d634ae0e124c79))
* Fix usage of scicookie for pipx ([#285](https://github.com/osl-incubator/scicookie/issues/285)) ([41b80b8](https://github.com/osl-incubator/scicookie/commit/41b80b88d9b93a26298ae51f610ab21c44d6066d))
* Improve pyproject.toml output and keep workflow more consistent ([#277](https://github.com/osl-incubator/scicookie/issues/277)) ([b2cc87d](https://github.com/osl-incubator/scicookie/commit/b2cc87d57f6c9de162ab3d53a413e9f0291e49c2))
* Move back to cookiecutter ([#284](https://github.com/osl-incubator/scicookie/issues/284)) ([f7cc72a](https://github.com/osl-incubator/scicookie/commit/f7cc72a3942b0539dcafe2ce08463658c45756db))

## [0.8.1](https://github.com/osl-incubator/scicookie/compare/0.8.0...0.8.1) (2024-05-03)


### Bug Fixes

* Add nodejs-wheel as a dependency ([#276](https://github.com/osl-incubator/scicookie/issues/276)) ([a470d28](https://github.com/osl-incubator/scicookie/commit/a470d283795311b3489b98e1f3f34ab5a45b7da1))

# [0.8.0](https://github.com/osl-incubator/scicookie/compare/0.7.2...0.8.0) (2024-05-03)


### Bug Fixes

* **file:** remove mypy filter #type:ignore ([#250](https://github.com/osl-incubator/scicookie/issues/250)) ([55de1e2](https://github.com/osl-incubator/scicookie/commit/55de1e2b482db2346b24bd27fe06f8db65cc2cc5))
* Fix issues with dependencies and default tools ([#274](https://github.com/osl-incubator/scicookie/issues/274)) ([ed65b11](https://github.com/osl-incubator/scicookie/commit/ed65b11937325e36b3fa6bcecc9512550e7e673c))
* Fix the default slug used for the package name ([#245](https://github.com/osl-incubator/scicookie/issues/245)) ([9c53ee3](https://github.com/osl-incubator/scicookie/commit/9c53ee378d93e47becb033c10c98c4b8ff238c9c))


### Features

* **template:** Add quarto documentation engine ([#257](https://github.com/osl-incubator/scicookie/issues/257)) ([9aed15b](https://github.com/osl-incubator/scicookie/commit/9aed15b5cb3eba56e51b8af1934b7a9814ef4ea5))

## [0.7.2](https://github.com/osl-incubator/scicookie/compare/0.7.1...0.7.2) (2024-03-25)


#### Bug Fixes

* **cli:** Add an initial code for the CLI option defined by the user ([#225](https://github.com/osl-incubator/scicookie/issues/225)) ([1b1db90](https://github.com/osl-incubator/scicookie/commit/1b1db90358d11c97d02fa7462bfcb1ef6b6b786c))
* Fix the HELP url ([#241](https://github.com/osl-incubator/scicookie/issues/241)) ([42cf544](https://github.com/osl-incubator/scicookie/commit/42cf5441da3122afb7b1b61683ccf52dac3f20aa))
* **pkg:** Add project metadata long description (readme) ([#248](https://github.com/osl-incubator/scicookie/issues/248)) ([6be8e03](https://github.com/osl-incubator/scicookie/commit/6be8e03e5511da23dd07dce78f94195e963c2bda))
* Update makim config file for compatibility  with v1.14 ([#243](https://github.com/osl-incubator/scicookie/issues/243)) ([d9e8ce8](https://github.com/osl-incubator/scicookie/commit/d9e8ce8b68f22150592b791c5745435b58921942))

## [0.7.1](https://github.com/osl-incubator/scicookie/compare/0.7.0...0.7.1) (2024-03-12)


#### Bug Fixes

* Fix SciCookie documentation ([#236](https://github.com/osl-incubator/scicookie/issues/236)) ([fdff49e](https://github.com/osl-incubator/scicookie/commit/fdff49eb81f44c6e56ab7122230450e9714c0ae1))

## [0.7.0](https://github.com/osl-incubator/scicookie/compare/0.6.3...0.7.0) (2024-03-12)


#### Bug Fixes

* **actions:** update setup-miniconda to v3 ([#202](https://github.com/osl-incubator/scicookie/issues/202)) ([6786a92](https://github.com/osl-incubator/scicookie/commit/6786a9202b302f20646328b05c2b810a4538e8d9))
* Fix conda activate inside the smoke test ([#226](https://github.com/osl-incubator/scicookie/issues/226)) ([2831f1e](https://github.com/osl-incubator/scicookie/commit/2831f1e3f7370db5a91664038e0605df970a8930))


#### Features

* Add prettier configuration to the root project and template ([#231](https://github.com/osl-incubator/scicookie/issues/231)) ([e57579c](https://github.com/osl-incubator/scicookie/commit/e57579cf95e05c9b8ad801a5b15effd33ae70c03))
* **upgrade:** add numfocus coc option ([#219](https://github.com/osl-incubator/scicookie/issues/219)) ([177df05](https://github.com/osl-incubator/scicookie/commit/177df056fc7a84619ea905a17030b3e2f937caf6))
* **upgrade:** adding python coc option ([#222](https://github.com/osl-incubator/scicookie/issues/222)) ([6334b2b](https://github.com/osl-incubator/scicookie/commit/6334b2bbed806d2379b270c9e50894485ccdf188))

## [0.6.3](https://github.com/osl-incubator/scicookie/compare/0.6.2...0.6.3) (2023-12-08)


#### Bug Fixes

* Add a dynamic version attribute for the `setuptools` build-backend ([#188](https://github.com/osl-incubator/scicookie/issues/188)) ([21fa953](https://github.com/osl-incubator/scicookie/commit/21fa953ca790b4464ac10794e899d1a58bf3a547))
* Fix profile's mechanism and update OSL profile ([#189](https://github.com/osl-incubator/scicookie/issues/189)) ([4eaf7b4](https://github.com/osl-incubator/scicookie/commit/4eaf7b4c1cadcdb6293b71b791ad66551afe6dcb))


#### Performance Improvements

* **template:** Improving the git workflow for the template ([#162](https://github.com/osl-incubator/scicookie/issues/162)) ([7ab065e](https://github.com/osl-incubator/scicookie/commit/7ab065e2c18f237a6525b4a26e160f2222cad422))

## [0.6.2](https://github.com/osl-incubator/scicookie/compare/0.6.1...0.6.2) (2023-08-31)


#### Bug Fixes

* Fix issues with docs, makim/make, release, and CI ([#182](https://github.com/osl-incubator/scicookie/issues/182)) ([12efe9a](https://github.com/osl-incubator/scicookie/commit/12efe9a1b2990051efb18131b1aee39ed5e8155f))

## [0.6.1](https://github.com/osl-incubator/scicookie/compare/0.6.0...0.6.1) (2023-08-21)


#### Bug Fixes

* Update LICENSE ([#170](https://github.com/osl-incubator/scicookie/issues/170)) ([be88300](https://github.com/osl-incubator/scicookie/commit/be88300bed9de584598a0360c274c0334d4414cf))

## [0.6.0](https://github.com/osl-incubator/scicookie/compare/0.5.0...0.6.0) (2023-08-11)


#### Features

* Add help information to the TUI ([#167](https://github.com/osl-incubator/scicookie/issues/167)) ([8c05a6d](https://github.com/osl-incubator/scicookie/commit/8c05a6d161111e4c8d752dbe78df1450926659fb))
* **template:** Added pybind11 as an option for build system  ([#163](https://github.com/osl-incubator/scicookie/issues/163)) ([b3d59cd](https://github.com/osl-incubator/scicookie/commit/b3d59cddc1d0f6381f442f5cec5af25d23e05d01))

## [0.5.0](https://github.com/osl-incubator/scicookie/compare/0.4.0...0.5.0) (2023-08-09)


#### Bug Fixes

* Fix error in `__author__` introduced by [#156](https://github.com/osl-incubator/scicookie/issues/156) ([67a40af](https://github.com/osl-incubator/scicookie/commit/67a40afba6d0041b226e1c37ff46f252a36f843d))
* Make `black` "yes" and `blue` "no" by default ([#164](https://github.com/osl-incubator/scicookie/issues/164)) ([88048e4](https://github.com/osl-incubator/scicookie/commit/88048e43165c5918f4f5e70e9a5b374f9d5d5cf2))


#### Features

* dynamic versioning for hatch ([#156](https://github.com/osl-incubator/scicookie/issues/156)) ([bea6ad2](https://github.com/osl-incubator/scicookie/commit/bea6ad2742decb4c05ee52478ea37386b870588b))
* **template:** Added maturin as an option for build-system ([#152](https://github.com/osl-incubator/scicookie/issues/152)) ([4a6bfbd](https://github.com/osl-incubator/scicookie/commit/4a6bfbd9cf50a9f2b4a0d5008f79bde524fcf862))
* **template:** Added scikit as an option for build system ([#161](https://github.com/osl-incubator/scicookie/issues/161)) ([3dc8562](https://github.com/osl-incubator/scicookie/commit/3dc85623bab0c7fb677750ac296104beee8fb322))

## [0.4.0](https://github.com/osl-incubator/scicookie/compare/0.3.0...0.4.0) (2023-07-24)


#### Bug Fixes

* **template:** Solve missing information ([#151](https://github.com/osl-incubator/scicookie/issues/151)) ([8811b22](https://github.com/osl-incubator/scicookie/commit/8811b22427fd8f719b478cd1ba1d67cab66e1fa7))


#### Features

* **template:** Added hatchling as an option for build-system ([#144](https://github.com/osl-incubator/scicookie/issues/144)) ([32704a5](https://github.com/osl-incubator/scicookie/commit/32704a5fba35869f5a67c6b7db76f933e9abd211))


#### Performance Improvements

* **documentation:** Adding structure and content to guide.md ([#150](https://github.com/osl-incubator/scicookie/issues/150)) ([fe9ce87](https://github.com/osl-incubator/scicookie/commit/fe9ce872f311c04d0791dfb64dce9961e645c7c0))
* **project information:** adding missing information ([#149](https://github.com/osl-incubator/scicookie/issues/149)) ([76ee498](https://github.com/osl-incubator/scicookie/commit/76ee4983539e5b807525c3834c6a736bce9eb193))
* **project information:** Adding the maintainer section to readme ([#145](https://github.com/osl-incubator/scicookie/issues/145)) ([321417b](https://github.com/osl-incubator/scicookie/commit/321417b3ad2a08f0a452fa12821fd5c2543d2e4b))

## [0.3.0](https://github.com/osl-incubator/scicookie/compare/0.2.0...0.3.0) (2023-07-05)


#### Bug Fixes

* Fix package's name ([#137](https://github.com/osl-incubator/scicookie/issues/137)) ([4066549](https://github.com/osl-incubator/scicookie/commit/406654935b34e1b9f9a36d66f4020343594f65af))


#### Features

* **hypothesis:** Added hypothesis as an option  ([#134](https://github.com/osl-incubator/scicookie/issues/134)) ([791ca16](https://github.com/osl-incubator/scicookie/commit/791ca163838e42437790aac20d625c41df3b497b))
* **template:** Adding flit as a build-system option ([#136](https://github.com/osl-incubator/scicookie/issues/136)) ([44ecccf](https://github.com/osl-incubator/scicookie/commit/44ecccf03f4c7f04f37044b4fd1a4bb3d6e0e75c))
* **template:** adding meson-python as a build-system option ([#139](https://github.com/osl-incubator/scicookie/issues/139)) ([c05dc79](https://github.com/osl-incubator/scicookie/commit/c05dc79643272b22040769bbadbcebd0813244e2))
* **template:** Adding setuptools as a build-system option ([#140](https://github.com/osl-incubator/scicookie/issues/140)) ([4cd11c0](https://github.com/osl-incubator/scicookie/commit/4cd11c0ec7189ef2756f728a40c3c780c5bc9535)), closes [#53](https://github.com/osl-incubator/scicookie/issues/53)

## [0.2.0](https://github.com/osl-incubator/scicookie/compare/0.1.1...0.2.0) (2023-06-17)


#### Bug Fixes

* **linter:** Fix the linter configuration ([#131](https://github.com/osl-incubator/scicookie/issues/131)) ([e9843e2](https://github.com/osl-incubator/scicookie/commit/e9843e2f7016fa2fa9b13ee591b7963b478092b9))


#### Features

* **template:** Add API documentation to the template 2/4 (Sphinx) ([#124](https://github.com/osl-incubator/scicookie/issues/124)) ([e3b2baf](https://github.com/osl-incubator/scicookie/commit/e3b2baf67bbe5db98c9159ae11b672224c609e88))


#### Performance Improvements

* **template:** Update deps used by the template ([#126](https://github.com/osl-incubator/scicookie/issues/126)) ([b0d440f](https://github.com/osl-incubator/scicookie/commit/b0d440f2084e3ab9e5bdf43055675fd86340357e))

## [0.1.1](https://github.com/osl-incubator/scicookie/compare/0.1.0...0.1.1) (2023-06-11)


#### Bug Fixes

* Fix the ninjacookie call ([#116](https://github.com/osl-incubator/scicookie/issues/116)) ([8bd413c](https://github.com/osl-incubator/scicookie/commit/8bd413cc4350b931c4b3d598ed10f48bd86e0b1c))
