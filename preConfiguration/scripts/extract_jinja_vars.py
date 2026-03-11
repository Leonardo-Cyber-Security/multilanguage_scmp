#!/usr/bin/env python3
"""
extract_jinja_vars.py
Given a .docx file, extract all Jinja-style variables/placeholders (e.g., {{ var }} , {% ... %})
and print them as JSON (unique list).

Usage: python extract_jinja_vars.py template.docx
"""
import sys
import zipfile
import re
import json
from pathlib import Path

JINJA_EXPR_RE = re.compile(r"\{\{\s*([^\}]+?)\s*\}\}|\{%\s*([^%]+?)\s*%\}")


def extract_text_from_docx(docx_path):
    """Extract raw XML text contents from a .docx (word/document.xml and headers/footers)."""
    texts = []
    with zipfile.ZipFile(docx_path, 'r') as z:
        for name in z.namelist():
            if name.startswith('word/') and name.endswith('.xml'):
                try:
                    data = z.read(name).decode('utf-8', errors='ignore')
                    texts.append(data)
                except Exception:
                    continue
    return '\n'.join(texts)


def find_jinja_vars(text):
    found = set()
    for m in JINJA_EXPR_RE.finditer(text):
        if m.group(1):
            found.add(m.group(1).strip())
        if m.group(2):
            found.add(m.group(2).strip())
    return sorted(found)


def main():
    if len(sys.argv) < 2:
        print('Usage: extract_jinja_vars.py TEMPLATE.docx', file=sys.stderr)
        sys.exit(2)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f'File not found: {path}', file=sys.stderr)
        sys.exit(2)
    raw = extract_text_from_docx(path)
    vars = find_jinja_vars(raw)
    print(json.dumps({
        'file': str(path),
        'variables': vars,
        'count': len(vars)
    }, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
