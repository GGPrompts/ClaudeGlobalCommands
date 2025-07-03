# Contributing to CCGlobalCommands

Thank you for your interest in contributing to CCGlobalCommands! This project aims to provide a comprehensive collection of AI agent commands for Claude Code.

## How to Contribute

### 1. Adding New Commands

To add a new command:

1. Create a new `.md` file in the appropriate directory:
   - Core commands: `commands/core/`
   - Engineering: `commands/engineering/`
   - Analysis: `commands/analysis/`
   - Business: `commands/business/`
   - Workflows: `commands/workflows/`

2. Follow the XML structure template:

```xml
<role>
Define the agent's role and expertise
</role>

<motivation>
Explain why this role exists and its value
</motivation>

<core_function>
🎯 One-line description of primary purpose
</core_function>

<token_estimate>X,XXX-X,XXX tokens per request</token_estimate>

<responsibilities>
- List key responsibilities
- Be specific and actionable
- Include 5-10 items
</responsibilities>

<output_formats>
Define the formats this agent can produce
</output_formats>

<mcp_suggestions>
List relevant MCP servers that enhance capabilities
</mcp_suggestions>

<approach>
Describe the agent's philosophy and approach
</approach>
```

### 2. Enhancing Existing Commands

- Add new capabilities to responsibilities
- Include additional output formats
- Suggest new MCP integrations
- Update token estimates based on usage

### 3. Creating New Workflows

Workflows coordinate multiple agents. Include:
- Clear activation triggers
- Step-by-step agent coordination
- Expected outputs
- Success criteria
- Token usage estimates

### 4. Documentation Updates

- Keep README.md current with new commands
- Update QUICK_SETUP.md for new features
- Add examples to help users understand usage

## Guidelines

### Code Style
- Use clear, descriptive names
- Include token estimates for all commands
- Provide practical examples
- Keep descriptions concise but comprehensive

### Testing
- Test commands in Claude Code before submitting
- Verify token estimates are reasonable
- Ensure workflows coordinate properly
- Check for conflicts with existing commands

### Commit Messages
- Use clear, descriptive commit messages
- Format: `type: description`
- Types: `feat`, `fix`, `docs`, `refactor`, `test`

Example:
```
feat: add database-architect command
fix: update token estimates for visual-designer
docs: add examples to automation-engineer
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-command`)
3. Make your changes
4. Test thoroughly in Claude Code
5. Commit with clear messages
6. Push to your fork
7. Submit a pull request with:
   - Description of changes
   - Testing performed
   - Token usage verification

## Command Naming Conventions

- Use lowercase with hyphens: `visual-designer`
- Be descriptive but concise
- Avoid abbreviations unless widely known
- Group related commands with common prefixes

## Token Estimation Guidelines

- Small tasks: 500-1,500 tokens
- Medium tasks: 1,500-3,000 tokens
- Large tasks: 3,000-5,000 tokens
- Complex workflows: 4,000-6,000 tokens

Test actual usage and update estimates accordingly.

## Questions?

Open an issue for:
- Clarification on guidelines
- Suggestions for improvements
- Discussion of new features
- Help with contributions

Thank you for helping make CCGlobalCommands better!