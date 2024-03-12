#!/usr/bin/env python
import datetime
import os
import shutil
import subprocess

from pathlib import Path

PROJECT_DIRECTORY = Path(os.path.abspath(os.path.curdir)).resolve()

UNUSED_DOCS_DIRS = [
    PROJECT_DIRECTORY / 'docs-mkdocs',
    PROJECT_DIRECTORY / 'docs-sphinx',
    PROJECT_DIRECTORY / 'docs-jupyter-book'
]

DOCUMENTATION_ENGINE = "{{ cookiecutter.documentation_engine }}"
DOCS_SPEC_DIR = UNUSED_DOCS_DIRS.pop(
    UNUSED_DOCS_DIRS.index(
        PROJECT_DIRECTORY / f'docs-{DOCUMENTATION_ENGINE}'
    )
)

USE_SRC_LAYOUT = {{ cookiecutter.project_layout == "src" }}
if USE_SRC_LAYOUT:
    PACKAGE_PATH = PROJECT_DIRECTORY / "src" / "{{ cookiecutter.package_slug}}"
else:
    PACKAGE_PATH = PROJECT_DIRECTORY / "{{ cookiecutter.package_slug}}"

USE_BLACK = {{ cookiecutter.use_black == "yes" }}
USE_BANDIT = {{ cookiecutter.use_bandit == "yes" }}
USE_CONTAINERS = {{ cookiecutter.use_containers in ['Docker', 'Podman'] }}
USE_CLI = {{ cookiecutter.command_line_interface != "None" }}
USE_CONDA = {{ cookiecutter.use_conda == "yes" }}
USE_MAKE = {{ cookiecutter.use_make == "yes" }}
USE_MAKIM = {{ cookiecutter.use_makim == "yes" }}
USE_MYPY = {{ cookiecutter.use_mypy == "yes" }}
USE_PRETTIER = {{ cookiecutter.use_prettier == "yes" }}
{% if cookiecutter.code_of_conduct == "contributor-covenant" -%}
COC_PATH = PROJECT_DIRECTORY / 'coc' / 'CONTRIBUTOR_COVENANT.md'
{%- elif cookiecutter.code_of_conduct == "citizen-code-of-conduct" -%}
COC_PATH = PROJECT_DIRECTORY / 'coc' / 'CITIZEN.md'
{%- elif cookiecutter.code_of_conduct == "numfocus-adapted-coc" -%}
COC_PATH = PROJECT_DIRECTORY / 'coc' / 'NUMFOCUS_adapted_coc.md'
{%- elif cookiecutter.code_of_conduct == "python-adapted-coc" -%}
COC_PATH = PROJECT_DIRECTORY / 'coc' / 'PYTHON_ADAPTED_COC.md'
{% else %}
COC_PATH = None
{%- endif %}
{% if cookiecutter.governance_document == "numpy-governance" -%}
GOVERNANCE_PATH = PROJECT_DIRECTORY / 'governance' / 'numpy_governance.md'
{% elif cookiecutter.code_of_conduct == "sciml-governance" -%}
GOVERNANCE_PATH = PROJECT_DIRECTORY / 'governance' / 'sciml_governance.md'
{% else -%}
GOVERNANCE_PATH = None
{%- endif %}
{% if cookiecutter.roadmap_document == "pytorch-ignite-roadmap" -%}
ROADMAP_PATH = PROJECT_DIRECTORY / 'roadmap' / 'ignite_roadmap.md'
{%- else %}
ROADMAP_PATH = None
{%- endif %}
{% if cookiecutter.build_system == "poetry" -%}
BUILD_SYSTEM = "poetry"
{% elif cookiecutter.build_system == "flit" -%}
BUILD_SYSTEM = "flit"
{% elif cookiecutter.build_system == "mesonpy" -%}
BUILD_SYSTEM = "mesonpy"
{% elif cookiecutter.build_system == "setuptools" -%}
BUILD_SYSTEM = "setuptools"
{% elif cookiecutter.build_system == "pdm" -%}
BUILD_SYSTEM = "pdm"
{% elif cookiecutter.build_system == "hatch" -%}
BUILD_SYSTEM = "hatch"
{% elif cookiecutter.build_system == "maturin" -%}
BUILD_SYSTEM = "maturin"
{% elif cookiecutter.build_system == "scikit-build-core" -%}
BUILD_SYSTEM = "scikit-build-core"
{% elif cookiecutter.build_system == "pybind11" -%}
BUILD_SYSTEM = "pybind11"
{%- else %}
BUILD_SYSTEM = None
{%- endif %}


def remove_dirs(dirs: list):
    for dirs in dirs:
        shutil.rmtree(dirs)


def remove_dir(dir_path):
    """Remove a directory located at PROJECT_DIRECTORY/dir_path"""
    shutil.rmtree(PROJECT_DIRECTORY/dir_path)


def remove_project_file(filepath: str):
    os.remove(PROJECT_DIRECTORY / filepath)


def remove_package_file(filepath: str):
    os.remove(PACKAGE_PATH / filepath)


def move_selected_doc_dir():
    if DOCUMENTATION_ENGINE == "mkdocs":
        docs_target_dir = PROJECT_DIRECTORY
        remove_project_file(Path("docs/api") / "references.rst")
    else:
        docs_target_dir = PROJECT_DIRECTORY / "docs"
    for file_name in os.listdir(DOCS_SPEC_DIR):
        shutil.move(DOCS_SPEC_DIR / file_name, docs_target_dir)

    if DOCUMENTATION_ENGINE == "sphinx":
        remove_project_file(Path("docs") / "index.md")
        remove_project_file(Path("docs/api") / "references.md")

    shutil.rmtree(DOCS_SPEC_DIR)


def clean_up_automation():
    if not USE_MAKE:
        remove_project_file("Makefile")

    if not USE_MAKIM:
        remove_project_file(".makim.yaml")

def clean_up_docs():
    remove_dirs(UNUSED_DOCS_DIRS)
    move_selected_doc_dir()


def clean_up_project_layout():
    if USE_SRC_LAYOUT:
        if not os.path.exists("src"):
            os.mkdir("src")
            shutil.move('{{cookiecutter.package_slug}}', 'src')


def clean_up_code_of_conduct():
    if COC_PATH:
        shutil.move(
            COC_PATH,
            PROJECT_DIRECTORY / 'CODE_OF_CONDUCT.md'
        )
    remove_dir("coc")


def clean_up_conda():
    if not USE_CONDA:
        shutil.move(PROJECT_DIRECTORY / "virtualenvs" / "pyenv" / "requirements.txt", PROJECT_DIRECTORY)
        remove_dir("virtualenvs")
    else:
        shutil.move(PROJECT_DIRECTORY / "virtualenvs" / "conda", PROJECT_DIRECTORY)
        remove_dir("virtualenvs")


def clean_up_governance():
    if GOVERNANCE_PATH:
        shutil.move(
            GOVERNANCE_PATH,
            PROJECT_DIRECTORY / 'governance.md'
        )
    remove_dir("governance")


def clean_up_roadmap():
    if ROADMAP_PATH:
        shutil.move(
            ROADMAP_PATH,
            PROJECT_DIRECTORY / 'roadmap.md'
        )
    remove_dir("roadmap")


def clean_up_containers():
    if not USE_CONTAINERS:
        remove_dir("containers")


def clean_up_cli():
    if not USE_CLI:
        remove_package_file("__main__.py")

def clean_up_prettier():
    if not USE_PRETTIER:
        remove_project_file(".prettierrc.yaml")
        remove_project_file(".prettierignore")

def clean_up_build_system():
    build_system_dir = PROJECT_DIRECTORY / "build-system"

    if BUILD_SYSTEM == "poetry":
        shutil.move(
            build_system_dir / "poetry-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
    elif BUILD_SYSTEM == "flit":
        shutil.move(
            build_system_dir / "flit-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
    elif BUILD_SYSTEM == "mesonpy":
        shutil.move(
            build_system_dir / "mesonpy-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
        shutil.move(
            build_system_dir / "meson.build",
            PROJECT_DIRECTORY / 'meson.build'
        )
    elif BUILD_SYSTEM == "setuptools":
        shutil.move(
            build_system_dir / "setuptools-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
    elif BUILD_SYSTEM == "pdm":
        shutil.move(
            build_system_dir / "pdm-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
    elif BUILD_SYSTEM == "hatch":
        shutil.move(
            build_system_dir / "hatch-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
    elif BUILD_SYSTEM == "maturin":
        shutil.move(
            build_system_dir / "maturin-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
        shutil.move(
            build_system_dir / "Cargo.toml",
            PROJECT_DIRECTORY / 'Cargo.toml'
        )
    elif BUILD_SYSTEM == "scikit-build-core":
        shutil.move(
            build_system_dir / "scikit-build-core-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
        shutil.move(
            build_system_dir / "CMakeLists.txt",
            PROJECT_DIRECTORY / 'CMakeLists.txt'
        )
        shutil.move(
            build_system_dir / "skcdemo.cpp",
            PROJECT_DIRECTORY / 'skcdemo.cpp'
        )
    elif BUILD_SYSTEM == "pybind11":
        shutil.move(
            build_system_dir / "pybind11-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
        shutil.move(
            build_system_dir / "CMakeLists.txt",
            PROJECT_DIRECTORY / 'CMakeLists.txt'
        )
        shutil.move(
            build_system_dir / "setup.py",
            PROJECT_DIRECTORY / 'setup.py'
        )
    else:
        shutil.move(
            build_system_dir / "base-pyproject.toml",
            PROJECT_DIRECTORY / 'pyproject.toml'
        )
    remove_dir("build-system")


def http2ssh(url):
    url = url.replace("https://", "git@")
    return url.replace("/", ":", 1)


def prepare_git() -> None:
    git_https_origin = http2ssh("{{cookiecutter.git_https_origin}}")
    git_https_upstream = http2ssh("{{cookiecutter.git_https_upstream}}")
    git_main_branch = http2ssh("{{cookiecutter.git_main_branch}}")
    unique_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    git_new_branch = f"initial-from-scicookie-{unique_id}"
    git_stash_branch = f"stash-from-scicookie-{unique_id}"

    git_author_name = "{{cookiecutter.author_full_name}}"
    git_author_email = "{{cookiecutter.author_email}}"

    use_remote = git_https_origin != '' or git_https_upstream != ''

    if not use_remote:
        subprocess.call(["git", "init", "-b", git_main_branch])
        subprocess.call(
            ["git", "config", "user.name", git_author_name]
        )
        subprocess.call(
            ["git", "config", "user.email", git_author_email]
        )
        subprocess.call(["git", "add", "."])
        subprocess.call([
            "git", "commit", "-m", "Initial commit from SciCookie", "--no-verify"
        ])
        return

    subprocess.call(["git", "init", "-b", git_stash_branch])

    # config
    subprocess.call(
        ["git", "config", "user.name", git_author_name]
    )
    subprocess.call(
        ["git", "config", "user.email", git_author_email]
    )
    if git_https_origin != "":
        subprocess.call(["git", "remote", "add", "origin", git_https_origin])

    if git_https_upstream != "":
        subprocess.call(
            ["git", "remote", "add", "upstream", git_https_upstream]
        )

    subprocess.call(["git", "fetch", "--all"])

    # prepare the first commit
    subprocess.call(["git", "add", "."])
    subprocess.call([
        "git",
        "commit",
        "-m",
        "A temporary from SciCookie",
        "--no-verify"
    ])

    subprocess.call(["git", "checkout", f"origin/{git_main_branch}"])
    subprocess.call(["git", "checkout", "-b", git_new_branch])
    subprocess.call(["git", "checkout", git_stash_branch, "--", "."])
    subprocess.call(["git", "add", "."])
    subprocess.call([
        "git", "commit", "-m", "Initial commit from SciCookie", "--no-verify"
    ])
    subprocess.call(["git", "branch", "-D", git_stash_branch])


def add_binding_source_files():
    if BUILD_SYSTEM == "maturin":
        build_system_dir = PROJECT_DIRECTORY / "build-system"
        src_system_dir = PROJECT_DIRECTORY/ "src"
        if USE_SRC_LAYOUT :
            shutil.move(build_system_dir / "lib.rs", "src")
        else:
            os.makedir(src_system_dir)
            shutil.move(build_system_dir / "lib.rs", src_system_dir)
    elif BUILD_SYSTEM == "pybind11" :
        build_system_dir = PROJECT_DIRECTORY / "build-system"
        src_system_dir = PROJECT_DIRECTORY/ "src"
        if USE_SRC_LAYOUT :
            shutil.move(build_system_dir / "main.cpp", "src")
        else:
            os.makedir(src_system_dir)
            shutil.move(build_system_dir / "main.cpp", src_system_dir)
    else:
        pass


def clean_up_mypy():
    if not USE_MYPY:
        remove_package_file("py.typed")


def post_gen():

    # keep this one first, because it changes the package folder
    clean_up_project_layout()
    add_binding_source_files()
    clean_up_automation()
    clean_up_cli()
    clean_up_mypy()
    clean_up_code_of_conduct()
    clean_up_conda()
    clean_up_containers()
    clean_up_docs()
    clean_up_governance()
    clean_up_roadmap()
    clean_up_build_system()
    clean_up_prettier()

    # keep it at the end, because it will create a new git commit
    prepare_git()


if __name__ == "__main__":
    post_gen()
