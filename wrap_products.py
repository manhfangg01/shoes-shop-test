import os
import re

for f in os.listdir('.'):
    if not f.endswith('.html'): continue
    with open(f, 'r', encoding='utf-8') as fr:
        c = fr.read()

    def safe_wrap(pattern, replacement, string):
        # Apply replacement if it does not already have <a
        return re.sub(pattern, replacement, string, flags=re.DOTALL)

    # Wrap product names
    product_classes = ['air-force', 'bolt', 'zenith', 'swift']
    for p in product_classes:
        c = safe_wrap(
            rf'(<div class="{p}"[^>]*>.*?</div>)',
            r'<a href="DetailedProduct.html" style="text-decoration:none; display:contents; color:inherit;">\1</a>',
            c
        )

    # Wrap product images: image-204 to image-217 (for index.html, testing shows these are shoes)
    # image-226 might be something else, let's wrap image-2\d{2} selectively if we can.
    # Actually, any image starting with image-204 to image-217. 
    # Let's just do image-204 up to image-217 specifically
    for i in range(204, 218):    
        c = safe_wrap(
            rf'(<img class="image-{i}"[^>]*/>)',
            r'<a href="DetailedProduct.html" style="display:contents;">\1</a>',
            c
        )

    with open(f, 'w', encoding='utf-8') as fw:
        fw.write(c)

print('Wrapped products!')