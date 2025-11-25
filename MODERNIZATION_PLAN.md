# CCGlobalCommands Modernization Plan

## Executive Summary

This document outlines the changes needed to bring CCGlobalCommands up to date with the current Claude Code system (2025) for slash commands.

**Based on real-world testing:**
- ❌ Skills auto-activation is unreliable - NOT implementing skills system
- ❌ Archive pattern no longer works in Claude Code - using standard subdirectories
- ✅ Focus on proper `.claude/commands/` structure with YAML frontmatter

## Key Gaps Identified

### 1. **Directory Structure** ⚠️ CRITICAL
**Current State:**
```
CCGlobalCommands/
├── commands/              # ❌ Wrong location
├── workflows/             # ❌ Wrong location
└── _archive/              # ❌ Wrong location
```

**Required State:**
```
CCGlobalCommands/
└── .claude/
    └── commands/          # ✅ Project-level slash commands
        ├── guide.md
        ├── agents.md
        ├── workflows.md
        ├── engineering/   # Engineering specialists
        │   ├── senior-engineer.md
        │   ├── visual-designer.md
        │   └── frontend-engineer.md
        ├── business/      # Business specialists
        │   ├── legal-expert.md
        │   └── marketing-expert.md
        ├── infrastructure/# Infrastructure specialists
        │   └── cloud-architect.md
        └── workflows/     # Multi-agent workflows
            ├── css-safety-check.md
            └── visual-testing.md
```

**NO skills directory** - Skills auto-activation doesn't work reliably in practice.

**Impact:** Commands won't be recognized by Claude Code without `.claude/` prefix

---

### 2. **Metadata Format** ⚠️ CRITICAL

**Current Format:**
```markdown
# Command Name

## Command: /command-name

```yaml
meta:
  name: command-name
  description: Description here
  version: 3.0.0
  token_estimate: 4k-8k

config:
  analysis_depth: comprehensive

capabilities:
  - Capability 1

instructions:
  role: Role description
  approach:
    security: [...]
```
```

**Required Format:**
```markdown
---
description: Brief description of what this command does
---

# Command Name

[Instructions for Claude in natural language]

## Capabilities
- Capability 1
- Capability 2

## Approach
...
```

**Issues:**
- Missing YAML frontmatter delimiters (`---`)
- Over-complicated nested YAML structure
- Only `description` field is required/used
- Content inside code blocks instead of markdown body

---

### 3. **Archive Pattern No Longer Works** ⚠️ HIGH PRIORITY

**Current:** Uses `_archive/` folder to hide specialists

**Reality:** Archive pattern doesn't work in current Claude Code

**Solution:** Use standard subdirectory organization

**Action:**
- Move all specialists to `.claude/commands/[category]/`
- Use subdirectories for organization (engineering/, business/, infrastructure/)
- All commands accessible via `/command-name` directly
- Use `/guide` to help users discover commands

---

### 4. **Hooks System** ℹ️ INFORMATIONAL

**Current:** Commands include detailed `hooks:` configuration in YAML

**Reality:**
- Hooks are configured separately via `.claude/hooks/` or settings
- Commands don't define hooks - hooks are external
- The hooks metadata in commands is documentation, not functional

**Action:**
- Remove `hooks:` from command metadata
- Create separate hooks documentation if needed
- Keep hooks info in README/guides only

---

### 5. **Skills System** ℹ️ SKIP THIS

**Decision:** NOT implementing skills system

**Reason:** Real-world testing shows skills auto-activation is unreliable

**Action:**
- Keep all agents as slash commands
- Users explicitly invoke commands when needed
- Better control and predictability
- No `.claude/skills/` directory needed

---

### 6. **Workflows as Commands vs Skills**

**Current:** Workflows in separate `/workflows/` directory

**Options:**
1. Move to `.claude/commands/workflows/`
2. Convert some to skills (auto-activate)
3. Keep as specialized commands

**Recommendation:** Move to `.claude/commands/workflows/`

---

## Modernization Checklist

### Phase 1: Directory Restructure ✅
- [ ] Create `.claude/commands/` directory structure
- [ ] Create subdirectories: engineering/, business/, infrastructure/, workflows/
- [ ] Move core commands to `.claude/commands/` root
- [ ] Move engineering specialists to `.claude/commands/engineering/`
- [ ] Move business specialists to `.claude/commands/business/`
- [ ] Move infrastructure specialists to `.claude/commands/infrastructure/`
- [ ] Move workflows to `.claude/commands/workflows/`
- [ ] Remove old `commands/`, `_archive/`, `workflows/` directories

### Phase 2: Metadata Updates ✅
- [ ] Convert all commands to YAML frontmatter format
- [ ] Each file gets `---\ndescription: ...\n---` header
- [ ] Move YAML content out of code blocks into markdown body
- [ ] Remove non-functional `hooks:`, `meta:`, `config:` from frontmatter
- [ ] Keep version/token/capabilities as markdown in body
- [ ] Ensure natural language instructions after frontmatter

### Phase 3: Documentation Updates ✅
- [ ] Update README.md with new `.claude/` structure
- [ ] Update CLAUDE.md to remove archive pattern references
- [ ] Update QUICK_SETUP.md with new installation paths
- [ ] Update all examples to show new command paths
- [ ] Add migration guide for existing users
- [ ] Update badges and links

### Phase 4: Testing ✅
- [ ] Validate all commands have proper frontmatter
- [ ] Test slash command invocation works
- [ ] Verify subdirectory commands accessible
- [ ] Check token estimates still accurate
- [ ] Test all workflows function correctly
- [ ] Verify cross-references work

---

## Command Organization Strategy

### Core Commands (Root of .claude/commands/)
- `/guide` - Help system and command catalog
- `/agents` - Directory listing of all specialists
- `/workflows` - Workflow selector and catalog
- `/prompt-engineer` - Prompt optimization
- `/documentation` - Documentation generation
- `/cicd-orchestrator` - CI/CD pipeline management
- `/incident-commander` - Incident response

### Engineering Commands (.claude/commands/engineering/)
- `/senior-engineer` - Code reviews and architecture
- `/visual-designer` - UI/UX, CSS, animations
- `/frontend-engineer` - Frontend development
- `/backend-engineer` - Backend APIs
- `/qa-automation` - Testing automation
- `/performance-optimizer` - Performance optimization
- `/security-engineer` - Security audits
- `/data-engineer` - Data pipelines

### Business Commands (.claude/commands/business/)
- `/legal-expert` - Legal compliance
- `/marketing-expert` - Marketing campaigns
- `/project-manager` - Project management
- `/product-manager` - Product strategy

### Infrastructure Commands (.claude/commands/infrastructure/)
- `/cloud-architect` - Cloud architecture
- `/kubernetes-specialist` - K8s management
- `/terraform-engineer` - Infrastructure as Code

### Workflows (.claude/commands/workflows/)
- All multi-agent workflows organized here
- Accessible via `/workflow-name`

**All are slash commands** - No skills directory needed.

---

## Migration Strategy

### Option A: Big Bang (Recommended for your project)
1. Create new `.claude/` structure
2. Update all files at once
3. Remove old directories
4. Single commit with all changes
5. Tag as v4.0.0 (breaking change)

### Option B: Gradual Migration
1. Create `.claude/` structure alongside old
2. Duplicate files in both locations
3. Deprecation notice in old files
4. Remove old structure after grace period

**Recommendation:** Option A - Clean break, easier to maintain

---

## Breaking Changes Communication

### For Users
- **v4.0.0 will require new installation**
- Old command paths won't work
- Setup scripts will be updated
- Migration guide will be provided
- All functionality preserved, just different paths

### Changelog Entry
```markdown
## v4.0.0 - 2025-01-XX - BREAKING CHANGES

### 🔥 Breaking Changes
- Commands moved from `commands/` to `.claude/commands/`
- Workflows moved to `.claude/commands/workflows/`
- New skills system in `.claude/skills/`
- Simplified metadata format (YAML frontmatter)
- Removed non-functional hooks configuration

### ✨ New Features
- Auto-activating skills for common tasks
- Standard Claude Code directory structure
- Cleaner command metadata
- Better organization with subdirectories

### 📦 Migration
See MIGRATION.md for upgrade instructions
```

---

## Estimated Impact

### File Changes
- ~40 command files to update
- ~6 workflow files to move
- ~5-8 new skill directories to create
- ~5 documentation files to update

### Token Impact
- Simplified frontmatter may save ~100-200 tokens per command
- Moving to skills may reduce overall token usage (auto-activation is more efficient)

### User Impact
- One-time reinstall required
- All commands work the same (just different paths)
- New skills provide better auto-completion

---

## Next Steps

1. **Get User Approval** on migration strategy
2. **Create v4.0.0 branch** for changes
3. **Implement Phase 1** - Directory restructure
4. **Implement Phase 2** - Metadata updates
5. **Implement Phase 3** - Skills creation
6. **Implement Phase 4** - Documentation
7. **Test thoroughly**
8. **Release v4.0.0**

---

## Questions to Resolve

1. Should we keep the "archive" concept with subdirectories?
2. Which specific commands should become skills?
3. Should workflows be commands or skills?
4. Keep version 4.0.0 or reset to 1.0.0 for new era?
5. Maintain backward compatibility or clean break?

**Recommendation:** Clean break with v4.0.0, clear migration guide
