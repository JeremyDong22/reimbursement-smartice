#!/usr/bin/env python3
"""
Generate PWA icons from the monkey image
Requires: pillow (pip install pillow)
"""

from PIL import Image
import os

# Icon sizes needed for PWA
sizes = [16, 32, 72, 96, 128, 144, 152, 192, 384, 512]

# Source image
source_image = "Gemini_Generated_Image_its151its151its1.png"

# Create icons directory if it doesn't exist
os.makedirs("icons", exist_ok=True)

try:
    # Open the source image
    img = Image.open(source_image)
    
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    print(f"Generating PWA icons from {source_image}...")
    
    for size in sizes:
        # Resize the image with high quality
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        
        # Save the icon
        output_path = f"icons/icon-{size}x{size}.png"
        resized.save(output_path, "PNG", optimize=True)
        print(f"✓ Generated {output_path}")
    
    print("\n✅ All icons generated successfully!")
    print("Icons saved in the 'icons' directory")
    
except FileNotFoundError:
    print(f"Error: {source_image} not found!")
except Exception as e:
    print(f"Error: {e}")