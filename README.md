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

## PDF Structure (39 slides)

Extracted using PyPDF2 (`pyenv exec pip install PyPDF2`):

| # | Title |
|---|-------|
| 1 | Six Months with AMD Strix Halo |
| 2 | What We're Covering (Agenda) |
| 3 | The Hardware: AMD Ryzen AI Max+ 395 (Corsair system + internals) |
| 4 | Physical Layout (specs) |
| 5 | APU Die Architecture |
| 6 | Component Breakdown (GPU/NPU) |
| 7 | Power Consumption & Performance (system comparison) |
| 8 | FastFlowLM + Query Performance Timeline |
| 9 | The Hardware Investment |
| 10 | Feat #1070: Core affinity when running multiple models |
| 11 | NUMA vs. Strix Halo: The CCD Problem |
| 12 | The Problem: NUMA Tools Can't See CCD Boundaries |
| 13 | Evidence: Threads Bouncing + Hardware Topology (part 1) |
| 14 | Evidence continued (amdgpu_top) |
| 15 | Cutting the Alexa Cord |
| 16 | Alexa Replacement Timeline |
| 17 | Home Assistant Dashboard |
| 18 | Home Assistant on Echo Show |
| 19 | Home Assistant Setup |
| 20 | LineageOS Device Compatibility |
| 21 | Issue #4: The Echo 8 Mic That Quit |
| 22 | Blender: Concrete Sign Mold Design |
| 23 | Blender process steps |
| 24 | OpenSCAD: Where Things Work |
| 25 | Dimensioned Parts View |
| 26 | Two Approaches to Physical Design |
| 27 | Project WWS: I Vibe-Coded an Entire System |
| 28 | AI Coding Editors: My Daily Drivers |
| 29 | Which Models? (chart) |
| 30 | Models in Use |
| 31 | Lessons Learned (Mostly) |
| 32 | Key Insights (8 takeaways) |
| 33 | 26 Years of Open Source (2000-2026) |
| 34 | GitHub Activity Heatmap (2018-2024 ghost town) |
| 35 | How Buying Hardware Got Me Back in Open Source |
| 36 | Contribution Breakdown |
| 37 | References & Sources (Power, Software) |
| 38 | References continued (Communities) |
| 39 | github.com/winmutt (End) |

### Verification

Run the verification script to ensure the black fill appears on all pages:

```bash
python3 verify_pdf.py
```

Or extract slide titles with PyPDF2:

```bash
pyenv exec pip install PyPDF2
pyenv exec python3 -c "
import PyPDF2
with open('assets/AMD_Strix_Halo_Talk.pdf', 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    print(f'Total slides: {len(reader.pages)}')
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            lines = [l.strip() for l in text.split('\n') if l.strip() and len(l.strip()) > 5]
            print(f'{i+1}: {lines[0][:80]}')
"
```

---

## History of attempts

- **Initial attempt**: Used `onPage` with a `draw_black_background` function but only the first page got the black fill.
- **Second attempt**: Introduced a `BlackCanvas` that drew the background in `__init__` and `showPage`. The first page was black, later pages were not.
- **Final solution**: Simplified to a proper `BlackCanvas` that draws the background before each page is finalized (via overridden `showPage`). The PDF now consistently shows a black background across all slides.

---

Feel free to explore the markdown files for deeper context on the presentation content and the development process.
