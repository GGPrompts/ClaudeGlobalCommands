#!/usr/bin/env python3
"""
Token Counter Utility

Count tokens in prompt files using tiktoken library.
Supports before/after comparison and generates reduction percentage reports.

Usage:
    python token-counter.py <file_path>
    python token-counter.py <before_file> <after_file> --compare
    python token-counter.py <directory> --recursive
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import tiktoken
except ImportError:
    print("Error: tiktoken library not installed. Install with: pip install tiktoken")
    sys.exit(1)


class TokenCounter:
    """Count tokens in text files using tiktoken."""
    
    def __init__(self, model: str = "gpt-4"):
        """Initialize with encoding for specified model."""
        try:
            self.encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            # Fallback to cl100k_base encoding
            self.encoding = tiktoken.get_encoding("cl100k_base")
    
    def count_tokens(self, text: str) -> int:
        """Count tokens in a given text."""
        return len(self.encoding.encode(text))
    
    def count_file_tokens(self, file_path: Path) -> int:
        """Count tokens in a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.count_tokens(content)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return 0
    
    def compare_files(self, before_path: Path, after_path: Path) -> Dict[str, any]:
        """Compare token counts between two files."""
        before_tokens = self.count_file_tokens(before_path)
        after_tokens = self.count_file_tokens(after_path)
        
        reduction = before_tokens - after_tokens
        reduction_pct = (reduction / before_tokens * 100) if before_tokens > 0 else 0
        
        return {
            'before_file': str(before_path),
            'after_file': str(after_path),
            'before_tokens': before_tokens,
            'after_tokens': after_tokens,
            'reduction': reduction,
            'reduction_percentage': reduction_pct,
            'increase': reduction < 0
        }
    
    def count_directory_tokens(self, directory: Path, recursive: bool = False, 
                             extensions: List[str] = None) -> Dict[str, int]:
        """Count tokens in all files in a directory."""
        if extensions is None:
            extensions = ['.txt', '.md', '.yaml', '.yml', '.json', '.xml']
        
        results = {}
        pattern = '**/*' if recursive else '*'
        
        for file_path in directory.glob(pattern):
            if file_path.is_file() and file_path.suffix in extensions:
                tokens = self.count_file_tokens(file_path)
                results[str(file_path)] = tokens
        
        return results


def format_report(comparison: Dict[str, any]) -> str:
    """Format a comparison report."""
    report = []
    report.append("=" * 60)
    report.append("TOKEN COMPARISON REPORT")
    report.append("=" * 60)
    report.append(f"Before: {comparison['before_file']}")
    report.append(f"After:  {comparison['after_file']}")
    report.append("-" * 60)
    report.append(f"Before tokens: {comparison['before_tokens']:,}")
    report.append(f"After tokens:  {comparison['after_tokens']:,}")
    report.append("-" * 60)
    
    if comparison['increase']:
        report.append(f"Token INCREASE: {abs(comparison['reduction']):,} tokens")
        report.append(f"Increase percentage: {abs(comparison['reduction_percentage']):.2f}%")
    else:
        report.append(f"Token reduction: {comparison['reduction']:,} tokens")
        report.append(f"Reduction percentage: {comparison['reduction_percentage']:.2f}%")
    
    report.append("=" * 60)
    return '\n'.join(report)


def format_directory_report(results: Dict[str, int], directory: str) -> str:
    """Format a directory scan report."""
    report = []
    report.append("=" * 60)
    report.append(f"TOKEN COUNT REPORT - {directory}")
    report.append("=" * 60)
    
    total_tokens = 0
    for file_path, tokens in sorted(results.items()):
        report.append(f"{file_path}: {tokens:,} tokens")
        total_tokens += tokens
    
    report.append("-" * 60)
    report.append(f"Total files: {len(results)}")
    report.append(f"Total tokens: {total_tokens:,}")
    report.append("=" * 60)
    return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='Count tokens in prompt files using tiktoken library',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Count tokens in a single file
  python token-counter.py prompt.txt
  
  # Compare before and after files
  python token-counter.py original.txt optimized.txt --compare
  
  # Count tokens in all files in a directory
  python token-counter.py prompts/ --recursive
  
  # Count only specific file types
  python token-counter.py prompts/ --extensions .txt .md
        """
    )
    
    parser.add_argument('paths', nargs='+', help='File or directory paths')
    parser.add_argument('--compare', action='store_true', 
                       help='Compare two files (requires exactly 2 paths)')
    parser.add_argument('--recursive', '-r', action='store_true',
                       help='Recursively scan directories')
    parser.add_argument('--model', default='gpt-4',
                       help='Model to use for tokenization (default: gpt-4)')
    parser.add_argument('--extensions', nargs='+',
                       help='File extensions to include (default: .txt .md .yaml .yml .json .xml)')
    parser.add_argument('--output', '-o', help='Output file for report')
    
    args = parser.parse_args()
    
    # Initialize token counter
    counter = TokenCounter(model=args.model)
    
    # Handle comparison mode
    if args.compare:
        if len(args.paths) != 2:
            parser.error("--compare requires exactly 2 file paths")
        
        before_path = Path(args.paths[0])
        after_path = Path(args.paths[1])
        
        if not before_path.exists() or not after_path.exists():
            print("Error: Both files must exist for comparison")
            sys.exit(1)
        
        comparison = counter.compare_files(before_path, after_path)
        report = format_report(comparison)
        
    # Handle single file or directory
    else:
        path = Path(args.paths[0])
        
        if path.is_file():
            tokens = counter.count_file_tokens(path)
            report = f"{path}: {tokens:,} tokens"
        
        elif path.is_dir():
            results = counter.count_directory_tokens(
                path, 
                recursive=args.recursive,
                extensions=args.extensions
            )
            report = format_directory_report(results, str(path))
        
        else:
            print(f"Error: {path} is not a valid file or directory")
            sys.exit(1)
    
    # Output report
    print(report)
    
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\nReport saved to: {args.output}")
        except Exception as e:
            print(f"Error saving report: {e}")


if __name__ == '__main__':
    main()