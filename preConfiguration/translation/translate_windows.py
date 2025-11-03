#!/usr/bin/env python3
"""
Wrapper Windows-friendly per markdown-translator.
Risolve problemi di encoding e percorsi su Windows.
"""

import os
import sys
import subprocess
from pathlib import Path
import json

def run_node_command(cmd, cwd=None):
    """Esegue un comando Node.js in modo Windows-friendly."""
    try:
        # Su Windows, forziamo UTF-8 e gestiamo gli errori
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        env['NODE_OPTIONS'] = '--no-warnings'
        
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',  # Sostituisce caratteri problematici
            env=env,
            shell=False  # Evita problemi con shell
        )
        
        if result.returncode == 0:
            return result.stdout, True
        else:
            return result.stderr, False
            
    except Exception as e:
        return str(e), False

def check_api_key():
    """Verifica che l'API key sia impostata."""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY non impostata!")
        print("📝 Imposta la variabile d'ambiente:")
        print('   $env:GEMINI_API_KEY = "your-api-key-here"')
        print("📖 Ottieni la key da: https://aistudio.google.com/app/apikey")
        return False
    
    print(f"✅ API key configurata (termina con: ...{api_key[-8:]})")
    return True

def check_markdown_translator():
    """Verifica che markdown-translator sia installato."""
    translator_dir = Path("markdown-translator")
    cli_path = translator_dir / "bin" / "cli.js"
    
    if not cli_path.exists():
        print("❌ markdown-translator non trovato!")
        print("📝 Esegui: python setup_markdown_translator.py")
        return False
    
    print("✅ markdown-translator trovato")
    return True

def translate_with_retry(pattern, target_lang, output_dir, max_retries=3):
    """Traduce con retry automatico in caso di errori."""
    translator_dir = Path("markdown-translator")
    cli_path = translator_dir / "bin" / "cli.js"
    
    cmd = [
        "node",
        str(cli_path),
        "translate",
        "-i", pattern,
        "-l", target_lang,
        "-d", output_dir
    ]
    
    for attempt in range(max_retries):
        print(f"🔄 Tentativo {attempt + 1}/{max_retries}...")
        
        output, success = run_node_command(cmd, cwd=translator_dir.parent)
        
        if success:
            print("✅ Traduzione completata!")
            print(output)
            return True
        else:
            print(f"❌ Tentativo {attempt + 1} fallito:")
            print(output)
            
            if attempt < max_retries - 1:
                print("⏳ Pausa 5 secondi prima del retry...")
                import time
                time.sleep(5)
    
    return False

def main():
    """Funzione principale Windows-friendly."""
    print("🌍 Traduttore Markdown - Versione Windows")
    print("=" * 50)
    
    # Verifica prerequisiti
    if not check_api_key():
        sys.exit(1)
    
    if not check_markdown_translator():
        sys.exit(1)
    
    # Verifica che docs/it esista e contenga file .md
    docs_it = Path("../../docs/it")
    if not docs_it.exists():
        print(f"❌ Directory non trovata: {docs_it.absolute()}")
        sys.exit(1)
    
    md_files = list(docs_it.glob("*.md"))
    if not md_files:
        print(f"❌ Nessun file .md trovato in: {docs_it.absolute()}")
        sys.exit(1)
    
    print(f"📁 Trovati {len(md_files)} file .md in docs/it")
    
    # Crea directory output
    docs_en = Path("../../docs/en")
    docs_en.mkdir(exist_ok=True)
    print(f"📂 Directory output: {docs_en.absolute()}")
    
    # Esegui traduzione
    print("\n🚀 Inizio traduzione...")
    success = translate_with_retry(
        "../../docs/it/*.md", 
        "English", 
        "../../docs/en"
    )
    
    if success:
        print("\n🎉 Traduzione completata con successo!")
        
        # Verifica file tradotti
        translated_files = list(docs_en.glob("*.md"))
        print(f"📊 File tradotti: {len(translated_files)}")
        
        for file in translated_files:
            size = file.stat().st_size
            print(f"   📄 {file.name} ({size} bytes)")
        
    else:
        print("\n❌ Traduzione fallita dopo tutti i tentativi")
        print("🔧 Suggerimenti:")
        print("   1. Verifica la connessione internet")
        print("   2. Controlla che l'API key sia valida") 
        print("   3. Prova a tradurre un singolo file per test")
        sys.exit(1)

if __name__ == "__main__":
    main()