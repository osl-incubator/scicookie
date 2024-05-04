{% if cookiecutter.project_layout == "src" -%}
{% set package_path = "src/" + cookiecutter.package_slug -%}
{% else -%}
{% set package_path = cookiecutter.package_slug -%}
{% endif -%}
{% set cpp_path = "src/" -%}
project(
  '{{ cookiecutter.project_slug }}',
  'cpp',
  version: '{{ cookiecutter.project_version }}',  # semantic-release
  license: '{{ cookiecutter.project_license }}',
  meson_version: '>= 1.1.0',
)
name = '{{ cookiecutter.package_slug }}'

py_mod = import('python')
py = py_mod.find_installation(pure: false)

py.extension_module(
    '{{ cpp_path }}/main.cpp',
    subdir: '{{ cookiecutter.project_slug }}',
    install: true,
)

install_subdir(
    '{{ package_path }}',
    install_dir: py.get_install_dir() / '{{ cookiecutter.project_slug }}',
    strip_directory: true
)
