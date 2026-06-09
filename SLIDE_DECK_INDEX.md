# AMD Strix Halo 6-Month Experience
## Slide Deck Index and References

**Talk Duration**: 45 minutes  
**Date**: June 2026  
**Author**: winmutt

---

## Slide Deck Files

### Main Presentation (PDF)
- **File**: `assets/AMD_Strix_Halo_Talk.pdf`
- **Format**: PDF (dark theme, black background)
- **Slides**: 18 slides across 3 sections

### Generation Scripts
- `generate_pdf.py` - PDF generation script
- `generate_heatmap.py` - GitHub heatmap generation
- `generate_numa_diagrams.py` - NUMA/CCD diagram generation
- `generate_issue_screenshots.py` - Issue #1070 annotated screenshots
- `fetch_github_graphql.py` - GitHub GraphQL API data fetcher

---

## Slide Structure

### Section 1: The Hardware Stack (Slides 1-6)

**Slide 1: Title**
- "Six Months with AMD Strix Halo: Local AI, Open Source, and Hardware Reality"
- winmutt | June 2026

**Slide 2: Agenda**
- Section 1: The Hardware Stack (3 topics)
- Section 2: Projects & Applications (4 topics)
- Section 3: Open Source Journey (4 topics)

**Slide 3: Power Reality**
- Corsair 300 (~300W) vs RTX 5090 (~800-1000W) vs Commercial Server (~1500-3000W)
- 3x more efficient, single APU vs discrete CPU+GPU

**Slide 4: The Hardware - APU Die + GPU + NPU**
- 16 cores (12 perf + 4 efficiency)
- 2x CCD with 32MB L3 cache each
- 128GB LPDDR5X-8000 soldered
- AMD Radeon 680M GPU: RDNA 3.5, 40 CUs, ~4.6 TFLOPS
- AMD XDNA 2 NPU: Neural Processing Unit, FastFlowLM support
- Performance stats: Coming soon (logs being processed)

**Slide 5: Issue #1070 - Problem & Solution**
- "Feat #1070: [enhancement] Core affinity when running multiple models."
- Filed: February 8, 2026 | Repository: github.com/lemonade-sdk/lemonade/issues/1070
- Hardware Reality: 2 CCDs with separate 32MB L3 caches
- Problem: NUMA tools can't see CCD boundaries → threads bounce → L3 thrashing
- Solution: Manual core pinning per CCD

**Slide 6: Issue #1070 - Evidence**
- Traditional NUMA vs Strix Halo diagrams
- ps output with L3 + AVG_MHZ highlighting
- lscpu topology showing load shifting across CCDs

### Section 2: Projects & Applications (Slides 7-12)

**Slide 7: Home Assistant - Process**
- LineageOS on Echo: amonet → TWRP → LineageOS 18.1 → ViewAssist
- Philosophy: "Basically anything with a USB port..."

**Slide 8: Home Assistant - Timeline**
- Dec 6 → Feb 2026 timeline
- Issue #4: Echo 8 mic dies after 24h

**Slide 9: Home Assistant - Screenshot + Compatibility**
- HA on Echo Show (full width)
- Echo Show 5 (1st/2nd gen), Echo Show 8
- MT8163 SoC, LineageOS 18.1 by @R0rt1z2

**Slide 10: 3D Modeling**
- Concrete sign mold design
- Blender + OpenSCAD workflow
- AI → STL → 3D print → silicone mold → concrete

**Slide 11: AI Coding Editors**
- Opencode: Web server (localhost:3000), remote access, autonomous dev
- Cline: Good TUI but regressions
- Also use: Koo Roo, Aider

**Slide 12: Project WWS**
- Winmutt Work Spaces (github.com/winmutt/wws)
- Quote: "Definitely no Athena and its taken months..."
- KVM/Podman isolation, code-server, GitHub OAuth + RBAC

### Section 3: Open Source Journey (Slides 13-18)

**Slide 13: Lessons Learned**
- What Worked: Cline + Qwen3-Coder, Prompt Caching, AMD GPU libs 2x faster
- What Didn't: Memory (32GB reserved), Ollama crashes, NPU (still waiting)

**Slide 14: Key Insights**
- 8 takeaways: Hardware hype ≠ reality, bleeding edge = bleeding fingers,
  context is king, AI coding > IDEs, AI → physical objects,
  Echo → HA = OSS win, autonomous dev possible, buying hardware got me back in OSS

**Slide 15: 26 Years of Open Source**
- From LKML 2000 to Strix Halo
- LKML 2000 email (HighPoint IDE RAID, kernel 2.2.14)
- GitHub heatmap 2018-2026
- 2018-2024: Ghost town, 2025: Strix Halo arrives
- AI + local hardware reinvigorated my love for open source

**Slide 16: OSS Contributions**
- Catalyst Effect: 3.5x increase
- 2026 contribution calendar
- Project breakdown: WWS 38%, Lemonade 15%, ROCm 8%, HA 12%, Cline 8%, Concrete 5%

**Slide 17: References**
- Power sources (Reddit, NVIDIA, Tom's Hardware)
- Software (Lemonade, Ollama, ROCm, WWS, HA)
- Communities (r/LocalLLaMA, XDA Forums)

**Slide 18: Q&A**
- 5 discussion questions
- github.com/winmutt

---

## Project References

### 1. WWS (Winmutt Work Spaces)
**URL**: https://github.com/winmutt/wws  
**Local Path**: `/opt/opencode/src/winmutt/wws/`

**Key Files**:
- `README.md` - Full project documentation
- `TODO.md` - Detailed task breakdown (274 tasks)
- `docs/screenshots/dashboard.png` - Dashboard screenshot

**GitHub Activity**:
- Phase 1: Core Foundation ✅ Complete
- Phase 2: Team Features ✅ Complete (27 PRs tracked)
- Phase 3: Advanced Features 🔄 In Progress

### 2. Concrete Sign Molds
**Local Path**: `/opt/opencode/src/concrete/sign-molds/`

**Key Files**:
- `example_sign_mold.scad` - Mold for "example" sign
- `use_case_sign_mold.scad` - Mold for "use case" sign
- `generate.py` - Automated STL export script

### 3. Home Assistant on Echo
**Screenshot**: `/tmp/ha.jpeg`

**External References**:
- XDA Forums: https://xdaforums.com/f/amazon-echo.6148/
- Hey Jarvis Wake Words: https://github.com/fwartner/home-assistant-wakewords-collection

**Timeline**:
- Dec 6: Started exploring Echo hacking
- Jan 19: HA setup on Echo Show Gen 2
- Jan 29: End-to-end complete

### 4. AI/LLM Stack
**Backends**: Lemonade (llama.cpp + ROCm), Ollama

**Models**: Qwen3-Coder, Qwen 3.5 9B (sub-agents)

**GitHub Forks**:
- https://github.com/winmutt/lemonade
- https://github.com/winmutt/cline

### 5. Opencode
**URL**: https://github.com/anomalyco/opencode

**Features**:
- Web server mode (http://localhost:3000)
- Remote access with localized agent
- Autonomous development support

---

## Performance Data

### December 14, 2025 Benchmark
```
prompt eval time =    2823.77 ms /   804 tokens (284.73 tokens/sec)
eval time =    5964.43 ms /   276 tokens (46.27 tokens/sec)
```

### Performance Timeline
| Date | TPS | Context | Notes |
|------|-----|---------|-------|
| Nov 29 | 45 | 400k | Initial setup |
| Feb 8 | 24 | Single | Single thread |
| Mar 11 | ? | ? | "Really humming" (prompt caching) |

### Memory Usage
- Total: 128GB LPDDR5X-8000
- Addressable: 96GB (initially)
- 32GB reserved for Lemonade/llama.cpp/opencode

---

## GitHub Repository Summary

### winmutt GitHub Profile
- **Total Repos**: 8
- **Followers**: 4
- **Following**: 4

### Key Repositories
1. **wws** (Go/React) - Workspace provisioning system
2. **lemonade** (C++) - Fork with NPU backend work
3. **cline** (TypeScript) - Fork with TUI fixes
4. **vscode** (TypeScript) - Fork
5. **concrete** - 3D printable molds

---

## Asset Inventory

### Images
1. `assets/apu_die_diagram.png` - APU die architecture
2. `assets/numa_traditional.png` - Traditional NUMA diagram
3. `assets/strix_halo_numa.png` - Strix Halo NUMA diagram
4. `assets/issue_1070_ps_output.png` - Annotated ps output
5. `assets/issue_1070_lscpu.png` - Annotated lscpu topology
6. `assets/concrete_sign.png` - Concrete sign mold design
7. `assets/ha.jpeg` - Home Assistant on Echo Show
8. `assets/dashboard.png` - WWS Dashboard
9. `assets/editor_collage.png` - AI coding editors collage
10. `assets/contribution_calendar_2026.png` - 2026 GitHub activity
11. `assets/project_breakdown.png` - Contribution pie chart
12. `assets/github_heatmap_10year.png` - 2018-2026 GitHub heatmap

### Documents
1. `generate_pdf.py` - PDF generation script
2. `HOME_ASSISTANT_SETUP.md` - HA setup guide
3. `LINEAGEOS_INSTALLATION_GUIDE.md` - LineageOS installation

---

## Next Steps

1. **NPU Performance Stats** - Add logs when provided
2. **OpenSCAD k-baffle Screenshot** - Add when provided
3. **Practice Timing** - Ensure 45-minute delivery
4. **Prepare Demo** - Show WWS dashboard or Home Assistant

---

## Contact & Credits

**Author**: winmutt  
**GitHub**: https://github.com/winmutt  
**Date**: June 2026  

**Special Thanks**:
- AMD for Strix Halo APU
- Lemonade SDK team
- Cline team
- Qwen team
- Home Assistant community
- FWartner (Hey Jarvis wake words)
