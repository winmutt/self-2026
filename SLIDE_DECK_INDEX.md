# AMD Strix Halo 6-Month Experience
## Slide Deck Index and References

**Talk Duration**: 45 minutes  
**Date**: May 2026  
**Author**: winmutt

---

## Slide Deck Files

### Main Presentation
- **File**: `AMD_STRIX_TALK_SLIDES.md`
- **Format**: Markdown slides (can be converted to reveal.js, PowerPoint, etc.)
- **Slides**: ~60 slides across 8 parts

### Context Document
- **File**: `AMD_STRIX_TALK_README.md`
- **Purpose**: Background information for AI assistants working on this project

---

## Slide Structure

### Part 1: The Decision (5 min)
- Why AMD Strix Halo?
- Hardware specifications
- The NVIDIA to AMD transition

### Part 2: Hardware Reality (7 min)
- Strix Halo architecture
- Memory challenges (128GB → 96GB)
- VRAM vs GTT issues

### Part 3: Software Stack Evolution (8 min)
- Lemonade vs Ollama comparison
- ROCm + llama.cpp backend
- The "Resurgens" reinstall moment
- AMD GPU library updates

### Part 4: Performance Deep Dive (7 min)
- TPS benchmarks at various context sizes
- Memory placement problems
- Prompt caching breakthrough
- Core affinity optimization

### Part 5: Project WWS (6 min)
- Workspace provisioning system
- Autonomous development setup
- Tech stack and architecture
- "Vibe coded" achievement

### Part 6: Home Assistant (5 min)
- Echo device repurposing
- Wake word implementation
- HA OS vs Docker container discovery
- Timeline from Dec 6 to Jan 29

### Part 7: Concrete Signs (3 min)
- From AI design to physical objects
- OpenSCAD + 3D printing workflow
- Etsy potential
- "Concrete not abstract" motivation

### Part 8: Lessons Learned (4 min)
- What worked / What didn't
- Performance reality vs marketing
- Future work and NPU potential
- Terminator warning (AI safety)

---

## Project References

### 1. WWS (Winmutt Work Spaces)
**URL**: https://github.com/winmutt/wws  
**Local Path**: `/opt/opencode/src/winmutt/wws/`

**Key Files**:
- `README.md` - Full project documentation (333 lines)
- `TODO.md` - Detailed task breakdown (300 lines, 274 tasks)
- `docs/screenshots/dashboard.png` - Dashboard screenshot
- `api/` - Go backend (99 Go files)
- `web/` - React frontend (14 TSX files)

**GitHub Activity**:
- Phase 1: Core Foundation ✅ Complete
- Phase 2: Team Features ✅ Complete (27 PRs tracked)
- Phase 3: Advanced Features 🔄 In Progress

**Key PRs**:
- PR #3 - Project initialization
- PR #214-223 - Authentication & Organization
- PR #224-232 - Workspace Provisioning
- PR #248 - Protocol Buffers Migration
- PR #250-259 - Security Features
- PR #260-271 - Team Collaboration
- PR #272-274 - Documentation

### 2. Concrete Sign Molds
**Local Path**: `/opt/opencode/src/concrete/sign-molds/`

**Key Files**:
- `example_sign_mold.scad` - Mold for "example" sign
- `example_sign_positive.scad` - Positive model for mold creation
- `use_case_sign_mold.scad` - Mold for "use case" sign
- `models.scad` - Shared OpenSCAD definitions
- `generate.py` - Automated STL export script
- `example_sign_mold_preview.png` - Preview image (420.7KB)
- `example_sign_positive_preview.png` - Preview image (523.9KB)

**Related Chat**:
```
Dec 1: "Wow that's cool. I am going to use it to create a 
3d printed cast for a silicone mold so I can some desktop 
signs out of concrete. One will read 'example' and the 
other 'use case'. It's for my PE, she's always belaboring 
the need to get concrete and not speak in abstract."
```

### 3. Home Assistant on Echo
**Screenshot**: `/tmp/ha.jpeg` (65.6KB, 600x450)

**External References**:
- XDA Forums: https://xdaforums.com/f/amazon-echo.6148/
- Hey Jarvis Wake Words: https://github.com/fwartner/home-assistant-wakewords-collection/tree/main/en

**Timeline**:
- Dec 6: Started exploring Echo hacking
- Jan 19: HA setup on Echo Show Gen 2
- Jan 21: Working except wake word
- Jan 25: Wake word sorted with Hey Jarvis
- Jan 29: End-to-end complete

### 4. AI/LLM Stack
**Backends Tested**:
- Lemonade (llama.cpp + ROCm) - Nov 28 to Dec 7
- Ollama - Dec 7 onwards (with issues)

**Models Used**:
- Qwen3-Coder - Primary coding model
- Qwen 3.5 9B - Sub-agents

**Performance Metrics**:
- <100k tokens: ~40 TPS
- 100k-200k: ~14 TPS
- >200k: ~8 TPS
- Dec 14 benchmark: 284.73 tokens/sec prompt, 46.27 tokens/sec generation

**GitHub Forks**:
- https://github.com/winmutt/lemonade
- https://github.com/winmutt/cline
- https://github.com/winmutt/vscode

---

## Chat Snippet References

All chat snippets from conversations with friend, Nov 2025 - May 2026:

### November 2025
```
Nov 22: "BTW I have a corsair 300 AMD 395 max+ enroute. 
Sold my 4060 rig today."

Nov 28: "Using lemonade instead of ollama. There is a patch 
for ollama that will make it work with the APU, but I've 
been working to get the NPUS working as well."

Nov 29: "Why not use the mcp. I guess its repeatable with 
python. That's something I've been focused on lately."

Nov 29: "I've really been liking Cline lately. Cline+qwen3-coder 
is making some really good results."

Nov 29: "I've got a 400k context window with the new Ai 
workstation. Still need to work on tuning it."

Nov 29: "Its 128g total but I've only been able to get it 
to address 96."

Nov 29: "No but it lpddr5x-8000 and soldered to the apu 
board. Its basically the fastest nom vram out there."
```

### December 2025
```
Dec 1: "Wow that's cool. I am going to use it to create a 
3d printed cast for a silicone mold..."

Dec 5: "Lol I've been talking about terminator all week long..."

Dec 6: "Basically anything with a USB port. If there is a 
port, there is a way."

Dec 7: "Went back to using ollama. lemonade-server, for 
whatever reason, was not behaving properly"

Dec 7: https://www.reddit.com/r/LocalLLaMA/comments/1pdh0sm/8_local_llms_on_a_single_strix_halo_debating/

Dec 9: "The TPS goes down pretty sharply >64k context."

Dec 14: "I think thats the only backend I can run. Upgraded 
OS and ollama last night and sad things happened."
```

### January 2026
```
Jan 19: "Got linkages and home assistant setup on a echo 
show gen 2. Still haven't figure out voice assistant yet"

Jan 21: "Fully working everything but wake word. I dont 
know why but HA companion app doesn't support it"

Jan 25: "I got the wake word sorted and now have a fully 
functioning * echo"

Jan 29: "I got the new amd GPU libraries working on my 
strix halo and stable and its 2x faster than before."
```

### February 2026
```
Feb 3: "6 days out of return policy i am having strix remorse. 
Its gotten better but there is a linear performance regression 
in token processing."

Feb 8: "Ive been using it with various degrees of success 
with open code. Tools, especially editing, failed a few times."

Feb 8: "It's putting together a pr for llamacpp to manage 
core affinity on the strix. Its one apu but 2 core dies and 
2x64mb l3 caches."

Feb 8: "Getting 24tps now on a single thread."
```

### March 2026
```
Mar 11: "I think I got into full autonomous mode this morning. 
The newest llamacpp fixed prompts caching finally and things 
are really humming now."

Mar 11: "I have sub agents running on qwen 3.5 9b. And NPU 
support is working in dev now."
```

### May 2026
```
May 12: "Definitely no Athena and its taken months to get 
there but this is something I entirely vibe coded."
```

---

## Performance Data

### December 14, 2025 Benchmark
```
prompt eval time =    2823.77 ms /   804 tokens (    3.51 ms per token,   284.73 tokens per second)
eval time =    5964.43 ms /   276 tokens (   21.61 ms per token,    46.27 tokens per second)
total time =    8788.20 ms /  1080 tokens
```

### Performance Timeline
| Date | TPS | Context | Notes |
|------|-----|---------|-------|
| Nov 29 | 45 | 400k | Initial setup |
| Nov 29 | 14 | 200k | After tuning |
| Dec 9 | N/A | >64k | Sharp decline |
| Dec 14 | 46 | 804 | Prompt eval |
| Feb 8 | 24 | Single | Single thread |
| Mar 11 | ? | ? | "Really humming" |

### Memory Usage
- Total: 128GB LPDDR5X-8000
- Addressable: 96GB (initially)
- Qwen3-Coder + 400k window: ~59GB
- 2 cached prompts: ~8GB

---

## GitHub Repository Summary

### winmutt GitHub Profile
- **Total Repos**: 8
- **Followers**: 4
- **Following**: 4
- **Stars Given**: 5

### Repositories
1. **slow_log_parse** (Go) - 2 stars, 1 fork
   - Slow MySQL query and session analysis in ELK

2. **self_2019_slow_session** (Shell) - 2 stars
   - Slow MySQL query and session analysis in ELK

3. **twirp** (PHP) - Fork from twirphp/twirp
   - PHP port of Twitch's Twirp RPC framework

4. **vscode** (TypeScript) - Fork from microsoft/vscode
   - Visual Studio Code

5. **cline** (TypeScript) - Fork from cline/cline
   - Autonomous coding agent in IDE

6. **lemonade** (C++) - Fork from lemonade-sdk/lemonade
   - Local LLM serving with GPU/NPU support

7. **wws** (Go/React) - Main project
   - Workspace provisioning system

8. **concrete** - Local project
   - 3D printable molds for concrete signs

---

## Asset Inventory

### Images
1. `/tmp/ha.jpeg` - Home Assistant on Echo Show (65.6KB, 600x450)
2. `/opt/opencode/src/concrete/sign-molds/example_sign_mold_preview.png` (420.7KB)
3. `/opt/opencode/src/concrete/sign-molds/example_sign_positive_preview.png` (523.9KB)
4. `/opt/opencode/src/winmutt/wws/docs/screenshots/dashboard.png` (302.8KB)

### Documents
1. `/opt/opencode/src/self-2026/AMD_STRIX_TALK_README.md` - Context document
2. `/opt/opencode/src/self-2026/AMD_STRIX_TALK_SLIDES.md` - Main slide deck
3. `/opt/opencode/src/winmutt/wws/README.md` - WWS documentation
4. `/opt/opencode/src/winmutt/wws/TODO.md` - Task breakdown
5. `/opt/opencode/src/concrete/sign-molds/README.md` - Concrete sign documentation

### Source Code
1. `/opt/opencode/src/winmutt/wws/` - WWS project (172 files, 56 days)
2. `/opt/opencode/src/concrete/sign-molds/` - Concrete sign molds (14 files)

---

## Conversion Instructions

### To Reveal.js (HTML Slides)
```bash
# Install reveal.js
npm install reveal.js

# Create index.html
cat > index.html << 'EOF'
<!doctype html>
<html>
<head>
  <link rel="stylesheet" href="node_modules/reveal.js/css/reveal.css">
  <link rel="stylesheet" href="node_modules/reveal.js/css/theme/black.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <!-- Paste slides here -->
    </div>
  </div>
  <script src="node_modules/reveal.js/js/reveal.js"></script>
  <script>Reveal.initialize();</script>
</body>
</html>
EOF

# Serve
npx serve .
```

### To PowerPoint
1. Export markdown to HTML
2. Import HTML into PowerPoint
3. Or use pandoc:
```bash
pandoc AMD_STRIX_TALK_SLIDES.md -o AMD_STRIX_TALK.pptx
```

### To PDF
```bash
pandoc AMD_STRIX_TALK_SLIDES.md -o AMD_STRIX_TALK.pdf
```

---

## Next Steps

1. **Review slides** - Check accuracy of all claims and metrics
2. **Add screenshots** - Insert actual images into slide deck
3. **Practice timing** - Ensure 45-minute delivery (35 min talk + 10 min Q&A)
4. **Prepare demo** - Show WWS dashboard or Home Assistant in action
5. **Gather testimonials** - Get quotes from friend about Cline/Qwen3-Coder
6. **Update references** - Verify all GitHub links and URLs

---

## Contact & Credits

**Author**: winmutt  
**GitHub**: https://github.com/winmutt  
**Date**: May 2026  

**Special Thanks**:
- AMD for Strix Halo APU
- Lemonade SDK team
- Cline team
- Qwen team
- Home Assistant community
- FWartner (Hey Jarvis wake words)
- Friend for chat conversations and feedback
