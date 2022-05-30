.DEFAULT_GOAL := help

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
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

.PHONY:lint
lint:
	pre-commit run --all-files

.PHONY:test
test: ## run tests quickly with the default Python
	pytest

.PHONY:docs
docs:
	$(MAKE_DOCS)

.PHONY:build
build:
	poetry build

# Documentation Engine: {{ cookiecutter.documentation_engine }}

{%- if cookiecutter.documentation_engine == 'mkdocs' %}
define MAKE_DOCS
mkdocs build
endef
{% endif -%}

{%- if cookiecutter.documentation_engine == 'Sphinx' %}
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = {{ cookiecutter.project_slug }}
SOURCEDIR     = docs/
BUILDDIR      = docs/_build

define MAKE_DOCS
sphinx-apidoc -o docs/_build {{ cookiecutter.package_slug }}
$(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
endef
{% endif -%}
