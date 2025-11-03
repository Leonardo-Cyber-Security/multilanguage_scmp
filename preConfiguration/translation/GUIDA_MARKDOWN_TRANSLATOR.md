# Guida all'integrazione di markdown-translator di PlayCanvas

## 🎯 Panoramica

Abbiamo integrato il [markdown-translator di PlayCanvas](https://github.com/playcanvas/markdown-translator) nel progetto per migliorare significativamente la qualità delle traduzioni. Questo strumento usa Google Gemini AI e offre molti vantaggi rispetto al vecchio sistema basato su `translate-shell`.

## ✨ Vantaggi del nuovo sistema

### 🆚 Confronto con il vecchio sistema

| Caratteristica | Vecchio (translate-shell) | Nuovo (Gemini AI) |
|---|---|---|
| **Qualità traduzione** | Letterale, spesso incorretta | Contestuale, naturale |
| **Formattazione** | Spesso danneggiata | Perfettamente preservata |
| **Code blocks** | Tradotti (errore!) | Preservati correttamente |
| **Link e URL** | Tradotti (errore!) | Preservati correttamente |
| **File grandi** | Problemi di memoria | Chunking automatico |
| **Velocità** | Lenta | Veloce con parallelizzazione |
| **Lingue supportate** | Limitate | 40+ lingue |

### 🌟 Caratteristiche principali

- **🌍 Multi-lingua**: Supporta oltre 40 lingue
- **📝 Markdown-aware**: Preserva headers, link, code blocks, tabelle
- **🔄 Chunking intelligente**: Divide automaticamente file grandi
- **🎯 Traduzione selettiva**: Solo testo, preserva codice e URL
- **📂 Batch processing**: Pattern glob per più file
- **🏗️ Preservazione struttura**: Mantiene la struttura delle directory
- **⚡ Veloce**: Ottimizzato per velocità con Gemini

## 🚀 Setup completato

Il setup è già stato eseguito automaticamente. I file creati sono:

```
preConfiguration/translation/
├── markdown-translator/          # Tool clonato da GitHub
├── new_translate_markdown.py     # Script principale nuovo
├── translate_markdown_enhanced.py # Script compatibilità
├── translate_markdown_old.py     # Backup vecchio sistema
├── setup_markdown_translator.py  # Script di setup
└── integrate_markdown_translator.py # Script integrazione
```

## 🔑 Configurazione API Key

### Opzione 1: Variabile d'ambiente (consigliata)

```powershell
# Windows PowerShell
$env:GEMINI_API_KEY = "your-api-key-here"

# Command Prompt
set GEMINI_API_KEY=your-api-key-here

# Per rendere permanente, aggiungi alle variabili di sistema
```

### Opzione 2: File .env

Modifica il file `markdown-translator/.env`:

```env
GEMINI_API_KEY=your-api-key-here
```

### Ottenere l'API Key

1. Vai su [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Crea una nuova API key
3. Copia la chiave generata

## 📖 Utilizzo

### 🔄 Traduzione automatica (raccomandato)

```bash
# Da italiano a inglese (sostituisce il vecchio flusso)
python new_translate_markdown.py --direction it-en

# Da inglese a italiano
python new_translate_markdown.py --direction en-it

# Con API key specifica
python new_translate_markdown.py --direction it-en --api-key YOUR_KEY
```

### 🎯 Traduzione singolo file

```bash
cd markdown-translator
node bin/cli.js translate -i ../docs/it/index.md -l English -o ../docs/en/index.md
```

### 📁 Traduzione batch con pattern

```bash
cd markdown-translator

# Tutti i .md nella directory corrente
node bin/cli.js translate -i "*.md" -l Spanish -d ./spanish/

# Tutti i markdown in docs/ ricorsivamente
node bin/cli.js translate -i "docs/**/*.md" -l French -d ./translations/

# Struttura piatta (no sottodirectory)
node bin/cli.js translate -i "content/**/*.md" -l German -d ./output/ --flat
```

## 🔧 Integrazione nel workflow esistente

### GitHub Actions (.github/workflows/Automation.yml)

Sostituire la sezione di traduzione:

```yaml
# PRIMA (vecchio sistema)
- name: Run translation
  run: python preConfiguration/translation/translate_markdown.py

# DOPO (nuovo sistema)
- name: Setup translation environment
  run: |
    echo "GEMINI_API_KEY=${{ secrets.GEMINI_API_KEY }}" >> $GITHUB_ENV
    
- name: Run enhanced translation
  run: python preConfiguration/translation/new_translate_markdown.py --direction it-en
```

### Script di compatibilità

Per mantenere compatibilità con script esistenti, usa:

```python
# Sostituisce automaticamente il vecchio sistema
from translate_markdown_enhanced import translate_markdown_dir

# Mantiene la stessa interfaccia
translate_markdown_dir("docs/it", "docs/en")
```

## 🧪 Test del nuovo sistema

### Test rapido

```bash
# Imposta la API key
$env:GEMINI_API_KEY = "your-key"

# Test traduzione di un file
cd markdown-translator
node bin/cli.js translate -i ../docs/it/index.md -l English

# Test traduzione batch
python new_translate_markdown.py --direction it-en
```

### Verifica risultati

Controlla che:
- ✅ I code blocks non siano tradotti
- ✅ I link e URL siano preservati
- ✅ La formattazione Markdown sia intatta
- ✅ Le immagini abbiano alt text tradotto ma path preservato
- ✅ Le tabelle mantengano la struttura

## 🚨 Risoluzione problemi

### Errore API Key

```
❌ API key mancante. Usa --api-key o imposta GEMINI_API_KEY
```

**Soluzione**: Imposta correttamente la API key (vedi sezione Configurazione)

### Errore Node.js

```
❌ Node.js versione X.X.X trovata. Richiesta versione 16+
```

**Soluzione**: Aggiorna Node.js da [nodejs.org](https://nodejs.org/)

### File non trovato

```
❌ Errore nel clonare markdown-translator
```

**Soluzione**: Verifica connessione internet e riesegui setup

### Rate limiting

Se ricevi errori di rate limiting:
- Aspetta qualche minuto
- Il tool ha già retry automatico
- Considera di dividere file molto grandi

## 🔄 Migrazione graduale

### Strategia raccomandata:

1. **Test in locale** con pochi file
2. **Backup** dei file tradotti esistenti
3. **Confronto** qualità vecchio vs nuovo
4. **Aggiornamento** workflow GitHub Actions
5. **Monitoraggio** delle prime traduzioni automatiche

### Rollback se necessario:

```bash
# Ripristina il vecchio sistema
cp translate_markdown_old.py translate_markdown.py
```

## 📊 Monitoraggio e metriche

Il nuovo sistema fornisce output dettagliato:

```
📋 Translation Details:
   Input:    docs/it/index.md
   Output:   docs/en/index.md
   Language: English

⠋ Translating chunk 2/3...
✅ Translation completed successfully!

📊 Summary:
   Original length:  2,845 characters
   Translated length: 3,120 characters
   Files processed: 5
   Successful: 5
   Failed: 0
```

## 🎯 Best practices

1. **Testa sempre** le traduzioni prima del deploy
2. **Mantieni backup** dei file originali
3. **Monitora i costi** dell'API Gemini
4. **Usa variabili d'ambiente** per le API key
5. **Verifica la formattazione** dopo la traduzione

## 🆘 Supporto

- **Issues**: Crea issue nel repository del progetto
- **Documentazione originale**: [PlayCanvas markdown-translator](https://github.com/playcanvas/markdown-translator)
- **API Gemini**: [Google AI Studio](https://aistudio.google.com/)

---

## 🎉 Risultato finale

Con questa integrazione, il tuo progetto ora ha:

- ✅ Traduzioni di qualità professionale
- ✅ Preservazione perfetta della formattazione
- ✅ Automazione completa del workflow
- ✅ Compatibilità con il sistema esistente
- ✅ Scalabilità per progetti futuri

Il sistema è pronto per l'uso! 🚀