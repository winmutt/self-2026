#!/usr/bin/env python3
"""
Generate NUMA vs Strix Halo APU comparison diagrams
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch
import os

def create_numa_diagram():
    """Create Traditional NUMA Architecture diagram"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    
    # Title
    ax.text(6, 7.5, 'Traditional NUMA Architecture', fontsize=16, fontweight='bold', 
            color='#c9d1d9', ha='center')
    
    # NUMA Node 0
    node0 = FancyBboxPatch((0.5, 1.5), 4.5, 5, boxstyle="round,pad=0.1,rounding_size=0.2",
                           linewidth=2, edgecolor='#58a6ff', facecolor='#161b22')
    ax.add_patch(node0)
    ax.text(2.75, 6.8, 'NUMA Node 0', fontsize=12, fontweight='bold', color='#58a6ff', ha='center')
    
    # Cores in Node 0
    cores0 = Rectangle((1.0, 4.5), 3.5, 1.5, linewidth=1.5, edgecolor='#30363d', facecolor='#21262d')
    ax.add_patch(cores0)
    ax.text(2.75, 5.5, '4-8 Cores', fontsize=10, color='#c9d1d9', ha='center')
    
    # L3 Cache in Node 0
    l3_0 = Rectangle((1.0, 3.2), 3.5, 1.0, linewidth=1.5, edgecolor='#3fb950', facecolor='#1a1f26')
    ax.add_patch(l3_0)
    ax.text(2.75, 3.7, '32MB L3 Cache', fontsize=9, color='#3fb950', ha='center')
    
    # Memory Controller in Node 0
    mem0 = Rectangle((1.0, 2.0), 3.5, 0.9, linewidth=1.5, edgecolor='#ffa657', facecolor='#1a1f26')
    ax.add_patch(mem0)
    ax.text(2.75, 2.45, 'Memory Controller (Local RAM)', fontsize=8, color='#ffa657', ha='center')
    
    # NUMA Node 1
    node1 = FancyBboxPatch((7.0, 1.5), 4.5, 5, boxstyle="round,pad=0.1,rounding_size=0.2",
                           linewidth=2, edgecolor='#58a6ff', facecolor='#161b22')
    ax.add_patch(node1)
    ax.text(9.25, 6.8, 'NUMA Node 1', fontsize=12, fontweight='bold', color='#58a6ff', ha='center')
    
    # Cores in Node 1
    cores1 = Rectangle((7.5, 4.5), 3.5, 1.5, linewidth=1.5, edgecolor='#30363d', facecolor='#21262d')
    ax.add_patch(cores1)
    ax.text(9.25, 5.5, '4-8 Cores', fontsize=10, color='#c9d1d9', ha='center')
    
    # L3 Cache in Node 1
    l3_1 = Rectangle((7.5, 3.2), 3.5, 1.0, linewidth=1.5, edgecolor='#3fb950', facecolor='#1a1f26')
    ax.add_patch(l3_1)
    ax.text(9.25, 3.7, '32MB L3 Cache', fontsize=9, color='#3fb950', ha='center')
    
    # Memory Controller in Node 1
    mem1 = Rectangle((7.5, 2.0), 3.5, 0.9, linewidth=1.5, edgecolor='#ffa657', facecolor='#1a1f26')
    ax.add_patch(mem1)
    ax.text(9.25, 2.45, 'Memory Controller (Local RAM)', fontsize=8, color='#ffa657', ha='center')
    
    # Interconnect arrow
    ax.annotate('', xy=(5.0, 3.0), xytext=(7.0, 3.0),
                arrowprops=dict(arrowstyle='<->', color='#8b949e', lw=2, ls='--'))
    ax.text(6.0, 3.3, 'High-latency interconnect', fontsize=8, color='#8b949e', ha='center')
    
    # Legend
    ax.text(6, 0.8, 'Each node has dedicated cores, L3 cache, and memory. '
                    'Process pinned to Node 0 stays in Node 0 domain.', 
            fontsize=10, color='#8b949e', ha='center')
    
    plt.tight_layout()
    plt.savefig('/opt/opencode/src/self-2026/assets/numa_traditional.png', 
               dpi=150, bbox_inches='tight', facecolor='#0d1117')
    plt.close()
    print("Created: numa_traditional.png")


def create_strix_halo_diagram():
    """Create Strix Halo APU Architecture diagram"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_facecolor('#0d1117')
    ax.axis('off')
    
    # Title
    ax.text(6, 7.5, 'Strix Halo APU Architecture', fontsize=16, fontweight='bold', 
            color='#c9d1d9', ha='center')
    
    # Single NUMA Node box
    numa_node = FancyBboxPatch((0.5, 0.5), 11, 6.5, boxstyle="round,pad=0.1,rounding_size=0.2",
                               linewidth=2, edgecolor='#bc8cff', facecolor='#161b22', linestyle='--')
    ax.add_patch(numa_node)
    ax.text(6, 7.0, 'Single NUMA Node (0-31)', fontsize=11, fontweight='bold', color='#bc8cff', ha='center')
    
    # CCD 0
    ccd0 = FancyBboxPatch((1.0, 2.5), 4.5, 3.5, boxstyle="round,pad=0.1,rounding_size=0.15",
                          linewidth=2, edgecolor='#58a6ff', facecolor='#0d1117')
    ax.add_patch(ccd0)
    ax.text(3.25, 6.0, 'CCD 0', fontsize=12, fontweight='bold', color='#58a6ff', ha='center')
    
    # Cores in CCD 0
    cores0 = Rectangle((1.5, 3.8), 3.5, 1.5, linewidth=1.5, edgecolor='#30363d', facecolor='#21262d')
    ax.add_patch(cores0)
    ax.text(3.25, 4.6, '8 Cores (0-7)', fontsize=10, color='#c9d1d9', ha='center')
    
    # L3 Cache in CCD 0
    l3_0 = Rectangle((1.5, 2.9), 3.5, 0.7, linewidth=1.5, edgecolor='#3fb950', facecolor='#1a1f26')
    ax.add_patch(l3_0)
    ax.text(3.25, 3.25, '32MB L3 Cache', fontsize=9, color='#3fb950', ha='center')
    
    # CCD 1
    ccd1 = FancyBboxPatch((6.5, 2.5), 4.5, 3.5, boxstyle="round,pad=0.1,rounding_size=0.15",
                          linewidth=2, edgecolor='#58a6ff', facecolor='#0d1117')
    ax.add_patch(ccd1)
    ax.text(8.75, 6.0, 'CCD 1', fontsize=12, fontweight='bold', color='#58a6ff', ha='center')
    
    # Cores in CCD 1
    cores1 = Rectangle((7.0, 3.8), 3.5, 1.5, linewidth=1.5, edgecolor='#30363d', facecolor='#21262d')
    ax.add_patch(cores1)
    ax.text(8.75, 4.6, '8 Cores (8-15)', fontsize=10, color='#c9d1d9', ha='center')
    
    # L3 Cache in CCD 1
    l3_1 = Rectangle((7.0, 2.9), 3.5, 0.7, linewidth=1.5, edgecolor='#3fb950', facecolor='#1a1f26')
    ax.add_patch(l3_1)
    ax.text(8.75, 3.25, '32MB L3 Cache', fontsize=9, color='#3fb950', ha='center')
    
    # Unified Memory
    mem = Rectangle((1.0, 1.0), 10, 1.2, linewidth=1.5, edgecolor='#ffa657', facecolor='#1a1f26')
    ax.add_patch(mem)
    ax.text(6, 1.6, 'Unified Memory (128GB LPDDR5X-8000) - Shared by all cores', 
            fontsize=9, color='#ffa657', ha='center')
    
    # Problem annotation
    ax.text(6, 0.5, 'PROBLEM: NUMA tools see 1 node, cannot detect CCD boundaries. '
                    'Threads bounce across CCDs -> L3 cache misses.', 
            fontsize=9, color='#f85149', ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/opt/opencode/src/self-2026/assets/strix_halo_numa.png', 
               dpi=150, bbox_inches='tight', facecolor='#0d1117')
    plt.close()
    print("Created: strix_halo_numa.png")


if __name__ == '__main__':
    os.makedirs('/opt/opencode/src/self-2026/assets', exist_ok=True)
    create_numa_diagram()
    create_strix_halo_diagram()
    print("All diagrams created!")
