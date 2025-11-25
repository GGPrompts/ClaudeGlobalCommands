# Claude Context - ClaudeGlobalCommands

## Project Structure

A collection of slash commands and workflows for Claude Code, organized by category:

```
.claude/commands/
├── Core Commands (directly in /commands)
│   guide.md, agents.md, workflows.md, execute.md,
│   prompt-engineer.md, documentation.md,
│   cicd-orchestrator.md, incident-commander.md
├── engineering/
│   senior-engineer.md, visual-designer.md
├── business/
│   legal-expert.md, marketing-expert.md
├── infrastructure/
│   cloud-architect.md
└── workflows/
    start-workflow.md, css-safety-check.md, visual-testing.md,
    documentation-update.md, legal-compliance.md, social-media-campaign.md
```

## Usage

All commands are directly accessible via slash commands:

```bash
/guide                    # Help system
/agents                   # List all available agents
/senior-engineer          # Code review specialist
/engineering/visual-designer  # UI/UX design (subfolder)
/workflows/css-safety-check   # CSS validation workflow
```

## Design Philosophy

- **Actionable prompts**: Commands contain step-by-step workflows, not just descriptions
- **Interactive refinement**: Use `AskUserQuestion` for dialog-based iteration
- **Token-conscious**: Keep prompts focused and avoid unnecessary verbosity

## Key Commands

- `/prompt-engineer` - Interactive prompt crafting with refinement loop
- `/guide` - Command catalog and help
- `/execute` - Quick task routing to appropriate specialist
