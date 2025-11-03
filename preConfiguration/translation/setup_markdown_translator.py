#!/usr/bin/env python3
"""
Setup script per integrare markdown-translator di PlayCanvas nel progetto.
Questo script installa e configura markdown-translator per il progetto multilanguage_scmp.
"""

import os
import subprocess
import sys
import json
from pathlib import Path

def run_command(command, cwd=None):
    """Esegue un comando shell e restituisce il risultato."""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            capture_output=True, 
            text=True,
            cwd=cwd
        )
        return result.stdout.strip(), True
    except subprocess.CalledProcessError as e:
        print(f"Errore nell'eseguire il comando: {command}")
        print(f"Errore: {e.stderr}")
        return e.stderr, False

def check_node_version():
    """Controlla se Node.js è installato e la versione."""
    output, success = run_command("node --version")
    if not success:
        print("❌ Node.js non è installato. Installalo da https://nodejs.org/")
        return False
    
    version = output.replace('v', '')
    major_version = int(version.split('.')[0])
    
    if major_version < 16:
        print(f"❌ Node.js versione {version} trovata. Richiesta versione 16+")
        return False
    
    print(f"✅ Node.js versione {version} OK")
    return True

def clone_markdown_translator():
    """Clona il repository markdown-translator."""
    translator_dir = Path("markdown-translator")
    
    if translator_dir.exists():
        print("📁 Directory markdown-translator già esistente")
        return str(translator_dir)
    
    print("📥 Clonando markdown-translator...")
    output, success = run_command("git clone https://github.com/playcanvas/markdown-translator.git")
    
    if success:
        print("✅ markdown-translator clonato con successo")
        return str(translator_dir)
    else:
        print("❌ Errore nel clonare markdown-translator")
        return None

def install_dependencies(translator_dir):
    """Installa le dipendenze di markdown-translator."""
    print("📦 Installando dipendenze...")
    
    output, success = run_command("npm install", cwd=translator_dir)
    
    if success:
        print("✅ Dipendenze installate con successo")
        return True
    else:
        print("❌ Errore nell'installare le dipendenze")
        return False

def create_env_file(translator_dir):
    """Crea il file .env con la configurazione."""
    env_path = Path(translator_dir) / ".env"
    
    if env_path.exists():
        print("📄 File .env già esistente")
        return True
    
    # Copia il template
    env_example = Path(translator_dir) / "env.example"
    if env_example.exists():
        with open(env_example, 'r') as f:
            content = f.read()
        
        with open(env_path, 'w') as f:
            f.write(content)
        
        print("📄 File .env creato da env.example")
        print("⚠️  IMPORTANTE: Aggiungi la tua API key di Google Gemini nel file .env")
        print("   Ottieni la key da: https://aistudio.google.com/app/apikey")
        return True
    
    return False

def create_translation_script():
    """Crea uno script Python per usare markdown-translator nel nostro workflow."""
    script_content = '''#!/usr/bin/env python3
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
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"✅ Tradotto: {input_file} -> {target_language}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Errore nella traduzione di {input_file}: {e.stderr}")
            return False
    
    def translate_batch(self, pattern, target_language, output_dir, api_key=None, flat=False):
        """Traduce più file usando pattern glob."""
        cmd = ["node", str(self.cli_path), "translate", "-i", pattern, "-l", target_language, "-d", output_dir]
        
        if api_key:
            cmd.extend(["--key", api_key])
        
        if flat:
            cmd.append("--flat")
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"✅ Traduzione batch completata: {pattern} -> {target_language}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Errore nella traduzione batch: {e.stderr}")
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
'''
    
    script_path = Path("new_translate_markdown.py")
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print(f"✅ Script di traduzione creato: {script_path}")
    return str(script_path)

def main():
    """Funzione principale di setup."""
    print("🚀 Setup markdown-translator per multilanguage_scmp")
    print("=" * 50)
    
    # Controlla Node.js
    if not check_node_version():
        sys.exit(1)
    
    # Clona il repository
    translator_dir = clone_markdown_translator()
    if not translator_dir:
        sys.exit(1)
    
    # Installa dipendenze
    if not install_dependencies(translator_dir):
        sys.exit(1)
    
    # Crea file .env
    create_env_file(translator_dir)
    
    # Crea script di traduzione
    script_path = create_translation_script()
    
    print("\n🎉 Setup completato con successo!")
    print("=" * 50)
    print("📋 Prossimi passi:")
    print("1. Ottieni una API key da: https://aistudio.google.com/app/apikey")
    print(f"2. Aggiungi la key nel file: {translator_dir}/.env")
    print("   Oppure imposta la variabile d'ambiente: export GEMINI_API_KEY=your-key")
    print(f"3. Usa lo script: python {script_path} --direction it-en")
    print(f"4. Oppure: python {script_path} --direction en-it")
    print("\n✨ Buona traduzione!")

if __name__ == "__main__":
    main()