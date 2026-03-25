import os
import re

for f in os.listdir('.'):
    if not f.endswith('.html'): continue
    with open(f, 'r', encoding='utf-8') as fr:
        c = fr.read()

    # Search for anything obvious destroying the layout like <style> issue
    # We noticed min-min-height: 4935px earlier. Let's see if <body ... is rendered properly.
    if '<style>' in c and '</style>' not in c:
        print(f"Missing style closing tag in {f}")

