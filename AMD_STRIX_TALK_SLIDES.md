# Building an AI Workstation: 6 Months with AMD Strix Halo

## A Journey from Hardware Hype to Real-World Autonomous Development

---

## Speaker Introduction

- **Background**: Software engineer, open source contributor
- **Current Setup**: AMD Strix Halo APU workstation (128GB LPDDR5X-8000)
- **Timeline**: November 2025 - May 2026
- **Focus**: Local LLMs, autonomous development, home automation

---

## Agenda (45 minutes)

1. **The Decision** (5 min) - Why AMD Strix Halo?
2. **Hardware Reality** (7 min) - 128GB APU architecture
3. **Software Stack Evolution** (8 min) - Lemonade, Ollama, ROCm
4. **Performance Deep Dive** (7 min) - TPS, context windows, bottlenecks
5. **Project: WWS** (6 min) - Vibe-coded workspace system
6. **Project: Home Assistant** (5 min) - Alexa replacement on Echo
7. **Project: Concrete Signs** (3 min) - From AI to physical objects
8. **Lessons Learned** (4 min) - What worked, what didn't

---

## Part 1: The Decision

### Why AMD Strix Halo?

**Your Original Setup**:
- Generic home PC with RTX 3060 (6GB GDDR6 VRAM)
- 128GB of RAM (shared with GPU via 6GB GDDR6)
- Performance was poor across the shared 6GB GDDR6 VRAM

**The Strix Halo Journey**:
```
November 22, 2025
"BTW I have a corsair 300 AMD 395 max+ enroute. 
Sold my 3060 rig today."
```

**The Pitch**:
- 128GB unified memory (LPDDR5X-8000) - SOLDERED to APU
- Fastest "nom" VRAM available (8000 MT/s LPDDR5X)
- NPU for AI acceleration
- No discrete GPU needed - single APU solution

**The Trade**:
- Sold NVIDIA RTX 3060 rig (6GB GDDR6)
- Invested in 128GB RAM first (perhaps should have held onto that investment)
- Performance issues: shared 6GB GDDR6 VRAM was bottleneck
- Black Friday 2025: $1800 for Corsair 128GB Strix Halo system
- **Note**: Corsair 300 shares motherboard with other Strix Halo manufacturers (Sixunited)
- **Today**: Similar high-end systems start at ~$3000+ (RTX 4090 configurations)
  - "Today's price" quote: "The Strix Halo was a bargain at $1800 for what it delivers - 
    today you'd pay 2x that for equivalent performance with discrete GPU"

---

## Part 2: Hardware Reality

### AMD Strix Halo Architecture

```
┌─────────────────────────────────────────┐
│           AMD Strix Halo APU            │
│  ┌─────────────┐  ┌─────────────┐       │
│  │ Core Die 1  │  │ Core Die 2  │       │
│  │ 64MB L3     │  │ 64MB L3     │       │
│  └─────────────┘  └─────────────┘       │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │   128GB LPDDR5X-8000 (soldered) │   │
│  │   (Only 96GB addressable)       │   │
│  └─────────────────────────────────┘    │
│                                         │
│  GPU | NPU | Media Engine               │
└─────────────────────────────────────────┘
```

**Key Challenge**: 
- 128GB total, only 96GB accessible initially
- Memory placement: VRAM vs GTT issues
- Swapping despite unified memory

---

## Part 3: Software Stack Evolution

### Agent Configuration & MTP Improvements

**Current Models**:
- Qwen3.6-35B-A3B-MTP-GGUF (go-to today)
- Qwen3-Coder-Next-GGUF (coding)
- Flux-2-Klein-9B-GGUF (image gen)
- Whisper-Large-v3-Turbo (speech)
- Kokoro-v1 (TTS)
- And more...

**Multi-Token Prediction (MTP)**:
- MTP = Multi-Token Prediction capability
- Qwen series models with MTP-GGUF files
- Predicts multiple tokens in single forward pass
- Significantly improves throughput and reduces latency

**Agent Selection**:
- Cline: Good for direct coding tasks
- Opencode: Preferred for portable web UI experience
- Makes it portable for mobile/different locations

---

### The Backend War: Lemonade vs Ollama

| Feature | Lemonade | Ollama |
|---------|----------|--------|
| Backend | llama.cpp + ROCm | Various |
| Observability | Good (token batching visible) | Poor |
| NPU Support | In development | Patch available |
| Stability | Issues after OS upgrade | GPU crashes |
| Multi-model | Yes (2 models + OpenCode) | Limited |

**November 28**: "Using lemonade instead of ollama. Working on getting NPUs working."

**December 7**: "Went back to using ollama. lemonade-server, for whatever reason, was not behaving properly"

---

## Part 3: Software Stack (continued)

### The Resurgens Moment

```
December 14
"Upgraded OS and ollama last night and sad things happened.
GPU crashes about 3-4 prompts in"
```

**Phoenix Rising Out of the Ashes**:
- System reinstalled and formatted
- Fresh kernel, fresh ROCm, fresh hope
- Led to AMD GPU library update (Jan 29)

**January 29 Victory**:
"I got the new amd GPU libraries working on my strix halo 
and stable and its 2x faster than before."

---

## Part 4: Performance Deep Dive

### Token Processing Performance

| Context Size | TPS | Notes |
|--------------|-----|-------|
| <100k tokens | ~40 | Consistent |
| 100k-200k | ~14-18 | Degradation |
| >200k tokens | ~8-18 | Variable |
| >64k (ingress) | N/A | Sharp TPS drop |

**December 14 Benchmark**:
```
prompt eval: 284.73 tokens/sec (3.51ms/token)
generation:  46.27 tokens/sec (21.61ms/token)
total:       1080 tokens in 8.788s
```

**May 30, 2026 - Recent ~200k Token Processing**:
```
Input tokens:    193,795
Output tokens:   5,997
TTFT (s):        2,267.139
TPS:             18.65
```

---

## Part 4: Performance (continued)

### The Memory Placement Problem

```
┌────────────────────────────────────┐
│         Unified Memory (128GB)      │
│  ┌──────────────┬────────────────┐  │
│  │    VRAM      │      GTT       │  │
│  │  (Fast)      │  (Slower)      │  │
│  │  Model loads │  Model loads   │  │
│  │  here ✓      │  here ✗        │  │
│  └──────────────┴────────────────┘  │
└────────────────────────────────────┘
```

**February 3 Insight**:
"One thing I have learned is its important to get the 
kv cache in vram too, not just the model."

**February 8 Progress**:
"Getting 24tps now on a single thread."

---

## Part 4: Performance (continued)

### Prompt Caching Breakthrough

**March 11**: "I think I got into full autonomous mode this morning."

```
┌──────────────────────────────────────────┐
│      Prompt Caching Architecture         │
│                                          │
│  Prompt 1 (cached) ──┐                  │
│  Prompt 2 (cached) ──┼──> Multi-task    │
│  New requests ───────┘   without reload │
│                                          │
│  2 cached prompts = ~8GB memory         │
└──────────────────────────────────────────┘
```

**Key Achievement**: Latest llama.cpp fixed prompt caching

---

## Part 5: Project WWS

### Winmutt Work Spaces

**GitHub**: https://github.com/winmutt/wws

```
May 12: "Definitely no Athena and its taken months 
to get there but this is something I entirely 
vibe coded."
```

**What is WWS?**
- Remote workspace provisioning system
- KVM/Podman-based isolated environments
- code-server (VSCode) integration
- GitHub OAuth + RBAC
- Team collaboration features

**Tech Stack**: Go, React, SQLite, KVM, Podman

---

## Part 5: WWS Architecture

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
│  KVM    │ │  Podman  │ │ Digital  │
│  VMs    │ │ Containers│ │Ocean     │
└─────────┘ └──────────┘ └──────────┘
```

**Status**: Phase 2 complete (Team Features)

---

## Part 5: WWS Autonomous Development

### The Autonomous Mode

**March 11 Setup**:
- Sub-agents running on Qwen 3.5 9B
- NPU support in development
- Prompt caching enabled
- Leveraging other providers/GPUs for sub-agents

**Tools**:
- Cline + Qwen3-Coder (VS Code extension)
- 400k context window
- Multiple OpenCode instances
- "The tuition just needs to catch up with the vscode extension"

---

## Part 6: Home Assistant on Echo

### LineageOS Installation Journey

**December 2025**: Started exploring XDA Forums for Echo device hacking

**Key Threads**:
- https://xdaforums.com/t/rom-unofficial-11-checkers-lineageos-18-1-for-the-amazon-echo-show-5-2019.4763475/
- https://xdaforums.com/t/unlock-root-twrp-unbrick-amazon-echo-show-5-1st-gen-2019-checkers.4762900/

**Process**:
1. Unlock bootloader via amonet exploit
2. Create stock backup (critical!)
3. Install TWRP recovery
4. Flash LineageOS 18.1 (Android 11)
5. Configure ViewAssist for Home Assistant

**Quote**: "Basically anything with a USB port. If there is a port, there is a way."

---

### Alexa Replacement Journey

**December 6**: Started exploring XDA forums
"Basically anything with a USB port. If there is a 
port, there is a way."

**Timeline**:
- **Dec 6**: Started exploring XDA forums for Echo device hacking
- **Dec 7**: Started using Home Assistant on Echo devices
- **Jan 19**: HA setup on Echo Show Gen 2
- **Jan 21**: Everything working except wake word
- **Jan 25**: Wake word sorted with Hey Jarvis
- **Jan 29**: End-to-end complete
- **Feb 2026**: Echo 8 mic stability testing (ongoing)
- **Jan 7, 2026**: Issue #4 filed - Echo 8 audio stops after ~24h

**Hardware**: Echo Show Gen 2, Echo Spot (eBay), Echo 8 (main device)

---

### The Echo 8 Mic Issue

**Issue**: Audio stops working after ~24 hours on Echo 8

**Reference**: https://github.com/amazon-oss/releases/issues/4

**Context**: 
- Using LineageOS 18.1 (checkers for Echo 5, crown for Echo 8)
- Both devices running ViewAssist for STT/TTS
- Echo 5: Mic stable for days
- Echo 8: Audio issue after ~24 hours, similar to Echo 5's original problem
- Fix applied to Echo 5 (Build 3) but not yet to Echo 8
- User: lawhazl reported issue on Jan 7, 2026

**Quote**: "I've got the Echo 8 and Echo 5... The mic on the Echo 5 and 8 is stable and will constantly listen without issue for days at a time without a reboot. However, the Echo 8 seems to exhibit the audio issue that the Echo 5 originally had until that was fixed in a later build."

**Status**: Issue filed on Jan 7, 2026 - awaiting fix

---

### Alexa Replacement Journey (continued)

---

## Part 6: Home Assistant Architecture

```
┌─────────────────────────────────────────┐
│         Amazon Echo Show Gen 2          │
│  ┌───────────────────────────────────┐  │
│  │      Home Assistant OS            │  │
│  │  (Not Docker container!)          │  │
│  │                                   │  │
│  │  Wake Word: Hey Jarvis            │  │
│  │  Actions: Timers ✓ Alarms ✗       │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

**Key Discovery**: "You need the full blown HA OS not the 
docker container for voice assist."

**Reference**: https://github.com/fwartner/home-assistant-wakewords-collection

---

## Part 7: Concrete Sign Molds

### From AI to Physical Objects

**December 1**: 
"I am going to use it to create a 3d printed cast 
for a silicone mold so I can some desktop signs 
out of concrete."

**The Motivation**:
"For my PE, she's always belaboring the need to 
get concrete and not speak in abstract."

**Etsy Potential**: "Thought I'd sell some on Etsy too."

---

## Part 7: Concrete Signs Project

### Files and Models

**Location**: `/opt/opencode/src/concrete/sign-molds/`

| File | Purpose |
|------|---------|
| `example_sign_mold.scad` | Mold for raised cursive "example" |
| `use_case_sign_mold.scad` | Mold for embossed "use case" |
| `example_sign_positive.stl` | 3D print for mold creation |
| `generate.py` | Automated STL export |

**Dimensions**: 12" x 2" x 2" (304.8mm x 50.8mm x 50.8mm)
**Fonts**: Dancing Script (cursive), Times New Roman

**Process**: AI design → 3D print mold → Silicone → Concrete cast

---

## Part 8: Lessons Learned

### What Worked

✓ **Cline + Qwen3-Coder**: "Making some really good results"
✓ **Prompt Caching**: "Things are really humming now"
✓ **AMD GPU Libraries Update**: 2x performance improvement
✓ **Home Assistant**: Fully functional on repurposed Echo
✓ **WWS Project**: Months of development, now complete

### What Didn't

✗ **Memory Addressing**: Never got full 128GB (only 96GB)
✗ **Ollama Stability**: GPU crashes after upgrades
✗ **NPU Support**: Still in development (Mar 11)
✗ **Context Scaling**: Sharp TPS decline >64k

---

## Part 8: Key Insights

### Performance Reality

**Strix Halo Architecture**:
- "Supposed to be good at PP (prefill) and not inference"
- Linear performance regression observed (Feb 3)
- "6 days out of return policy i am having strix remorse"

**Context Window Tradeoffs**:
- 400k window achievable
- 14 TPS at 200k window
- 8 TPS at >200k tokens
- Ingress performance worse than generation

### The Repeatable Work Philosophy

**November 29**:
"Why not use the mcp. I guess its repeatable with python. 
That's something I've been focused on lately. 
Not just doing the work but making it repeatable."

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

## Future Work

### Immediate
- NPU support stabilization
- Memory addressing optimization
- Core affinity management (PR for lemonade/llama.cpp)

### Long-term
- Multi-GPU/NPU orchestration
- Better observability for Ollama
- Custom wake word training
- WWS Phase 3 (Cloud providers)

### The Terminator Warning

**December 5**:
"Lol I've been talking about terminator all week long. 
When some fool starts training moe models on movies 
and terminator sneaks in and then we ask the AI to 
program the androids to be ready for tomorrow outcomes..."

---

## Q&A

### Questions to Consider

1. Is Strix Halo ready for production AI workloads?
2. When will NPU support mature?
3. How do we solve the 128GB addressing issue?
4. What's the best backend for multi-model setups?
5. Is autonomous development the future?

**Contact**: github.com/winmutt

---

## Appendix: Performance Charts

### TPS vs Context Size

```
40 ┤     ●
   │    ╱
30 ┤   ╱
   │  ╱
20 ┤ ╱     ●
   │╱     ╱
10 ┤     ●    ╱   ●
   └────┬────┬────┬───
       50k  100k  200k
           Context (tokens)
```

### Timeline of Major Milestones

```
Nov ┤ ● Hardware arrives
Dec ┤ ●●● Software struggles
Jan ┤ ●● Breakthrough
Feb ┤ ● Performance tuning
Mar ┤ ● Autonomous mode
May ┤ ● WWS complete
```

---

## References

### Projects
- WWS: https://github.com/winmutt/wws
- Concrete Signs: /opt/opencode/src/concrete/sign-molds/
- Home Assistant Wake Words: https://github.com/fwartner/home-assistant-wakewords-collection

### Communities
- Reddit r/LocalLLaMA: 8 Local LLMs on Strix Halo
- XDA Forums: Amazon Echo development
- GitHub: winmutt (8 repos, forks of lemonade, cline, vscode)

### Screenshots
- Home Assistant on Echo: `/opt/opencode/src/self-2026/assets/ha.jpeg`
- WWS Dashboard: `/opt/opencode/src/self-2026/assets/dashboard.png`
- Concrete Sign Molds: `/opt/opencode/src/self-2026/assets/concrete_sign.png`
- All assets in: `/opt/opencode/src/self-2026/assets/`
