#!/usr/bin/env python3
"""
Script di traduzione usando markdown-translator di PlayCanvas.
Integrazione per il progetto multilanguage_scmp.
"""

import os
import subprocess
import sys
from pathlib import Path

class MarkdownTranslator:
    def __init__(self, translator_path="markdown-translator"):
        self.translator_path = Path(translator_path)
        self.cli_path = self.translator_path / "bin" / "cli.js"
        
    def translate_file(self, input_file, target_language, output_file=None, api_key=None):
        """Traduce un singolo file markdown."""
        cmd = ["node", str(self.cli_path), "translate", "-i", input_file, "-l", target_language]
        
        if output_file:
            cmd.extend(["-o", output_file])
        
        if api_key:
            cmd.extend(["--key", api_key])
        
        try:
            result = subprocess.run(
                cmd, 
                check=True, 
                capture_output=True, 
                text=True,
                encoding='utf-8',
                errors='ignore'
            )
            print(f"✅ Tradotto: {input_file} -> {target_language}")
            return True
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr if e.stderr else str(e)
            print(f"❌ Errore nella traduzione di {input_file}: {error_msg}")
            return False
    
    def translate_batch(self, pattern, target_language, output_dir, api_key=None, flat=False):
        """Traduce più file usando pattern glob."""
        cmd = ["node", str(self.cli_path), "translate", "-i", pattern, "-l", target_language, "-d", output_dir]
        
        if api_key:
            cmd.extend(["--key", api_key])
        
        if flat:
            cmd.append("--flat")
        
        try:
            result = subprocess.run(
                cmd, 
                check=True, 
                capture_output=True, 
                text=True,
                encoding='utf-8',
                errors='ignore'
            )
            print(f"✅ Traduzione batch completata: {pattern} -> {target_language}")
            return True
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr if e.stderr else str(e)
            print(f"❌ Errore nella traduzione batch: {error_msg}")
            return False
    
    def translate_italian_to_english(self, api_key=None):
        """Traduce tutti i file dalla cartella docs/it a docs/en."""
        print("🌍 Traduzione da Italiano a Inglese...")
        
        # Crea la directory di output se non esiste
        os.makedirs("docs/en", exist_ok=True)
        
        # Traduce tutti i file .md da docs/it
        return self.translate_batch(
            "docs/it/**/*.md",
            "English",
            "docs/en",
            api_key=api_key
        )
    
    def translate_english_to_italian(self, api_key=None):
        """Traduce tutti i file dalla cartella docs/en a docs/it."""
        print("🌍 Traduzione da Inglese a Italiano...")
        
        # Crea la directory di output se non esiste
        os.makedirs("docs/it", exist_ok=True)
        
        # Traduce tutti i file .md da docs/en
        return self.translate_batch(
            "docs/en/**/*.md",
            "Italian",
            "docs/it",
            api_key=api_key
        )

def main():
    """Funzione principale."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Traduttore markdown per multilanguage_scmp")
    parser.add_argument("--direction", choices=["it-en", "en-it"], required=True,
                       help="Direzione traduzione: it-en (italiano->inglese) o en-it (inglese->italiano)")
    parser.add_argument("--api-key", help="Google Gemini API key")
    parser.add_argument("--translator-path", default="markdown-translator",
                       help="Percorso al directory markdown-translator")
    
    args = parser.parse_args()
    
    # Carica API key da variabile d'ambiente se non fornita
    api_key = args.api_key or os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ API key mancante. Usa --api-key o imposta GEMINI_API_KEY")
        sys.exit(1)
    
    translator = MarkdownTranslator(args.translator_path)
    
    if args.direction == "it-en":
        success = translator.translate_italian_to_english(api_key)
    else:
        success = translator.translate_english_to_italian(api_key)
    
    if success:
        print("🎉 Traduzione completata con successo!")
    else:
        print("❌ Traduzione fallita")
        sys.exit(1)

if __name__ == "__main__":
    main()
