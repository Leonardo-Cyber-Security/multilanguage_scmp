#!/usr/bin/env python3
"""
Script to clean up generated HTML before PDF conversion.
Removes only specific text elements without breaking HTML structure.
"""

import re
import sys
from pathlib import Path


def cleanup_html(file_path):
    """
    Remove unwanted text elements from HTML file.
    
    Args:
        file_path: Path to the HTML file to clean
    """
    print(f"🔧 Cleaning HTML file: {file_path}")
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_size = len(content)
    
    # 1. Remove "SCMP Documentazione (IT)" or "SCMP Documentazione (EN)"
    content = re.sub(
        r'SCMP Documentazione \((IT|EN)\)',
        '',
        content,
        flags=re.IGNORECASE
    )
    print("✅ Removed 'SCMP Documentazione' text")
    
    # 2. Remove "REST API" text
    content = re.sub(
        r'REST\s*API',
        '',
        content,
        flags=re.IGNORECASE
    )
    print("✅ Removed 'REST API' text")
    
    # Write cleaned content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_size = len(content)
    removed_bytes = original_size - new_size
    
    print(f"✅ Cleanup complete! Removed {removed_bytes} bytes")
    print(f"   Original size: {original_size} bytes")
    print(f"   New size: {new_size} bytes")


def main():
    if len(sys.argv) < 2:
        print("Usage: python cleanup_html.py <path_to_html_file>")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"❌ Error: File not found: {file_path}")
        sys.exit(1)
    
    cleanup_html(file_path)


if __name__ == "__main__":
    main()
