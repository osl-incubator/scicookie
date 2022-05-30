#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

{% if cookiecutter.documentation_engine != 'Sphinx' %}
from pathlib import Path
import glob
DOCS_FILES_PATH = Path(PROJECT_DIRECTORY) / 'docs' / '*'
DOCS_FILES = glob.glob(str(DOCS_FILES_PATH))

def remove_docs():
    for f in DOCS_FILES: os.remove(f)
{% endif %}

{% if cookiecutter.documentation_engine != 'mkdocs' %}
from pathlib import Path
import glob
MKDOCS_FILE = Path(PROJECT_DIRECTORY) / 'mkdocs.yaml'

def remove_mkdocs_yaml():
    os.remove(MKDOCS_FILE)
{% endif %}

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def http2ssh(url):
    url = url.replace("https://", "git@")
    return url.replace("/", ":", 1)


def post_gen():
    subprocess.call(["git", "init"])

    git_https_origin = http2ssh("{{cookiecutter.git_https_origin}}")
    git_https_upstream = http2ssh("{{cookiecutter.git_https_upstream}}")
    #git_main_branch = http2ssh("{{cookiecutter.git_main_branch}}")
    git_new_branch = "add-initial-structure"

    if git_https_origin != "":
        subprocess.call(["git", "remote", "add", "origin", git_https_origin])
        subprocess.call(["git", "fetch", "--all"])

    if git_https_upstream != "":
        subprocess.call(
            ["git", "remote", "add", "upstream", git_https_upstream]
        )
        subprocess.call(["git", "fetch", "--all"])

    subprocess.call(
        ["git", "config", "user.name", "{{cookiecutter.author_full_name}}"]
    )
    subprocess.call(
        ["git", "config", "user.email", "{{cookiecutter.author_email}}"]
    )

    subprocess.call(["git", "checkout", "-b", git_new_branch])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "Initial commit"])

    {% if cookiecutter.documentation_engine != 'Sphinx' %}
    remove_docs()
    {% endif %}

    {% if cookiecutter.documentation_engine != 'mkdocs' %}
    remove_mkdocs_yaml()
    {% endif %}

if __name__ == "__main__":
    post_gen()
