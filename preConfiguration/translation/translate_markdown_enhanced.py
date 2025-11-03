#!/usr/bin/env python3
"""
Script di integrazione per sostituire translate_markdown.py nel workflow esistente.
Mantiene la stessa interfaccia ma usa markdown-translator internamente.
"""

import os
import sys
from pathlib import Path

# Aggiungi il percorso dello script new_translate_markdown.py
sys.path.insert(0, str(Path(__file__).parent))

from new_translate_markdown import MarkdownTranslator

def translate_markdown_dir(src_dir, dst_dir):
    """
    Funzione compatibile con il vecchio sistema.
    Mantiene la stessa interfaccia di translate_markdown.py
    """
    print(f"🔄 Traduzione da {src_dir} a {dst_dir} usando markdown-translator...")
    
    # Carica API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY non impostata. Fallback al vecchio sistema.")
        # Importa e usa il vecchio sistema come fallback
        try:
            from translate_markdown_old import translate_markdown_dir as old_translate
            return old_translate(src_dir, dst_dir)
        except ImportError:
            print("❌ Vecchio sistema non disponibile. Imposta GEMINI_API_KEY.")
            return False
    
    # Usa il nuovo sistema
    translator = MarkdownTranslator("markdown-translator")
    
    # Determina la direzione in base ai percorsi
    if "it" in src_dir.lower() and "en" in dst_dir.lower():
        # Da italiano a inglese
        success = translator.translate_italian_to_english(api_key)
    elif "en" in src_dir.lower() and "it" in dst_dir.lower():
        # Da inglese a italiano
        success = translator.translate_english_to_italian(api_key)
    else:
        print(f"⚠️  Direzione non riconosciuta: {src_dir} -> {dst_dir}")
        print("Assumo traduzione da italiano a inglese...")
        success = translator.translate_italian_to_english(api_key)
    
    return success

def main():
    """Mantiene la stessa interfaccia del vecchio script."""
    src_dir = os.path.join("docs", "it")
    dst_dir = os.path.join("docs", "en")
    translate_markdown_dir(src_dir, dst_dir)

if __name__ == "__main__":
    main()
