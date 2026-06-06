# self-2026

This repository contains the artifacts for the **AMD Strix Halo 6‑month experience** presentation.

## What’s included

- `generate_pdf.py` – the script that builds the PDF using ReportLab.
- `verify_pdf.py` – a small helper that checks each page for the black‑background drawing operation.
- All image assets used in the slides (screenshots, charts, diagrams, etc.) under the `assets/` directory.
- The generated PDF: `AMD_Strix_Halo_Talk.pdf`.
- Supporting markdown files that document the outline, notes, and the evolution of the code.

## Goal

The presentation must have a **consistent black background** on **every page** with light‑colored text. Several approaches were tried:

1. **Custom `PageTemplate` with `onPage` callback** – only the first page was painted black.
2. **Custom `BlackCanvas` subclass** – the background was drawn for the first page but not subsequent ones.
3. **Using `canvasmaker=BlackCanvas`** – after fixing the canvas implementation, the PDF now correctly draws a full‑page black rectangle on each page (verified with `verify_pdf.py`).

## Verification

Run the verification script to ensure the black fill appears on all pages:

```bash
python3 verify_pdf.py
```

It will output something like:

```
Page 1: black=True
Page 2: black=True
...
All pages black? True
```

If any page reports `black=False`, the PDF generation logic needs to be revisited.

## How to rebuild

```bash
# (optional) recreate a fresh virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # if any are needed

# Generate the PDF
python3 generate_pdf.py
```

The script writes `AMD_Strix_Halo_Talk.pdf` to the repository root and also copies it into `assets/` for easy access.

## History of attempts

- **Initial attempt**: Used `onPage` with a `draw_black_background` function but only the first page got the black fill.
- **Second attempt**: Introduced a `BlackCanvas` that drew the background in `__init__` and `showPage`. The first page was black, later pages were not.
- **Final solution**: Simplified to a proper `BlackCanvas` that draws the background before each page is finalized (via overridden `showPage`). The PDF now consistently shows a black background across all slides.

---

Feel free to explore the markdown files for deeper context on the presentation content and the development process.
