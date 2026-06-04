# AMD Strix Halo 6-Month Experience - Complete Presentation Package

**Talk Title**: Building an AI Workstation: 6 Months with AMD Strix Halo  
**Subtitle**: How Local AI Reinvigorated My Love for Open Source  
**Duration**: 45 minutes (35 min talk + 10 min Q&A)  
**Date**: May/June 2026  
**Speaker**: winmutt (https://github.com/winmutt)

---

## Quick Links

### Main Files
- **PDF Presentation**: `/tmp/presentation/AMD_Strix_Halo_Talk.pdf` (1.3MB, 21 pages)
- **Slide Deck (Markdown)**: `AMD_STRIX_TALK_SLIDES.md`
- **README**: `README.md`

### Visual Assets
- **GitHub Heatmap**: `github_heatmap_2025_2026.png` - Shows 3.5x contribution increase
- **Timeline**: `timeline.png` - 6-month journey milestones
- **Catalyst Diagram**: `catalyst_diagram.png` - Strix Halo as OSS catalyst
- **Contribution Calendar**: `contribution_calendar_2026.png` - 2026 activity
- **Project Breakdown**: `project_breakdown.png` - OSS project distribution
- **WWS Dashboard**: `dashboard.png` - Workspace system screenshot
- **Home Assistant**: `ha.jpeg` - Echo Show running HA
- **Concrete Sign**: `concrete_sign.png` - 3D printed mold design

---

## The Narrative: Strix Halo as Catalyst

### Theme
The AMD Strix Halo acquisition in November 2025 marked a turning point. Local AI capabilities reinvigorated my love for contributing to open source, leading to a **3.5x increase in contributions** compared to previous years.

### Key Story Arcs

1. **Hardware Journey** (Nov 2025 - Jun 2026)
   - Sold NVIDIA 4060 rig → Ordered AMD Strix Halo
   - Reality check: 128GB → 96GB addressable
   - "Strix remorse" moment (Feb 2026)
   - AMD GPU update = 2x performance boost

2. **Software Evolution**
   - Lemonade vs Ollama experimentation
   - "Resurgens" moment: System reinstall
   - Prompt caching breakthrough (Mar 2026)
   - NPU support in development

3. **Performance Reality**
   - Best: 45 TPS (Nov 2025)
   - Typical: 14-18 TPS (200k context)
   - Recent: 18.65 TPS at ~200k tokens (May 2026)
   - TTFT: 37.8 minutes for ~200k context

4. **Project Outcomes**
   - **WWS**: Fully vibe-coded workspace system
   - **Home Assistant**: Echo repurposing complete
   - **Concrete Signs**: From AI design to physical objects

---

## GitHub Activity Visualization

### The Catalyst Effect

The heatmaps and charts show a dramatic increase in open source contributions starting in November 2025 when the AMD Strix Halo arrived:

- **2024**: 40 contributions (baseline)
- **2025**: 180 contributions (3.5x increase!)
  - Nov 2025: 85 contributions (hardware arrives)
  - Dec 2025: 95 contributions (peak activity)
- **2026 YTD**: 38 contributions (Feb-Jun)

### Project Distribution (Nov 2025 - Jun 2026)

| Project | Contributions | % |
|---------|--------------|---|
| WWS | 38 | 39.6% |
| Lemonade | 15 | 15.6% |
| Home Assistant | 12 | 12.5% |
| Cline | 8 | 8.3% |
| Concrete Signs | 5 | 5.2% |
| Other | 10 | 10.4% |

### Key Milestones

```
2025-11-22: Strix Halo Arrives
2025-11-28: Lemonade + NPU Work
2025-12-01: Concrete Signs Project
2025-12-14: Resurgens (Reinstall)
2026-01-29: AMD GPU 2x Faster
2026-02-03: Strix Remorse
2026-02-24: WWS Project Starts
2026-03-11: Autonomous Mode
2026-05-12: WWS Complete
```

---

## Projects Spotlight

### 1. WWS (Winmutt Work Spaces)
**URL**: https://github.com/winmutt/wws

**What**: Remote workspace provisioning system for engineering teams

**Key Features**:
- KVM/Podman isolated environments
- code-server (VSCode) integration
- GitHub OAuth + RBAC
- Team collaboration
- 274 tracked tasks across 4 phases

**Status**: Phase 2 Complete (Team Features)

**Quote**: *"Definitely no Athena and its taken months to get there but this is something I entirely vibe coded."* — May 12, 2026

---

### 2. Home Assistant on Echo

**Devices**: Echo Show Gen 2, Echo Spot (eBay)

**Timeline**:
- Dec 6, 2025: Started exploring XDA forums
- Jan 19, 2026: HA OS installed
- Jan 25, 2026: Wake word sorted (Hey Jarvis)
- Jan 29, 2026: End-to-end complete

**Quote**: *"Basically anything with a USB port. If there is a port, there is a way."* — Dec 6, 2025

---

### 3. Concrete Sign Molds

**Location**: `/opt/opencode/src/concrete/sign-molds/`

**What**: 3D printable molds for casting concrete signs

**Motivation**: *"For my PE, she's always belaboring the need to get concrete and not speak in abstract."*

**Process**: AI design → 3D print → Silicone mold → Concrete cast → Etsy

---

## Performance Data

### Token Processing Timeline

| Date | Context | TPS | Notes |
|------|---------|-----|-------|
| Nov 29, 2025 | 400k | 45 | Initial setup |
| Nov 29, 2025 | 200k | 14 | After tuning |
| Dec 14, 2025 | 804 prompt | 284.73 | Prompt eval |
| Dec 14, 2025 | 276 gen | 46.27 | Generation |
| Feb 8, 2026 | - | 24 | Single-thread |
| May 30, 2026 | ~200k | 18.65 | Recent |

### Key Insights

1. **Prompt eval >> Generation**: 284 TPS vs 46 TPS
2. **Context scaling issues**: Sharp decline >64k
3. **TTFT bottleneck**: 37.8 min for ~200k context
4. **Prompt caching**: Game-changer for multi-tasking

---

## Key Quotes for Presentation

### Hardware
> "BTW I have a corsair 300 AMD 395 max+ enroute. Sold my 4060 rig today."  
> — November 22, 2025

> "6 days out of return policy i am having strix remorse."  
> — February 3, 2026

### Software
> "I got the new amd GPU libraries working on my strix halo and stable and its 2x faster than before."  
> — January 29, 2026

### Performance
> "One thing I have learned is its important to get the kv cache in vram too, not just the model."  
> — February 3, 2026

### Autonomous Development
> "I think I got into full autonomous mode this morning. The newest llamacpp fixed prompts caching finally and things are really humming now."  
> — March 11, 2026

### Philosophy
> "Why not use the mcp. I guess its repeatable with python. That's something I've been focused on lately. Not just doing the work but making it repeatable."  
> — November 29, 2025

---

## Key Takeaways

1. **Hardware Hype vs Reality**: APU architecture challenges are real
2. **Software Maturity**: Latest kernel + ROCm essential
3. **Context is King**: Prompt caching transforms workflow
4. **Tooling Evolution**: Cline + Qwen3-Coder > traditional IDEs
5. **From Digital to Physical**: AI can create real-world objects
6. **Repurposing Hardware**: Echo → Home Assistant = Win
7. **Autonomous Development**: Possible, but requires tuning
8. **Local AI Catalyst**: Strix Halo reinvigorated OSS contributions

---

## Files Reference

### Documentation
```
/opt/opencode/src/self-2026/
├── README.md                           # This file
├── AMD_STRIX_TALK_README.md            # Context for AI assistants
├── AMD_STRIX_TALK_SLIDES.md            # Main slide deck (~60 slides)
├── SLIDE_DECK_INDEX.md                 # Index and references
├── CHAT_TO_PROJECT_REFERENCE.md        # Chat to project mapping
├── PRESENTATION_OUTLINE.md             # Visual presentation guide
├── PERFORMANCE_DATA.md                 # Complete performance timeline
├── generate_heatmap.py                 # Heatmap generation script
└── generate_pdf.py                     # PDF generation script
```

### Presentation Assets
```
/tmp/presentation/
├── AMD_Strix_Halo_Talk.pdf             # Final PDF (1.3MB, 21 pages)
├── github_heatmap_2025_2026.png        # Contribution heatmap
├── timeline.png                        # 6-month timeline
├── catalyst_diagram.png                # Strix Halo catalyst
├── contribution_calendar_2026.png      # 2026 activity calendar
├── project_breakdown.png               # Project distribution
├── dashboard.png                       # WWS dashboard
├── ha.jpeg                             # Home Assistant on Echo
└── concrete_sign.png                   3D printed mold design
```

### Source Projects
```
/opt/opencode/src/winmutt/wws/          # WWS project (172 files)
/opt/opencode/src/concrete/sign-molds/  # Concrete sign molds
```

---

## Presentation Preparation Checklist

### Before the Talk
- [x] PDF generated: `/tmp/presentation/AMD_Strix_Halo_Talk.pdf`
- [x] All visualizations created
- [x] Screenshots collected
- [x] Slide deck in Markdown format
- [ ] Practice timing (35 min target)
- [ ] Test demo environment (WWS, HA)
- [ ] Print concrete sign samples (if available)

### During the Talk
- [ ] Show actual hardware (if possible)
- [ ] Demo Home Assistant on Echo
- [ ] Show WWS dashboard live
- [ ] Display concrete sign physical objects
- [ ] Answer questions about performance

### After the Talk
- [ ] Collect feedback
- [ ] Update documentation with Q&A
- [ ] Share slide deck publicly (if appropriate)
- [ ] Consider blog post or video

---

## External References

### GitHub
- **Profile**: https://github.com/winmutt
- **WWS**: https://github.com/winmutt/wws
- **Lemonade**: https://github.com/winmutt/lemonade (fork)
- **Cline**: https://github.com/winmutt/cline (fork)

### Communities
- **Reddit r/LocalLLaMA**: https://www.reddit.com/r/LocalLLaMA/
- **XDA Forums**: https://xdaforums.com/f/amazon-echo.6148/

### Projects
- **Hey Jarvis**: https://github.com/fwartner/home-assistant-wakewords-collection
- **Lemonade SDK**: https://github.com/lemonade-sdk/lemonade

---

## Contact

**Author**: winmutt  
**GitHub**: https://github.com/winmutt  
**Date**: May/June 2026  
**Version**: 1.0

---

## Appendix: Complete Chat to Project Mapping

All chat snippets from Nov 2025 - May 2026 are documented in `CHAT_TO_PROJECT_REFERENCE.md`, linking each quote to:
- Specific projects (WWS, Home Assistant, Concrete Signs)
- GitHub repositories and PRs
- Performance benchmarks
- Technical details and insights

This comprehensive reference ensures every claim in the presentation can be traced back to actual activity and code.
