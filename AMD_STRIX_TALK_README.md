# AMD Strix Halo Experience - 45 Minute Talk

## Overview
This document provides context for creating a slide deck about 6 months of experience with an AMD Strix Halo AI workstation (Nov 2025 - May 2026).

## Project Context

### Hardware
- **Machine**: Corsair 300 AMD 395 Max+ with AMD Strix Halo APU
- **Memory**: 128GB LPDDR5X-8000 (soldered to APU)
- **Architecture**: Single APU with 2 core dies, 2x64MB L3 caches
- **Status**: Sold NVIDIA 4060 rig, transitioned to APU-only setup

### Key Projects

#### 1. WWS (Winmutt Work Spaces) - https://github.com/winmutt/wws
- **Status**: Fully vibe-coded (May 2026)
- **Description**: Remote workspace provisioning system for engineering teams
- **Tech Stack**: Go backend, React frontend, KVM/Podman, SQLite
- **Features**: 
  - Isolated development environments
  - Persistent storage with resource quotas
  - code-server (VSCode) integration
  - GitHub OAuth + RBAC
  - Team collaboration features
- **Timeline**: Months of development, achieved "no Athena" autonomous mode

#### 2. Concrete Sign Molds - /opt/opencode/src/concrete/sign-molds/
- **Purpose**: 3D printable molds for casting concrete desktop signs
- **Connection**: Created for PE (Partner/Engineer) who emphasizes "concrete not abstract"
- **Files**: 
  - `example_sign_mold.scad` - Raised cursive "example" in Dancing Script
  - `use_case_sign_mold.scad` - Embossed "use case" in Times New Roman
- **Etsy potential**: Intended for sale

#### 3. Home Assistant on Amazon Echo
- **Goal**: Replace Alexa with Home Assistant
- **Devices**: Echo Show Gen 2, Echo Spot (eBay purchase)
- **Timeline**:
  - Dec 6: Started exploring XDA forums for Amazon Echo hacking
  - Jan 19: Got linkages and HA setup on Echo Show Gen 2
  - Jan 21: Fully working except wake word
  - Jan 25: Wake word sorted using Hey Jarvis
  - Jan 29: End-to-end working
- **Screenshot**: /tmp/ha.jpeg

### AI/LLM Stack Evolution

#### Backend Choices
1. **Lemonade** (Nov 28 - Dec 7)
   - Uses llama.cpp + ROCm backend
   - Good metrics/observability (token batching visible)
   - Issue: Not behaving properly after OS upgrade
   - PR work: Core affinity management for Strix dual-die architecture

2. **Ollama** (Dec 7+, intermittent issues)
   - Patch exists for APU support
   - Poor metrics/observability
   - GPU crashes after 3-4 prompts post-upgrade (Dec 14)

#### Models Used
- **Qwen3-Coder**: Primary coding model, stable after tuning
- **Qwen 3.5 9B**: Sub-agents with NPU support (Mar 11)

#### Performance Metrics
- **<100k tokens**: ~40 TPS consistent
- **>200k tokens**: Drops to 8-18 TPS (variable)
- **64k+ context**: Sharp TPS decline on ingress (not generation)
- **Dec 14 Performance**:
  - Prompt eval: 284.73 tokens/sec (3.51ms/token)
  - Generation: 46.27 tokens/sec (21.61ms/token)
  - Total: 1080 tokens in 8.788s
- **Feb 8**: 24 TPS single-threaded with lemonade
- **Feb 29**: AMD GPU libraries update = 2x faster
- **May 30, 2026**: 18.65 TPS at ~200k tokens (TTFT: 2,267s)

#### Key Technical Challenges
1. **Memory addressing**: Only 96GB of 128GB accessible initially
2. **Memory placement**: Models loading to GTT instead of VRAM, causing swap thrashing
3. **KV Cache**: Critical to get KV cache in VRAM, not just model
4. **Strix Architecture**: Supposed to be good at Prefill (PP), not inference
5. **Performance regression**: Linear degradation in token processing observed (Feb 3)
6. **Prompt caching**: Fixed in latest llama.cpp (Mar 11)

#### Autonomous Development Setup
- **Tools**: Cline + Qwen3-Coder (VS Code extension)
- **Context Window**: 400k tokens (achieved ~14 TPS at 200k window)
- **Caching**: Prompt caching allows multi-tasking without reload
  - 2 cached prompts = ~8GB memory
- **Sub-agents**: Qwen 3.5 9B with NPU support (Mar 11)
- **Multi-model**: Running 2 models with multiple OpenCode instances

### Timeline Summary

| Date | Event |
|------|-------|
| Nov 22 | Corsair 300 AMD 395 Max+ ordered, 4060 rig sold |
| Nov 28 | Started with Lemonade, working on NPU support |
| Nov 29 | 400k context window, 96GB of 128GB accessible |
| Dec 1 | Concrete sign molds project started |
| Dec 5 | Terminator AI discussions |
| Dec 6 | Home Assistant on Echo exploration begins |
| Dec 7 | Switched back to Ollama (Lemonade issues) |
| Dec 9 | TPS performance issues >64k context |
| Dec 14 | GPU crashes after OS/ollama upgrade |
| Jan 19 | HA on Echo Show Gen 2, no voice assistant |
| Jan 21 | Everything working except wake word |
| Jan 25 | Wake word sorted with Hey Jarvis |
| Jan 29 | New AMD GPU libraries = 2x faster, HA complete |
| Feb 3 | "Strix remorse" - performance regression observed |
| Feb 8 | Lemonade PR for core affinity, 24 TPS single-thread |
| Mar 11 | Full autonomous mode with prompt caching, NPU dev |
| May 12 | WWS fully vibe-coded |

### Key Learnings
1. **Repeatable workflows**: Focus on making work repeatable with Python/MCP
2. **Hardware limitations**: Strix Halo memory architecture challenges
3. **Software maturity**: Need for latest kernel/Ubuntu for APU support
4. **Tooling evolution**: Cline+Qwen3-Coder vs Ollama vs Lemonade tradeoffs
5. **Context caching**: Critical for multi-agent workflows
6. **NPU potential**: Still in development, future optimization target

### References
- GitHub: https://github.com/winmutt (8 repos, including forks of lemonade, cline, vscode)
- Reddit: https://www.reddit.com/r/LocalLLaMA/comments/1pdh0sm/8_local_llms_on_a_single_strix_halo_debating/
- XDA Forums: https://xdaforums.com/f/amazon-echo.6148/
- Hey Jarvis wake words: https://github.com/fwartner/home-assistant-wakewords-collection/tree/main/en

### Assets
- `/tmp/ha.jpeg` - Home Assistant on Echo Show screenshot
- `/opt/opencode/src/concrete/sign-molds/` - Concrete sign mold projects
- `/opt/opencode/src/winmutt/wws/` - WWS project with full documentation
