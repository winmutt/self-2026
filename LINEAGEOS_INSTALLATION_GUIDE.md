# Installing LineageOS on Amazon Echo Devices - Complete Guide

## Overview

This guide documents the complete process of installing LineageOS 18.1 on Amazon Echo Show devices using the XDA Forums community work by @Rortiz2, @bengris32, and others.

---

## Device Compatibility

### Echo Show 5 (1st Gen - 2019)
- **Codename**: checkers
- **SoC**: MediaTek MT8163
- **ROM Thread**: https://xdaforums.com/t/rom-unofficial-11-checkers-lineageos-18-1-for-the-amazon-echo-show-5-2019.4763475/
- **Unlock Thread**: https://xdaforums.com/t/unlock-root-twrp-unbrick-amazon-echo-show-5-1st-gen-2019-checkers.4762900/

### Echo Show 5 (2nd Gen - 2021)
- **Codename**: cronos
- **SoC**: MediaTek MT8163
- **ROM Thread**: https://xdaforums.com/t/rom-unofficial-11-cronos-lineageos-18-1-for-the-amazon-echo-show-5-2021.4772598/
- **Unlock Thread**: https://xdaforums.com/t/unlock-root-twrp-unbrick-amazon-echo-show-5-2nd-gen-2021-cronos.4772596/

### Echo Show 8 (1st Gen - 2019)
- **Codename**: crown
- **SoC**: MediaTek MT8163
- **ROM Thread**: https://xdaforums.com/t/rom-unofficial-11-crown-lineageos-18-1-for-the-amazon-echo-show-8-2019.4766709/

---

## Prerequisites

### Hardware Requirements
- Windows or Linux-based computer
- MicroUSB cable
- AC charger
- Optional: USB-to-TTL serial adapter for UART debugging

### Software Requirements
- ADB & Fastboot tools
- TWRP recovery
- LineageOS 18.1 ROM ZIP file

---

## Unlocking the Bootloader

### Critical Warning
> "This process carries a significant risk of permanently bricking your device if anything goes wrong. Proceed entirely at your own risk."

### Step-by-Step Process

1. **Prepare Your Computer**
   ```bash
   # Download amonet package
   wget https://github.com/R0rt1z2/amonet/releases/download/v1.1.3/amonet-cronos-v1.1.3.zip
   
   # Extract
   unzip amonet-cronos-v1.1.3.zip
   cd amonet-cronos-v1.1.3
   ```

2. **Install USB Drivers (Windows)**
   - Install Kindle Fire Driver OR Google's USB driver for ADB & Fastboot
   - Alternative: Use Linux for simpler driver management

3. **Enter Fastboot Mode**
   - Connect device to AC charger
   - Hold all three buttons (Volume Up, Volume Down, Mute) simultaneously
   - Wait until "=> FASTBOOT mode..." appears on screen
   - Connect device to computer via MicroUSB

4. **Execute Exploit**
   ```bash
   # Windows
   fastbrick.bat
   
   # Linux
   ./fastbrick.sh
   ```

5. **Confirm Unlock**
   - Type "YES" when prompted
   - Follow on-screen instructions
   - DO NOT INTERRUPT - 10-second grace period, then exploit runs

6. **Wait for Completion**
   - Process takes up to 5 minutes
   - Device will reboot into TWRP

### Creating a Stock Backup (CRITICAL)
```bash
# Windows
backup.bat

# Linux
./backup.sh
```

**Store this backup safely** - it's your only way back to stock Fire OS.

---

## Installing LineageOS

### From TWRP

1. **Format Data**
   ```
   Wipe > Format Data > type yes > hit checkmark
   ```

2. **Advanced Wipe**
   ```
   Wipe > Advanced Wipe > wipe Data, System, and Cache partitions
   ```

3. **Transfer ROM**
   - Use ADB or MTP to copy ROM ZIP to device

4. **Flash ROM**
   ```
   Install > select the ROM ZIP > Swipe to flash
   ```

5. **Reformat Data**
   ```
   Wipe > Format Data > type yes > hit checkmark
   ```

6. **Reboot System**
   ```
   Reboot > System
   ```

---

## Post-Installation Configuration

### Initial Setup
- Device boots to LineageOS 11 (Android 11)
- Setup process may take several minutes
- Use scrcpy for easier initial configuration:
  ```bash
  scrcpy --turn-screen-off
  ```

### Key Configuration Notes

1. **Wi-Fi Setup**
   - 2.4GHz-only networks recommended
   - Some users report issues with 5GHz
   - Wi-Fi may disconnect randomly (fixed in v0.4+)

2. **Audio Configuration**
   - Microphones may be quieter than expected
   - A2DP sink enabled (device can be Bluetooth speaker)
   - Mic stability varies by device/build

3. **Display Settings**
   - AOD (Always On Display) enabled by default
   - Auto-brightness supported
   - Deep sleep intentionally disabled

4. **Buttons**
   - Mute button acts as Power button
   - Volume buttons for boot mode selection

---

## Troubleshooting

### Wi-Fi Issues
- Fixed in v0.4+ (suspend blocker, Wi-Fi fixes)
- Use 2.4GHz-only network
- Reboot if Wi-Fi becomes unresponsive

### Audio Issues
- Echo 5: Fixed in Build 3 (Oct 25, 2025)
- Echo 8: Issue persists (see Issue #4 on GitHub)

### ADB/USB Issues
- USB debugging may become unresponsive
- Try rebooting device
- Use MTP for file transfers if ADB fails

### Recovery
- **Soft-brick**: Reboot into TWRP automatically fixes
- **Hard-brick**: Requires UART dump + LK reflash
- **Stock recovery**: Use backup or restore-stock scripts

---

## Building LineageOS from Source

### Source Code Repositories

| Component | Repository |
|-----------|-----------|
| Kernel | https://github.com/amazon-oss/android_kernel_amazon_mt8163 |
| Wi-Fi | https://github.com/amazon-oss/android_kernel_amazon_mt76x8-wifi |
| Bluetooth | https://github.com/amazon-oss/android_kernel_amazon_mt76x8-bt |
| Device Tree (common) | https://github.com/amazon-oss/android_device_amazon_mt8163-common |
| Device Tree (cronos) | https://github.com/amazon-oss/android_device_amazon_cronos |
| Recovery | https://github.com/amazon-oss/android_bootable_recovery |

### Build Environment
```bash
# Initialize repository
repo init -u https://github.com/LineageOS/android.git -b lineage-18.1

# Sync sources
repo sync

# Add device tree
git clone https://github.com/amazon-oss/android_device_amazon_cronos.git \
    device/amazon/cronos

# Build
source build/envsetup.sh
lunch lineage_cronos-userdebug
make -j$(nproc)
```

---

## Updating LineageOS

### From TWRP (Recommended)
1. Download new ROM ZIP
2. Reboot to TWRP
3. Install ZIP on top of existing installation
4. No need to wipe data

### ADB Sideload
```bash
adb reboot recovery
adb sideload lineage-18.1-cronos-vX.X.zip
```

---

## Known Issues

### All Devices
- **Camera**: Not functional (hardware limitation)
- **Experimental**: May encounter more bugs than expected
- **Microphones**: May be quieter than expected
- **Battery**: System reports 100% always (fake battery)

### Echo 8 Specific
- **Audio stability**: Stops working after ~24 hours (Issue #4)
- **Mic fix**: Not yet applied to Echo 8 builds

### Workarounds
- Keep device awake (no deep sleep)
- Use external microphones if needed
- Regular reboots for Echo 8 to maintain audio

---

## Going Back to Stock

### Option 1: Restore Backup (Recommended)
```bash
# Windows
restore.bat

# Linux
./restore.sh
```

### Option 2: Manual Restore
```bash
adb restore data.ab
adb restore system.ab
adb restore boot.ab
```

### Option 3: Fully Restore Stock
1. Download restore-stock-cronos.zip
2. Extract and run restore-stock.sh
3. Select Fire OS version
4. Wait for download and flash

---

## Technical Details

### Hardware Architecture
- **SoC**: MediaTek MT8163
- **CPU**: Quad-core ARM Cortex-A53
- **GPU**: ARM Mali-450 MP4
- **RAM**: 1GB (Echo Show 5), 2GB (Echo Show 8)
- **Storage**: 8GB eMMC

### Android Compatibility
- **LineageOS 18.1**: Android 11
- **Why not newer?**: 
  - Kernel 4.9 lacks modern Android features
  - Proprietary blobs break with newer Android versions
  - Performance issues on weak hardware

### Boot Modes
- **HACKED FASTBOOT**: Hold Mute (Power) key + power
- **TWRP/RECOVERY**: Hold Volume Up key + power
- **Regular FASTBOOT**: Hold all three buttons + power

### UART Access
- **Pin**: TP55 (TX pin)
- **Baud**: 921600
- **Use**: Kernel logs, LK dump for unsupported firmware

---

## Community Resources

### Contributors
- @Rortiz2 (Lead developer)
- @bengris32
- @FieryFlames
- @k4y0z

### Discord
- View-Assist community Discord (for Home Assistant integration)
- XDA Forums thread for general discussion

### Related Projects
- **ViewAssist**: Home Assistant integration app
- **Wyoming Protocol**: Speech-to-text/TTS protocol
- **A2DP Sink**: Bluetooth speaker mode

---

## Safety Recommendations

1. **Always create a backup** before unlocking
2. **Read the entire guide** before starting
3. **Use 2.4GHz-only network** for stability
4. **Keep device charged** during flashing
5. **Do not interrupt** the exploit process
6. **Test thoroughly** before daily use

---

## Connection to Presentation

### Themes Highlighted
- **OSS Reinvigoration**: Community-driven custom ROMs
- **Hardware Repurposing**: Alexa devices as general-purpose tablets
- **Local AI Enablement**: LineageOS enables Home Assistant + ViewAssist
- **Community Collaboration**: XDA Forums as knowledge sharing platform

### Quotes from Community
> "For fun! It's also a great showcase of the custom firmware potential that this device could have, thanks to the bootloader unlock!"

> "The more Android versions away you are from the original blobs, the more broken they will become."

---

## References

- **ROM Downloads**: https://github.com/amazon-oss/releases/releases
- **Unlock Exploit**: https://github.com/R0rt1z2/amonet/tree/mt8163-cronos
- **XDA Thread (cronos)**: https://xdaforums.com/t/rom-unofficial-11-cronos-lineageos-18-1-for-the-amazon-echo-show-5-2021.4772598/
- **XDA Thread (checkers)**: https://xdaforums.com/t/rom-unofficial-11-checkers-lineageos-18-1-for-the-amazon-echo-show-5-2019.4763475/
- **ViewAssist**: https://dinki.github.io/View-Assist/
