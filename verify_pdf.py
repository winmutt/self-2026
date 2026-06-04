#!/usr/bin/env python3
import sys
from PyPDF2 import PdfReader

pdf_path = sys.argv[1] if len(sys.argv) > 1 else '/opt/opencode/src/self-2026/assets/AMD_Strix_Halo_Talk.pdf'
reader = PdfReader(pdf_path)
for i, page in enumerate(reader.pages[:5], start=1):
    # Get raw content stream
    content = page.get_contents()
    if isinstance(content, list):
        data = b''.join([c.get_data() for c in content])
    else:
        data = content.get_data()
    txt = data.decode('latin1', errors='ignore')
    has_black_fill = '0 g' in txt and 're' in txt
    print(f'Page {i}: black fill detected={has_black_fill}')
