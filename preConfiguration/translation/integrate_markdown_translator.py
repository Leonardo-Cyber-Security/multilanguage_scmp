#!/usr/bin/env python3
"""
Script migliorato di traduzione che sostituisce translate_markdown.py
Usa markdown-translator di PlayCanvas con Google Gemini AI.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def backup_old_translation_system():
    """Backup del vecchio sistema di traduzione."""
    old_script = Path("translate_markdown.py")
    if old_script.exists():
        backup_path = Path("translate_markdown_old.py")
        shutil.copy2(old_script, backup_path)
        print(f"✅ Backup del vecchio script: {backup_path}")

def update_translation_in_build_config():
    """Suggerisce modifiche al build_config.py per usare il nuovo sistema."""
    build_config_path = Path("../build/build_config.py")
    
    if build_config_path.exists():
        print("\n📝 SUGGERIMENTO per build_config.py:")
        print("Sostituisci le chiamate a translate_markdown.py con:")
        print("python preConfiguration/translation/new_translate_markdown.py --direction it-en")
        print("\nNel workflow GitHub Actions, sostituisci:")
        print("- python preConfiguration/translation/translate_markdown.py")
        print("+ python preConfiguration/translation/new_translate_markdown.py --direction it-en")

def create_integration_script():
    """Crea uno script di integrazione per il workflow esistente."""
    integration_content = '''#!/usr/bin/env python3
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
'''
    
    integration_path = Path("translate_markdown_enhanced.py")
    with open(integration_path, 'w', encoding='utf-8') as f:
        f.write(integration_content)
    
    print(f"✅ Script di integrazione creato: {integration_path}")
    return str(integration_path)

def check_installation():
    """Verifica che markdown-translator sia installato correttamente."""
    translator_dir = Path("markdown-translator")
    cli_path = translator_dir / "bin" / "cli.js"
    
    if not cli_path.exists():
        print("❌ markdown-translator non installato correttamente")
        return False
    
    # Test del CLI
    try:
        result = subprocess.run(
            ["node", str(cli_path), "--help"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ markdown-translator funziona correttamente")
        return True
    except subprocess.CalledProcessError:
        print("❌ Errore nel test di markdown-translator")
        return False

def show_usage_examples():
    """Mostra esempi di utilizzo."""
    print("\n📖 ESEMPI DI UTILIZZO:")
    print("=" * 50)
    
    print("\n1. Traduzione manuale:")
    print("   python new_translate_markdown.py --direction it-en --api-key YOUR_KEY")
    print("   python new_translate_markdown.py --direction en-it --api-key YOUR_KEY")
    
    print("\n2. Con variabile d'ambiente:")
    print("   $env:GEMINI_API_KEY='your-key-here'")
    print("   python new_translate_markdown.py --direction it-en")
    
    print("\n3. Singolo file:")
    print("   cd markdown-translator")
    print("   node bin/cli.js translate -i ../docs/it/index.md -l English -o ../docs/en/index.md")
    
    print("\n4. Batch con pattern:")
    print("   cd markdown-translator") 
    print("   node bin/cli.js translate -i '../docs/it/**/*.md' -l English -d ../docs/en/")

def main():
    """Funzione principale."""
    print("🔧 Configurazione integrazione markdown-translator")
    print("=" * 50)
    
    # Backup del vecchio sistema
    backup_old_translation_system()
    
    # Verifica installazione
    if not check_installation():
        print("❌ Esegui prima setup_markdown_translator.py")
        sys.exit(1)
    
    # Crea script di integrazione
    integration_script = create_integration_script()
    
    # Suggerimenti per build_config.py
    update_translation_in_build_config()
    
    # Mostra esempi
    show_usage_examples()
    
    print("\n🎉 Integrazione completata!")
    print("=" * 50)
    print("📋 RACCOMANDAZIONI:")
    print("1. Imposta GEMINI_API_KEY come variabile d'ambiente")
    print("2. Testa la traduzione con il nuovo sistema")
    print("3. Aggiorna il workflow GitHub Actions")
    print(f"4. Usa {integration_script} per compatibilità con il vecchio sistema")
    print("\n⚠️  IMPORTANTE: Il nuovo sistema è molto più potente del vecchio!")
    print("   - Preserva la formattazione Markdown")
    print("   - Traduzione più accurata con AI")
    print("   - Gestisce file grandi automaticamente")

if __name__ == "__main__":
    main()