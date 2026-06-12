#!/usr/bin/env python3
"""Render PDF slides as images for review"""

import fitz  # PyMuPDF
import os

pdf_path = '/opt/opencode/src/self-2026/assets/AMD_Strix_Halo_Talk.pdf'
output_dir = '/opt/opencode/src/self-2026/assets/slides'

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Open PDF
print(f"Opening {pdf_path}...")
doc = fitz.open(pdf_path)

print(f"Total slides: {len(doc)}")

# Render each page as image (zoom factor for DPI)
zoom = 2.0  # ~192 DPI for 96 DPI base
mat = fitz.Matrix(zoom, zoom)

for i, page in enumerate(doc, 1):
    pix = page.get_pixmap(matrix=mat)
    output_path = os.path.join(output_dir, f'slide_{i:03d}.png')
    pix.save(output_path)
    print(f"Saved: {output_path} ({pix.width}x{pix.height})")

doc.close()
print(f"\nAll slides saved to: {output_dir}")
