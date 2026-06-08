#!/usr/bin/env python3
"""
Generate annotated screenshots of Issue #1070 ps output and lscpu topology
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch
import os

def create_ps_output_screenshot():
    """Create annotated ps output screenshot showing threads bouncing across CCDs"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    
    # Title
    ax.text(5, 5.6, 'ps Output: Threads Bouncing Across CCDs', fontsize=14, fontweight='bold', 
            color='#c9d1d9', ha='center')
    
    # Header
    ax.text(1.0, 4.8, 'PID', fontsize=10, color='#8b949e', fontfamily='monospace')
    ax.text(3.0, 4.8, 'LAST_CPU', fontsize=10, color='#8b949e', fontfamily='monospace')
    ax.text(5.0, 4.8, 'AVG_MHZ', fontsize=10, color='#8b949e', fontfamily='monospace')
    ax.text(6.5, 4.8, 'COMMAND', fontsize=10, color='#8b949e', fontfamily='monospace')
    
    # Separator line
    ax.plot([0.8, 9.5], [4.5, 4.5], color='#30363d', linewidth=1)
    
    # Data rows with annotations
    rows = [
        (56840, 6, 55.7, 'llama-server (Model 1)', 'CCD0', 55.7),
        (56840, 20, 54.2, 'llama-server (Model 1)', 'CCD0 SMT', 54.2),
        (59798, 0, 51.2, 'llama-server (Model 2)', 'CCD0', 51.2),
        (59798, 2, 47.5, 'llama-server (Model 2)', 'CCD0', 47.5),
        ('---', '---', '---', '---', '---', 0),
        (56840, 22, 55.7, 'llama-server (Model 1)', 'CCD0', 55.7),
        (56840, 4, 54.2, 'llama-server (Model 1)', 'CCD0', 54.2),
        (59798, 16, 51.2, 'llama-server (Model 2)', 'CCD1', 51.2),
        (59798, 18, 47.5, 'llama-server (Model 2)', 'CCD1', 47.5),
    ]
    
    y_pos = 4.0
    for i, (pid, cpu, mhz, cmd, ccd, val) in enumerate(rows):
        if pid == '---':
            y_pos -= 0.4
            ax.plot([0.8, 9.5], [y_pos, y_pos], color='#30363d', linewidth=1, ls='--')
            y_pos -= 0.4
            continue
        
        ax.text(1.0, y_pos, str(pid), fontsize=9, color='#c9d1d9', fontfamily='monospace')
        ax.text(3.0, y_pos, str(cpu), fontsize=9, color='#c9d1d9', fontfamily='monospace')
        ax.text(5.0, y_pos, f'{mhz:.1f}', fontsize=9, color='#c9d1d9', fontfamily='monospace')
        ax.text(6.5, y_pos, cmd, fontsize=9, color='#c9d1d9', fontfamily='monospace')
        
        # Red box around LAST_CPU column (showing bounce)
        if i < 4 or i > 5:
            rect = Rectangle((2.5, y_pos - 0.15), 0.8, 0.3, 
                           edgecolor='#f85149', facecolor='#f85149', alpha=0.2, linewidth=2)
            ax.add_patch(rect)
        
        y_pos -= 0.4
    
    # CCD boundary annotation
    ax.text(5, 0.8, 'Notice: LAST_CPU jumps across CCD boundaries', 
            fontsize=10, color='#f85149', ha='center', fontweight='bold')
    ax.text(5, 0.5, 'CCD0: cores 0-7, 16-23 | CCD1: cores 8-15, 24-31', 
            fontsize=9, color='#8b949e', ha='center')
    
    plt.tight_layout()
    plt.savefig('/opt/opencode/src/self-2026/assets/issue_1070_ps_output.png', 
               dpi=150, bbox_inches='tight', facecolor='#0d1117')
    plt.close()
    print("Created: issue_1070_ps_output.png")


def create_lscpu_topology_screenshot():
    """Create annotated lscpu topology screenshot showing CCD structure"""
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    
    # Title
    ax.text(5.5, 6.5, 'lscpu Output: CCD Topology', fontsize=14, fontweight='bold', 
            color='#c9d1d9', ha='center')
    
    # Header
    headers = ['CPU', 'NODE', 'CORE', 'L3', 'MAXMHZ', 'AVG_MHZ']
    x_pos = [0.5, 1.8, 4.0, 6.0, 7.8, 9.2]
    for i, h in enumerate(headers):
        ax.text(x_pos[i], 5.8, h, fontsize=9, color='#8b949e', fontfamily='monospace', ha='center')
    
    ax.plot([0.3, 10.5], [5.5, 5.5], color='#30363d', linewidth=1)
    
    # CCD0 cores (with red box)
    ccd0_cores = [
        (0, 0, 0, '0', 5187.0, 4937.8),
        (1, 0, 1, '0', 5187.0, 2000.0),
        (2, 0, 2, '0', 5187.0, 4909.0),
        (3, 0, 3, '0', 5187.0, 4904.9),
        (4, 0, 4, '0', 5187.0, 4889.9),
        (5, 0, 5, '0', 5187.0, 4845.2),
        (6, 0, 6, '0', 5187.0, 4882.0),
        (7, 0, 7, '0', 5187.0, 4950.4),
    ]
    
    # CCD1 cores (with red box)
    ccd1_cores = [
        (8, 0, 8, '1', 5187.0, 2000.0),
        (9, 0, 9, '1', 5187.0, 2000.0),
        (10, 0, 10, '1', 5187.0, 2000.0),
        (11, 0, 11, '1', 5187.0, 2425.1),
        (12, 0, 12, '1', 5187.0, 3056.8),
        (13, 0, 13, '1', 5187.0, 4661.1),
        (14, 0, 14, '1', 5187.0, 2000.0),
        (15, 0, 15, '1', 5187.0, 2000.0),
    ]
    
    y_pos = 5.0
    # CCD0
    for cpu, node, core, l3, max_mhz, avg_mhz in ccd0_cores:
        ax.text(x_pos[0], y_pos, str(cpu), fontsize=8, color='#58a6ff', fontfamily='monospace', ha='center')
        ax.text(x_pos[1], y_pos, str(node), fontsize=8, color='#c9d1d9', fontfamily='monospace', ha='center')
        ax.text(x_pos[2], y_pos, str(core), fontsize=8, color='#c9d1d9', fontfamily='monospace', ha='center')
        ax.text(x_pos[3], y_pos, l3, fontsize=8, color='#3fb950', fontfamily='monospace', ha='center')
        ax.text(x_pos[4], y_pos, f'{max_mhz:.1f}', fontsize=8, color='#c9d1d9', fontfamily='monospace', ha='center')
        ax.text(x_pos[5], y_pos, f'{avg_mhz:.1f}', fontsize=8, color='#c9d1d9', fontfamily='monospace', ha='center')
        
        # Red box around L3 column showing CCD0
        rect = Rectangle((x_pos[3] - 0.15, y_pos - 0.12), 0.3, 0.24, 
                       edgecolor='#f85149', facecolor='#f85149', alpha=0.2, linewidth=1.5)
        ax.add_patch(rect)
        
        y_pos -= 0.28
    
    # Separator
    y_pos -= 0.2
    ax.plot([0.3, 10.5], [y_pos, y_pos], color='#30363d', linewidth=1, ls='--')
    y_pos -= 0.3
    
    # CCD1
    for cpu, node, core, l3, max_mhz, avg_mhz in ccd1_cores:
        ax.text(x_pos[0], y_pos, str(cpu), fontsize=8, color='#58a6ff', fontfamily='monospace', ha='center')
        ax.text(x_pos[1], y_pos, str(node), fontsize=8, color='#c9d1d9', fontfamily='monospace', ha='center')
        ax.text(x_pos[2], y_pos, str(core), fontsize=8, color='#c9d1d9', fontfamily='monospace', ha='center')
        ax.text(x_pos[3], y_pos, l3, fontsize=8, color='#3fb950', fontfamily='monospace', ha='center')
        ax.text(x_pos[4], y_pos, f'{max_mhz:.1f}', fontsize=8, color='#c9d1d9', fontfamily='monospace', ha='center')
        ax.text(x_pos[5], y_pos, f'{avg_mhz:.1f}', fontsize=8, color='#c9d1d9', fontfamily='monospace', ha='center')
        
        # Red box around L3 column showing CCD1
        rect = Rectangle((x_pos[3] - 0.15, y_pos - 0.12), 0.3, 0.24, 
                       edgecolor='#f85149', facecolor='#f85149', alpha=0.2, linewidth=1.5)
        ax.add_patch(rect)
        
        y_pos -= 0.28
    
    # Annotations
    ax.text(5.5, 2.0, 'L3 Cache Column: Shows CCD boundary (0 or 1)', 
            fontsize=10, color='#f85149', ha='center', fontweight='bold')
    ax.text(5.5, 1.65, 'NUMA tools see: 1 node (0-31) | Reality: 2 CCDs with separate L3 caches', 
            fontsize=9, color='#8b949e', ha='center')
    
    plt.tight_layout()
    plt.savefig('/opt/opencode/src/self-2026/assets/issue_1070_lscpu.png', 
               dpi=150, bbox_inches='tight', facecolor='#0d1117')
    plt.close()
    print("Created: issue_1070_lscpu.png")


if __name__ == '__main__':
    os.makedirs('/opt/opencode/src/self-2026/assets', exist_ok=True)
    create_ps_output_screenshot()
    create_lscpu_topology_screenshot()
    print("All screenshots created!")
