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
    body.append(Paragraph("How I Bought an AI Computer", title_style))
    body.append(Paragraph("And Accidentally Became an Open Source Maintainer Again", subtitle_style))
    body.append(Spacer(1, 0.5*inch))
    body.append(Paragraph("A Six Month Review of My Strix Halo Rig", normal_style))
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph("linux | ROCm | Local AI | Home Assistant | Coding", humor_style))
    body.append(Spacer(1, 1.5*inch))
    body.append(Paragraph("winmutt | June 2026", normal_style))
    body.append(Paragraph("github.com/winmutt", normal_style))
    body.append(PageBreak())
    
    # ============================================
    # AGENDA
    # ============================================
    body.append(Paragraph("What We're Covering", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    agenda_items = [
        "🛒 The impulse purchase that changed everything",
        "🖥️ Hardware reality check (spoiler: it's complicated)",
        "🐧 Linux + ROCm = Pain (but beautiful pain)",
        "⚡ Performance: How fast can my AI think?",
        "🏠 I cut the Alexa cord (and replaced it with OSS)",
        "💻 Vibe-coded an entire workspace system",
        "🧊 From digital to physical: Concrete signs?",
        "📈 How buying hardware got me back in open source",
        "🤔 What I'd do differently (and what I'd do again)"
    ]
    
    for item in agenda_items:
        body.append(Paragraph(f"  {item}", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # GitHub activity image (on new page)
    body.append(Paragraph("The 10-Year GitHub Glow-Up", heading_style))
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph("Before Strix Halo: Ghost in the machine", humor_style))
    body.append(Spacer(1, 0.3*inch))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/github_activity_original.png', 7*inch, 3*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.5*inch))
    body.append(Paragraph("November 2025: Bought a Strix Halo rig", normal_style))
    body.append(Paragraph("Result: 3.5x increase in open source contributions", normal_style))
    body.append(Paragraph("Moral of the story: Hardware buys you time (and motivation)", humor_style))
    
    body.append(PageBreak())
    
    body.append(PageBreak())
    
    # ============================================
    # PART 1: THE DECISION
    # ============================================
    body.append(Paragraph("The Impulse Purchase", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Why AMD Strix Halo?", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>November 22, 2025</b><br/>"BTW I have a corsair 300 AMD 395 max+ enroute. '
        'Sold my 3060 rig today."', quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Before: RTX 3060 with 12GB VRAM", normal_style))
    body.append(Paragraph("After: 128GB LPDDR5X-8000 unified memory", normal_style))
    body.append(Paragraph("Translation: My AI stopped choking on context", humor_style))
    
    body.append(Spacer(1, 0.3*inch))
    body.append(PageBreak())
    
    # Corsair AI Workstation render
    body.append(Paragraph("Meet My New Overlord", subheading_style))
    body.append(Paragraph("Corsair AI Workstation 300", humor_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/corsair_rig.png', 7*inch, 5*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph("Note: Corsair 300 shares motherboard with other Strix Halo manufacturers (Sixunited)", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    body.append(PageBreak())
    
    # Corsair price comparison
    body.append(Paragraph("The Price Tag That Made My Wallet Cry", subheading_style))
    body.append(Paragraph("Black Friday 2025: $1,800", humor_style))
    body.append(Paragraph("Today's equivalent: ~$2,700", humor_style))
    body.append(Paragraph("TL;DR: I got a good deal (mostly)", normal_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/corsair_price.png', 7*inch, 6*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.3*inch))
    body.append(PageBreak())
    
    body.append(Paragraph("CRSR Stock: Because Why Not?", subheading_style))
    body.append(Paragraph("My investment strategy: Buy hardware, watch stock", humor_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/crsr_stock.png', 7*inch, 4*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Pitch:", subheading_style))
    body.append(Paragraph("• 128GB unified memory (LPDDR5X-8000)", normal_style))
    body.append(Paragraph("• Fastest 'nom' VRAM available", normal_style))
    body.append(Paragraph("• NPU for AI acceleration", normal_style))
    body.append(Paragraph("• No discrete GPU needed", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 2: HARDWARE REALITY
    # ============================================
    body.append(Paragraph("Hardware Reality: It's Complicated", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("AMD Strix Halo Architecture", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    # Architecture diagram as table
    arch_data = [
        ['AMD Strix Halo APU'],
        ['┌─────────────┐  ┌─────────────┐'],
        ['│ Core Die 1  │  │ Core Die 2  │'],
        ['│ 64MB L3     │  │ 64MB L3     │'],
        ['└─────────────┘  └─────────────┘'],
        ['128GB LPDDR5X-8000 (soldered)'],
        ['(Only 96GB addressable - RIP 32GB)'],
        ['GPU | NPU | Media Engine']
    ]
    
    arch_table = Table(arch_data, colWidths=[5*inch])
    arch_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Courier'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#e0e0e0')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#444444')),
    ]))
    body.append(arch_table)
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("The Plot Thickens:", subheading_style))
    body.append(Paragraph("• 128GB total, only 96GB accessible", normal_style))
    body.append(Paragraph("• Memory placement: VRAM vs GTT drama", normal_style))
    body.append(Paragraph("• Swapping happens anyway (thanks unified memory!)", humor_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 2.5: AGENTS & MODELS
    # ============================================
    body.append(Paragraph("My AI Menagerie", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Models in Rotation", subheading_style))
    body.append(Paragraph("• Qwen3.6-35B-A3B-MTP-GGUF (the daily driver)", normal_style))
    body.append(Paragraph("• Qwen3.5-122B (when I want to wait 40 minutes)", humor_style))
    body.append(Paragraph("• gpt-oss-120b (for variety)", normal_style))
    body.append(Paragraph("• Qwen3-Coder-Next (my coding co-pilot)", normal_style))
    body.append(Paragraph("• Flux-2-Klein-9B (for art, apparently)", normal_style))
    body.append(Paragraph("• Whisper-Large-v3-Turbo (because typing is hard)", normal_style))
    body.append(Paragraph("• Plus 8 more I forgot about", humor_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Multi-Token Prediction (MTP)", subheading_style))
    body.append(Paragraph("• MTP = Multi-Token Prediction (not Mixed Tensor Precision!)", humor_style))
    body.append(Paragraph("• Predicts multiple tokens at once", normal_style))
    body.append(Paragraph("• Translation: My AI thinks faster", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    body.append(PageBreak())
    
    # Opencode screenshot
    body.append(Paragraph("Opencode: The Portable Web UI I Actually Use", subheading_style))
    body.append(Paragraph("Cline is good for direct coding", normal_style))
    body.append(Paragraph("Opencode is portable (I can code from my couch)", humor_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/opencode_screenshot.png', 7*inch, 4*inch)
    if img:
        body.append(img)
    
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph("• Cline: Good for direct coding tasks", normal_style))
    body.append(Paragraph("• Opencode: Preferred for portable web UI experience", normal_style))
    body.append(Paragraph("• Opencode makes it portable for mobile/different locations", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 3: SOFTWARE STACK
    # ============================================
    body.append(Paragraph("The Software Stack: A Love-Hate Relationship", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Lemonade vs Ollama", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    # Comparison table
    data = [
        ['Feature', 'Lemonade', 'Ollama'],
        ['Backend', 'llama.cpp + ROCm', 'Various'],
        ['Observability', 'Good (I can see tokens)', normal_style],
        ['NPU Support', 'Coming soon™', 'Patch exists'],
        ['Stability', 'Breaks after updates', 'GPU crashes'],
        ['Multi-model', 'Yes', 'Good luck']
    ]
    
    table = Table(data, colWidths=[2*inch, 2.5*inch, 2.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2a2a2a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#58a6ff')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#1a1a1a')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#e0e0e0')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#444444')),
    ]))
    body.append(table)
    
    body.append(Spacer(1, 0.3*inch))
    
    # Resurgens section
    body.append(Paragraph("The Resurgens Moment", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>December 14, 2025</b><br/>"Upgraded OS and ollama last night and sad things happened. '
        'GPU crashes about 3-4 prompts in"', quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Bleeding Edge = Cutting My Finger", subheading_style))
    body.append(Paragraph("• Near-bleeding edge kernels for APU support", normal_style))
    body.append(Paragraph("• AI apps change faster than I can debug", normal_style))
    body.append(Paragraph("• Each update = new drama", humor_style))
    body.append(Paragraph("• Stability vs features: pick your poison", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Phoenix Rising: Fresh install → AMD GPU update → 2x faster", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 4: PERFORMANCE
    # ============================================
    body.append(Paragraph("Performance: How Fast Does My AI Think?", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Token Processing Reality", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    perf_data = [
        ['Context Size', 'TPS', 'Notes'],
        ['<100k tokens', '~40', 'Actually usable'],
        ['100k-200k', '~14-18', 'I have time to get coffee'],
        ['>200k tokens', '~8-18', 'Go read a book'],
        ['>64k (ingress)', 'N/A', 'My AI needs a nap']
    ]
    
    perf_table = Table(perf_data, colWidths=[2*inch, 1.5*inch, 2.5*inch])
    perf_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2a2a2a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#58a6ff')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#1a1a1a')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#e0e0e0')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#444444')),
    ]))
    body.append(perf_table)
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("May 30, 2026 - 200k Token Processing", subheading_style))
    body.append(Paragraph("Input: 193,795 | Output: 5,997 | TTFT: 37.8 min | TPS: 18.65", normal_style))
    body.append(Paragraph("Translation: I made dinner while waiting", humor_style))
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # Performance chart
    body.append(Paragraph("Performance Timeline", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/timeline.png', 7*inch, 3.5*inch)
    if img:
        body.append(img)
    
    body.append(PageBreak())
    
    # ============================================
    # PART 5: WWS PROJECT
    # ============================================
    body.append(Paragraph("Project WWS: I Vibe-Coded an Entire System", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Winmutt Work Spaces", subheading_style))
    body.append(Paragraph("github.com/winmutt/wws", normal_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        '<b>May 12, 2026</b><br/>"Definitely no Athena and its taken months '
        'to get there but this is something I entirely vibe coded."', quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("What is WWS?", subheading_style))
    body.append(Paragraph("• Remote workspace provisioning", normal_style))
    body.append(Paragraph("• KVM/Podman isolated environments", normal_style))
    body.append(Paragraph("• code-server (VSCode in browser)", normal_style))
    body.append(Paragraph("• GitHub OAuth + RBAC", normal_style))
    body.append(Paragraph("• Months of work, zero Athena", humor_style))
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    # WWS Dashboard screenshot
    body.append(Paragraph("WWS Dashboard", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/dashboard.png', 7*inch, 4*inch)
    if img:
        body.append(img)
    
    body.append(PageBreak())
    
    # ============================================
    # PART 6: HOME ASSISTANT
    # ============================================
    body.append(Paragraph("Cutting the Alexa Cord", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("LineageOS on Echo: Because I Said So", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>December 2025</b><br/>Started exploring XDA Forums for Echo device hacking',
        normal_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Process:", subheading_style))
    body.append(Paragraph("1. Unlock bootloader via amonet exploit", normal_style))
    body.append(Paragraph("2. Create stock backup (don't skip this!)", humor_style))
    body.append(Paragraph("3. Install TWRP recovery", normal_style))
    body.append(Paragraph("4. Flash LineageOS 18.1 (Android 11)", normal_style))
    body.append(Paragraph("5. Configure ViewAssist for Home Assistant", normal_style))
    
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
    
    # Home Assistant screenshot
    body.append(Paragraph("Home Assistant on Echo Show", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/ha.jpeg', 5*inch, 4*inch)
    if img:
        body.append(img)
    
    body.append(PageBreak())
    
    # Echo 8 mic issue
    body.append(Paragraph("Issue #4: The Echo 8 Mic That Quit", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Audio stops working after ~24 hours", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>Filed</b><br/>January 7, 2026<br/>'
        '<b>Repository</b><br/>https://github.com/amazon-oss/releases<br/>'
        '<b>Status</b><br/>Open (still waiting, it\'s fine)',
        normal_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Problem", subheading_style))
    body.append(Paragraph("• Echo 5: Stable for days", normal_style))
    body.append(Paragraph("• Echo 8: Dies after ~24 hours", normal_style))
    body.append(Paragraph("• Root cause: Unknown (yet)", humor_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        '<b>TL;DR</b><br/>I participate in open source bugs now. You\'re welcome.',
        humor_style
    ))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 7: CONCRETE SIGNS
    # ============================================
    body.append(Paragraph("From AI to Concrete: My PE's Worst Nightmare", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Motivation", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>December 1, 2025</b><br/>"I am going to use it to create a 3d printed cast '
        'for a silicone mold so I can some desktop signs out of concrete."', quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        '"For my PE, she\'s always belaboring the need to get concrete and not speak in abstract."',
        quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Process", subheading_style))
    body.append(Paragraph("1. AI generates OpenSCAD design", normal_style))
    body.append(Paragraph("2. Export to STL", normal_style))
    body.append(Paragraph("3. 3D print mold", normal_style))
    body.append(Paragraph("4. Create silicone mold", normal_style))
    body.append(Paragraph("5. Cast concrete", normal_style))
    body.append(Paragraph("6. Sell on Etsy (eventually)", humor_style))
    
    body.append(Spacer(1, 0.5*inch))
    body.append(PageBreak())
    
    body.append(Paragraph("Concrete Sign Mold Design", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/concrete_sign.png', 6*inch, 6*inch)
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
    body.append(Paragraph("• Home Assistant: Alexa is dead, long live OSS", normal_style))
    body.append(Paragraph("• WWS Project: Months of vibe-coding complete", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("What Didn't ✗", subheading_style))
    body.append(Paragraph("• Memory: 32GB disappeared forever", normal_style))
    body.append(Paragraph("• Ollama: Still crashes after updates", normal_style))
    body.append(Paragraph("• NPU: Coming soon™ (always)", normal_style))
    body.append(Paragraph("• Context >64k: TPS drops like a stone", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # KEY INSIGHTS
    # ============================================
    body.append(Paragraph("Key Insights (Take What You Want)", heading_style))
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
    
    body.append(Spacer(1, 1*inch))
    
    # Catalyst diagram
    body.append(Paragraph("The Catalyst Effect", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/catalyst_diagram.png', 7*inch, 6*inch)
    if img:
        body.append(img)
    
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
    body.append(PageBreak())
    
    # Project breakdown
    body.append(Paragraph("Project Contributions (Nov 2025 - Jun 2026)", subheading_style))
    img = get_scaled_image('/opt/opencode/src/self-2026/assets/project_breakdown.png', 7*inch, 5*inch)
    if img:
        body.append(img)
    
    body.append(PageBreak())
    
    # ============================================
    # FUTURE WORK
    # ============================================
    body.append(Paragraph("What's Next (Probably)", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Immediate", subheading_style))
    body.append(Paragraph("• NPU support (still waiting)", normal_style))
    body.append(Paragraph("• Memory addressing (32GB, come back)", normal_style))
    body.append(Paragraph("• llama.cpp PRs (because why not)", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("Long-term", subheading_style))
    body.append(Paragraph("• Multi-GPU/NPU (more toys)", normal_style))
    body.append(Paragraph("• Ollama observability (I need logs)", normal_style))
    body.append(Paragraph("• Custom wake word (goodbye Alexa)", normal_style))
    body.append(Paragraph("• WWS Phase 3 (cloud? maybe)", normal_style))
    
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
