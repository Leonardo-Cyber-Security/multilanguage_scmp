
#!/usr/bin/env python3
"""
Script di traduzione aggiornato che usa markdown-translator di PlayCanvas.
Mantiene la compatibilità con il sistema esistente ma offre qualità superiore.
"""

import os
import sys
from pathlib import Path

# Importa il nuovo sistema
try:
    from translate_simple import translate_all_files, check_prerequisites
    NEW_SYSTEM_AVAILABLE = True
except ImportError:
    NEW_SYSTEM_AVAILABLE = False

def translate_markdown_dir(src_dir, dst_dir):
    """
    Funzione compatibile con il vecchio sistema.
    Ora usa il nuovo markdown-translator quando possibile.
    """
    print(f"🔄 Traduzione da {src_dir} a {dst_dir}")
    
    if NEW_SYSTEM_AVAILABLE and check_prerequisites():
        print("✅ Usando il nuovo sistema markdown-translator")
        return translate_all_files()
    else:
        print("⚠️  Fallback al vecchio sistema translate-shell")
        
        # Fallback al vecchio sistema
        import subprocess
        
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for filename in os.listdir(src_dir):
            if filename.endswith(".md"):
                src_path = os.path.join(src_dir, filename)
                dst_path = os.path.join(dst_dir, filename)
                with open(src_path, encoding="utf-8") as f:
                    text = f.read()
                print(f"Translating {src_path} -> {dst_path}")
                try:
                    result = subprocess.run([
                        "trans", "-b", "-no-ansi", "-s", "it", "-t", "en"],
                        input=text, text=True, capture_output=True, check=True
                    )
                    translated = result.stdout
                except Exception as e:
                    print(f"Translation failed for {src_path}: {e}")
                    translated = text
                with open(dst_path, "w", encoding="utf-8") as f:
                    f.write(translated)
        return True

def main():
    """Mantiene la stessa interfaccia del vecchio script."""
    src_dir = os.path.join("docs", "it")
    dst_dir = os.path.join("docs", "en")
    
    # Cambia alla directory root del progetto se necessario
    if not os.path.exists(src_dir):
        # Probabilmente siamo nella directory translation
        os.chdir("../..")
    
    translate_markdown_dir(src_dir, dst_dir)

if __name__ == "__main__":
    main()
