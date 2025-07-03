#!/usr/bin/env python3
"""
Template Interpolator

Replace template references with actual content.
Supports parameter substitution and handles nested template references.

Usage:
    python template-interpolator.py <template_file> [--vars key=value ...]
    python template-interpolator.py <template_file> --template-dir <dir>
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Any, Tuple
import json

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Install with: pip install pyyaml")
    sys.exit(1)


class TemplateInterpolator:
    """Interpolate template references and variables in text files."""
    
    # Template reference patterns
    TEMPLATE_PATTERNS = [
        (r'\{\{(\w+)\}\}', 'double_braces'),           # {{template_name}}
        (r'\$\{(\w+)\}', 'dollar_braces'),             # ${template_name}
        (r'<template:(\w+)/>', 'xml_style'),           # <template:name/>
        (r'@include\((\w+)\)', 'include_style'),       # @include(name)
        (r'\[\[(\w+)\]\]', 'double_brackets'),         # [[template_name]]
    ]
    
    # Variable patterns
    VAR_PATTERNS = [
        (r'\{\{(\w+)\.(\w+)\}\}', 'dot_notation'),     # {{var.property}}
        (r'\$(\w+)', 'dollar_sign'),                   # $variable
        (r'%\{(\w+)\}', 'percent_braces'),             # %{variable}
    ]
    
    def __init__(self, template_dir: Path = None, max_depth: int = 10):
        """Initialize with template directory and maximum recursion depth."""
        self.template_dir = template_dir or Path.cwd()
        self.max_depth = max_depth
        self.template_cache = {}
        self.processed_templates = set()
    
    def load_template(self, template_name: str) -> str:
        """Load a template file by name."""
        if template_name in self.template_cache:
            return self.template_cache[template_name]
        
        # Search for template file
        search_paths = [
            self.template_dir / f"{template_name}",
            self.template_dir / f"{template_name}.txt",
            self.template_dir / f"{template_name}.tmpl",
            self.template_dir / f"{template_name}.template",
            self.template_dir / f"{template_name}.yaml",
            self.template_dir / f"{template_name}.yml",
        ]
        
        for path in search_paths:
            if path.exists():
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    self.template_cache[template_name] = content
                    return content
                except Exception as e:
                    raise RuntimeError(f"Error loading template {path}: {e}")
        
        raise FileNotFoundError(f"Template '{template_name}' not found in {self.template_dir}")
    
    def find_template_references(self, content: str) -> List[Tuple[str, str, str]]:
        """Find all template references in content."""
        references = []
        
        for pattern, style in self.TEMPLATE_PATTERNS:
            for match in re.finditer(pattern, content):
                full_match = match.group(0)
                template_name = match.group(1)
                references.append((full_match, template_name, style))
        
        return references
    
    def find_variables(self, content: str) -> List[Tuple[str, str, str]]:
        """Find all variable references in content."""
        variables = []
        
        for pattern, style in self.VAR_PATTERNS:
            for match in re.finditer(pattern, content):
                full_match = match.group(0)
                if style == 'dot_notation':
                    var_name = f"{match.group(1)}.{match.group(2)}"
                else:
                    var_name = match.group(1)
                variables.append((full_match, var_name, style))
        
        return variables
    
    def interpolate_variables(self, content: str, variables: Dict[str, Any]) -> str:
        """Replace variable references with values."""
        result = content
        
        for full_match, var_name, style in self.find_variables(content):
            value = None
            
            # Handle dot notation
            if '.' in var_name:
                parts = var_name.split('.')
                value = variables
                for part in parts:
                    if isinstance(value, dict) and part in value:
                        value = value[part]
                    else:
                        value = None
                        break
            else:
                value = variables.get(var_name)
            
            if value is not None:
                result = result.replace(full_match, str(value))
        
        return result
    
    def interpolate_templates(self, content: str, depth: int = 0) -> Tuple[str, Set[str]]:
        """Recursively interpolate template references."""
        if depth >= self.max_depth:
            raise RecursionError(f"Maximum template nesting depth ({self.max_depth}) exceeded")
        
        used_templates = set()
        result = content
        
        # Find and replace template references
        references = self.find_template_references(content)
        
        for full_match, template_name, style in references:
            if template_name in self.processed_templates:
                # Circular reference detected
                raise RecursionError(f"Circular template reference detected: {template_name}")
            
            try:
                # Mark as being processed
                self.processed_templates.add(template_name)
                
                # Load template content
                template_content = self.load_template(template_name)
                
                # Recursively process the template
                processed_content, nested_templates = self.interpolate_templates(
                    template_content, depth + 1
                )
                
                # Replace reference with processed content
                result = result.replace(full_match, processed_content)
                
                # Track used templates
                used_templates.add(template_name)
                used_templates.update(nested_templates)
                
            except FileNotFoundError:
                print(f"Warning: Template '{template_name}' not found, leaving reference unchanged")
            finally:
                # Unmark after processing
                self.processed_templates.discard(template_name)
        
        return result, used_templates
    
    def interpolate(self, content: str, variables: Dict[str, Any] = None) -> Dict[str, Any]:
        """Perform full interpolation of templates and variables."""
        variables = variables or {}
        
        # Reset state
        self.processed_templates.clear()
        
        # First, interpolate templates
        result, used_templates = self.interpolate_templates(content)
        
        # Then, interpolate variables
        result = self.interpolate_variables(result, variables)
        
        return {
            'content': result,
            'used_templates': list(used_templates),
            'variables': variables,
            'stats': {
                'original_length': len(content),
                'final_length': len(result),
                'templates_used': len(used_templates),
                'variables_used': len(variables)
            }
        }


def parse_variables(var_strings: List[str]) -> Dict[str, Any]:
    """Parse variable assignments from command line."""
    variables = {}
    
    for var_string in var_strings:
        if '=' not in var_string:
            print(f"Warning: Invalid variable format '{var_string}', expected 'key=value'")
            continue
        
        key, value = var_string.split('=', 1)
        
        # Try to parse value as JSON first
        try:
            parsed_value = json.loads(value)
            variables[key] = parsed_value
        except json.JSONDecodeError:
            # If not JSON, treat as string
            variables[key] = value
    
    return variables


def load_variables_file(file_path: Path) -> Dict[str, Any]:
    """Load variables from a JSON or YAML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if file_path.suffix in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            elif file_path.suffix == '.json':
                return json.load(f)
            else:
                print(f"Warning: Unknown file type {file_path.suffix}, trying JSON")
                return json.load(f)
    except Exception as e:
        print(f"Error loading variables file: {e}")
        return {}


def main():
    parser = argparse.ArgumentParser(
        description='Replace template references with actual content',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic interpolation
  python template-interpolator.py template.txt
  
  # With variables
  python template-interpolator.py template.txt --vars name=John age=30
  
  # With template directory
  python template-interpolator.py main.tmpl --template-dir ./templates
  
  # Load variables from file
  python template-interpolator.py template.txt --vars-file config.yaml
  
  # Output to file
  python template-interpolator.py template.txt -o output.txt
  
  # Show statistics
  python template-interpolator.py template.txt --stats

Template Reference Formats Supported:
  {{template_name}}     - Double brace style
  ${template_name}      - Dollar brace style
  <template:name/>      - XML style
  @include(name)        - Include style
  [[template_name]]     - Double bracket style

Variable Reference Formats Supported:
  {{var.property}}      - Dot notation for nested values
  $variable             - Dollar sign style
  %{variable}           - Percent brace style
        """
    )
    
    parser.add_argument('input_file', help='Template file to process')
    parser.add_argument('--template-dir', '-t', type=Path,
                       help='Directory containing template files')
    parser.add_argument('--vars', '-v', nargs='+', default=[],
                       help='Variables in key=value format')
    parser.add_argument('--vars-file', type=Path,
                       help='JSON or YAML file containing variables')
    parser.add_argument('--output', '-o', type=Path,
                       help='Output file (default: stdout)')
    parser.add_argument('--max-depth', type=int, default=10,
                       help='Maximum template nesting depth (default: 10)')
    parser.add_argument('--stats', action='store_true',
                       help='Show interpolation statistics')
    parser.add_argument('--debug', action='store_true',
                       help='Show debug information')
    
    args = parser.parse_args()
    
    # Validate input file
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found")
        sys.exit(1)
    
    # Set template directory
    template_dir = args.template_dir or input_path.parent
    
    # Initialize interpolator
    interpolator = TemplateInterpolator(
        template_dir=template_dir,
        max_depth=args.max_depth
    )
    
    # Load variables
    variables = {}
    
    # From command line
    if args.vars:
        variables.update(parse_variables(args.vars))
    
    # From file
    if args.vars_file:
        file_vars = load_variables_file(args.vars_file)
        variables.update(file_vars)
    
    try:
        # Read input file
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Perform interpolation
        result = interpolator.interpolate(content, variables)
        
        # Output result
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result['content'])
            print(f"Output written to: {args.output}")
        else:
            print(result['content'])
        
        # Show statistics if requested
        if args.stats:
            print("\n" + "=" * 60)
            print("INTERPOLATION STATISTICS")
            print("=" * 60)
            print(f"Original length: {result['stats']['original_length']:,} chars")
            print(f"Final length: {result['stats']['final_length']:,} chars")
            print(f"Templates used: {result['stats']['templates_used']}")
            if result['used_templates']:
                print(f"  - {', '.join(result['used_templates'])}")
            print(f"Variables provided: {result['stats']['variables_used']}")
            if variables:
                print(f"  - {', '.join(variables.keys())}")
        
        # Debug information
        if args.debug:
            print("\n" + "=" * 60)
            print("DEBUG INFORMATION")
            print("=" * 60)
            print(f"Template directory: {template_dir}")
            print(f"Max depth: {args.max_depth}")
            print(f"Variables: {json.dumps(variables, indent=2)}")
            
    except Exception as e:
        print(f"Error: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()