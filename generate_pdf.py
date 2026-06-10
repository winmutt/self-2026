#!/usr/bin/env python3
"""
Generate PDF Presentation for AMD Strix Halo Talk
Dark theme with black background and light text
"""

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, Flowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import TopPadder
from reportlab.platypus.doctemplate import PageTemplate, Frame
import os
from PIL import Image as PILImage

# Custom canvas that draws a full-page black background for every page
def draw_black_background(canvas, doc):
    """Draw a full-page black rectangle before any flowables"""
    canvas.saveState()
    canvas.setFillColor(colors.black)
    canvas.rect(0, 0, canvas._pagesize[0], canvas._pagesize[1], fill=1, stroke=0)
    canvas.restoreState()
# Function to draw black background on each page before content







# Output file
output_pdf = '/opt/opencode/src/self-2026/assets/AMD_Strix_Halo_Talk.pdf'

def get_scaled_image(path, max_width, max_height):
    """Load image and scale to fit within max_width/max_height while preserving aspect ratio"""
    try:
        pil_img = PILImage.open(path)
        orig_w, orig_h = pil_img.size
        aspect = orig_w / orig_h
        
        # Scale to fit within constraints
        if max_width / max_height > aspect:
            # Height is limiting factor
            new_h = max_height
            new_w = new_h * aspect
        else:
            # Width is limiting factor
            new_w = max_width
            new_h = new_w / aspect
        
        return Image(path, width=new_w, height=new_h)
    except Exception as e:
        print(f"Warning: Could not load image {path}: {e}")
        return None



def create_pdf():
    """Create the complete PDF presentation"""
    
    global page_width, page_height
    page_width, page_height = landscape(letter)
    
    # Set up the PDF with black background via custom canvas
    margin = 0.5*inch
    
    doc = SimpleDocTemplate(output_pdf, pagesize=landscape(letter),
                           rightMargin=margin, leftMargin=margin,
                           topMargin=margin, bottomMargin=margin)

    
    # Styles - Dark theme with light text
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=colors.HexColor('#58a6ff'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#bc8cff'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=20,
        textColor=colors.HexColor('#58a6ff'),
        spaceAfter=12,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading3'],
        fontSize=15,
        textColor=colors.HexColor('#bc8cff'),
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#e0e0e0'),
        spaceAfter=8,
        fontName='Helvetica'
    )
    
    quote_style = ParagraphStyle(
        'Quote',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#a0a0a0'),
        spaceAfter=12,
        fontName='Helvetica-Oblique',
        leftIndent=20,
        rightIndent=20
    )
    
    humor_style = ParagraphStyle(
        'Humor',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#f0b37e'),
        spaceAfter=6,
        fontName='Helvetica-Oblique'
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#e0e0e0'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#58a6ff'),
        spaceAfter=12,
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor('#bc8cff'),
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#e0e0e0'),
        spaceAfter=6,
        fontName='Helvetica'
    )
    
    quote_style = ParagraphStyle(
        'Quote',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#a0a0a0'),
        spaceAfter=12,
        fontName='Helvetica-Oblique',
        leftIndent=20,
        rightIndent=20
    )
    
    body = []
    
    # ============================================
    # TITLE SLIDE
    # ============================================
    body.append(Spacer(1, 1.5*inch))
    body.append(Paragraph("Six Months with AMD Strix Halo", title_style))
    body.append(Paragraph("Local AI, Open Source, and Hardware Reality", subtitle_style))
    body.append(Spacer(1, 0.5*inch))
    body.append(Paragraph("A Six Month Review of a Strix Halo Rig", normal_style))
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph("AMD Strix Halo | Local AI | Home Assistant | 3D Modeling | Open Source", humor_style))
    body.append(Spacer(1, 1.5*inch))
    body.append(Paragraph("winmutt | June 2026", normal_style))
    body.append(Paragraph("github.com/winmutt", normal_style))
    body.append(PageBreak())
    
    # ============================================
    # AGENDA
    # ============================================
    body.append(Paragraph("What We're Covering", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Section 1: The Hardware Stack", subheading_style))
    agenda_items = [
        "• Power Consumption: Corsair 300 vs RTX 5090 vs Cloud",
        "• The Hardware: AMD Ryzen AI Max+ 395 APU",
        "• The Stack: ROCm + Lemonade Server",
        "• Issue #1070: Core affinity across dual CCDs"
    ]
    for item in agenda_items:
        body.append(Paragraph(f"  {item}", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Section 2: Projects & Applications", subheading_style))
    agenda_items = [
        "• Home Assistant: Cutting the Alexa cord",
        "• 3D Modeling: AI to concrete signs",
        "• AI Coding Editors: Opencode, Cline, Aider",
        "• Project WWS: Remote workspace provisioning"
    ]
    for item in agenda_items:
        body.append(Paragraph(f"  {item}", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Section 3: Open Source Journey", subheading_style))
    agenda_items = [
        "• Lessons Learned: What worked, what didn't",
        "• Key Insights: 8 takeaways from 6 months",
        "• OSS Contributions: 3.5x increase",
        "• 26 Years: From LKML 2000 to Strix Halo"
    ]
    for item in agenda_items:
        body.append(Paragraph(f"  {item}", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # ============================================
    # PART 5: THE HARDWARE
    # ============================================
    body.append(Paragraph("The Hardware: AMD Ryzen AI Max+ 395", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    # APU die diagram
    body.append(Paragraph("APU Die Architecture", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/apu_die_diagram.png', 7*inch, 4.5*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Physical Layout", subheading_style))
    body.append(Paragraph("• 16 cores (12 performance + 4 efficiency)", normal_style))
    body.append(Paragraph("• 2x Core Complex Dies (CCD) with 32MB L3 cache each", normal_style))
    body.append(Paragraph("• 768KB L1d + 512KB L1i + 16MB L2", normal_style))
    body.append(Paragraph("• Integrated RDNA 3.5 GPU (40 Compute Units)", normal_style))
    body.append(Paragraph("• 128GB LPDDR5X-8000 unified memory (soldered)", normal_style))
    body.append(Paragraph("• Source: AMD Ryzen AI Max+ 395 teardown analysis (Chiphell, TechPowerUp)", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("AMD Radeon 680M GPU", subheading_style))
    body.append(Paragraph("• RDNA 3.5 architecture, 40 Compute Units", normal_style))
    body.append(Paragraph("• Peak performance: ~4.6 TFLOPS", normal_style))
    body.append(Paragraph("• Shared memory with CPU (128GB unified)", normal_style))
    body.append(Paragraph("• Supports ROCm for AI/ML workloads", normal_style))
    body.append(Paragraph("• Source: AMD Ryzen AI Max+ 395 specifications", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("AMD XDNA 2 NPU", subheading_style))
    body.append(Paragraph("• Neural Processing Unit for AI workloads", normal_style))
    body.append(Paragraph("• Integrated into Ryzen AI Max+ 395 APU", normal_style))
    body.append(Paragraph("• Supports FastFlowLM for efficient inference", normal_style))
    body.append(Paragraph("• Power-efficient alternative to GPU processing", normal_style))
    body.append(Spacer(1, 0.2*inch))
    body.append(Paragraph("FastFlowLM Performance (June 2026):", subheading_style))
    body.append(Paragraph("• 6784 tokens prefill in ~15 seconds", normal_style))
    body.append(Paragraph("• ~455 tokens/sec on NPU", normal_style))
    body.append(Paragraph("• Chunked processing: 4096 + 2688 tokens", normal_style))
    body.append(Paragraph("• End-to-end (prefill to response): ~16.2 seconds", normal_style))
    body.append(Paragraph("• Source: FastFlowLM logs (lemonade-server)", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # ============================================
    # ISSUE #1070: NUMA/CCD CORE AFFINITY
    # ============================================
    body.append(Paragraph("Feat #1070: [enhancement] Core affinity when running multiple models.", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        '<b>Filed</b><br/>February 8, 2026<br/>'
        '<b>Repository</b><br/>github.com/lemonade-sdk/lemonade/issues/1070<br/>'
        '<b>Status</b><br/>Open',
        normal_style
    ))
    
    body.append(Spacer(1, 0.4*inch))
    
    body.append(Paragraph("Hardware Reality", subheading_style))
    body.append(Paragraph("• One processor, but 2x core dies (CCDs) with separate 32MB L3 caches", normal_style))
    body.append(Paragraph("• Traditional NUMA: 2 nodes, each with own cores + L3 cache", normal_style))
    body.append(Paragraph("• Strix Halo: Single node, but 2 CCDs with separate L3 caches", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # Architecture Comparison Diagrams - Separate Slide
    body.append(Paragraph("Traditional NUMA vs. Strix Halo APU", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    # Traditional NUMA diagram (shrunk 10%)
    img1 = get_scaled_image('/opt/opencode/src/self-2026/assets/numa_traditional.png', 6.3*inch, 3.15*inch)
    if img1:
        body.append(img1)
    
    body.append(Spacer(1, 0.3*inch))
    
    # Strix Halo diagram (shrunk 10%)
    img2 = get_scaled_image('/opt/opencode/src/self-2026/assets/strix_halo_numa.png', 6.3*inch, 3.15*inch)
    if img2:
        body.append(img2)
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    body.append(Paragraph("The Problem: NUMA Tools Can't See CCD Boundaries", subheading_style))
    body.append(Paragraph(
        "• Traditional NUMA tools (numactl, NUMATopologyFilter) detect only 1 node"
        '<br/>• Cannot see CCD boundaries automatically'
        '<br/>• Manual core pinning required to keep workloads on same CCD'
        '<br/>• Running multiple LLMs: threads bounce across CCDs → L3 cache thrashing'
        '<br/>'
        '<b>Result:</b> Cross-CCD traffic → slower inference, higher latency',
        normal_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Solution (Proposed)", subheading_style))
    body.append(Paragraph(
        'Manual core pinning (like Red Hat\'s vcpu_pin_set approach):'
        '<br/>• Reserve cores per CCD, pin llama-server accordingly'
        '<br/>• Pin based on number of models loaded and CCD boundaries'
        '<br/>• Prevent cache-crossing penalties'
        '<br/>'
        '<b>Result:</b> Each model stays in its own L3 cache domain → no cross-CCD traffic',
        normal_style
    ))
    
    body.append(PageBreak())
    
    # Evidence: ps output with red boxes
    body.append(Paragraph("Evidence: Threads Bouncing Across CCDs", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    img_ps = get_scaled_image('/opt/opencode/src/self-2026/assets/issue_1070_ps_output.png', 7*inch, 4*inch)
    if img_ps:
        body.append(img_ps)
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # Hardware Topology: CCD Boundaries - Separate Slide
    body.append(Paragraph("Hardware Topology: CCD Boundaries (lscpu)", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    img_lscpu = get_scaled_image('/opt/opencode/src/self-2026/assets/issue_1070_lscpu.png', 7*inch, 5*inch)
    if img_lscpu:
        body.append(img_lscpu)
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # Evidence: amdgpu_top
    body.append(Paragraph("Evidence: amdgpu_top", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    img_amdgpu = get_scaled_image('/opt/opencode/src/self-2026/assets/amdgpu_top.png', 7*inch, 4*inch)
    if img_amdgpu:
        body.append(img_amdgpu)
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # ============================================
    # PART 6: HOME ASSISTANT
    # ============================================
    body.append(Paragraph("Cutting the Alexa Cord", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("LineageOS on Echo", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>December 2025</b><br/>Started exploring XDA Forums for Echo device hacking',
        normal_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Process:", subheading_style))
    body.append(Paragraph("1. Unlock bootloader via amonet exploit", normal_style))
    body.append(Paragraph("  github.com/R0rt1z2/amonet", normal_style))
    body.append(Paragraph("2. Install TWRP recovery", normal_style))
    body.append(Paragraph("3. Flash LineageOS 18.1 (Android 11)", normal_style))
    body.append(Paragraph("4. Configure ViewAssist for Home Assistant", normal_style))
    body.append(Paragraph("  dinki.github.io/View-Assist", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        '<b>Philosophy</b><br/>"Basically anything with a USB port. '
        'If there is a port, there is a way."', quote_style
    ))
    
    body.append(PageBreak())
    
    body.append(Paragraph("Alexa Replacement Timeline", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    timeline_data = [
        ['Dec 6', 'Started exploring XDA forums'],
        ['Dec 7', 'HA running on Echo devices'],
        ['Jan 19', 'HA setup on Echo Show Gen 2'],
        ['Jan 21', 'Everything works (except wake word)'],
        ['Jan 25', 'Hey Jarvis to the rescue'],
        ['Jan 29', 'End-to-end complete'],
        ['Jan 7, 2026', 'Issue #4: Echo 8 mic dies after 24h'],
        ['Feb 2026', 'Still debugging (it\'s fine)']
    ]
    
    timeline_table = Table(timeline_data, colWidths=[1.5*inch, 5.5*inch])
    timeline_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#1a1a1a')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#e0e0e0')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#444444')),
    ]))
    body.append(timeline_table)
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # Home Assistant screenshot - Echo Show
    body.append(Paragraph("Home Assistant on Echo Show", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/ha.jpeg', 6*inch, 3.5*inch)
    if img:
        body.append(img)
    
    body.append(PageBreak())
    
    # Home Assistant dashboard screenshot
    body.append(Paragraph("Home Assistant Dashboard", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/homeasssistant.png', 6*inch, 3.5*inch)
    if img:
        body.append(img)
    
    body.append(PageBreak())
    
    # Home Assistant install screenshot
    body.append(Paragraph("Home Assistant Setup", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/myha.png', 6*inch, 3.5*inch)
    if img:
        body.append(img)
    
    body.append(PageBreak())
    
    # ============================================
    # DEVICE COMPATIBILITY
    # ============================================
    body.append(Paragraph("LineageOS Device Compatibility", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Echo Show Devices Supported", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    data = [
        ['Device', 'Codename', 'SoC', 'XDA Thread'],
        ['Echo Show 5 (1st Gen 2019)', 'checkers', 'MT8163', 'xdaforums.com/t/rom-unofficial-11-checkers...'],
        ['Echo Show 5 (2nd Gen 2021)', 'cronos', 'MT8163', 'xdaforums.com/t/rom-unofficial-11-cronos...'],
        ['Echo Show 8 (1st Gen 2019)', 'crown', 'MT8163', 'xdaforums.com/t/rom-unofficial-11-crown...'],
    ]
    
    table = Table(data, colWidths=[2.2*inch, 1.2*inch, 1.2*inch, 2.4*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#30363d')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#c9d1d9')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#0d1117')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#c9d1d9')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#30363d')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    body.append(table)
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("All devices use MediaTek MT8163 SoC", normal_style))
    body.append(Paragraph("LineageOS 18.1 (Android 11) - community builds by @R0rt1z2", normal_style))
    
    body.append(PageBreak())
    
    # Echo 8 mic issue
    body.append(Paragraph("Issue #4: The Echo 8 Mic That Quit", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Audio stops working after ~24 hours", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>Filed</b><br/>January 7, 2026<br/>'
        '<b>Repository</b><br/>https://github.com/amazon-oss/releases/issues/4<br/>'
        '<b>Status</b><br/>Open (still waiting, it\'s fine)',
        normal_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Problem", subheading_style))
    body.append(Paragraph("• Echo 5: Stable for days", normal_style))
    body.append(Paragraph("• Echo 8: Dies after ~24 hours", normal_style))
    body.append(Paragraph("• Root cause: Unknown (yet)", humor_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 5B: BLENDER - CONCRETE SIGNS
    # ============================================
    body.append(Paragraph("Blender: Concrete Sign Mold Design", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("AI-Assisted Physical Design", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph("Blender + AI workflow for creating physical objects", normal_style))
    body.append(Spacer(1, 0.3*inch))
    
    # Concrete sign image
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/concrete_sign.png', 6*inch, 4*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Process", subheading_style))
    body.append(Paragraph("1. AI generates Blender design", normal_style))
    body.append(Paragraph("2. Export to STL", normal_style))
    body.append(Paragraph("3. 3D print mold", normal_style))
    body.append(Paragraph("4. Create silicone mold", normal_style))
    body.append(Paragraph("5. Cast concrete", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph("December 1, 2025 — More physical projects coming soon", humor_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 5C: OPENS CAD COMPARISON
    # ============================================
    body.append(Paragraph("OpenSCAD: Where Things Work", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("wmi002 Session — Precision Engineering", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>Success Story</b><br/>'
        '• Parametric design: Caliber-specific constants (.308 Winchester, 5.56 NATO)'
        '<br/>• Modular architecture: include <threading.scad>, <std.scad> (BOSL2)'
        '<br/>• Precision engineering: Thread pitches (5/8-24 UNF), bore dimensions, tolerances'
        '<br/>• Working output: K-baffles, blast chambers, threaded end caps',
        normal_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    # s1.png: K-baffle internal view
    body.append(Paragraph("K-Baffle Assembly (Internal View)", subheading_style))
    img_s1 = get_scaled_image('/opt/opencode/src/self-2026/assets/s1.png', 7*inch, 4*inch)
    if img_s1:
        body.append(img_s1)
    
    body.append(Spacer(1, 0.3*inch))
    
    # s2.png: Dimensioned parts
    body.append(Paragraph("Dimensioned Parts View", subheading_style))
    img_s2 = get_scaled_image('/opt/opencode/src/self-2026/assets/s2.png', 7*inch, 4*inch)
    if img_s2:
        body.append(img_s2)
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # Comparison section
    body.append(Paragraph("Two Approaches to Physical Design", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    comparison_data = [
        ['OpenSCAD (wmi002)', 'Blender + AI (Concrete Signs)'],
        ['Code-driven parametrics', 'AI-generated meshes'],
        ['Thread tolerances: 5/8-24 UNF', 'Mold fit: "test and adjust"'],
        ['BOSL2 library: threaded_rod()', 'AI hallucinates topology'],
        ['$fn=100 precision', '$fn=32 vibes'],
        ['K-baffles: 15° frustum angles', 'Text: "Dancing Script:style=Bold"'],
        ['Stainless steel ready', 'Concrete ready'],
        ['Documented specs in code', 'Documented by hope'],
    ]
    
    table = Table(comparison_data, colWidths=[3.2*inch, 3.2*inch])
    table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
    ]))
    body.append(table)
    
    body.append(Spacer(1, 0.5*inch))
    body.append(Paragraph(
        '<b>Lesson:</b> OpenSCAD sessions produce working parts. '
        'Blender sessions produce concrete. '
        'Both are valid. Only one has thread tolerances.',
        humor_style
    ))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 7: WWS PROJECT
    # ============================================
    body.append(Paragraph("Project WWS: I Vibe-Coded an Entire System", heading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph("Winmutt Work Spaces — github.com/winmutt/wws", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>May 12, 2026</b><br/>"Definitely no Athena and its taken months '
        'to get there but this is something I entirely vibe coded."', quote_style
    ))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph("Remote workspace provisioning with KVM/Podman isolation", normal_style))
    body.append(Paragraph("code-server (VSCode in browser) + GitHub OAuth + RBAC", normal_style))
    body.append(Paragraph("First commit: Feb 22, 2026 → Production: May 12, 2026", normal_style))
    body.append(Spacer(1, 0.3*inch))
    
    # WWS Dashboard screenshot
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/dashboard.png', 7*inch, 3.5*inch)
    if img:
        body.append(img)
    
    body.append(PageBreak())
    
    # ============================================
    # PART 8: LESSONS LEARNED
    # ============================================
    body.append(Paragraph("Lessons Learned (Mostly)", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("What Worked ✓", subheading_style))
    body.append(Paragraph("• Cline + Qwen3-Coder: Actually produces code", normal_style))
    body.append(Paragraph("• Prompt Caching: Things hum now", normal_style))
    body.append(Paragraph("• AMD GPU Libraries: 2x faster (worth the pain)", normal_style))
    body.append(Paragraph("• WWS Project: Vibe-coded from Feb 22 (first commit) to May 12", normal_style))
    body.append(Paragraph("• Home Assistant: Alexa is dead, long live OSS", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("What Didn't ✗", subheading_style))
    body.append(Paragraph("• Memory: 32GB reserved for Lemonade/llama.cpp/opencode", normal_style))
    body.append(Paragraph("• Ollama: Still crashes after updates", normal_style))
    body.append(Paragraph("• NPU: Coming soon™ (always)", normal_style))
    body.append(Paragraph("• Context >64k: TPS drops like a stone", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # KEY INSIGHTS
    # ============================================
    body.append(Spacer(1, 0.3*inch))
    
    insights = [
        "1. Hardware hype ≠ reality (APU challenges are real)",
        "2. Software maturity: bleeding edge = bleeding fingers",
        "3. Context > everything (prompt caching is life)",
        "4. AI coding > traditional IDEs (for me, anyway)",
        "5. AI → physical objects (concrete signs, apparently)",
        "6. Echo → Home Assistant = OSS win",
        "7. Autonomous dev: possible, painful, worth it",
        "8. Buying hardware got me back in open source"
    ]
    
    for insight in insights:
        body.append(Paragraph(f"  {insight}", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # 26 YEARS OF OPEN SOURCE
    # ============================================
    body.append(Paragraph("26 Years of Open Source (2000-2026)", heading_style))
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph("From LKML to Strix Halo: How Hardware Bought My Time", normal_style))
    body.append(Spacer(1, 0.5*inch))
    
    # The Story
    body.append(Paragraph("The Long Detour", subheading_style))
    body.append(Paragraph(
        'For 20+ years I built corporate SaaS products. Cloud disconnected me from the metal. '
        'Linux became something I deployed to, not something I touched daily. '
        'The kernel, the drivers, the hardware—left that world behind. '
        'Then Strix Halo arrived and changed everything.',
        normal_style
    ))
    body.append(Spacer(1, 0.3*inch))
    
    # LKML 2000 email text
    body.append(Paragraph("June 9, 2000: Asking on LKML", subheading_style))
    body.append(Paragraph(
        '<font face="Courier" size="8">'
        'From: Rolf Martin-Hoster (winmutt@hotmail.com)'
        '<br/>Date: Thu Jun 08 2000 - 19:24:59 EST'
        '<br/>Subject: HighPoint IDE RAID (kernel 2.2.14)'
        '<br/>'
        '<br/>Does anyone know where I can find developer info about the driver for this'
        '<br/>chipset?'
        '<br/>'
        '<br/>-Rolf'
        '</font>',
        normal_style
    ))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        'Back then: Hands-on with kernel 2.2.14, digging into IDE RAID drivers, '
        'asking questions on linux-kernel mailing list.',
        humor_style
    ))
    body.append(Spacer(1, 0.5*inch))
    
    # 10-year GitHub activity heatmap
    body.append(Paragraph("The Return: GitHub Activity (2018-2026)", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/github_heatmap_10year.png', 7*inch, 3.5*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph(
        '2018-2024: Ghost town. 2025: Strix Halo arrives. '
        'November 2025: Back on the metal, every single day. '
        'AI + local hardware reinvigorated my love for open source.',
        normal_style
    ))
    body.append(Paragraph(
        'Moral: Sometimes the best way back in is to buy new toys.',
        humor_style
    ))
    body.append(PageBreak())
    
    # ============================================
    # OSS CONTRIBUTION GROWTH
    # ============================================
    body.append(Paragraph("How Buying Hardware Got Me Back in Open Source", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Catalyst Effect", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        "November 2025: Bought Strix Halo rig. "
        "Local AI reinvigorated my love for OSS. "
        "Result: 3.5x increase in contributions.",
        normal_style
    ))
    
    body.append(Spacer(1, 0.5*inch))
    
    # Contribution calendar
    body.append(Paragraph("2026: The Year I Came Back", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/contribution_calendar_2026.png', 7*inch, 3*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.5*inch))
    
    # Project breakdown
    body.append(Paragraph("Projects I've Actually Contributed To", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/project_breakdown.png', 7*inch, 5*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("Contribution Breakdown", subheading_style))
    body.append(Paragraph("• WWS: 38% (remote workspace provisioning)", normal_style))
    body.append(Paragraph("• Lemonade: 15% (NPU backend, custom NUMA mapping)", normal_style))
    body.append(Paragraph("• ROCm: 8% (Issue #5926 memory management)", normal_style))
    body.append(Paragraph("• Home Assistant: 12% (wake words, Echo)", normal_style))
    body.append(Paragraph("• Cline: 8% (TUI regressions)", normal_style))
    body.append(Paragraph("• Concrete Signs: 5% (Blender/OpenSCAD)", normal_style))
    body.append(Paragraph("• Other: 10% (miscellaneous)", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # ============================================
    # AI CODING EDITORS
    # ============================================
    body.append(Paragraph("AI Coding Editors: My Daily Drivers", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Opencode", subheading_style))
    body.append(Paragraph(
        "Most usable, portable, and stable. Best agentic coding experience. "
        "Runs as a web server (http://localhost:3000) allowing remote access "
        "with a localized agent running for autonomous development. "
        "github.com/anomalyco/opencode",
        normal_style
    ))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Cline", subheading_style))
    body.append(Paragraph("Good TUI but many regressions over time.", normal_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Also Use: Koo Roo, Aider", normal_style))
    body.append(Spacer(1, 0.3*inch))
    
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/editor_collage.png', 7*inch, 5*inch)
    if img:
        body.append(img)
    
    body.append(PageBreak())
    
    # ============================================
    # REFERENCES & SOURCES
    # ============================================
    body.append(Paragraph("References & Sources", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Power Consumption Sources", subheading_style))
    body.append(Paragraph("• AMD Ryzen AI Max 395: 140-157W sustained power (Framework Reddit, 2025)", normal_style))
    body.append(Paragraph("  https://www.reddit.com/r/framework/comments/1najh1n/max_wattage_of_the_ryzen_ai_max_395_motherboard/", normal_style))
    body.append(Paragraph("• NVIDIA RTX 5090: 600W TDP (NVIDIA, 2025)", normal_style))
    body.append(Paragraph("  https://www.nvidia.com/geforce/rtx-5090", normal_style))
    body.append(Paragraph("• NVIDIA RTX 4090: 450W TDP (NVIDIA, 2022)", normal_style))
    body.append(Paragraph("  https://www.nvidia.com/geforce/rtx-4090", normal_style))
    body.append(Paragraph("• Corsair 300 AI Workstation: ~300W system power (Corsair, 2025)", normal_style))
    body.append(Paragraph("  https://www.corsair.com/ai-workstations", normal_style))
    body.append(Paragraph("• Tom's Hardware GPU power reviews (2024-2025)", normal_style))
    body.append(Paragraph("  https://www.tomshardware.com/reviews/gpu-hierarchy", normal_style))
    body.append(Paragraph("• TechPowerUp GPU database: Power benchmarks", normal_style))
    body.append(Paragraph("  https://www.techpowerup.com/gpu-specs", normal_style))
    body.append(Paragraph("• NVIDIA A100/H100: 400W-700W per GPU (NVIDIA Data Center)", normal_style))
    body.append(Paragraph("  Multi-GPU server: 1500W-3000W (NVIDIA DGX specs)", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Software & Projects", subheading_style))
    body.append(Paragraph("• Lemonade: AMD's llama.cpp + ROCm backend (github.com/winmutt/lemonade)", normal_style))
    body.append(Paragraph("• Ollama: Community llama.cpp wrapper (github.com/ollama/ollama)", normal_style))
    body.append(Paragraph("• ROCm: AMD's open compute platform (github.com/RadeonOpenCompute/ROCm)", normal_style))
    body.append(Paragraph("• ROCm Issue #5926: Memory management bugs (github.com/ROCm/ROCm/issues/5926)", normal_style))
    body.append(Paragraph("• WWS: github.com/winmutt/wws", normal_style))
    body.append(Paragraph("• Home Assistant Wake Words: github.com/fwartner/home-assistant-wakewords-collection", normal_style))
    body.append(Paragraph("• NUMA/CPU Pinning: Red Hat OpenStack docs (vcpu_pin_set, NUMATopologyFilter)", normal_style))
    body.append(Paragraph("  https://docs.redhat.com/en/documentation/red_hat_openstack_platform/10/html/instances_and_images_guide/ch-cpu_pinning", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Communities", subheading_style))
    body.append(Paragraph("• Reddit r/LocalLLaMA: 8 Local LLMs on Strix Halo", normal_style))
    body.append(Paragraph("• XDA Forums: Amazon Echo development", normal_style))
    body.append(Paragraph("• GitHub: winmutt (8 repos, forks of lemonade, cline, vscode)", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # Q&A
    # ============================================
    body.append(Spacer(1, 2*inch))
    body.append(Paragraph("Questions? (I Have Answers, Mostly)", title_style))
    body.append(Spacer(1, 1*inch))
    
    questions = [
        "1. Is Strix Halo production-ready? (It's complicated)",
        "2. When will NPU support mature? (Coming soon™)",
        "3. How do we solve 128GB addressing? (We don't)",
        "4. Best backend for multi-model? (Lemonade, but...",
        "5. Is autonomous dev the future? (Ask my AI)"
    ]
    
    for q in questions:
        body.append(Paragraph(f"  {q}", normal_style))
    
    body.append(Spacer(1, 1*inch))
    body.append(Paragraph("github.com/winmutt", subtitle_style))
    body.append(Paragraph("Come find me after - I'll show you the rig", humor_style))
    
    # Build PDF
    doc.build(body, onFirstPage=draw_black_background, onLaterPages=draw_black_background)
    print(f"PDF created successfully: {output_pdf}")

if __name__ == '__main__':
    create_pdf()
