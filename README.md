# AMD Strix Halo 6-Month Experience - Complete Project Summary

**Talk**: Building an AI Workstation: 6 Months with AMD Strix Halo  
**Duration**: 45 minutes  
**Date**: May 2026  
**Author**: winmutt (https://github.com/winmutt)

---

## Document Index

### Core Documents
1. **AMD_STRIX_TALK_README.md** - Context for AI assistants
2. **AMD_STRIX_TALK_SLIDES.md** - Main slide deck (~60 slides)
3. **SLIDE_DECK_INDEX.md** - Slide deck index and references
4. **CHAT_TO_PROJECT_REFERENCE.md** - Chat snippets mapped to projects
5. **PRESENTATION_OUTLINE.md** - Visual presentation outline
6. **PERFORMANCE_DATA.md** - Complete performance timeline
7. **README.md** - This summary document

### Assets
- `assets/AMD_Strix_Halo_Talk.pdf` - Final PDF presentation (1.4MB, 24 pages)
- `assets/ha.jpeg` - Home Assistant on Echo Show screenshot
- `assets/dashboard.png` - WWS Dashboard
- `assets/concrete_sign.png` - Concrete sign mold design
- `assets/github_heatmap_2025_2026.png` - GitHub activity heatmap
- `assets/timeline.png` - 6-month journey timeline
- `assets/catalyst_diagram.png` - OSS catalyst diagram
- `assets/contribution_calendar_2026.png` - 2026 activity calendar
- `assets/project_breakdown.png` - Project distribution
- All assets in: `assets/` directory

---

## Talk Overview

### Title
**Building an AI Workstation: 6 Months with AMD Strix Halo**

### Subtitle
A Journey from Hardware Hype to Real-World Autonomous Development

### Duration
45 minutes (35 min presentation + 10 min Q&A)

### Target Audience
- AI/ML engineers
- Hardware enthusiasts
- Developers interested in local LLMs
- Open source contributors

---

## Key Story Arcs

### 1. Hardware Journey
- **November 2025**: Sold NVIDIA 4060 rig, ordered AMD Strix Halo
- **Reality Check**: 128GB → 96GB addressable, VRAM/GTT issues
- **February 2026**: "Strix remorse" - buyer's remorse moment
- **January 2026**: AMD GPU library update = 2x performance boost

### 2. Software Stack Evolution
- **Lemonade** (Nov-Dec): Good observability, stability issues
- **Ollama** (Dec+): Simpler, but poor metrics, GPU crashes
- **llama.cpp** (Mar+): Prompt caching breakthrough
- **NPU Support**: Still in development

### 3. Performance Reality
- **Best**: 45 TPS (Nov 29, initial)
- **Typical**: 14-18 TPS (200k context)
- **Recent**: 18.65 TPS at ~200k tokens (May 30)
- **TTFT**: 37.8 minutes for ~200k context (May 30)

### 4. Project Outcomes
- **WWS**: Fully vibe-coded workspace system (May 2026)
- **Home Assistant**: Echo repurposing complete (Jan 2026)
- **Concrete Signs**: From AI design to physical objects

---

## Project Summaries

### WWS (Winmutt Work Spaces)

**URL**: https://github.com/winmutt/wws  
**Status**: Phase 2 Complete (Team Features)

**What**: Remote workspace provisioning system for engineering teams

**Features**:
- KVM/Podman isolated environments
- code-server (VSCode) integration
- GitHub OAuth + RBAC
- Team collaboration
- 274 tracked tasks across 4 phases

**Timeline**: Months of development, "entirely vibe coded"

**Tech Stack**: Go, React, SQLite, KVM, Podman

---

### Home Assistant on Echo

**Devices**: Echo Show Gen 2, Echo Spot (eBay)  
**Status**: Complete (Jan 29, 2026)

**What**: Replace Alexa with Home Assistant

**Timeline**:
- Dec 6: Started exploring XDA forums
- Jan 19: HA OS installed
- Jan 25: Wake word sorted (Hey Jarvis)
- Jan 29: End-to-end complete

**Screenshot**: `/tmp/ha.jpeg`

---

### Concrete Sign Molds

**Location**: `/opt/opencode/src/concrete/sign-molds/`  
**Status**: In Progress

**What**: 3D printable molds for casting concrete signs

**Motivation**: "For my PE, she's always belaboring the need to get concrete and not speak in abstract."

**Files**:
- OpenSCAD designs (example, use case)
- STL exports
- Python automation script

**Process**: AI design → 3D print → Silicone mold → Concrete cast → Etsy

---

## Performance Data Summary

| Metric | Value | Date | Context |
|--------|-------|------|---------|
| Best TPS | 45 | Nov 29, 2025 | Initial 400k setup |
| Typical TPS | 14-18 | Nov 2025 - May 2026 | 200k context |
| Generation TPS | 46 | Dec 14, 2025 | Ollama backend |
| Prompt Eval TPS | 284 | Dec 14, 2025 | Ollama backend |
| Single-thread TPS | 24 | Feb 8, 2026 | Lemonade backend |
| Recent TPS | 18.65 | May 30, 2026 | ~200k context |
| Worst TTFT | 2,267s | May 30, 2026 | ~200k context |

---

## Key Quotes for Presentation

### Hardware
> "BTW I have a corsair 300 AMD 395 max+ enroute. Sold my 4060 rig today."  
> — November 22, 2025

> "6 days out of return policy i am having strix remorse."  
> — February 3, 2026

### Software
> "Using lemonade instead of ollama. Working on getting NPUs working."  
> — November 28, 2025

> "Went back to using ollama. lemonade-server, for whatever reason, was not behaving properly"  
> — December 7, 2025

> "I got the new amd GPU libraries working on my strix halo and stable and its 2x faster than before."  
> — January 29, 2026

### Performance
> "The TPS goes down pretty sharply >64k context. I dont know why. But that's on ingress, not generation."  
> — December 9, 2025

> "One thing I have learned is its important to get the kv cache in vram too, not just the model."  
> — February 3, 2026

### Autonomous Development
> "I think I got into full autonomous mode this morning. The newest llamacpp fixed prompts caching finally and things are really humming now."  
> — March 11, 2026

> "Definitely no Athena and its taken months to get there but this is something I entirely vibe coded."  
> — May 12, 2026 (WWS complete)

### Philosophy
> "Why not use the mcp. I guess its repeatable with python. That's something I've been focused on lately. Not just doing the work but making it repeatable."  
> — November 29, 2025

> "Basically anything with a USB port. If there is a port, there is a way."  
> — December 6, 2025 (Echo repurposing)

---

## Key Takeaways

1. **Hardware Hype vs Reality**: APU architecture challenges are real
2. **Software Maturity**: Latest kernel + ROCm essential
3. **Context is King**: Prompt caching transforms workflow
4. **Tooling Evolution**: Cline + Qwen3-Coder > traditional IDEs
5. **From Digital to Physical**: AI can create real-world objects
6. **Repurposing Hardware**: Echo → Home Assistant = Win
7. **Autonomous Development**: Possible, but requires tuning

---

## GitHub Activity Summary

### winmutt Profile
- **Total Repos**: 8
- **Followers**: 4
- **Following**: 4
- **Stars Given**: 5

### Key Repositories
1. **wws** - Workspace provisioning (main project)
2. **lemonade** - Fork (LLM serving)
3. **cline** - Fork (autonomous coding)
4. **vscode** - Fork (editor)
5. **slow_log_parse** - MySQL analysis
6. **self_2019_slow_session** - ELK analysis

### WWS PRs (Sample)
- PR #3 - Project initialization
- PR #214-223 - Authentication & Organization
- PR #224-232 - Workspace Provisioning
- PR #248 - Protocol Buffers Migration
- PR #250-259 - Security Features
- PR #260-271 - Team Collaboration

---

## External References

### Communities
- Reddit r/LocalLLaMA: https://www.reddit.com/r/LocalLLaMA/comments/1pdh0sm/8_local_llms_on_a_single_strix_halo_debating/
- XDA Forums: https://xdaforums.com/f/amazon-echo.6148/

### Projects
- Hey Jarvis Wake Words: https://github.com/fwartner/home-assistant-wakewords-collection
- Lemonade SDK: https://github.com/lemonade-sdk/lemonade
- Cline: https://github.com/cline/cline

---

## Presentation Preparation Checklist

### Before the Talk
- [ ] Review all slide content
- [ ] Verify all GitHub links work
- [ ] Test screenshot images load correctly
- [ ] Practice timing (35 min target)
- [ ] Prepare demo environment (WWS, HA)
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

## Appendix: Complete File List

### Documentation Files
```
/opt/opencode/src/self-2026/
├── AMD_STRIX_TALK_README.md      # Context for AI assistants
├── AMD_STRIX_TALK_SLIDES.md      # Main slide deck
├── SLIDE_DECK_INDEX.md           # Index and references
├── CHAT_TO_PROJECT_REFERENCE.md  # Chat to project mapping
├── PRESENTATION_OUTLINE.md       # Visual outline
├── PERFORMANCE_DATA.md           # Performance timeline
└── README.md                     # This file
```

### Project Files
```
/opt/opencode/src/winmutt/wws/
├── README.md                     # WWS documentation
├── TODO.md                       # Task breakdown (274 tasks)
├── docs/screenshots/dashboard.png
└── [172 files, 56 days]

/opt/opencode/src/concrete/sign-molds/
├── example_sign_mold.scad
├── example_sign_positive.scad
├── use_case_sign_mold.scad
├── use_case_sign_positive.scad
├── models.scad
├── generate.py
├── *.stl
└── *_preview.png

/tmp/ha.jpeg                      # Home Assistant screenshot
```

---

## Contact & Credits

**Author**: winmutt  
**GitHub**: https://github.com/winmutt  
**WWS Project**: https://github.com/winmutt/wws  

**Special Thanks**:
- AMD for Strix Halo APU
- Lemonade SDK team
- Cline team
- Qwen team
- Home Assistant community
- FWartner (Hey Jarvis wake words)
- Friend for chat conversations and feedback

---

**Created**: May 2026  
**Last Updated**: May 30, 2026  
**Version**: 1.0
