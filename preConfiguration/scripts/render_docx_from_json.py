#!/usr/bin/env python3
"""
render_docx_from_json.py
Given a .docx template containing Jinja-like placeholders and a JSON file with values,
render a new .docx with placeholders replaced.

The approach: unzip the docx, replace occurrences in XML files using Jinja2 rendering,
then rezip to output.docx. This preserves most docx structure.

Usage: python render_docx_from_json.py TEMPLATE.docx data.json output.docx
"""
import sys
import zipfile
import json
from pathlib import Path
from jinja2 import Environment


def load_context(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def render_docx(template_path, context, output_path):
    template_path = Path(template_path)
    output_path = Path(output_path)

    env = Environment()

    with zipfile.ZipFile(template_path, 'r') as zin:
        # Read all files into memory, rendering XML/text files
        items = {name: zin.read(name) for name in zin.namelist()}

    rendered = {}
    for name, data in items.items():
        # Only attempt rendering on XML files within word/ (document, headers, footers, etc.)
        if name.startswith('word/') and name.endswith('.xml'):
            try:
                text = data.decode('utf-8')
            except Exception:
                rendered[name] = data
                continue
            # Render with jinja2; keep undefined variables as empty string
            tpl = env.from_string(text)
            out = tpl.render(**context)
            rendered[name] = out.encode('utf-8')
        else:
            rendered[name] = data

    # Write out a new docx
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, data in rendered.items():
            zout.writestr(name, data)


def main():
    if len(sys.argv) < 4:
        print('Usage: render_docx_from_json.py TEMPLATE.docx data.json output.docx', file=sys.stderr)
        sys.exit(2)
    tpl = sys.argv[1]
    datafile = sys.argv[2]
    out = sys.argv[3]

    ctx = load_context(datafile)
    render_docx(tpl, ctx, out)
    print(f'Wrote {out}')


if __name__ == '__main__':
    main()
