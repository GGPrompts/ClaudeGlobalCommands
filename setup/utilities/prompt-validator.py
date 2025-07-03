#!/usr/bin/env python3
"""
Prompt Validator

Validate optimized prompts for:
- Missing template references
- Template existence verification
- YAML syntax validation
- Structure consistency
- Reference integrity

Usage:
    python prompt-validator.py <prompt_file>
    python prompt-validator.py <directory> --recursive
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any
import json

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Install with: pip install pyyaml")
    sys.exit(1)


class ValidationIssue:
    """Represents a validation issue found in a prompt."""
    
    SEVERITY_ERROR = 'ERROR'
    SEVERITY_WARNING = 'WARNING'
    SEVERITY_INFO = 'INFO'
    
    def __init__(self, severity: str, category: str, message: str, 
                 line: int = None, column: int = None, context: str = None):
        self.severity = severity
        self.category = category
        self.message = message
        self.line = line
        self.column = column
        self.context = context
    
    def __str__(self):
        location = f" (line {self.line}" if self.line else ""
        location += f", col {self.column})" if self.column else ")" if self.line else ""
        
        result = f"[{self.severity}] {self.category}: {self.message}{location}"
        if self.context:
            result += f"\n    Context: {self.context}"
        return result


class PromptValidator:
    """Validate prompt files for various issues."""
    
    # Template reference patterns
    TEMPLATE_PATTERNS = [
        (r'\{\{(\w+)\}\}', 'double_braces'),
        (r'\$\{(\w+)\}', 'dollar_braces'),
        (r'<template:(\w+)/>', 'xml_style'),
        (r'@include\((\w+)\)', 'include_style'),
        (r'\[\[(\w+)\]\]', 'double_brackets'),
    ]
    
    # Variable patterns
    VAR_PATTERNS = [
        (r'\{\{(\w+)\.(\w+)\}\}', 'dot_notation'),
        (r'\$(\w+)(?!\{)', 'dollar_sign'),
        (r'%\{(\w+)\}', 'percent_braces'),
    ]
    
    # Common prompt structure keys
    EXPECTED_KEYS = {
        'metadata', 'version', 'description', 'author',
        'content', 'templates', 'variables', 'sections'
    }
    
    def __init__(self, template_dir: Path = None, strict: bool = False):
        """Initialize validator with options."""
        self.template_dir = template_dir or Path.cwd()
        self.strict = strict
        self.issues = []
        self.checked_templates = set()
    
    def add_issue(self, severity: str, category: str, message: str, **kwargs):
        """Add a validation issue."""
        self.issues.append(ValidationIssue(severity, category, message, **kwargs))
    
    def validate_yaml_syntax(self, file_path: Path) -> bool:
        """Validate YAML syntax."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                yaml.safe_load(content)
            return True
        except yaml.YAMLError as e:
            # Extract line/column from error if available
            line = getattr(e, 'problem_mark', None)
            if line:
                self.add_issue(
                    ValidationIssue.SEVERITY_ERROR,
                    'YAML Syntax',
                    f"Invalid YAML syntax: {e.problem}",
                    line=line.line + 1,
                    column=line.column + 1
                )
            else:
                self.add_issue(
                    ValidationIssue.SEVERITY_ERROR,
                    'YAML Syntax',
                    f"Invalid YAML syntax: {str(e)}"
                )
            return False
        except Exception as e:
            self.add_issue(
                ValidationIssue.SEVERITY_ERROR,
                'File Read',
                f"Cannot read file: {str(e)}"
            )
            return False
    
    def find_template_references(self, content: str) -> Set[str]:
        """Find all template references in content."""
        references = set()
        
        for pattern, style in self.TEMPLATE_PATTERNS:
            for match in re.finditer(pattern, content):
                template_name = match.group(1)
                references.add(template_name)
        
        return references
    
    def find_variable_references(self, content: str) -> Set[str]:
        """Find all variable references in content."""
        variables = set()
        
        for pattern, style in self.VAR_PATTERNS:
            for match in re.finditer(pattern, content):
                if style == 'dot_notation':
                    var_name = f"{match.group(1)}.{match.group(2)}"
                else:
                    var_name = match.group(1)
                variables.add(var_name)
        
        return variables
    
    def check_template_exists(self, template_name: str) -> bool:
        """Check if a template file exists."""
        if template_name in self.checked_templates:
            return True
        
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
                self.checked_templates.add(template_name)
                return True
        
        return False
    
    def validate_structure(self, data: Dict[str, Any], file_path: Path):
        """Validate the structure of parsed YAML data."""
        # Check for recommended top-level keys
        missing_keys = []
        for key in ['metadata', 'content']:
            if key not in data and self.strict:
                missing_keys.append(key)
        
        if missing_keys:
            self.add_issue(
                ValidationIssue.SEVERITY_WARNING,
                'Structure',
                f"Missing recommended top-level keys: {', '.join(missing_keys)}"
            )
        
        # Validate metadata if present
        if 'metadata' in data:
            metadata = data['metadata']
            if not isinstance(metadata, dict):
                self.add_issue(
                    ValidationIssue.SEVERITY_ERROR,
                    'Structure',
                    "Metadata should be a dictionary/object"
                )
            else:
                # Check for version
                if 'version' not in metadata and self.strict:
                    self.add_issue(
                        ValidationIssue.SEVERITY_INFO,
                        'Structure',
                        "No version specified in metadata"
                    )
        
        # Check for unused keys
        all_keys = set(data.keys())
        known_keys = self.EXPECTED_KEYS | {'_metadata', '_comments'}
        unknown_keys = all_keys - known_keys
        
        if unknown_keys and self.strict:
            self.add_issue(
                ValidationIssue.SEVERITY_INFO,
                'Structure',
                f"Unknown top-level keys: {', '.join(unknown_keys)}"
            )
    
    def validate_references(self, content: str, file_path: Path):
        """Validate template and variable references."""
        # Find all template references
        template_refs = self.find_template_references(content)
        
        for template_name in template_refs:
            if not self.check_template_exists(template_name):
                # Find line number for better error reporting
                line_num = None
                for i, line in enumerate(content.split('\n'), 1):
                    if template_name in line:
                        line_num = i
                        break
                
                self.add_issue(
                    ValidationIssue.SEVERITY_ERROR,
                    'Template Reference',
                    f"Template '{template_name}' not found",
                    line=line_num,
                    context=f"Searched in: {self.template_dir}"
                )
        
        # Find all variable references
        var_refs = self.find_variable_references(content)
        
        if var_refs:
            self.add_issue(
                ValidationIssue.SEVERITY_INFO,
                'Variables',
                f"Found {len(var_refs)} variable reference(s): {', '.join(sorted(var_refs))}"
            )
    
    def validate_file(self, file_path: Path) -> List[ValidationIssue]:
        """Validate a single prompt file."""
        self.issues = []
        
        # Check file exists
        if not file_path.exists():
            self.add_issue(
                ValidationIssue.SEVERITY_ERROR,
                'File',
                f"File not found: {file_path}"
            )
            return self.issues
        
        # Read file content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.add_issue(
                ValidationIssue.SEVERITY_ERROR,
                'File Read',
                f"Cannot read file: {str(e)}"
            )
            return self.issues
        
        # Validate based on file type
        if file_path.suffix in ['.yaml', '.yml']:
            # Validate YAML syntax
            if self.validate_yaml_syntax(file_path):
                # Parse and validate structure
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = yaml.safe_load(f)
                    
                    if isinstance(data, dict):
                        self.validate_structure(data, file_path)
                    
                except Exception as e:
                    self.add_issue(
                        ValidationIssue.SEVERITY_ERROR,
                        'Parse',
                        f"Error parsing file: {str(e)}"
                    )
        
        # Always validate references
        self.validate_references(content, file_path)
        
        # Check for common issues
        self.check_common_issues(content, file_path)
        
        return self.issues
    
    def check_common_issues(self, content: str, file_path: Path):
        """Check for common prompt issues."""
        lines = content.split('\n')
        
        # Check for very long lines
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                self.add_issue(
                    ValidationIssue.SEVERITY_INFO,
                    'Formatting',
                    f"Line exceeds 120 characters ({len(line)} chars)",
                    line=i
                )
        
        # Check for tabs vs spaces
        has_tabs = '\t' in content
        has_spaces = '    ' in content  # 4 spaces
        
        if has_tabs and has_spaces:
            self.add_issue(
                ValidationIssue.SEVERITY_WARNING,
                'Formatting',
                "Mixed tabs and spaces for indentation"
            )
        
        # Check for trailing whitespace
        for i, line in enumerate(lines, 1):
            if line.endswith(' ') or line.endswith('\t'):
                self.add_issue(
                    ValidationIssue.SEVERITY_INFO,
                    'Formatting',
                    "Trailing whitespace",
                    line=i
                )
        
        # Check for TODO/FIXME comments
        todo_pattern = re.compile(r'(TODO|FIXME|XXX|HACK|BUG):', re.IGNORECASE)
        for i, line in enumerate(lines, 1):
            if todo_pattern.search(line):
                self.add_issue(
                    ValidationIssue.SEVERITY_INFO,
                    'Comments',
                    f"Found TODO/FIXME comment",
                    line=i,
                    context=line.strip()
                )


def format_validation_report(file_path: Path, issues: List[ValidationIssue]) -> str:
    """Format a validation report."""
    report = []
    report.append("=" * 60)
    report.append(f"VALIDATION REPORT: {file_path}")
    report.append("=" * 60)
    
    if not issues:
        report.append("✓ No issues found!")
    else:
        # Count by severity
        error_count = sum(1 for i in issues if i.severity == ValidationIssue.SEVERITY_ERROR)
        warning_count = sum(1 for i in issues if i.severity == ValidationIssue.SEVERITY_WARNING)
        info_count = sum(1 for i in issues if i.severity == ValidationIssue.SEVERITY_INFO)
        
        report.append(f"Found {len(issues)} issue(s):")
        report.append(f"  - Errors: {error_count}")
        report.append(f"  - Warnings: {warning_count}")
        report.append(f"  - Info: {info_count}")
        report.append("-" * 60)
        
        # Group issues by category
        by_category = {}
        for issue in issues:
            if issue.category not in by_category:
                by_category[issue.category] = []
            by_category[issue.category].append(issue)
        
        for category, category_issues in sorted(by_category.items()):
            report.append(f"\n{category}:")
            for issue in category_issues:
                report.append(f"  {issue}")
    
    report.append("=" * 60)
    return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(
        description='Validate optimized prompts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate a single prompt file
  python prompt-validator.py prompt.yaml
  
  # Validate with template directory
  python prompt-validator.py prompt.yaml --template-dir ./templates
  
  # Validate all YAML files in directory
  python prompt-validator.py prompts/ --recursive
  
  # Strict validation mode
  python prompt-validator.py prompt.yaml --strict
  
  # Output report to file
  python prompt-validator.py prompt.yaml --output report.txt
  
  # Show only errors
  python prompt-validator.py prompt.yaml --errors-only

Validation Checks:
  - YAML syntax validation
  - Template reference existence
  - Variable reference tracking
  - Structure consistency
  - Formatting issues
  - Common problems (long lines, mixed indentation, etc.)
        """
    )
    
    parser.add_argument('path', help='File or directory to validate')
    parser.add_argument('--template-dir', '-t', type=Path,
                       help='Directory containing template files')
    parser.add_argument('--recursive', '-r', action='store_true',
                       help='Recursively validate directories')
    parser.add_argument('--strict', action='store_true',
                       help='Enable strict validation mode')
    parser.add_argument('--output', '-o', type=Path,
                       help='Output file for validation report')
    parser.add_argument('--errors-only', action='store_true',
                       help='Show only errors, not warnings or info')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Minimal output (exit code indicates success)')
    parser.add_argument('--format', choices=['text', 'json'], default='text',
                       help='Output format (default: text)')
    
    args = parser.parse_args()
    
    path = Path(args.path)
    if not path.exists():
        print(f"Error: Path '{path}' not found")
        sys.exit(1)
    
    # Initialize validator
    validator = PromptValidator(
        template_dir=args.template_dir,
        strict=args.strict
    )
    
    # Collect files to validate
    files_to_validate = []
    
    if path.is_file():
        files_to_validate.append(path)
    elif path.is_dir():
        pattern = '**/*.{yaml,yml}' if args.recursive else '*.{yaml,yml}'
        for ext in ['yaml', 'yml']:
            pattern = f"**/*.{ext}" if args.recursive else f"*.{ext}"
            files_to_validate.extend(path.glob(pattern))
    
    if not files_to_validate:
        print(f"No files to validate in {path}")
        sys.exit(0)
    
    # Validate all files
    all_issues = {}
    total_errors = 0
    
    for file_path in sorted(files_to_validate):
        issues = validator.validate_file(file_path)
        
        # Filter issues if requested
        if args.errors_only:
            issues = [i for i in issues if i.severity == ValidationIssue.SEVERITY_ERROR]
        
        all_issues[str(file_path)] = issues
        total_errors += sum(1 for i in issues if i.severity == ValidationIssue.SEVERITY_ERROR)
    
    # Generate output
    if args.format == 'json':
        # JSON output
        output = {
            'files_validated': len(files_to_validate),
            'total_errors': total_errors,
            'issues': {}
        }
        
        for file_path, issues in all_issues.items():
            output['issues'][file_path] = [
                {
                    'severity': i.severity,
                    'category': i.category,
                    'message': i.message,
                    'line': i.line,
                    'column': i.column,
                    'context': i.context
                }
                for i in issues
            ]
        
        report = json.dumps(output, indent=2)
    else:
        # Text output
        reports = []
        for file_path, issues in all_issues.items():
            if issues or not args.errors_only:
                reports.append(format_validation_report(Path(file_path), issues))
        
        report = '\n\n'.join(reports)
        
        # Add summary
        if len(files_to_validate) > 1:
            report += f"\n\nSummary: {len(files_to_validate)} files validated, {total_errors} error(s) found"
    
    # Output report
    if not args.quiet:
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Validation report saved to: {args.output}")
        else:
            print(report)
    
    # Exit with error code if errors found
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == '__main__':
    main()