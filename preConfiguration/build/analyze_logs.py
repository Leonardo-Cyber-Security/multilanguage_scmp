import re
import sys
from pathlib import Path

def parse_logs(file_path):
    print(f"{'TIMESTAMP':<20} | {'STATUS':<6} | {'RESPONSE TYPE':<15} | {'QUERY PARAMS'}")
    print("-" * 100)
    
    # Pattern per estrarre: Timestamp, Metodo/URL, Status Code, Bytes
    # Esempio log: 100.67.2.2 - - [21/Jul/2026:06:57:23 +0000] "GET /api/... HTTP/1.1" 200 33
    log_pattern = re.compile(r'\[(?P<timestamp>.*?)\] "GET (?P<url>.*?) HTTP/1\.1" (?P<status>\d{3}) (?P<bytes>\d+)')

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = log_pattern.search(line)
                if match:
                    timestamp = match.group('timestamp')
                    url = match.group('url')
                    status = match.group('status')
                    size = int(match.group('bytes'))
                    
                    # Estrai solo la parte dei parametri (dopo ?)
                    query_params = url.split('?')[-1] if '?' in url else "No params"
                    
                    # Determina se la risposta è vuota o no (basandosi sui byte)
                    # Solitamente un JSON vuoto {} è circa 2-4 byte, qui vediamo 33
                    is_empty = "Vuota (o quasi)" if size < 5 else f"Contenuto ({size} bytes)"
                    
                    print(f"{timestamp:<20} | {status:<6} | {is_empty:<15} | {query_params}")
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    # Percorsi dei file log dell'utente
    log_files = [
        r"c:\Users\Personal\Downloads\logs.yaml",
        r"c:\Users\Personal\Downloads\logs2.yaml"
    ]
    
    for log_file in log_files:
        if Path(log_file).exists():
            print(f"\n--- ANALISI FILE: {log_file} ---")
            parse_logs(log_file)
        else:
            print(f"\n⚠️ File non trovato: {log_file}")
