# AMD Strix Halo Experience - Chat to Project Reference

This document maps chat snippets to actual projects, GitHub activity, and technical details.

---

## November 2025

### November 22, 2025
```
"BTW I have a corsair 300 AMD 395 max+ enroute. Sold my 4060 rig today."
```

**Context**: Hardware acquisition
- **Hardware**: Corsair 300 AMD 395 Max+ with AMD Strix Halo APU
- **Trade**: Sold NVIDIA 4060 rig (discrete GPU setup)
- **Significance**: Going all-in on APU architecture
- **Related**: No direct GitHub activity, but marks start of timeline

---

### November 28, 2025
```
"Using lemonade instead of ollama. There is a patch for ollama 
that will make it work with the APU, but I've been working to 
get the NPUS working as well. Having to run latest kernel and 
Ubuntu. Main issue has really only been addressing the full 128g. 
Sometimes it loads the models into gtt instead of vram and seems 
to spend a lot of time swapping in and out even though its all 
the same memory."
```

**Related Projects**:
1. **Lemonade**: https://github.com/winmutt/lemonade (fork)
   - Backend: llama.cpp + ROCm
   - NPU support: In development
   
2. **Ollama**: 
   - Patch exists for APU support
   - Not forked by winmutt

**Technical Details**:
- Memory addressing issue: 128GB → 96GB accessible
- Memory placement: GTT vs VRAM confusion
- Kernel requirement: Latest Ubuntu kernel needed

**GitHub Activity**:
- Fork of lemonade-sdk/lemonade exists
- No specific PRs mentioned for NPU support yet

---

### November 29, 2025 (Multiple messages)

#### Message 1
```
"Why not use the mcp. I guess its repeatable with python. 
That's something I've been focused on lately. Not just doing 
the work but making it repeatable."
```

**Related Projects**:
1. **WWS** - https://github.com/winmutt/wws
   - Focus on repeatable workflows
   - Python scripts for automation
   - MCP (Model Context Protocol) integration

**Technical Details**:
- Philosophy shift: From one-off work to repeatable processes
- Python as automation language
- MCP integration for AI tooling

**GitHub Activity**:
- WWS project shows extensive automation
- `generate.py` in concrete project shows repeatable approach

#### Message 2
```
"I've really been liking Cline lately. Cline+qwen3-coder is 
making some really good results."
```

**Related Projects**:
1. **Cline**: https://github.com/winmutt/cline (fork)
   - VS Code extension for autonomous coding
   - Forked from cline/cline
   
2. **Qwen3-Coder**: 
   - Model used with Cline
   - Primary coding model

**Technical Details**:
- Tool combination: Cline (IDE) + Qwen3-Coder (model)
- Result: High-quality code generation
- VS Code extension ecosystem

**GitHub Activity**:
- Fork of cline/cline exists
- Active development on integration

#### Message 3
```
"I've got a 400k context window with the new Ai workstation. 
Still need to work on tuning it, was getting about 45tps and 
was around 14tps when I left it last night with a nearly 200k 
window"
```

**Technical Details**:
- Context window: 400k tokens achievable
- Performance:
  - Initial: 45 TPS
  - After tuning: 14 TPS at 200k window
- Degradation: Linear with context size

**Related Projects**:
- WWS autonomous development setup
- Multiple OpenCode instances

#### Message 4
```
"Its 128g total but I've only been able to get it to address 96. 
Currently with qwen3-coder and 400k window its using about 59g. 
Using lemonade which uses llama.cpp and rocm on the backend"
```

**Technical Details**:
- Memory: 128GB total, 96GB addressable
- Model memory: Qwen3-Coder + 400k = 59GB
- Backend: llama.cpp + ROCm via Lemonade

**Related Projects**:
- Lemonade: https://github.com/winmutt/lemonade

#### Message 5
```
"The cool thing is that it will cache the prompt and just keep 
building on it. So you can multi task wo having to reload the 
prompt context every time. Caching 2 prompts took about 8g"
```

**Technical Details**:
- Prompt caching: Key feature for multi-tasking
- Memory cost: 2 prompts = 8GB
- Benefit: No reload overhead

**Related**:
- llama.cpp prompt caching
- Later fixed in March 2026

#### Message 6
```
"Cline is really decent, the tuition just needs to catch up 
with the vscode extension"
```

**Context**:
- Cline extension quality: High
- Documentation ("tuition"): Needs improvement
- VS Code ecosystem maturity

#### Message 7
```
"No but it lpddr5x-8000 and soldered to the apu board. Its 
basically the fastest nom vram out there."
```

**Technical Details**:
- Memory type: LPDDR5X-8000
- Configuration: Soldered to APU
- Performance: Fastest "nom" (non-discrete) VRAM

#### Message 8
```
"Under 100k tokens I get 40ish tps consistently. >200k it goes 
down to 8tps"
```

**Performance Data**:
| Context | TPS |
|---------|-----|
| <100k | ~40 |
| >200k | ~8 |

**Related**:
- Context scaling challenges
- Ingress vs generation performance

---

## December 2025

### December 1, 2025
```
"Wow that's cool. I am going to use it to create a 3d printed 
cast for a silicone mold so I can some desktop signs out of 
concrete. One will read 'example' and the other 'use case'. 
It's for my PE, she's always belaboring the need to get 
concrete and not speak in abstract. Thought I'd sell some 
on Etsy too."
(Look at ~opencode/src/concrete for most recent incarnation)
```

**Related Project**: **Concrete Sign Molds**
- **Location**: `/opt/opencode/src/concrete/sign-molds/`
- **Files**:
  - `example_sign_mold.scad` - Mold for "example"
  - `use_case_sign_mold.scad` - Mold for "use case"
  - `example_sign_positive.scad` - Positive model
  - `use_case_sign_positive.scad` - Positive model
  - `models.scad` - Shared definitions
  - `generate.py` - Automation script
  - `*.stl` - Exported models
  - `*_preview.png` - Preview images

**Process**:
1. AI generates design (OpenSCAD)
2. Export to STL
3. 3D print mold
4. Create silicone mold
5. Cast concrete
6. Finish and sell

**Motivation**:
- For PE (Partner/Engineer)
- Theme: "Concrete not abstract"
- Etsy sales potential

**GitHub Activity**:
- Local project (not on GitHub yet)
- OpenSCAD files show version control readiness

---

### December 5, 2025
```
"Lol I've been talking about terminator all week long. When 
some fool starts training moe models on movies and terminator 
sneaks in and then we ask tge AI to program the androids to 
be ready for tomorrow outcomes..."
```

**Context**: 
- AI safety discussion
- Terminator movie references
- Mixture of Experts (MoE) models trained on movies
- Warning about unintended consequences

**Related**:
- No direct project
- Theme appears in talk conclusion

---

### December 6, 2025
```
"https://xdaforums.com/f/amazon-echo.6148/"
(I started looking at using home assistant as an alexa replacement)
```

**Related Project**: **Home Assistant on Echo**
- **External Reference**: https://xdaforums.com/f/amazon-echo.6148/
- **Goal**: Replace Alexa with Home Assistant
- **Devices**: Echo Show Gen 2, Echo Spot

**Technical Details**:
- XDA Forums: Community for device hacking
- Home Assistant: Open source home automation
- Voice assistant replacement

---

```
"Basically anything with a USB port. Thats definitely an 
overstatement, but if there is a port, there is a way. I 
really want to do the amazon flexs. We bought them because 
they were cheap and plug right into the wall. The sound 
quality sucks, but to have a device in every room was pretty 
easy. Ended up buying an echo spot on ebay."
```

**Technical Details**:
- Philosophy: "If there is a port, there is a way"
- Target: Amazon Flex devices (wall-plug)
- Constraint: Sound quality vs convenience
- Purchase: Echo Spot on eBay

**Related**:
- Hardware repurposing theme
- Home automation project

---

### December 7, 2025

#### Morning
```
"Went back to using ollama. lemonade-server, for whatever 
reason, was not behaving properly"
```

**Context**:
- Backend switch: Lemonade → Ollama
- Issue: Lemonade stability problems
- Possible cause: OS upgrade (confirmed Dec 14)

**Related Projects**:
- Lemonade: https://github.com/winmutt/lemonade
- Ollama: Not forked

---

#### Evening
```
"https://www.reddit.com/r/LocalLLaMA/comments/1pdh0sm/8_local_llms_on_a_single_strix_halo_debating/"
```

**External Reference**:
- Reddit: r/LocalLLaMA
- Thread: 8 Local LLMs on Strix Halo
- Community discussion about multi-model setups

**Related**:
- Demonstrates community interest
- Validates Strix Halo as AI workstation

---

### December 9, 2025
```
"The TPS goes down pretty sharply >64k context. I dont know 
why. But that's on ingress, not generation. Are using vscode 
extension or somethint?"
```

**Technical Details**:
- Performance cliff: >64k context
- Issue location: Ingress (prompt processing), not generation
- Question: VS Code extension impact?

**Related**:
- Performance investigation ongoing
- Later resolved with prompt caching (Mar 11)

---

### December 14, 2025
```
"I think thats the only backend I can run. Upgraded OS and 
ollama last night and sad things happened. GPU crashes about 
3-4 prompts in"

prompt eval time =    2823.77 ms /   804 tokens (    3.51 ms per token,   284.73 tokens per second)
eval time =    5964.43 ms /   276 tokens (   21.61 ms per token,    46.27 tokens per second)
total time =    8788.20 ms /  1080 tokens
```

**Context**:
- "Resurgens" moment: System reinstall
- Trigger: OS + Ollama upgrade
- Symptom: GPU crashes after 3-4 prompts

**Performance Data**:
```
Prompt eval:  284.73 tokens/sec (3.51ms/token)
Generation:   46.27 tokens/sec (21.61ms/token)
Total:        1080 tokens in 8.788s
```

**Related**:
- Phoenix rising: Fresh install leads to improvements
- Later: AMD GPU library update (Jan 29) = 2x faster

---

## January 2026

### January 19, 2026
```
"Got linkages and home assistant setup on a echo show gen 2. 
Still haven't figure out voice assistant yet. Discovered you 
need the full blown HA OS not the docker container for voice 
assist."
```

**Related Project**: **Home Assistant on Echo**
- **Device**: Echo Show Gen 2
- **Progress**: HA OS installed
- **Issue**: Voice assistant not working
- **Discovery**: Need HA OS, not Docker container

**Technical Details**:
- Home Assistant OS vs Docker
- Voice assistant requires full OS
- Linkages configured

---

### January 21, 2026
```
"Fully working everything but wake word. I dont know why but 
HA companion app doesn't support it"
```

**Progress**:
- Everything working except wake word
- Issue: HA companion app limitation
- Next: Find alternative wake word solution

---

### January 25, 2026
```
"I got the wake word sorted and now have a fully functiong * 
echo. I wasn't able to get the voice assistant to set an alarm 
but I did get it to set a timer."
```

**Progress**:
- Wake word: Working
- Voice assistant: Partial (timers ✓, alarms ✗)
- Status: "Fully functioning"

**External Reference**:
```
"i havent trained my own yet, but I am using Hey Jarvis 
(Alexa is another option)
https://github.com/fwartner/home-assistant-wakewords-collection/tree/main/en"
```

**Related Project**: **Hey Jarvis Wake Words**
- **URL**: https://github.com/fwartner/home-assistant-wakewords-collection
- **Usage**: Pre-trained wake word models
- **Alternative**: Alexa wake word

**Hardware Note**:
```
"view assistant + view assistant companion app. As it was the 
first 2 gen of echo show 5 didnt have dedicated hw for wake 
words."
```

- Echo Show 5 Gen 1-2: No dedicated wake word hardware
- Echo Show 2 Gen 2: Has hardware support

---

## February 2026

### January 29, 2026
```
"I got the new amd GPU libraries working on my strix halo 
and stable and its 2x faster than before. Also finally have 
home assitant working end to end"
```

**Progress**:
- AMD GPU libraries: Updated and stable
- Performance: 2x faster than before
- Home Assistant: End-to-end complete

**Related**:
- "Resurgens" payoff: Fresh install + updates = performance gain
- Home Assistant milestone achieved

---

### February 3, 2026
```
"6 days out of return policy i am having strix remorse. Its 
gotten better but there is a linear performance regression 
in token processing. One thing I have learned is its important 
to get the kv cache in vram too, not just the model. And strix 
is supposed to be good at PP and not inference."
```

**Context**:
- "Strix remorse": Buyer's remorse moment
- Timing: 6 days past return window
- Issue: Linear performance regression

**Technical Insights**:
- KV cache must be in VRAM, not just model
- Strix Halo architecture: Good at Prefill (PP), not inference
- Performance degradation: Linear with context

**Related**:
- Hardware architecture limitations
- Memory placement optimization needed

---

### February 8, 2026
```
"Ive been using it with various degrees of success with open 
code. Tools, especially editing, failed a few times. I got 
qwen3-coder stable now."
```

**Context**:
- Tool: OpenCode (AI coding assistant)
- Issue: Editing tools failed intermittently
- Status: Qwen3-Coder now stable

---

```
"It's putting together a pr for llamacpp to manage core affinity 
on the strix. Its one apu but 2 core dies and 2x64mb l3 caches."
```

**Related Project**: **llama.cpp PR**
- **Purpose**: Core affinity management for Strix Halo
- **Architecture**: 2 core dies, 2x64MB L3 caches
- **Status**: PR in progress
- **Target**: llama.cpp (via Lemonade)

**Technical Details**:
- NUMA optimization needed
- Cross-die memory access penalty
- Core pinning for performance

---

```
"Well a pr for lemonade. I probably should just run llamacpp 
directly because I've had good luck running 2 models with 
multiple open code instances running. Getting 24tps now on 
a single thread."
```

**Related Projects**:
- Lemonade: https://github.com/winmutt/lemonade
- llama.cpp: Direct usage consideration
- OpenCode: Multiple instances

**Performance**:
- 24 TPS single-threaded
- Multi-model setup working
- Multiple OpenCode instances

**Decision**:
- Consider running llama.cpp directly
- Lemonade abstraction may add overhead

---

## March 2026

### March 11, 2026
```
"I think I got into full autonomous mode this morning. The 
newest llamacpp fixed prompts caching finally and things are 
really humming now."
```

**Milestone**: **Full Autonomous Mode**
- Trigger: Latest llama.cpp prompt caching fix
- Status: "Really humming"
- Significance: Major productivity breakthrough

**Related**:
- llama.cpp: Prompt caching resolved
- Performance: Dramatic improvement

---

```
"I have sub agents running on qwen 3.5 9b. And NPU support 
is working in dev now. Leveraging other providers/gpus for 
the sub agents is going to be the win"
```

**Technical Details**:
- Sub-agents: Qwen 3.5 9B
- NPU support: Working in development
- Strategy: Leverage other providers/GPUs for sub-agents

**Related Projects**:
- WWS: Autonomous development setup
- NPU: AMD NPU integration in progress
- Multi-GPU: Future optimization target

---

## May 2026

### May 12, 2026
```
"Definitely no Athena and its taken months to get there but 
this is something I entirely vibe coded. (this is the 
~/opensource/src/wws project https://github.com/winmutt/wws)"
```

**Milestone**: **WWS Complete**
- Project: WWS (Winmutt Work Spaces)
- URL: https://github.com/winmutt/wws
- Method: "Vibe coded" (AI-assisted development)
- Timeline: Months of development
- Reference: "No Athena" (possibly referring to a specific milestone or feature)

**Related Project**: **WWS**
- **Location**: `/opt/opencode/src/winmutt/wws/`
- **GitHub**: https://github.com/winmutt/wws
- **Status**: Phase 2 complete (Team Features)
- **Files**: 172 files, 56 days of development

**Key Features**:
- Remote workspace provisioning
- KVM/Podman support
- code-server integration
- GitHub OAuth + RBAC
- Team collaboration
- 274 tracked tasks across 4 phases

**GitHub Activity**:
- Multiple PRs (tracked in TODO.md)
- Phase 1: Core Foundation ✅
- Phase 2: Team Features ✅
- Phase 3: Advanced Features 🔄

---

## Summary: Chat to Project Mapping

| Chat Date | Topic | Related Project | GitHub/Local Path |
|-----------|-------|-----------------|-------------------|
| Nov 22 | Hardware acquisition | N/A | N/A |
| Nov 28 | Lemonade, NPU support | Lemonade | https://github.com/winmutt/lemonade |
| Nov 29 | MCP, repeatable workflows | WWS | https://github.com/winmutt/wws |
| Nov 29 | Cline + Qwen3-Coder | Cline | https://github.com/winmutt/cline |
| Nov 29 | 400k context, 128GB memory | AI Stack | N/A |
| Dec 1 | Concrete sign molds | Concrete | /opt/opencode/src/concrete/sign-molds/ |
| Dec 5 | Terminator AI safety | N/A | N/A |
| Dec 6 | Home Assistant on Echo | HA on Echo | /tmp/ha.jpeg |
| Dec 7 | Lemonade → Ollama switch | Lemonade/Ollama | N/A |
| Dec 9 | TPS degradation >64k | Performance | N/A |
| Dec 14 | GPU crashes, benchmark | Performance | N/A |
| Jan 19 | HA on Echo Show Gen 2 | HA on Echo | N/A |
| Jan 21 | Wake word issue | HA on Echo | N/A |
| Jan 25 | Wake word solved | HA on Echo | https://github.com/fwartner/home-assistant-wakewords-collection |
| Jan 29 | AMD GPU update, 2x faster | AI Stack | N/A |
| Feb 3 | Strix remorse, KV cache | Performance | N/A |
| Feb 8 | OpenCode, llama.cpp PR | WWS, llama.cpp | https://github.com/winmutt/wws |
| Feb 8 | 24 TPS single-thread | Performance | N/A |
| Mar 11 | Autonomous mode, NPU | WWS | https://github.com/winmutt/wws |
| May 12 | WWS complete | WWS | https://github.com/winmutt/wws |

---

## External References

### GitHub Repositories
- https://github.com/winmutt (main profile)
- https://github.com/winmutt/wws (WWS project)
- https://github.com/winmutt/lemonade (fork)
- https://github.com/winmutt/cline (fork)
- https://github.com/fwartner/home-assistant-wakewords-collection (wake words)

### Communities
- https://www.reddit.com/r/LocalLLaMA/ (LLM discussion)
- https://xdaforums.com/f/amazon-echo.6148/ (Echo hacking)

### Documentation
- /opt/opencode/src/self-2026/AMD_STRIX_TALK_README.md
- /opt/opencode/src/self-2026/AMD_STRIX_TALK_SLIDES.md
- /opt/opencode/src/self-2026/SLIDE_DECK_INDEX.md

---

## Performance Timeline Summary

| Date | Event | TPS | Notes |
|------|-------|-----|-------|
| Nov 29 | Initial setup | 45 | 400k context |
| Nov 29 | After tuning | 14 | 200k context |
| Nov 29 | >200k context | 8 | Sharp decline |
| Dec 9 | >64k ingress | N/A | Performance cliff |
| Dec 14 | Post-crash benchmark | 46 | Prompt eval |
| Dec 14 | Generation | 46 | 21.61ms/token |
| Feb 8 | Single-thread | 24 | After tuning |
| Feb 8 | AMD update | 2x | Faster than before |
| Mar 11 | Prompt caching | ? | "Really humming" |

---

## Project Status Summary

| Project | Status | Location | GitHub |
|---------|--------|----------|--------|
| WWS | Phase 2 Complete | /opt/opencode/src/winmutt/wws/ | ✅ |
| Concrete Signs | In Progress | /opt/opencode/src/concrete/sign-molds/ | ❌ |
| Home Assistant on Echo | Complete | N/A | N/A |
| Lemonade PR | In Progress | N/A | 🔄 |
| NPU Support | Dev | N/A | 🔄 |

---

## Screenshots and Assets

| Asset | Location | Description |
|-------|----------|-------------|
| ha.jpeg | /tmp/ha.jpeg | Home Assistant on Echo Show |
| dashboard.png | /opt/opencode/src/winmutt/wws/docs/screenshots/ | WWS Dashboard |
| example_sign_mold_preview.png | /opt/opencode/src/concrete/sign-molds/ | Concrete sign mold |
| example_sign_positive_preview.png | /opt/opencode/src/concrete/sign-molds/ | Concrete sign positive |

---

## Notes for Presentation

1. **Use actual screenshots** from the assets list
2. **Reference specific GitHub PRs** from WWS TODO.md
3. **Show performance graphs** using the timeline data
4. **Demo WWS** if possible (local deployment)
5. **Show concrete sign photos** (if physical objects created)
6. **Live demo Home Assistant** on Echo device
7. **Discuss "vibe coding"** methodology and results

---

## References in Talk

### Hardware
- AMD Strix Halo APU
- 128GB LPDDR5X-8000 (96GB addressable)
- 2 core dies, 2x64MB L3 caches

### Software
- Lemonade (llama.cpp + ROCm)
- Ollama
- Cline (VS Code extension)
- Qwen3-Coder
- Qwen 3.5 9B
- Home Assistant OS

### Projects
- WWS: Workspace provisioning
- Concrete Signs: 3D printing + casting
- Home Assistant: Echo repurposing

### Performance
- 40 TPS <100k tokens
- 8 TPS >200k tokens
- 24 TPS single-thread (Feb 8)
- 2x improvement (Jan 29)

---

**Last Updated**: May 2026  
**Author**: winmutt
