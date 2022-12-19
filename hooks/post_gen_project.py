#!/usr/bin/env python
import os
import shutil
import subprocess
from pathlib import Path

PROJECT_DIRECTORY = Path(os.path.abspath(os.path.curdir)).resolve()


def make_documentation_for(choice):
    docs_dirs = [
        'docs-mkdocs',
        'docs-sphinx-md',
        'docs-sphinx-rst',
        'docs-jupyter-book']
        
    docs_target_dir = PROJECT_DIRECTORY / "docs"

    match choice:
        case 'mkdocs':
            doc_dir = 'docs-mkdocs'

        case 'sphinx[.md]':
            doc_dir = 'docs-sphinx-md'

        case 'sphinx[.rst]':
            doc_dir = 'docs-sphinx-rst'
            
            md_files = [
                'changelog.md',
                'contributing.md',
                'index.md',
                'installation.md']

            for file in md_files:
                file = Path(docs_target_dir) / file
                file.unlink(missing_ok=True)

        case 'jupyter-book':
            doc_dir = 'docs-jupyter-book'

    doc_dir = Path(PROJECT_DIRECTORY/doc_dir).resolve()
    
    # Move the all docs files into `docs` dir
    for file in os.listdir(doc_dir):
        file = Path(doc_dir/file).resolve()
        if file.exists():
            shutil.move(file, docs_target_dir, )

    # Remove all `docs-*` directories
    for dir in docs_dirs:
        dir = Path(PROJECT_DIRECTORY/dir).resolve()
        if Path(dir).exists():
            shutil.rmtree(dir)


def http2ssh(url):
    url = url.replace("https://", "git@")
    return url.replace("/", ":", 1)


def post_gen():
    make_documentation_for("{{cookiecutter.documentation_engine}}")

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
