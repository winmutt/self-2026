# AMD Strix Halo 6-Month Journey
## Visual Presentation Outline

**Talk Title**: Building an AI Workstation: 6 Months with AMD Strix Halo  
**Duration**: 45 minutes (35 min talk + 10 min Q&A)  
**Date**: May 2026  
**Speaker**: winmutt

---

## Slide Deck Structure

### Opening (3 minutes)

#### Slide 1: Title Slide
**Content**:
- Title: Building an AI Workstation
- Subtitle: 6 Months with AMD Strix Halo
- Date: May 2026
- Speaker: winmutt
- GitHub: https://github.com/winmutt

**Visual**: AMD Strix Halo APU image or logo

---

#### Slide 2: Who Am I?
**Content**:
- Software engineer, open source contributor
- Focus: AI-assisted development, home automation
- Current setup: AMD Strix Halo (128GB LPDDR5X-8000)
- Timeline: Nov 2025 - May 2026

**Visual**: GitHub profile snapshot showing 8 repos

---

#### Slide 3: Agenda
**Content**:
1. The Decision (5 min)
2. Hardware Reality (7 min)
3. Software Stack Evolution (8 min)
4. Performance Deep Dive (7 min)
5. Project: WWS (6 min)
6. Project: Home Assistant (5 min)
7. Project: Concrete Signs (3 min)
8. Lessons Learned (4 min)

**Visual**: Timeline graphic

---

### Part 1: The Decision (5 minutes)

#### Slide 4: The Hardware Choice
**Content**:
- November 22, 2025: "BTW I have a corsair 300 AMD 395 max+ enroute. Sold my 4060 rig today."
- Transition: NVIDIA 4060 → AMD Strix Halo
- Why? Unified memory, NPU, no discrete GPU needed

**Visual**: Side-by-side comparison (4060 vs Strix Halo)

---

#### Slide 5: The Pitch
**Content**:
- 128GB LPDDR5X-8000 unified memory
- NPU for AI acceleration
- "Fastest nom VRAM out there"
- All-in-one APU architecture

**Visual**: AMD marketing slide or spec sheet

---

### Part 2: Hardware Reality (7 minutes)

#### Slide 6: Strix Halo Architecture
**Content**:
```
┌─────────────────────────────────────────┐
│           AMD Strix Halo APU            │
│  ┌─────────────┐  ┌─────────────┐       │
│  │ Core Die 1  │  │ Core Die 2  │       │
│  │ 64MB L3     │  │ 64MB L3     │       │
│  └─────────────┘  └─────────────┘       │
│  128GB LPDDR5X-8000 (soldered)          │
│  GPU | NPU | Media Engine               │
└─────────────────────────────────────────┘
```

**Visual**: Architecture diagram

---

#### Slide 7: The Memory Challenge
**Content**:
- Total: 128GB
- Addressable: 96GB (initially)
- Issue: Models loading to GTT instead of VRAM
- Result: Swapping despite unified memory

**Quote**: "Sometimes it loads the models into gtt instead of vram and seems to spend a lot of time swapping in and out even though its all the same memory."

**Visual**: Memory placement diagram (VRAM vs GTT)

---

#### Slide 8: Architecture Quirks
**Content**:
- Single APU, dual core dies
- 2x 64MB L3 caches
- NUMA-like behavior
- Core affinity matters

**Quote**: "Its one apu but 2 core dies and 2x64mb l3 caches."

**Visual**: Die shot or core layout

---

### Part 3: Software Stack Evolution (8 minutes)

#### Slide 9: The Backend War
**Content**: Lemonade vs Ollama

| Feature | Lemonade | Ollama |
|---------|----------|--------|
| Backend | llama.cpp + ROCm | Various |
| Observability | Good | Poor |
| NPU Support | In dev | Patch available |
| Stability | Issues | Crashes |
| Multi-model | Yes | Limited |

**Visual**: Comparison table

---

#### Slide 10: Lemonade Journey
**Content**:
- November 28: Started with Lemonade
- Working on NPU support
- December 7: "Went back to using ollama. lemonade-server, for whatever reason, was not behaving properly"
- February 8: PR for core affinity management

**Visual**: Lemonade GitHub repo screenshot

---

#### Slide 11: The Resurgens Moment
**Content**:
- December 14: "Upgraded OS and ollama last night and sad things happened. GPU crashes about 3-4 prompts in"
- System reinstalled and formatted
- Phoenix rising out of the ashes
- Led to AMD GPU library update

**Visual**: Reinstall timeline graphic

---

#### Slide 12: The Breakthrough
**Content**:
- January 29: "I got the new amd GPU libraries working on my strix halo and stable and its 2x faster than before."
- Fresh kernel + ROCm + stability
- Performance doubled

**Visual**: Before/after performance chart

---

### Part 4: Performance Deep Dive (7 minutes)

#### Slide 13: Token Processing Performance
**Content**:

| Context Size | TPS | Notes |
|--------------|-----|-------|
| <100k tokens | ~40 | Consistent |
| 100k-200k | ~14 | Degradation |
| >200k tokens | ~8 | Sharp decline |
| >64k (ingress) | N/A | Performance cliff |

**Visual**: Line graph showing TPS vs context

---

#### Slide 14: December 14 Benchmark
**Content**:
```
prompt eval time =    2823.77 ms /   804 tokens
                      (3.51 ms per token, 
                       284.73 tokens per second)
eval time =    5964.43 ms /   276 tokens
             (21.61 ms per token, 
              46.27 tokens per second)
total time =    8788.20 ms /  1080 tokens
```

**Visual**: Benchmark output screenshot

---

#### Slide 15: The KV Cache Insight
**Content**:
- February 3: "One thing I have learned is its important to get the kv cache in vram too, not just the model."
- Memory placement critical
- Strix architecture: Good at Prefill, not inference

**Visual**: Memory hierarchy diagram

---

#### Slide 16: Prompt Caching Breakthrough
**Content**:
- March 11: "I think I got into full autonomous mode this morning. The newest llamacpp fixed prompts caching finally and things are really humming now."
- 2 cached prompts = ~8GB
- Multi-tasking without reload

**Visual**: Caching architecture diagram

---

### Part 5: Project WWS (6 minutes)

#### Slide 17: What is WWS?
**Content**:
- **Winmutt Work Spaces**
- Remote workspace provisioning system
- KVM/Podman-based isolated environments
- code-server (VSCode) integration
- GitHub: https://github.com/winmutt/wws

**Visual**: WWS logo or architecture diagram

---

#### Slide 18: WWS Architecture
**Content**:
```
┌─────────────────────────────────────────────┐
│         Web Management UI (React)           │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│              Go Backend API                 │
│            (SQLite + RBAC)                  │
└─────────────────┬───────────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
┌─────────┐ ┌──────────┐ ┌──────────┐
│  KVM    │ │  Podman  │ │ Cloud    │
│  VMs    │ │ Containers│ │ (Future) │
└─────────┘ └──────────┘ └──────────┘
```

**Visual**: Architecture diagram from README

---

#### Slide 19: WWS Dashboard
**Content**:
- Workspaces with persistent storage
- Resource quotas
- Team collaboration
- Idle management

**Visual**: `/opt/opencode/src/winmutt/wws/docs/screenshots/dashboard.png`

---

#### Slide 20: Autonomous Development
**Content**:
- March 11: Full autonomous mode
- Sub-agents: Qwen 3.5 9B
- NPU support in development
- May 12: "Definitely no Athena and its taken months to get there but this is something I entirely vibe coded."

**Visual**: Multi-agent workflow diagram

---

#### Slide 21: WWS Progress
**Content**:
- **Phase 1**: Core Foundation ✅
- **Phase 2**: Team Features ✅ (27 PRs)
- **Phase 3**: Advanced Features 🔄
- **Tasks**: 274 tracked tasks
- **Files**: 172 files, 56 days

**Visual**: Progress bar or milestone chart

---

### Part 6: Home Assistant (5 minutes)

#### Slide 22: Echo Repurposing
**Content**:
- December 6: Started exploring XDA forums
- Goal: Replace Alexa with Home Assistant
- Devices: Echo Show Gen 2, Echo Spot (eBay)
- January 29: End-to-end complete

**Quote**: "Basically anything with a USB port. If there is a port, there is a way."

**Visual**: Echo devices photo

---

#### Slide 23: HA on Echo Timeline
**Content**:
```
Dec 6  ┤ Started exploring
Jan 19 ┤ HA OS installed
Jan 21 ┤ Everything except wake word
Jan 25 ┤ Wake word sorted
Jan 29 ┤ End-to-end complete
```

**Visual**: Timeline graphic

---

#### Slide 24: Wake Word Solution
**Content**:
- Issue: HA companion app doesn't support wake word
- Solution: Hey Jarvis (https://github.com/fwartner/home-assistant-wakewords-collection)
- Working: Timers ✓
- Not working: Alarms ✗

**Visual**: Hey Jarvis GitHub screenshot

---

#### Slide 25: Home Assistant Screenshot
**Content**:
- Running on Echo Show Gen 2
- Full HA OS (not Docker)
- Voice assistant integrated

**Visual**: `/tmp/ha.jpeg`

---

### Part 7: Concrete Signs (3 minutes)

#### Slide 26: From AI to Physical
**Content**:
- December 1: "I am going to use it to create a 3d printed cast for a silicone mold so I can some desktop signs out of concrete."
- For PE: "She's always belaboring the need to get concrete and not speak in abstract."
- Etsy potential

**Visual**: Process flow diagram

---

#### Slide 27: Concrete Sign Molds
**Content**:
- OpenSCAD designs
- "example" - Cursive (Dancing Script)
- "use case" - Times New Roman
- Dimensions: 12" x 2" x 2"

**Files**:
- `example_sign_mold.scad`
- `use_case_sign_mold.scad`
- `generate.py`

**Visual**: `/opt/opencode/src/concrete/sign-molds/example_sign_mold_preview.png`

---

#### Slide 28: Process
**Content**:
1. AI generates OpenSCAD design
2. Export to STL
3. 3D print mold (PETG/ABS)
4. Create silicone mold
5. Cast concrete
6. Finish and sell

**Visual**: Step-by-step photos (if available)

---

### Part 8: Lessons Learned (4 minutes)

#### Slide 29: What Worked ✓
**Content**:
- Cline + Qwen3-Coder: "Making some really good results"
- Prompt caching: "Things are really humming now"
- AMD GPU libraries: 2x performance improvement
- Home Assistant: Fully functional
- WWS: Months of development, now complete

**Visual**: Green checkmarks

---

#### Slide 30: What Didn't ✗
**Content**:
- Memory addressing: Never got full 128GB (only 96GB)
- Ollama stability: GPU crashes after upgrades
- NPU support: Still in development
- Context scaling: Sharp TPS decline >64k
- February 3: "6 days out of return policy i am having strix remorse"

**Visual**: Red X marks

---

#### Slide 31: Key Insights
**Content**:
1. **Hardware Hype vs Reality**: APU architecture challenges are real
2. **Software Maturity**: Latest kernel + ROCm essential
3. **Context is King**: Prompt caching transforms workflow
4. **Tooling Evolution**: Cline + Qwen3-Coder > traditional IDEs
5. **From Digital to Physical**: AI can create real-world objects
6. **Repurposing Hardware**: Echo → Home Assistant = Win
7. **Autonomous Development**: Possible, but requires tuning

**Visual**: Key insights graphic

---

#### Slide 32: The Terminator Warning
**Content**:
- December 5: "Lol I've been talking about terminator all week long. When some fool starts training moe models on movies and terminator sneaks in and then we ask the AI to program the androids to be ready for tomorrow outcomes..."

**Visual**: Terminator movie poster (optional, fair use)

---

### Closing (3 minutes)

#### Slide 33: Future Work
**Content**:
- **Immediate**: NPU support stabilization, memory optimization
- **Long-term**: Multi-GPU/NPU orchestration, custom wake words
- **WWS**: Phase 3 (Cloud providers)
- **Performance**: Better context scaling

**Visual**: Roadmap graphic

---

#### Slide 34: Q&A
**Content**:
**Questions to Consider**:
1. Is Strix Halo ready for production AI workloads?
2. When will NPU support mature?
3. How do we solve the 128GB addressing issue?
4. What's the best backend for multi-model setups?
5. Is autonomous development the future?

**Contact**: github.com/winmutt

**Visual**: Q&A graphic

---

#### Slide 35: Thank You
**Content**:
- Thank you for your time
- GitHub: https://github.com/winmutt
- WWS: https://github.com/winmutt/wws
- Reddit: r/LocalLLaMA
- Home Assistant community

**Visual**: Contact info with QR codes

---

## Visual Assets Checklist

### Images to Include
- [ ] `/tmp/ha.jpeg` - Home Assistant on Echo
- [ ] `/opt/opencode/src/winmutt/wws/docs/screenshots/dashboard.png` - WWS Dashboard
- [ ] `/opt/opencode/src/concrete/sign-molds/example_sign_mold_preview.png` - Concrete sign mold
- [ ] `/opt/opencode/src/concrete/sign-molds/example_sign_positive_preview.png` - Concrete sign positive
- [ ] AMD Strix Halo APU image (external)
- [ ] GitHub profile screenshot (external)

### Diagrams to Create
- [ ] Strix Halo architecture diagram
- [ ] Memory placement (VRAM vs GTT)
- [ ] WWS architecture diagram
- [ ] Prompt caching workflow
- [ ] Performance graphs (TPS vs context)
- [ ] Timeline graphics

### Charts to Generate
- [ ] TPS performance over time
- [ ] Context size vs performance
- [ ] Project progress (WWS phases)

---

## Speaker Notes

### Timing Guide
- Opening: 3 minutes
- Part 1 (Decision): 5 minutes
- Part 2 (Hardware): 7 minutes
- Part 3 (Software): 8 minutes
- Part 4 (Performance): 7 minutes
- Part 5 (WWS): 6 minutes
- Part 6 (Home Assistant): 5 minutes
- Part 7 (Concrete): 3 minutes
- Part 8 (Lessons): 4 minutes
- Closing: 3 minutes
- **Total**: 51 minutes (adjust for Q&A)

### Key Messages
1. AMD Strix Halo is powerful but has challenges
2. Software maturity matters as much as hardware
3. Prompt caching is a game-changer for AI workflows
4. Autonomous development is achievable with the right setup
5. From AI code to physical objects is possible

### Demo Ideas
- Live WWS dashboard demo (if possible)
- Home Assistant on Echo demonstration
- Concrete sign physical display (if created)

---

## References

### Documents
- `/opt/opencode/src/self-2026/AMD_STRIX_TALK_README.md`
- `/opt/opencode/src/self-2026/AMD_STRIX_TALK_SLIDES.md`
- `/opt/opencode/src/self-2026/SLIDE_DECK_INDEX.md`
- `/opt/opencode/src/self-2026/CHAT_TO_PROJECT_REFERENCE.md`

### Projects
- WWS: https://github.com/winmutt/wws
- Lemonade: https://github.com/winmutt/lemonade
- Cline: https://github.com/winmutt/cline
- Concrete: `/opt/opencode/src/concrete/sign-molds/`

### Communities
- Reddit r/LocalLLaMA
- XDA Forums Amazon Echo
- Home Assistant community

---

**Created**: May 2026  
**Author**: winmutt  
**Version**: 1.0
