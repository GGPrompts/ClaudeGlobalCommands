# Claude Context - CCGlobalCommands

## Archive Folder Design

The `_archive/` folder is intentionally used to prevent command list overload when users type slash commands. Instead of showing 20+ commands, users see only the most essential ones.

### Structure:
- **Core Commands** (in `/commands`): Immediately available via slash commands
  - /guide, /agents, /workflows, /senior-engineer, etc.
- **Archived Specialists** (in `/_archive`): Available via `/load` command
  - engineering/: visual-designer, frontend-engineer, etc.
  - infrastructure/: cloud-architect, kubernetes-specialist, etc.
  - analysis/: business-analyst, security-analyst, etc.
  - business/: project-manager, product-manager, etc.

### Usage:
```bash
# Core commands - directly accessible
/senior-engineer

# Archived commands - load first
/load _archive/engineering/visual-designer
```

## Design Rationale
This keeps the slash command UI clean and focused on the most commonly used commands, while still providing full access to all specialists when needed.