#!/usr/bin/env python3
"""
Script to clean up generated HTML before PDF conversion.
Removes unwanted elements like header titles, PDF links, and REST API navigation.
"""

import re
import sys
from pathlib import Path


def cleanup_html(file_path):
    """
    Remove unwanted elements from HTML file.
    
    Args:
        file_path: Path to the HTML file to clean
    """
    print(f"🔧 Cleaning HTML file: {file_path}")
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_size = len(content)
    
    # 1. Remove md-header__title div and its content
    # Match from opening div to its closing div (multi-line, non-greedy)
    content = re.sub(
        r'<div\s+class="md-header__title"[^>]*>.*?</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    print("✅ Removed md-header__title section")
    
    # 2. Remove PDF link navigation item
    # Match li containing PDF link (case insensitive search for "PDF" and ".pdf")
    content = re.sub(
        r'<li\s+class="md-nav__item">\s*<a\s+href="[^"]*\.pdf"[^>]*>.*?</a>\s*</li>',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    print("✅ Removed PDF download link")
    
    # 3. Remove REST API navigation link in table of contents
    # Match anchor tags containing "REST API" text
    content = re.sub(
        r'<li\s+class="md-nav__item">\s*<a\s+href="#[^"]*"[^>]*>.*?REST\s*API.*?</a>\s*</li>',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    print("✅ Removed REST API navigation link")
    
    # 4. Additional cleanup: Remove any remaining ms-Icon--PDF references
    content = re.sub(
        r"<span\s+class=['\"]ms-Icon\s+ms-Icon--PDF['\"]></span>",
        '',
        content,
        flags=re.IGNORECASE
    )
    
    # 5. Additional cleanup: Remove "Versione PDF completa" text variations
    content = re.sub(
        r'<span\s+class="md-ellipsis">\s*<span\s+class=[\'"]ms-Icon\s+ms-Icon--PDF[\'"]></span>\s*Versione\s+PDF\s+completa\s*</span>',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
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
