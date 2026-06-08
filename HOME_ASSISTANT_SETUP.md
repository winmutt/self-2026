# Home Assistant + Local LLM + Voice Assistant Setup

## Overview

This guide documents setting up a complete local voice assistant system on repurposed Echo hardware with:
- **Home Assistant**: Smart home automation hub
- **Local LLM**: Running on AMD Strix Halo via Lemonade/llama.cpp
- **Voice Assistant**: Wyoming protocol with wakeword support
- **Hardware**: Amazon Echo devices running LineageOS

## Hardware Requirements

### Echo Devices Supported
- **Echo Show 5 (1st Gen 2019)**: Codename `checkers`, MediaTek MT8163
- **Echo Show 5 (2nd Gen 2021)**: Codename `cronos`, MediaTek MT8163  
- **Echo Show 8 (1st Gen 2019)**: Codename `crown`, MediaTek MT8163

### LineageOS Installation
See `LINEAGEOS_INSTALLATION_GUIDE.md` for detailed unlock and install process.

## Software Stack

### 1. Home Assistant Installation

**Option A: Home Assistant OS (Recommended)**
```bash
# On Strix Halo system
# Install Home Assistant OS as VM or bare metal
# https://www.home-assistant.io/installation/
```

**Option B: Docker Container**
```bash
docker run -d \
  --name homeassistant \
  --privileged \
  -v /mnt/data/homeassistant:/config \
  -e TZ=America/New_York \
  --network host \
  ghcr.io/home-assistant/home-assistant:stable
```

### 2. Local LLM Integration

#### Lemonade Server (AMD GPU Optimized)

**Installation:**
```bash
# Install Lemonade Server
git clone https://github.com/winmutt/lemonade.git
cd lemonade
cargo install --path lemonade-server

# Run with ROCm
export HSA_OVERRIDE_GFX_VERSION=11.0.0
lemonade-server --model /path/to/model.gguf --port 8080
```

**Configuration for Strix Halo:**
```bash
# Optimize for 32GB unified memory
lemonade-server \
  --model /models/llama-3.1-8b-instruct.Q4_K_M.gguf \
  --n-gpu-layers 99 \
  --ctx-size 8192 \
  --batch-size 2048 \
  --threads 16 \
  --port 8080
```

#### Home Assistant Integration

**configuration.yaml:**
```yaml
# Local LLM via REST API
rest:
  - name: Local LLM
    resource: http://localhost:8080/v1/chat/completions
    method: POST
    json:
      model: "llama-3.1-8b"
      messages:
        - role: "system"
          content: "You are a helpful home assistant."
        - role: "user"
          content: "{{ query }}"
      temperature: 0.7
      max_tokens: 500

# Alternative: Use llm_openai integration with local endpoint
llm:
  assistants:
    - name: local_assistant
      instruction: "You control the smart home."
      llm_platform: openai
      api_url: http://localhost:8080/v1
      api_key: not-needed
```

### 3. Voice Assistant Setup

#### Wyoming Protocol

**Components:**
- **whisper-server**: Speech-to-text
- **piper-tts**: Text-to-speech
- **wyoming-satellite**: Voice satellite

**Installation:**
```bash
# Install Wyoming components
docker run -d --name whisper-server ghcr.io/rhasspy/wyoming-whisper:latest
docker run -d --name piper-tts ghcr.io/rhasspy/wyoming-piper:latest

# Configure in Home Assistant
```

**Home Assistant Configuration:**
```yaml
# configuration.yaml
voice_assistant:
  pipelines:
    - name: Local Voice
      wake_word:
        - id: hey_jarvis
          platform: openwakeword
          model: hey_jarvis
      stt:
        platform: whisper
        whisper:
          url: http://localhost:10400
      tts:
        platform: piper
        piper:
          url: http://localhost:10200
          voice: en_US-lessac-medium
      asr:
        platform: whisper
        whisper:
          url: http://localhost:10400
      llm:
        platform: openai
        url: http://localhost:8080/v1
        model: llama-3.1-8b
```

#### OpenWakeWord

**Wakeword Models:**
```bash
# Download wakeword models
wget https://github.com/dscripka/openWakeWord/releases/download/v0.1.0/hey_jarvis.onnx
wget https://github.com/dscripka/openWakeWord/releases/download/v0.1.0/hello_rick.onnx

# Configure in Home Assistant
openwakeword:
  models:
    - hey_jarvis
    - hello_rick
  threshold: 0.5
```

### 4. Echo Show Integration

#### ViewAssist App

**Installation on LineageOS:**
```bash
# Install ViewAssist APK
adb install viewassist.apk

# Configure Home Assistant connection
# Settings → Home Assistant URL → ws://your-ha-ip:8123
```

**ViewAssist Configuration:**
- **Dashboard**: Select Home Assistant dashboard
- **Wake Word**: Enable microphone for wakeword detection
- **Display**: Set screen timeout to "Never"
- **Audio**: Configure for TTS playback

#### Microphone Setup

**Audio Configuration:**
```bash
# On Strix Halo host
# Configure ALSA/PulseAudio for microphone input

# Create .asoundrc
cat > ~/.asoundrc << 'ASOUND'
pcm.micloopback {
    type loopback
    slave.pcm "default"
}

pcm.!default {
    type plug
    slave.pcm "micloopback"
}
ASOUND
```

**Home Assistant Audio:**
```yaml
# configuration.yaml
audio:
  input: default
  output: default

# Microphone sensitivity
recorder:
  microphones:
    - name: Echo Show Mic
      device: default
      sample_rate: 16000
```

## Performance Optimization

### GPU Acceleration

**ROCm Configuration:**
```bash
# Verify ROCm installation
rocm-smi

# Set GPU memory limits
export HIP_VISIBLE_DEVICES=0
export ROCR_VISIBLE_DEVICES=0

# Lemonade server GPU optimization
lemonade-server --use-gpu true --gpu-layers 99
```

### Memory Management

**Strix Halo Memory Layout:**
```bash
# 128GB LPDDR5X-8000 unified memory
# Reserve 32GB for LLM, rest for system

# Set memory limits
ulimit -v 33554432  # 32GB virtual memory limit for LLM
```

### NUMA/Core Pinning

**Issue #1070 Solution:**
```bash
# Pin LLM to specific CCD cores
# CCD 0: Cores 0-7, CCD 1: Cores 8-15

# Pin llama-server to CCD 0
taskset -c 0-7 lemonade-server --model model.gguf

# Pin voice assistant to CCD 1
taskset -c 8-15 whisper-server
```

## Troubleshooting

### Audio Issues

**Problem**: Microphone stops working after 24 hours
**Solution**: See GitHub Issue #4
```bash
# Workaround: Reboot audio service
systemctl restart pipewire
```

### Wakeword False Positives

**Solution**: Adjust threshold
```yaml
openwakeword:
  threshold: 0.7  # Increase from 0.5
```

### LLM Crashes

**Solution**: Reduce context size
```bash
lemonade-server --ctx-size 4096  # Reduce from 8192
```

## References

### Recent Documentation (2025-2026)

- **Home Assistant Voice Assistant**: https://www.home-assistant.io/voice_assistant/
- **Wyoming Protocol**: https://github.com/rhasspy/wyoming
- **OpenWakeWord**: https://github.com/dscripka/openWakeWord
- **Lemonade Server**: https://github.com/winmutt/lemonade
- **LineageOS for Echo**: https://xdaforums.com/t/rom-unofficial-11-cronos-lineageos-18.4772598/

### GitHub Issues

- **#1070**: Core affinity for multi-model workloads
- **#4**: Echo 8 audio stability
- **#5926**: ROCm memory management (lemonade-sdk/lemonade)

## Future Enhancements

- **Multi-room audio**: Sync multiple Echo devices
- **Wake word hotword training**: Custom wakewords
- **Local RAG**: Knowledge base integration
- **Vision**: Use Echo Show camera for visual context
