project(
  '{{ cookiecutter.project_slug }}',
  'cpp',
  version: '{{ cookiecutter.project_version }}',  # semantic-release
  license: '{{ cookiecutter.project_license }}',
  meson_version: '>= 1.1.0',
)
name = '{{ cookiecutter.project_slug }}'

py_mod = import('python')
py = py_mod.find_installation(pure: false)

py.extension_module(
    '{{ cookiecutter.package_slug }}.py',
    install: true,
)
