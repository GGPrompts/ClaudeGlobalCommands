---
description: Master help system for Claude Command Framework with comprehensive command catalog, workflows, and usage examples
---

# Claude Command System v4.0 Help

**Version**: 4.0.0  
**Updated**: 2025-01-23  
**Token Estimate**: ~4k

All commands directly accessible via `/command-name` - no `/load` needed!

## Core Commands
- `/guide` - This help system
- `/agents` - Directory of all specialists
- `/workflows` - Workflow catalog  
- `/prompt-engineer` - Prompt optimization
- `/documentation` - Documentation generation
- `/cicd-orchestrator` - CI/CD management
- `/incident-commander` - Incident response
- `/execute` - Quick task execution

## Engineering Specialists
Located in `.claude/commands/engineering/`

- `/senior-engineer` - Code reviews, architecture (20+ years exp)
- `/visual-designer` - UI/UX, CSS, design systems

## Business Specialists
Located in `.claude/commands/business/`

- `/legal-expert` - Legal compliance, licensing
- `/marketing-expert` - Marketing campaigns, brand strategy

## Infrastructure Specialists
Located in `.claude/commands/infrastructure/`

- `/cloud-architect` - Multi-cloud architecture (AWS/Azure/GCP)

## Workflows
Located in `.claude/commands/workflows/`

- `/start-workflow` - Automated task execution
- `/css-safety-check` - CSS validation & compatibility
- `/visual-testing` - Visual regression testing
- `/documentation-update` - Doc generation
- `/legal-compliance` - Compliance review
- `/social-media-campaign` - Marketing campaigns

## Usage Examples

```bash
# Get help
/guide
/agents

# Use specialists
/senior-engineer review my authentication code
/visual-designer create a responsive navbar

# Run workflows
/css-safety-check
/visual-testing
```

## Token Management
- Small (1-3k): Help, directory commands
- Medium (2-5k): Specialists
- Large (3-8k): Complex workflows

For complete documentation, see README.md
