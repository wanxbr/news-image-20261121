#!/usr/bin/env python3
"""
Entry point for make.fun news-image-20261121 bounty.
Copies the news image to the output directory.
"""
import os
import shutil
import sys

def main():
    # Get the output directory from environment variable, default to /output
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    output_path = os.path.join(output_dir, 'entry.png')
    
    # Source image path (in the repository)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, 'news-image-20261121.png')
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Copy the image
    shutil.copy2(source_path, output_path)
    
    # Verify the copy
    if os.path.exists(output_path):
        size = os.path.getsize(output_path)
        print(f"Copied {source_path} -> {output_path} ({size} bytes)")
        return 0
    else:
        print(f"Failed to copy image to {output_path}")
        return 1

if __name__ == '__main__':
    sys.exit(main())