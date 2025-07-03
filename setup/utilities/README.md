# Prompt Optimization Utilities

This directory contains utility scripts for optimizing and managing prompt files.

## Prerequisites

Install required Python packages:
```bash
pip install tiktoken pyyaml
```

## Available Utilities

### 1. Token Counter (`token-counter.py`)

Count tokens in prompt files using tiktoken library. Supports before/after comparison and generates reduction percentage reports.

**Features:**
- Single file token counting
- Before/after comparison with reduction metrics
- Directory scanning (recursive option)
- Multiple encoding models support
- Detailed reduction reports

**Usage:**
```bash
# Count tokens in a single file
python token-counter.py prompt.txt

# Compare before and after files
python token-counter.py original.txt optimized.txt --compare

# Scan directory recursively
python token-counter.py prompts/ --recursive

# Specify file extensions
python token-counter.py prompts/ --extensions .txt .md

# Save report to file
python token-counter.py before.txt after.txt --compare --output report.txt
```

### 2. XML to YAML Converter (`xml-to-yaml.py`)

Convert XML structured prompts to YAML format while preserving all content and structure.

**Features:**
- Preserves element order and comments
- Handles nested elements properly
- Batch conversion for directories
- Clean, readable YAML output
- Metadata tracking

**Usage:**
```bash
# Convert single file
python xml-to-yaml.py prompt.xml

# Convert to specific output file
python xml-to-yaml.py input.xml output.yaml

# Batch convert directory
python xml-to-yaml.py prompts/ --batch

# Create sample XML for testing
python xml-to-yaml.py --sample

# Pretty print output
python xml-to-yaml.py prompt.xml --pretty
```

### 3. Template Interpolator (`template-interpolator.py`)

Replace template references with actual content. Supports parameter substitution and handles nested template references.

**Features:**
- Multiple template reference formats
- Variable substitution with dot notation
- Nested template support
- Circular reference detection
- Statistics reporting

**Supported Template Formats:**
- `{{template_name}}` - Double brace style
- `${template_name}` - Dollar brace style  
- `<template:name/>` - XML style
- `@include(name)` - Include style
- `[[template_name]]` - Double bracket style

**Supported Variable Formats:**
- `{{var.property}}` - Dot notation for nested values
- `$variable` - Dollar sign style
- `%{variable}` - Percent brace style

**Usage:**
```bash
# Basic interpolation
python template-interpolator.py template.txt

# With variables
python template-interpolator.py template.txt --vars name=John age=30

# With template directory
python template-interpolator.py main.tmpl --template-dir ./templates

# Load variables from file
python template-interpolator.py template.txt --vars-file config.yaml

# Show statistics
python template-interpolator.py template.txt --stats
```

### 4. Prompt Validator (`prompt-validator.py`)

Validate optimized prompts for missing references, syntax errors, and structural issues.

**Features:**
- YAML syntax validation
- Template reference verification
- Variable reference tracking
- Structure consistency checks
- Formatting issue detection
- Detailed error reporting with line numbers

**Validation Checks:**
- YAML syntax errors
- Missing template files
- Unknown top-level keys
- Long lines (>120 chars)
- Mixed tabs/spaces
- Trailing whitespace
- TODO/FIXME comments

**Usage:**
```bash
# Validate single file
python prompt-validator.py prompt.yaml

# Validate with template directory
python prompt-validator.py prompt.yaml --template-dir ./templates

# Validate directory recursively
python prompt-validator.py prompts/ --recursive

# Strict validation mode
python prompt-validator.py prompt.yaml --strict

# Show only errors
python prompt-validator.py prompt.yaml --errors-only

# JSON output format
python prompt-validator.py prompt.yaml --format json
```

## Example Workflow

1. **Convert XML prompts to YAML:**
   ```bash
   python xml-to-yaml.py legacy-prompts/ --batch --output converted/
   ```

2. **Validate converted files:**
   ```bash
   python prompt-validator.py converted/ --recursive --template-dir templates/
   ```

3. **Interpolate templates:**
   ```bash
   python template-interpolator.py main-prompt.yaml --vars-file config.yaml -o final-prompt.txt
   ```

4. **Compare token counts:**
   ```bash
   python token-counter.py original-prompt.txt final-prompt.txt --compare
   ```

## Error Handling

All utilities include comprehensive error handling:
- File not found errors
- Permission errors
- Syntax errors in YAML/XML
- Circular template references
- Missing dependencies

## Exit Codes

- `0`: Success
- `1`: Error occurred (validation errors, missing files, etc.)
- `2`: Invalid command line arguments

## Tips

1. **Token Counting**: Use the same model encoding as your target LLM for accurate counts
2. **Template Organization**: Keep templates in a dedicated directory for easier management
3. **Validation**: Run validation after any prompt modifications to catch issues early
4. **Version Control**: Track token reduction metrics in your commit messages

## Contributing

When adding new utilities:
1. Follow the existing argument parsing patterns
2. Include comprehensive help text and examples
3. Add proper error handling
4. Document all supported formats
5. Provide example usage in the help output