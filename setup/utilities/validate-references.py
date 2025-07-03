#!/usr/bin/env python3
"""
Utility to validate references in optimized prompts.
Checks that all $ref: references point to valid components.
"""

import yaml
import sys
import re
from pathlib import Path


def extract_references(content):
    """Extract all $ref: references from content."""
    pattern = r'\$ref:\s*([^\s\n]+)'
    return re.findall(pattern, content)


def parse_reference(ref):
    """Parse a reference into file and path components."""
    if '#' in ref:
        file_part, path_part = ref.split('#', 1)
        return file_part, path_part
    return ref, None


def validate_reference(ref, base_path):
    """Validate that a reference points to an existing component."""
    file_part, path_part = parse_reference(ref)
    
    # Resolve file path
    file_path = base_path / file_part
    if not file_path.exists():
        return False, f"File not found: {file_path}"
    
    # Load YAML file
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        return False, f"Failed to parse YAML: {e}"
    
    # If no path part, reference is valid
    if not path_part:
        return True, "Valid file reference"
    
    # Navigate to the referenced path
    path_parts = path_part.strip('/').split('/')
    current = data
    
    for part in path_parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return False, f"Path not found: {path_part}"
    
    return True, "Valid reference"


def validate_prompt_file(prompt_file, setup_path):
    """Validate all references in a prompt file."""
    print(f"\nValidating: {prompt_file}")
    
    try:
        with open(prompt_file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"  ERROR: Could not read file: {e}")
        return False
    
    references = extract_references(content)
    if not references:
        print("  No references found")
        return True
    
    all_valid = True
    for ref in references:
        valid, message = validate_reference(ref, setup_path)
        if valid:
            print(f"  ✓ {ref}")
        else:
            print(f"  ✗ {ref}: {message}")
            all_valid = False
    
    return all_valid


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python validate-references.py <prompt_file> [prompt_file...]")
        sys.exit(1)
    
    setup_path = Path(__file__).parent.parent
    all_valid = True
    
    for prompt_file in sys.argv[1:]:
        if not validate_prompt_file(Path(prompt_file), setup_path):
            all_valid = False
    
    if all_valid:
        print("\nAll references are valid!")
    else:
        print("\nSome references are invalid.")
        sys.exit(1)


if __name__ == "__main__":
    main()