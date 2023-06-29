project(
  '{{ cookiecutter.project_slug }}',
  'python',
  version: '{{ cookiecutter.project_version }}',  # semantic-release
  license: '{{ cookiecutter.project_license }}',
  meson_version: '>= 1.1.0',
)
name = '{{ cookiecutter.project_slug }}'

py_mod = import('python')
py = py_mod.find_installation(pure: false)

py.extension_module(
    '{{ cookiecutter.package_slug }}',
    '{{ cookiecutter.package_slug }}.py',
    install: true,
)

{% if cookiecutter.project_layout == "src" -%}
install_subdir('src' / '{{ cookiecutter.project_slug }}', install_dir: py.get_install_dir() / '{{ cookiecutter.project_slug }}')
{%- else %}
install_subdir('{{ cookiecutter.project_slug }}', install_dir: py.get_install_dir() / '{{ cookiecutter.project_slug }}')
{%- endif %}
