# Echo 8 Audio/Mic Issue Context

## Issue Details

**Issue**: Audio stops working after ~24 hours on Echo 8 devices  
**Reported**: January 7, 2026  
**Repository**: https://github.com/amazon-oss/releases  
**Issue #**: 4  
**Status**: Open (awaiting fix)

## User Report (lawhazl)

### Problem Summary
> "I've got the Echo 8 and Echo 5, both loaded up with their latest respective LineageOS 18.1 installs.
>
> So far, both have been rock solid on a 2.4 GHz–only IoT network SSID...
>
> The mic on the Echo 5 and 8 is stable and will constantly listen without issue for days at a time without a reboot. Both devices use the same Wi-Fi and interact with the same Home Assistant system.
>
> However, the Echo 8 seems to exhibit the audio issue that the Echo 5 originally had until that was fixed in a later build.
>
> With my Echos, I don't let them sleep ever. ViewAssist puts a nighttime image on the screen, but the screen is always on when this behaviour happens. It usually takes a day or so before it starts happening on the echo 8."

### Technical Details
- **Devices**: Echo Show 5 (checkers), Echo Show 8 (crown)
- **ROM**: LineageOS 18.1 (v0.3 for Echo 5, v0.5 for Echo 8)
- **Usage**: Home Assistant with ViewAssist integration for STT/TTS
- **Network**: 2.4 GHz-only IoT network SSID
- **Behavior**: Audio stops after ~24 hours, requires reboot
- **Not affected**: Screen stays on (ViewAssist keeps display active)

### Context: Echo 5 Fix
- Echo 5 originally had same audio issue
- Fixed in **Build 3** (October 25, 2025): "Included microphone fix in the build"
- Reference: https://github.com/amazon-oss/releases/releases/tag/lineage-18.1-checkers-v0.3

### Current Status
- Echo 8 running v0.5 (April 2026)
- Issue persists on Echo 8 despite fix being applied to Echo 5
- User is asking if the fix can be applied to Echo 8 as well

## Technical Background

### Hardware
- **Echo Show 5 (2019)**: Codenamed "checkers", MT8163 SoC
- **Echo Show 8 (2019)**: Codenamed "crown", similar architecture

### Software
- Both devices run LineageOS 18.1 based on Android 11
- ViewAssist app connects to Home Assistant via Wyoming protocol
- STT (Speech-to-Text) and TTS (Text-to-Speech) handled by HA

### Known Issue (from ROM OP)
- "Microphones may be quieter than expected" (known issue)
- "Deep sleep is intentionally disabled" to prevent sleep-related issues

## Related Resources

### XDA Forum Thread
https://xdaforums.com/t/rom-unofficial-11-checkers-lineageos-18-1-for-the-amazon-echo-show-5-2019.4763475/

### Issue Comments
- **Dec 14, 2025**: UserPFhortune reported audio stops after device "sleeps" (lock with display off)
- **Oct 31, 2025**: UserPFhortune submitted bug reports with logcat/dmesg
- **Nov 8, 2025**: Build 4 includes suspend blocker and Wi-Fi fixes

### Build History
- **v0.3** (Oct 25, 2025): Mic fix added
- **v0.4** (Nov 8, 2025): Suspend blocker, Wi-Fi fixes
- **v0.5** (Apr 2026): Latest for Echo 5
- **v0.5+** (Apr 2026): Latest for Echo 8

## Connection to Presentation

### Theme: Local AI Reinvigoration
The Echo devices represent the "Repurposing Hardware" theme:
- Echo Show 5: Used for home automation
- Echo Show 8: Main device for STT/TTS
- Both repurposed from Amazon Alexa to Home Assistant

### Context for Home Assistant Section
The mic stability issue is relevant to:
- **Home Assistant on Echo** slide
- **Hardware Repurposing** takeaway
- **OSS Reinvigoration** - showing real-world challenges with custom firmware

### Quote Integration
> "Basically anything with a USB port. If there is a port, there is a way."

This mindset applies to Echo device hacking and repurposing, but also highlights the ongoing challenges (like the mic issue) that require community collaboration.

## Status Update
As of May 2026:
- Issue #4 remains open
- No fix applied to Echo 8 yet
- User continues testing with ViewAssist
- Waiting for ROM maintainer response

## References
- GitHub Issue: https://github.com/amazon-oss/releases/issues/4
- XDA Thread: https://xdaforums.com/t/rom-unofficial-11-checkers-lineageos-18-1-for-the-amazon-echo-show-5-2019.4763475/
- ViewAssist: https://dinki.github.io/View-Assist/
