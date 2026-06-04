# AMD Strix Halo Performance Data

## Complete Performance Timeline

This document tracks all performance metrics from the 6-month AMD Strix Halo journey.

---

## Performance Metrics Summary

| Date | Context Size | TPS | TTFT | Notes |
|------|--------------|-----|------|-------|
| Nov 29, 2025 | 400k | 45 | N/A | Initial setup |
| Nov 29, 2025 | 200k | 14 | N/A | After tuning |
| Nov 29, 2025 | >200k | 8 | N/A | Sharp decline |
| Dec 9, 2025 | >64k | N/A | N/A | Performance cliff on ingress |
| Dec 14, 2025 | 804 prompt | 284.73 | N/A | Prompt eval only |
| Dec 14, 2025 | 276 gen | 46.27 | N/A | Generation only |
| Dec 14, 2025 | 1080 total | N/A | 8.788s | Total time |
| Feb 8, 2026 | N/A | 24 | N/A | Single-threaded |
| Feb 29, 2026 | N/A | 2x | N/A | AMD GPU library update |
| May 30, 2026 | 199,792 | 18.65 | 2,267s | Recent ~200k benchmark |

---

## Detailed Benchmarks

### November 29, 2025 - Initial Setup

**Quote**: "I've got a 400k context window with the new Ai workstation. Still need to work on tuning it, was getting about 45tps and was around 14tps when I left it last night with a nearly 200k window"

**Metrics**:
- 400k context: 45 TPS (initial)
- 200k context: 14 TPS (after tuning)
- >200k: 8 TPS (sharp decline)

**Backend**: Lemonade (llama.cpp + ROCm)

---

### December 9, 2025 - Ingress Performance Issue

**Quote**: "The TPS goes down pretty sharply >64k context. I dont know why. But that's on ingress, not generation."

**Issue**: Performance cliff at 64k context on prompt processing (ingress), not generation

---

### December 14, 2025 - Post-Crash Benchmark

**Quote**: "I think thats the only backend I can run. Upgraded OS and ollama last night and sad things happened. GPU crashes about 3-4 prompts in"

**Benchmark Output**:
```
prompt eval time =    2823.77 ms /   804 tokens (    3.51 ms per token,   284.73 tokens per second)
eval time =    5964.43 ms /   276 tokens (   21.61 ms per token,    46.27 tokens per second)
total time =    8788.20 ms /  1080 tokens
```

**Breakdown**:
- Prompt eval: 284.73 tokens/sec (3.51ms/token)
- Generation: 46.27 tokens/sec (21.61ms/token)
- Total: 1080 tokens in 8.788 seconds

**Backend**: Ollama (post-switch from Lemonade)

---

### February 8, 2026 - Single Thread Performance

**Quote**: "Getting 24tps now on a single thread."

**Metrics**:
- 24 TPS (single-threaded)
- Backend: Lemonade

**Context**: Working on PR for llama.cpp core affinity management

---

### January 29, 2026 - AMD GPU Library Update

**Quote**: "I got the new amd GPU libraries working on my strix halo and stable and its 2x faster than before."

**Improvement**: 2x performance increase after AMD GPU library update

---

### May 30, 2026 - Recent ~200k Token Processing

**Telemetry Output**:
```
May 30 16:06:53 wintermute lemond[1813200]: 2026-05-30 16:06:53.831 [Info] (Telemetry) === Telemetry ===
May 30 16:06:53 wintermute lemond[1813200]: 2026-05-30 16:06:53.831 [Info] (Telemetry) Input tokens:  193795
May 30 16:06:53 wintermute lemond[1813200]: 2026-05-30 16:06:53.831 [Info] (Telemetry) Output tokens: 5997
May 30 16:06:53 wintermute lemond[1813200]: 2026-05-30 16:06:53.831 [Info] (Telemetry) TTFT (s):      2267.139
May 30 16:06:53 wintermute lemond[1813200]: 2026-05-30 16:06:53.831 [Info] (Telemetry) TPS:           18.65
```

**Breakdown**:
- Input tokens: 193,795
- Output tokens: 5,997
- Total tokens: 199,792 (~200k)
- Time to First Token (TTFT): 2,267.139 seconds (~37.8 minutes)
- Throughput: 18.65 tokens/sec

**Backend**: Lemonade

---

## Performance Analysis

### Context Size vs TPS

```
TPS
45 | ● (Nov 29 - 400k, initial)
   |
40 |
   |
35 |
   |
30 |
   |
25 |                    ● (Feb 8 - single thread)
   |
20 |                          ● (May 30 - ~200k)
   |              ● (Nov 29 - 200k, tuned)
15 |
   |    ● (Dec 14 - generation)
10 |
   |
 5 |
   |
 0 +────────────────────────────────────
    0     50k    100k   150k   200k+
           Context Size (tokens)
```

### Key Observations

1. **Initial High Performance**: 45 TPS at 400k context (Nov 29) - likely not sustained
2. **Quick Degradation**: Dropped to 14 TPS at 200k after tuning
3. **Ingress Bottleneck**: Sharp decline >64k on prompt processing
4. **Generation vs Prompt**: Prompt eval (284 TPS) >> Generation (46 TPS)
5. **Single Thread**: 24 TPS achievable on single core (Feb 8)
6. **Recent Performance**: 18.65 TPS at ~200k with 37.8 min TTFT (May 30)

### Time to First Token (TTFT)

The May 30 benchmark shows a critical metric:
- **TTFT**: 2,267 seconds (~37.8 minutes) for ~200k context
- This is the time to process the prompt before generation begins
- Explains the "ingress performance" issues mentioned earlier

### Memory Impact

**Quote** (Nov 29): "Currently with qwen3-coder and 400k window its using about 59g."

- Qwen3-Coder + 400k context: ~59GB memory
- 2 cached prompts: ~8GB
- Total addressable: 96GB (of 128GB)

---

## Backend Comparison

### Lemonade (llama.cpp + ROCm)

**Pros**:
- Good observability (token batching visible)
- Multi-model support
- Core affinity PR in progress

**Cons**:
- Stability issues after OS upgrade
- NPU support in development

**Performance**:
- Feb 8: 24 TPS single-thread
- May 30: 18.65 TPS at ~200k

### Ollama

**Pros**:
- Patch available for APU support
- Simpler setup

**Cons**:
- Poor observability
- GPU crashes after upgrades
- Limited multi-model support

**Performance**:
- Dec 14: 46 TPS generation, 284 TPS prompt eval

---

## Performance Bottlenecks

### 1. Context Scaling
- Sharp TPS decline >64k context
- Ingress (prompt processing) worse than generation
- May 30: 37.8 min TTFT for ~200k context

### 2. Memory Placement
**Quote** (Nov 28): "Sometimes it loads the models into gtt instead of vram and seems to spend a lot of time swapping in and out"

**Quote** (Feb 3): "One thing I have learned is its important to get the kv cache in vram too, not just the model."

### 3. Architecture Limitations
**Quote** (Feb 3): "And strix is supposed to be good at PP and not inference."

- Strix Halo optimized for Prefill (PP), not inference
- Real-world usage shows inference bottleneck

### 4. Core Affinity
**Quote** (Feb 8): "Its one apu but 2 core dies and 2x64mb l3 caches."

- NUMA-like behavior across dies
- Core affinity management needed

---

## Optimization Timeline

| Date | Optimization | Impact |
|------|--------------|--------|
| Nov 29 | Initial tuning | 45 → 14 TPS |
| Jan 29 | AMD GPU libraries | 2x faster |
| Feb 8 | Single-thread focus | 24 TPS |
| Mar 11 | Prompt caching (llama.cpp) | "Really humming" |
| May 30 | Stable operation | 18.65 TPS @ 200k |

---

## Recommendations for Presentation

### Performance Graphs to Include

1. **TPS vs Context Size**
   - X-axis: Context size (0 to 200k+)
   - Y-axis: TPS (0 to 50)
   - Show degradation curve

2. **TTFT vs Context Size**
   - X-axis: Context size
   - Y-axis: TTFT in seconds/minutes
   - Highlight May 30: 37.8 min at ~200k

3. **Prompt Eval vs Generation Speed**
   - Bar chart comparing 284 TPS (prompt) vs 46 TPS (generation)
   - Shows fundamental bottleneck

4. **Performance Timeline**
   - X-axis: Date (Nov 2025 - May 2026)
   - Y-axis: TPS
   - Show improvements and setbacks

### Key Metrics to Highlight

- **Best TPS**: 45 (Nov 29, initial)
- **Typical TPS**: 14-18 (200k context)
- **Generation TPS**: 46 (Dec 14)
- **Prompt Eval TPS**: 284 (Dec 14)
- **Single-thread TPS**: 24 (Feb 8)
- **Recent TPS**: 18.65 (May 30, ~200k)
- **Worst TTFT**: 2,267s / 37.8 min (May 30, ~200k)

---

## Future Performance Goals

### Immediate
- Reduce TTFT for large contexts
- Optimize KV cache placement in VRAM
- Core affinity management (llama.cpp PR)

### Long-term
- NPU utilization for inference
- Multi-GPU/NPU orchestration
- Better context scaling (>200k)

---

**Last Updated**: May 30, 2026  
**Source**: Lemonade telemetry, chat logs, benchmarks
