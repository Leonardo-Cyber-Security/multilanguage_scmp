import json
from jinja2 import Template
import os
import shutil

# Base directory of this script (preConfiguration/pdf)
BASE_DIR = os.path.dirname(__file__)
# Root dir del progetto (due livelli sopra)
PROJECT_ROOT = os.path.normpath(os.path.join(BASE_DIR, '..', '..'))

# Carica config.json (moved under preConfiguration/build/config.json)
config_path = os.path.normpath(os.path.join(BASE_DIR, '..', 'build', 'config.json'))
with open(config_path, encoding='utf-8') as f:
    config = json.load(f)

# Percorso cartella template (this folder)
template_folder = BASE_DIR

def render_template(filename, context):
    path = os.path.join(template_folder, filename)
    with open(path, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**context)


def save_rendered(content, filename):
    # Converti il path relativo in path assoluto rispetto al project root
    output_path = os.path.join(PROJECT_ROOT, filename)
    dir_path = os.path.dirname(output_path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

# Lista dei template da generare e nomi file output (senza .j2)
# Genera PDF per la lingua italiana (come nel workflow)
lang_config = config["languages"]["it"]
print(f"Generando template PDF...")

templates = [
    ("pdf-header.html.j2", "documentation/pdfGeneration/pdf-header.html"),
    ("pdf-footer.html.j2", "documentation/pdfGeneration/pdf-footer.html"),
    ("pdf-firstPage.html.j2", "documentation/pdfGeneration/pdf-firstPage.html"),
]

for tpl_file, out_file in templates:
    rendered = render_template(tpl_file, lang_config)
    save_rendered(rendered, out_file)
    output_path = os.path.join(PROJECT_ROOT, out_file)
    print(f"  ✅ Generato {output_path}")

# Copy CSS into the destination folder alongside generated HTML
css_src = os.path.join(BASE_DIR, "pdf-leonardo.css")
css_dest_rel = os.path.join("documentation", "pdfGeneration", "pdf-leonardo.css")
css_dest_abs = os.path.join(PROJECT_ROOT, css_dest_rel)
css_dest_dir = os.path.dirname(css_dest_abs)
if not os.path.exists(css_dest_dir):
    os.makedirs(css_dest_dir, exist_ok=True)
shutil.copyfile(css_src, css_dest_abs)
print(f"  ✅ Copiato CSS {css_dest_abs}")

print("🎉 Template PDF generati con successo!")
