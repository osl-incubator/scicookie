"""

Generate the code reference pages and navigation.

REF:
https://github.com/mkdocstrings/mkdocstrings/blob/main/scripts/gen_ref_nav.py

"""

{%- if cookiecutter.use_black == "yes" %}
  {%- set QUOTE = '"' -%}
{%- else %}
  {%- set QUOTE = "'" -%}
{%- endif %}

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()
mod_symbol = (
    '<code class="doc-symbol doc-symbol-nav doc-symbol-module"></code>'
)

root = Path(__file__).parent.parent
{% if cookiecutter.project_layout == 'src' -%}
src = root / {{ QUOTE }}src{{ QUOTE }}
{% else -%}
src = root
{% endif -%}

for path in sorted(src.rglob({{ QUOTE }}*.py{{ QUOTE }})):
    module_path = path.relative_to(src).with_suffix({{ QUOTE }}{{ QUOTE }})
    doc_path = path.relative_to(src / {{ QUOTE }}{{ cookiecutter.package_slug }}{{ QUOTE }}).with_suffix({{ QUOTE }}.md{{ QUOTE }})
    full_doc_path = Path({{ QUOTE }}api{{ QUOTE }}, doc_path)

    parts = tuple(module_path.parts)

    if parts[-1] == {{ QUOTE }}__init__{{ QUOTE }}:
        parts = parts[:-1]
        doc_path = doc_path.with_name({{ QUOTE }}index.md{{ QUOTE }})
        full_doc_path = full_doc_path.with_name({{ QUOTE }}index.md{{ QUOTE }})
    elif parts[-1].startswith({{ QUOTE }}_{{ QUOTE }}):
        continue

    nav_parts = [f{{ QUOTE }}{mod_symbol} {part}{{ QUOTE }} for part in parts]
    nav[tuple(nav_parts)] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, {{ QUOTE }}w{{ QUOTE }}) as fd:
        ident = {{ QUOTE }}.{{ QUOTE }}.join(parts)
        fd.write(f{{ QUOTE }}::: {ident}{{ QUOTE }})

    mkdocs_gen_files.set_edit_path(
        full_doc_path, {{ QUOTE }}..{{ QUOTE }} / path.relative_to(root)
    )

with mkdocs_gen_files.open({{ QUOTE }}api/SUMMARY.md{{ QUOTE }}, {{ QUOTE }}w{{ QUOTE }}) as nav_file:
    nav_file.writelines(nav.build_literate_nav())
