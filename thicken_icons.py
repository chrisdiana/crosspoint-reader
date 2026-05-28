import os
import re

icon_files = [
    "calculator.h", "calculator24.h",
    "weather.h", "weather24.h",
    "sudoku.h", "sudoku24.h",
    "reddit.h", "reddit24.h"
]

base_dir = "/Users/zakerytclarke/Documents/crosspoint-reader-apps/src/components/icons"

def get_bit(data, width, x, y):
    if x < 0 or x >= width or y < 0 or y >= len(data) // (width // 8):
        return 1
    idx = y * (width // 8) + (x // 8)
    bit_idx = 7 - (x % 8)
    return (data[idx] >> bit_idx) & 1

def set_bit(data, width, x, y, val):
    idx = y * (width // 8) + (x // 8)
    bit_idx = 7 - (x % 8)
    if val:
        data[idx] |= (1 << bit_idx)
    else:
        data[idx] &= ~(1 << bit_idx)

for filename in icon_files:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"Not found: {filepath}")
        continue
    
    with open(filepath, "r") as f:
        content = f.read()
    
    # Extract the hex array
    match = re.search(r'\{(.*?)\}', content, re.DOTALL)
    if not match:
        continue
    
    hex_str = match.group(1)
    hex_vals = [int(x.strip(), 16) for x in hex_str.split(',') if x.strip()]
    
    # Determine width and height
    # e.g., 32x32 = 128 bytes (4 bytes per row)
    # 24x24 = 72 bytes (3 bytes per row)
    if len(hex_vals) == 128:
        width = 32
        height = 32
    elif len(hex_vals) == 72:
        width = 24
        height = 24
    else:
        print(f"Unknown size for {filename}: {len(hex_vals)} bytes")
        continue
    
    # Create output array filled with 1s (0xFF)
    new_data = [0xFF] * len(hex_vals)
    
    # Thicken: for every pixel, if it or any neighbor is 0, make it 0.
    for y in range(height):
        for x in range(width):
            b0 = get_bit(hex_vals, width, x, y)
            b1 = get_bit(hex_vals, width, x-1, y)
            b2 = get_bit(hex_vals, width, x+1, y)
            b3 = get_bit(hex_vals, width, x, y-1)
            b4 = get_bit(hex_vals, width, x, y+1)
            
            # If any is 0, output is 0
            if b0 == 0 or b1 == 0 or b2 == 0 or b3 == 0 or b4 == 0:
                set_bit(new_data, width, x, y, 0)
    
    # Format output
    new_hex_str = ""
    for i, val in enumerate(new_data):
        if i > 0 and i % 16 == 0:
            new_hex_str += "\n    "
        elif i == 0:
            new_hex_str += "\n    "
        else:
            new_hex_str += " "
        new_hex_str += f"0x{val:02X},"
    
    new_hex_str = new_hex_str.strip(',') + "\n"
    new_content = content[:match.start(1)] + new_hex_str + content[match.end(1):]
    
    with open(filepath, "w") as f:
        f.write(new_content)
    
    print(f"Thickened {filename}")
