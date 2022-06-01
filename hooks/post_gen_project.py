#!/usr/bin/env python
import os
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

{% if cookiecutter.documentation_engine == 'mkdocs' -%}
UNUSED_DOCS_DIRS = [
    f'{PROJECT_DIRECTORY}/docs-sphinx', 
    f'{PROJECT_DIRECTORY}/docs-jupyter-book'
]
{%- elif cookiecutter.documentation_engine == 'sphinx' -%}
UNUSED_DOCS_DIRS = [
    f'{PROJECT_DIRECTORY}/docs-mkdocs', 
    f'{PROJECT_DIRECTORY}/docs-jupyter-book'
]
{%- elif cookiecutter.documentation_engine == 'jupyter-book' -%}
UNUSED_DOCS_DIRS = [
    f'{PROJECT_DIRECTORY}/docs-sphinx', 
    f'{PROJECT_DIRECTORY}/docs-mkdocs'
]
{% endif %}

def remove_unused_docs_dirs():
    for dirs in UNUSED_DOCS_DIRS:
        shutil.rmtree(dirs)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def http2ssh(url):
    url = url.replace("https://", "git@")
    return url.replace("/", ":", 1)


def post_gen():
    remove_unused_docs_dirs()

    subprocess.call(["git", "init"])

    git_https_origin = http2ssh("{{cookiecutter.git_https_origin}}")
    git_https_upstream = http2ssh("{{cookiecutter.git_https_upstream}}")
    git_main_branch = http2ssh("{{cookiecutter.git_main_branch}}")
    git_new_branch = "add-initial-structure"

    if git_https_origin != "":
        subprocess.call(["git", "remote", "add", "origin", git_https_origin])
        subprocess.call(["git", "fetch", "--all"])

    if git_https_upstream != "":
        subprocess.call(
            ["git", "remote", "add", "upstream", git_https_upstream]
        )
        subprocess.call(["git", "checkout", f"upstream/{git_main_branch}"])
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



if __name__ == "__main__":
    post_gen()
