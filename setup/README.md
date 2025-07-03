# Claude Global Commands - Optimization Infrastructure

This directory contains the optimization infrastructure for Claude Global Commands, designed to reduce redundancy and improve maintainability across command prompts.

## Directory Structure

```
/setup/
├── shared-components.yaml    # Common patterns and instructions
├── template-manifest.yaml    # Registry of all available templates
├── templates/               # Output format templates
│   └── (template files)
└── utilities/              # Helper scripts and tools
    └── (utility scripts)
```

## Components

### shared-components.yaml

Contains reusable components extracted from existing prompts:

- **common_instructions**: Core instructions used across multiple commands
  - `task_focus`: Keep Claude focused on the specific task
  - `file_creation_policy`: Guidelines for file operations
  - `response_format`: Standard response formatting rules
  - `error_handling`: Common error handling patterns

- **xml_tags**: Standardized XML tags for structured responses
  - `thinking`: For internal reasoning
  - `answer`: For main response content
  - `file_content`: For code/file display
  - `summary`: For task summaries

- **shared_patterns**: Common operational patterns
  - `file_operations`: Read-before-edit, path validation
  - `git_operations`: Status checks, commit formats
  - `code_analysis`: Search strategies, refactoring approaches

- **tool_usage_patterns**: Optimized tool usage guidelines
  - `batch_operations`: Efficient batching strategies
  - `search_strategy`: Effective search patterns

- **response_templates**: Standard response formats
  - `task_completion`: Success response template
  - `error_response`: Error response template

### template-manifest.yaml

Registry of all available output templates with:
- Template descriptions and locations
- Required parameters
- Usage guidelines
- Category organization

### Templates Directory

Contains YAML templates for specific output formats:
- Code review templates
- Refactoring plans
- Documentation updates
- Test results
- Git operation summaries
- Project analysis
- Error diagnosis
- Performance analysis

### Utilities Directory

For helper scripts and tools that support the optimization infrastructure.

## Usage

### In Optimized Prompts

Reference shared components using YAML-style notation:

```yaml
# Reference a common instruction
$ref: shared-components.yaml#/common_instructions/task_focus

# Reference an XML tag pattern
$ref: shared-components.yaml#/xml_tags/thinking

# Reference a complete pattern
$ref: shared-components.yaml#/shared_patterns/file_operations/read_before_edit
```

### For Template Selection

1. Check `template-manifest.yaml` for available templates
2. Select appropriate template based on task type
3. Reference template in prompt with required parameters
4. Templates can be combined for complex operations

### Best Practices

1. **Reusability**: Extract patterns used in 3+ prompts
2. **Modularity**: Keep components focused and single-purpose
3. **Documentation**: Update manifest when adding new templates
4. **Versioning**: Track changes to shared components carefully
5. **Testing**: Verify prompts work correctly with referenced components

## Maintenance

### Adding New Shared Components

1. Identify common patterns across prompts
2. Add to appropriate section in `shared-components.yaml`
3. Document usage and parameters
4. Update existing prompts to reference new component

### Creating New Templates

1. Create template file in `/templates/` directory
2. Add entry to `template-manifest.yaml`
3. Include all required parameters
4. Provide usage examples

### Updating Existing Components

1. Review all prompts using the component
2. Test changes thoroughly
3. Update documentation
4. Consider versioning for breaking changes

## Benefits

1. **Reduced Redundancy**: Common patterns defined once
2. **Consistency**: Uniform behavior across commands
3. **Maintainability**: Single source of truth for patterns
4. **Scalability**: Easy to add new commands using existing components
5. **Quality**: Centralized improvements benefit all commands

## Future Enhancements

- Automated validation of prompt references
- Template parameter validation
- Component dependency tracking
- Performance optimization guidelines
- A/B testing framework for prompt variations