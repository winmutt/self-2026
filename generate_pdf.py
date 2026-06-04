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
        fontSize=28,
        textColor=colors.HexColor('#ffffff'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
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
    body.append(Spacer(1, 2*inch))
    body.append(Paragraph("Building an AI Workstation", title_style))
    body.append(Paragraph("6 Months with AMD Strix Halo", subtitle_style))
    body.append(Spacer(1, 0.5*inch))
    body.append(Paragraph("A Journey from Hardware Hype to Real-World", normal_style))
    body.append(Paragraph("Autonomous Development", normal_style))
    body.append(Spacer(1, 1*inch))
    body.append(Paragraph("winmutt | May 2026", normal_style))
    body.append(Paragraph("github.com/winmutt", normal_style))
    body.append(PageBreak())
    
    # ============================================
    # AGENDA
    # ============================================
    body.append(Paragraph("Agenda (45 minutes)", heading_style))
    body.append(Spacer(1, 0.2*inch))
    
    agenda_items = [
        "1. The Decision (5 min) - Why AMD Strix Halo?",
        "2. Hardware Reality (7 min) - 128GB APU architecture",
        "3. Software Stack Evolution (8 min) - Lemonade, Ollama, ROCm",
        "4. Performance Deep Dive (7 min) - TPS, context windows, bottlenecks",
        "5. Project: WWS (6 min) - Vibe-coded workspace system",
        "6. Project: Home Assistant (5 min) - Alexa replacement on Echo",
        "7. Project: Concrete Signs (3 min) - From AI to physical objects",
        "8. Lessons Learned (4 min) - What worked, what didn't"
    ]
    
    for item in agenda_items:
        body.append(Paragraph(f"  • {item}", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    # GitHub activity image
    body.append(Paragraph("GitHub Activity: 10-Year History", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/github_activity_original.png', width=7*inch, height=2.5*inch)
        body.append(img)
    except:
        pass
    
    body.append(Spacer(1, 0.5*inch))
    body.append(Paragraph("The Catalyst Effect - Nov 2025: Strix Halo acquisition led to 3.5x contribution increase", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 1: THE DECISION
    # ============================================
    body.append(Paragraph("Part 1: The Decision", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Why AMD Strix Halo?", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>November 22, 2025</b><br/>"BTW I have a corsair 300 AMD 395 max+ enroute. '
        'Sold my 3060 rig today."', quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Your Original Setup", subheading_style))
    body.append(Paragraph("Generic home PC with RTX 3060 (12GB GDDR6 VRAM) + 128GB RAM", normal_style))
    body.append(Paragraph("Performance was poor across shared 6GB GDDR6 VRAM", normal_style))
    body.append(Paragraph("Decided to invest in 128GB RAM for APU upgrade", normal_style))
    body.append(Spacer(1, 0.3*inch))
    
    # Corsair AI Workstation render
    body.append(Paragraph("The Corsair AI Workstation 300", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/corsair_rig.png', width=7*inch, height=4*inch)
        body.append(img)
    except:
        pass
    
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph("Note: Corsair 300 shares motherboard with other Strix Halo manufacturers (Sixunited)", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    # Corsair price comparison
    body.append(Paragraph("Price Comparison", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/corsair_price.png', width=7*inch, height=5*inch)
        body.append(img)
    except:
        pass
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("CRSR Stock Performance", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/crsr_stock.png', width=7*inch, height=4*inch)
        body.append(img)
    except:
        pass
    
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
    body.append(Paragraph("Part 2: Hardware Reality", heading_style))
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
        ['(Only 96GB addressable)'],
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
    
    body.append(Paragraph("Key Challenge:", subheading_style))
    body.append(Paragraph("• 128GB total, only 96GB accessible initially", normal_style))
    body.append(Paragraph("• Memory placement: VRAM vs GTT issues", normal_style))
    body.append(Paragraph("• Swapping despite unified memory", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 2.5: AGENTS & MODELS
    # ============================================
    body.append(Paragraph("Agents & Models Configuration", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Current Models in Lemonade Config", subheading_style))
    body.append(Paragraph("• qwen3-8b-FLM", normal_style))
    body.append(Paragraph("• Qwen3.5-122B-A10B-GGUF", normal_style))
    body.append(Paragraph("• Qwen3.5-122B-A10B-MTP-GGUF", normal_style))
    body.append(Paragraph("• gpt-oss-120b-mxfp-GGUF", normal_style))
    body.append(Paragraph("• qwen3.5-4b-FLM", normal_style))
    body.append(Paragraph("• gemma3-4b-FLM", normal_style))
    body.append(Paragraph("• embed-gemma-300m-FLM", normal_style))
    body.append(Paragraph("• Qwen3-Coder-Next-GGUF", normal_style))
    body.append(Paragraph("• Flux-2-Klein-9B-GGUF", normal_style))
    body.append(Paragraph("• Qwen3-VL-8B-Instruct-GGUF", normal_style))
    body.append(Paragraph("• Qwen3.6-35B-A3B-MTP-GGUF (go-to today)", normal_style))
    body.append(Paragraph("• Whisper-Large-v3-Turbo", normal_style))
    body.append(Paragraph("• kokoro-v1", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Multi-Token Prediction (MTP) - Qwen3.6-35B-A3B", subheading_style))
    body.append(Paragraph("• MTP = Multi-Token Prediction capability", normal_style))
    body.append(Paragraph("• Qwen series models with MTP-GGUF files", normal_style))
    body.append(Paragraph("• Predicts multiple tokens in single forward pass", normal_style))
    body.append(Paragraph("• Significantly improves throughput and reduces latency", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    # Opencode screenshot
    body.append(Paragraph("Opencode - Preferred Agent UI", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/opencode_screenshot.png', width=7*inch, height=4*inch)
        body.append(img)
    except:
        pass
    
    body.append(Spacer(1, 0.3*inch))
    body.append(Paragraph("• Cline: Good for direct coding tasks", normal_style))
    body.append(Paragraph("• Opencode: Preferred for portable web UI experience", normal_style))
    body.append(Paragraph("• Opencode makes it portable for mobile/different locations", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 3: SOFTWARE STACK
    # ============================================
    body.append(Paragraph("Part 3: Software Stack Evolution", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Lemonade vs Ollama", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    # Comparison table
    data = [
        ['Feature', 'Lemonade', 'Ollama'],
        ['Backend', 'llama.cpp + ROCm', 'Various'],
        ['Observability', 'Good (token batching)', 'Poor'],
        ['NPU Support', 'In development', 'Patch available'],
        ['Stability', 'Issues after upgrade', 'GPU crashes'],
        ['Multi-model', 'Yes', 'Limited']
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
    body.append(Paragraph("The Resurgens Moment - Bleeding Edge Challenges", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>December 14, 2025</b><br/>"Upgraded OS and ollama last night and sad things happened. '
        'GPU crashes about 3-4 prompts in"', quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Bleeding Edge Challenges:", subheading_style))
    body.append(Paragraph("• Staying on near bleeding edge kernels required for APU support", normal_style))
    body.append(Paragraph("• AI-related apps (Lemonade, Ollama, llama.cpp) change rapidly", normal_style))
    body.append(Paragraph("• Frequent breaking changes and bugs requiring troubleshooting", normal_style))
    body.append(Paragraph("• Each update risks stability - need to balance features vs reliability", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Phoenix Rising: Fresh install → AMD GPU update (Jan 29) → 2x faster", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 4: PERFORMANCE
    # ============================================
    body.append(Paragraph("Part 4: Performance Deep Dive", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Token Processing Performance", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    perf_data = [
        ['Context Size', 'TPS', 'Notes'],
        ['<100k tokens', '~40', 'Consistent'],
        ['100k-200k', '~14-18', 'Degradation'],
        ['>200k tokens', '~8-18', 'Variable'],
        ['>64k (ingress)', 'N/A', 'Sharp TPS drop']
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
    
    body.append(Paragraph("May 30, 2026 - Recent ~200k Token Processing", subheading_style))
    body.append(Paragraph("Input tokens: 193,795 | Output tokens: 5,997 | TTFT: 2,267s (37.8 min) | TPS: 18.65", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    # Performance chart
    body.append(Paragraph("Performance Timeline", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/timeline.png', width=7*inch, height=3*inch)
        body.append(img)
    except:
        pass
    
    body.append(PageBreak())
    
    # ============================================
    # PART 5: WWS PROJECT
    # ============================================
    body.append(Paragraph("Part 5: Project WWS", heading_style))
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
    body.append(Paragraph("• Remote workspace provisioning system", normal_style))
    body.append(Paragraph("• KVM/Podman-based isolated environments", normal_style))
    body.append(Paragraph("• code-server (VSCode) integration", normal_style))
    body.append(Paragraph("• GitHub OAuth + RBAC", normal_style))
    body.append(Paragraph("• Team collaboration features", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    # WWS Dashboard screenshot
    body.append(Paragraph("WWS Dashboard", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/dashboard.png', width=7*inch, height=4*inch)
        body.append(img)
    except:
        pass
    
    body.append(PageBreak())
    
    # ============================================
    # PART 6: HOME ASSISTANT
    # ============================================
    body.append(Paragraph("Part 6: Home Assistant on Echo", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("LineageOS Installation Journey", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>December 2025</b><br/>Started exploring XDA Forums for Echo device hacking',
        normal_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Key Threads:", subheading_style))
    body.append(Paragraph(
        '• https://xdaforums.com/t/rom-unofficial-11-checkers-lineageos-18-1-for-the-amazon-echo-show-5-2019.4763475/',
        normal_style
    ))
    body.append(Paragraph(
        '• https://xdaforums.com/t/unlock-root-twrp-unbrick-amazon-echo-show-5-1st-gen-2019-checkers.4762900/',
        normal_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Process:", subheading_style))
    body.append(Paragraph("1. Unlock bootloader via amonet exploit", normal_style))
    body.append(Paragraph("2. Create stock backup (critical!)", normal_style))
    body.append(Paragraph("3. Install TWRP recovery", normal_style))
    body.append(Paragraph("4. Flash LineageOS 18.1 (Android 11)", normal_style))
    body.append(Paragraph("5. Configure ViewAssist for Home Assistant", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Quote", subheading_style))
    body.append(Paragraph('"Basically anything with a USB port. If there is a port, there is a way."', quote_style))
    
    body.append(PageBreak())
    
    body.append(Paragraph("Alexa Replacement Journey", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        '<b>December 6, 2025</b><br/>"Basically anything with a USB port. '
        'If there is a port, there is a way."', quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    timeline_data = [
        ['Dec 6', 'Started exploring XDA forums'],
        ['Dec 7', 'Started using Home Assistant on Echo devices'],
        ['Jan 19', 'HA setup on Echo Show Gen 2'],
        ['Jan 21', 'Everything working except wake word'],
        ['Jan 25', 'Wake word sorted with Hey Jarvis'],
        ['Jan 29', 'End-to-end complete'],
        ['Feb 2026', 'Echo 8 mic stability testing (ongoing)'],
        ['Jan 7, 2026', 'Issue #4 filed - Echo 8 audio stops after ~24h']
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
    
    # Home Assistant screenshot
    body.append(Paragraph("Home Assistant on Echo Show", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/ha.jpeg', width=5*inch, height=4*inch)
        body.append(img)
    except:
        pass
    
    body.append(PageBreak())
    
    # Echo 8 mic issue
    body.append(Paragraph("The Echo 8 Mic Stability Issue", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Issue #4: Audio stops working after ~24 hours", subheading_style))
    body.append(Spacer(1, 0.2*inch))
    
    body.append(Paragraph(
        '<b>Reported</b><br/>January 7, 2026<br/>'
        '<b>Repository</b><br/>https://github.com/amazon-oss/releases<br/>'
        '<b>Status</b><br/>Open - awaiting fix',
        normal_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("User Report (lawhazl)", subheading_style))
    body.append(Paragraph(
        '"I\'ve got the Echo 8 and Echo 5, both loaded up with their latest respective '
        'LineageOS 18.1 installs. The mic on the Echo 5 and 8 is stable and will constantly '
        'listen without issue for days at a time without a reboot. However, the Echo 8 '
        'seems to exhibit the audio issue that the Echo 5 originally had until that was '
        'fixed in a later build."',
        quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Technical Context", subheading_style))
    body.append(Paragraph("• Devices: Echo Show 5 (checkers), Echo Show 8 (crown)", normal_style))
    body.append(Paragraph("• ROM: LineageOS 18.1 (v0.5 for Echo 8)", normal_style))
    body.append(Paragraph("• Usage: Home Assistant with ViewAssist for STT/TTS", normal_style))
    body.append(Paragraph("• Network: 2.4 GHz-only IoT network", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Echo 5 Fix Reference", subheading_style))
    body.append(Paragraph(
        '<b>Build 3</b> (Oct 25, 2025): "Included microphone fix in the build"<br/>'
        '<b>Status</b>: Mic stable on Echo 5, issue persists on Echo 8',
        normal_style
    ))
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph(
        '"With my Echos, I don\'t let them sleep ever. ViewAssist puts a nighttime '
        'image on the screen, but the screen is always on when this behaviour happens. '
        'It usually takes a day or so before it starts happening on the echo 8."',
        quote_style
    ))
    
    body.append(PageBreak())
    
    # ============================================
    # PART 7: CONCRETE SIGNS
    # ============================================
    body.append(Paragraph("Part 7: Concrete Sign Molds", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("From AI to Physical Objects", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        '<b>December 1, 2025</b><br/>"I am going to use it to create a 3d printed cast '
        'for a silicone mold so I can some desktop signs out of concrete."', quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Motivation", subheading_style))
    body.append(Paragraph(
        '"For my PE, she\'s always belaboring the need to get concrete and not speak in abstract."',
        quote_style
    ))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Files and Models", subheading_style))
    body.append(Paragraph("Location: /opt/opencode/src/concrete/sign-molds/", normal_style))
    body.append(Paragraph("• example_sign_mold.scad - Mold for raised cursive 'example'", normal_style))
    body.append(Paragraph("• use_case_sign_mold.scad - Mold for embossed 'use case'", normal_style))
    body.append(Paragraph("• generate.py - Automated STL export script", normal_style))
    
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Process", subheading_style))
    body.append(Paragraph("1. AI generates OpenSCAD design", normal_style))
    body.append(Paragraph("2. Export to STL", normal_style))
    body.append(Paragraph("3. 3D print mold (PETG/ABS)", normal_style))
    body.append(Paragraph("4. Create silicone mold", normal_style))
    body.append(Paragraph("5. Cast concrete", normal_style))
    body.append(Paragraph("6. Finish and potentially sell on Etsy", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("Concrete Sign Mold Design", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/concrete_sign.png', width=6*inch, height=4*inch)
        body.append(img)
    except:
        pass
    
    body.append(PageBreak())
    
    # ============================================
    # PART 8: LESSONS LEARNED
    # ============================================
    body.append(Paragraph("Part 8: Lessons Learned", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("What Worked ✓", subheading_style))
    body.append(Paragraph("• Cline + Qwen3-Coder: Making great results", normal_style))
    body.append(Paragraph("• Prompt Caching: Things are really humming", normal_style))
    body.append(Paragraph("• AMD GPU Libraries: 2x performance improvement", normal_style))
    body.append(Paragraph("• Home Assistant: Fully functional on Echo", normal_style))
    body.append(Paragraph("• WWS Project: Months of development complete", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("What Didn't ✗", subheading_style))
    body.append(Paragraph("• Memory Addressing: Never got full 128GB (only 96GB)", normal_style))
    body.append(Paragraph("• Ollama Stability: GPU crashes after upgrades", normal_style))
    body.append(Paragraph("• NPU Support: Still in development", normal_style))
    body.append(Paragraph("• Context Scaling: Sharp TPS decline >64k", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # KEY INSIGHTS
    # ============================================
    body.append(Paragraph("Key Insights", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    insights = [
        "1. Hardware Hype vs Reality: APU architecture challenges are real",
        "2. Software Maturity: Latest kernel + ROCm essential",
        "3. Context is King: Prompt caching transforms workflow",
        "4. Tooling Evolution: Cline + Qwen3-Coder > traditional IDEs",
        "5. From Digital to Physical: AI can create real-world objects",
        "6. Repurposing Hardware: Echo → Home Assistant = Win",
        "7. Autonomous Development: Possible, but requires tuning",
        "8. Bleeding Edge Tradeoff: Stability vs features"
    ]
    
    for insight in insights:
        body.append(Paragraph(f"  {insight}", normal_style))
    
    body.append(Spacer(1, 1*inch))
    
    # Catalyst diagram
    body.append(Paragraph("AMD Strix Halo: Catalyst for OSS Reinvigoration", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/catalyst_diagram.png', width=7*inch, height=5*inch)
        body.append(img)
    except:
        pass
    
    body.append(PageBreak())
    
    # ============================================
    # OSS CONTRIBUTION GROWTH
    # ============================================
    body.append(Paragraph("Open Source Reinvigoration", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("The Catalyst Effect", subheading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph(
        "The AMD Strix Halo acquisition in November 2025 marked a turning point. "
        "Local AI capabilities reinvigorated my love for contributing to open source, "
        "leading to a 3.5x increase in contributions compared to previous years.",
        normal_style
    ))
    
    body.append(Spacer(1, 0.5*inch))
    
    # Contribution calendar
    body.append(Paragraph("2026 Contribution Calendar", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/contribution_calendar_2026.png', width=7*inch, height=3*inch)
        body.append(img)
    except:
        pass
    
    body.append(Spacer(1, 0.5*inch))
    
    # Project breakdown
    body.append(Paragraph("Project Contributions (Nov 2025 - Jun 2026)", subheading_style))
    try:
        img = Image('/opt/opencode/src/self-2026/assets/project_breakdown.png', width=7*inch, height=4*inch)
        body.append(img)
    except:
        pass
    
    body.append(PageBreak())
    
    # ============================================
    # FUTURE WORK
    # ============================================
    body.append(Paragraph("Future Work", heading_style))
    body.append(Spacer(1, 0.3*inch))
    
    body.append(Paragraph("Immediate", subheading_style))
    body.append(Paragraph("• NPU support stabilization", normal_style))
    body.append(Paragraph("• Memory addressing optimization", normal_style))
    body.append(Paragraph("• Core affinity management (llama.cpp PR)", normal_style))
    
    body.append(Spacer(1, 0.5*inch))
    
    body.append(Paragraph("Long-term", subheading_style))
    body.append(Paragraph("• Multi-GPU/NPU orchestration", normal_style))
    body.append(Paragraph("• Better observability for Ollama", normal_style))
    body.append(Paragraph("• Custom wake word training", normal_style))
    body.append(Paragraph("• WWS Phase 3 (Cloud providers)", normal_style))
    
    body.append(PageBreak())
    
    # ============================================
    # Q&A
    # ============================================
    body.append(Spacer(1, 2*inch))
    body.append(Paragraph("Questions?", title_style))
    body.append(Spacer(1, 1*inch))
    
    questions = [
        "1. Is Strix Halo ready for production AI workloads?",
        "2. When will NPU support mature?",
        "3. How do we solve the 128GB addressing issue?",
        "4. What's the best backend for multi-model setups?",
        "5. Is autonomous development the future?"
    ]
    
    for q in questions:
        body.append(Paragraph(f"  {q}", normal_style))
    
    body.append(Spacer(1, 1*inch))
    body.append(Paragraph("Contact: github.com/winmutt", subtitle_style))
    
    # Build PDF
    doc.build(body, onFirstPage=draw_black_background, onLaterPages=draw_black_background)
    print(f"PDF created successfully: {output_pdf}")

if __name__ == '__main__':
    create_pdf()
