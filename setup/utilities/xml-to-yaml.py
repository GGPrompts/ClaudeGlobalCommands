#!/usr/bin/env python3
"""
XML to YAML Converter

Convert XML structured prompts to YAML format while preserving all content and structure.
Handles nested elements properly and maintains formatting.

Usage:
    python xml-to-yaml.py <xml_file> [output_file]
    python xml-to-yaml.py <directory> --batch
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List, Union, Any
import re

try:
    import yaml
    from xml.etree import ElementTree as ET
except ImportError as e:
    print(f"Error: Missing required library. Install with: pip install pyyaml")
    sys.exit(1)


class XMLToYAMLConverter:
    """Convert XML documents to YAML format."""
    
    def __init__(self, preserve_order: bool = True, preserve_comments: bool = True):
        """Initialize converter with options."""
        self.preserve_order = preserve_order
        self.preserve_comments = preserve_comments
        self.comment_pattern = re.compile(r'<!--(.*?)-->', re.DOTALL)
    
    def extract_comments(self, xml_content: str) -> List[Tuple[str, str]]:
        """Extract comments from XML content."""
        comments = []
        for match in self.comment_pattern.finditer(xml_content):
            comment_text = match.group(1).strip()
            comments.append((match.start(), comment_text))
        return comments
    
    def xml_to_dict(self, element: ET.Element) -> Union[Dict, str, List]:
        """Convert XML element to dictionary structure."""
        result = {}
        
        # Handle attributes
        if element.attrib:
            result['@attributes'] = dict(element.attrib)
        
        # Handle text content
        if element.text and element.text.strip():
            text = element.text.strip()
            if len(element) == 0 and not element.attrib:
                # Leaf node with only text
                return text
            else:
                result['@text'] = text
        
        # Handle child elements
        children = {}
        for child in element:
            child_data = self.xml_to_dict(child)
            
            if child.tag in children:
                # Multiple children with same tag - convert to list
                if not isinstance(children[child.tag], list):
                    children[child.tag] = [children[child.tag]]
                children[child.tag].append(child_data)
            else:
                children[child.tag] = child_data
            
            # Handle tail text (text after child element)
            if child.tail and child.tail.strip():
                if '@tail' not in result:
                    result['@tail'] = []
                result['@tail'].append({
                    'after': child.tag,
                    'text': child.tail.strip()
                })
        
        # Merge children into result
        result.update(children)
        
        # Simplify if only text content
        if len(result) == 1 and '@text' in result:
            return result['@text']
        
        return result if result else None
    
    def clean_yaml_structure(self, data: Any) -> Any:
        """Clean up the YAML structure for better readability."""
        if isinstance(data, dict):
            cleaned = {}
            
            # Handle special keys
            text_content = data.get('@text', '')
            attributes = data.get('@attributes', {})
            tail_content = data.get('@tail', [])
            
            # Remove special keys from main dict
            regular_keys = {k: v for k, v in data.items() 
                          if not k.startswith('@')}
            
            # Restructure based on content
            if attributes:
                cleaned['attributes'] = attributes
            
            if text_content and regular_keys:
                cleaned['content'] = text_content
            elif text_content and not regular_keys:
                return text_content
            
            # Process regular keys
            for key, value in regular_keys.items():
                cleaned[key] = self.clean_yaml_structure(value)
            
            if tail_content:
                cleaned['tail_text'] = tail_content
            
            return cleaned if cleaned else None
        
        elif isinstance(data, list):
            return [self.clean_yaml_structure(item) for item in data]
        
        else:
            return data
    
    def convert_file(self, xml_path: Path, yaml_path: Path = None) -> Dict:
        """Convert XML file to YAML format."""
        try:
            # Read XML content
            with open(xml_path, 'r', encoding='utf-8') as f:
                xml_content = f.read()
            
            # Extract comments if preserving
            comments = []
            if self.preserve_comments:
                comments = self.extract_comments(xml_content)
            
            # Parse XML
            root = ET.fromstring(xml_content)
            
            # Convert to dictionary
            data = {root.tag: self.xml_to_dict(root)}
            
            # Clean structure
            cleaned_data = self.clean_yaml_structure(data)
            
            # Add metadata
            result = {
                '_metadata': {
                    'source': str(xml_path),
                    'converter': 'xml-to-yaml.py',
                    'version': '1.0'
                }
            }
            
            if comments:
                result['_comments'] = [c[1] for c in comments]
            
            result.update(cleaned_data)
            
            # Write YAML if output path provided
            if yaml_path:
                with open(yaml_path, 'w', encoding='utf-8') as f:
                    yaml.dump(result, f, 
                             default_flow_style=False,
                             allow_unicode=True,
                             sort_keys=not self.preserve_order,
                             width=80,
                             indent=2)
            
            return result
            
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML in {xml_path}: {e}")
        except Exception as e:
            raise RuntimeError(f"Error converting {xml_path}: {e}")
    
    def convert_directory(self, directory: Path, output_dir: Path = None) -> Dict[str, str]:
        """Convert all XML files in a directory."""
        results = {}
        xml_files = list(directory.glob('*.xml'))
        
        if not xml_files:
            print(f"No XML files found in {directory}")
            return results
        
        if output_dir and not output_dir.exists():
            output_dir.mkdir(parents=True)
        
        for xml_file in xml_files:
            try:
                yaml_name = xml_file.stem + '.yaml'
                yaml_path = output_dir / yaml_name if output_dir else xml_file.parent / yaml_name
                
                self.convert_file(xml_file, yaml_path)
                results[str(xml_file)] = str(yaml_path)
                print(f"Converted: {xml_file} -> {yaml_path}")
                
            except Exception as e:
                print(f"Error converting {xml_file}: {e}")
                results[str(xml_file)] = f"ERROR: {e}"
        
        return results


def create_sample_xml():
    """Create a sample XML file for testing."""
    sample = """<?xml version="1.0" encoding="UTF-8"?>
<!-- Sample prompt structure -->
<prompt version="1.0">
    <metadata>
        <author>System</author>
        <date>2024-01-01</date>
        <tags>
            <tag>example</tag>
            <tag>template</tag>
        </tags>
    </metadata>
    <content>
        <section name="introduction">
            <text>This is an example prompt structure.</text>
            <note importance="high">Pay attention to formatting</note>
        </section>
        <section name="instructions">
            <instruction>Step 1: Read the input</instruction>
            <instruction>Step 2: Process the data</instruction>
            <instruction>Step 3: Generate output</instruction>
        </section>
    </content>
</prompt>"""
    return sample


def main():
    parser = argparse.ArgumentParser(
        description='Convert XML structured prompts to YAML format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert a single XML file
  python xml-to-yaml.py prompt.xml
  
  # Convert and save to specific file
  python xml-to-yaml.py input.xml output.yaml
  
  # Convert all XML files in a directory
  python xml-to-yaml.py prompts/ --batch
  
  # Convert directory and save to output directory
  python xml-to-yaml.py prompts/ --batch --output converted/
  
  # Create a sample XML file
  python xml-to-yaml.py --sample
        """
    )
    
    parser.add_argument('input_path', nargs='?', help='XML file or directory path')
    parser.add_argument('output_path', nargs='?', help='Output YAML file or directory')
    parser.add_argument('--batch', action='store_true',
                       help='Convert all XML files in directory')
    parser.add_argument('--output', '-o', help='Output directory for batch conversion')
    parser.add_argument('--no-preserve-order', action='store_true',
                       help='Do not preserve element order')
    parser.add_argument('--no-comments', action='store_true',
                       help='Do not preserve comments')
    parser.add_argument('--sample', action='store_true',
                       help='Create a sample XML file')
    parser.add_argument('--pretty', action='store_true',
                       help='Pretty print output to console')
    
    args = parser.parse_args()
    
    # Handle sample creation
    if args.sample:
        sample_path = Path('sample_prompt.xml')
        with open(sample_path, 'w', encoding='utf-8') as f:
            f.write(create_sample_xml())
        print(f"Sample XML file created: {sample_path}")
        return
    
    # Check input
    if not args.input_path:
        parser.error("Input path required unless using --sample")
    
    input_path = Path(args.input_path)
    if not input_path.exists():
        print(f"Error: {input_path} does not exist")
        sys.exit(1)
    
    # Initialize converter
    converter = XMLToYAMLConverter(
        preserve_order=not args.no_preserve_order,
        preserve_comments=not args.no_comments
    )
    
    # Handle batch conversion
    if args.batch or input_path.is_dir():
        if not input_path.is_dir():
            print("Error: Batch mode requires a directory path")
            sys.exit(1)
        
        output_dir = Path(args.output) if args.output else None
        results = converter.convert_directory(input_path, output_dir)
        
        print(f"\nConversion complete: {len(results)} files processed")
        
    # Handle single file conversion
    else:
        output_path = Path(args.output_path) if args.output_path else None
        if not output_path:
            output_path = input_path.with_suffix('.yaml')
        
        try:
            result = converter.convert_file(input_path, output_path)
            print(f"Converted: {input_path} -> {output_path}")
            
            if args.pretty:
                print("\nYAML Output:")
                print("-" * 60)
                print(yaml.dump(result, default_flow_style=False, width=80))
                
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == '__main__':
    main()