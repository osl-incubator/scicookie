.DEFAULT_GOAL := help

RELEASE_APP=npx --yes \
	-p semantic-release \
	-p "@semantic-release/commit-analyzer" \
	-p "@semantic-release/release-notes-generator" \
	-p "@semantic-release/changelog" \
	-p "@semantic-release/exec" \
	-p "@semantic-release/github" \
	-p "@semantic-release/git" \
	-p "@google/semantic-release-replace-plugin" \
	semantic-release

{% if cookiecutter.project_layout == "src" -%}
PACKAGE_PATH="src/{{cookiecutter.package_slug}}"
{% else %}
PACKAGE_PATH="{{cookiecutter.package_slug}}"
{% endif -%}


{%- if cookiecutter.documentation_engine == 'sphinx' %}
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = {{ cookiecutter.project_slug }}
SOURCEDIR     = docs/
BUILDDIR      = docs/_build
{%- endif +%}

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

.PHONY:help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY:clean
clean: ## remove build artifacts, compiled files, and cache
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name
	find . -name '__pycache__' -exec rm -fr '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +{} +
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

.PHONY:lint
lint:
	pre-commit run --all-files

{% if cookiecutter.use_pytest %}
.PHONY:test
test: ## run tests quickly with the default Python
	pytest
{% endif %}

{% if cookiecutter.documentation_engine == 'mkdocs' -%}
.PHONY:docs-build
docs-build:
	mkdocs build --config-file docs/mkdocs.yaml

.PHONY: docs-preview
docs-preview: docs-build
	mkdocs serve --watch docs --config-file docs/mkdocs.yaml

{%- elif cookiecutter.documentation_engine == 'sphinx' -%}
.PHONY:docs-build
docs-build:
	sphinx-apidoc -o docs/_build ${PACKAGE_PATH}
	$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: docs-preview
docs-preview: docs-build
	cd docs/_build && python -m http.server
{%- elif cookiecutter.documentation_engine == 'jupyter-book' -%}
#NOTE: This command will fail if ({{cookiecutter.git_https_origin}})<- this is not a correct URL.
.PHONY:docs-build
docs-build:
	jupyter-book build --all docs/

.PHONY: docs-preview
docs-preview: docs-build
	cd docs/_build/html/ && python -m http.server
{%- endif +%}

.PHONY:build
build:
	poetry build

.PHONY:release-ci
release-ci:
	$(RELEASE_APP) --ci

.PHONY:release-dry
release-dry:
	$(RELEASE_APP) --dry-run