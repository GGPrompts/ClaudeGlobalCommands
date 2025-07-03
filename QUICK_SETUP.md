# Quick Setup Guide

## 🚀 Instant Setup (Recommended)

1. Copy the entire contents of `CLAUDE_GLOBAL_COMMANDS_v2.1.md`
2. Open a new Claude Code session
3. Paste and say: "Please create the complete directory structure and all files as specified in this document for my Claude global commands system."
4. Claude will create everything in `~/.claude/commands/`

## 📁 Manual Setup

If you prefer to set up specific commands manually:

### Step 1: Create the directory structure
```bash
mkdir -p ~/.claude/commands/_archive/{engineering,analysis,business,infrastructure}
mkdir -p ~/.claude/commands/workflows
```

### Step 2: Copy individual command files
- Core commands go in `~/.claude/commands/`
- Specialized agents go in `~/.claude/commands/_archive/[category]/`
- Workflows go in `~/.claude/commands/workflows/`

### Step 3: Test your setup
```bash
# In Claude Code, type:
/guide
```

## 🎯 Most Useful Commands to Start With

1. **Help & Discovery**
   - `/guide` - See all available commands
   - `/agents` - Browse AI specialists

2. **Development**
   - `/senior-engineer` - Code review and architecture
   - `/visual-designer` - CSS and UI help
   - `/workflows code-review` - Multi-agent code review

3. **Testing**
   - `/automation-engineer` - Playwright and visual regression
   - `/workflows css-safety-check` - Prevent CSS breaks

4. **Planning**
   - `/workflows feature-planning` - Plan new features
   - `/prompt-engineer` - Optimize your prompts

## 💡 Pro Tips

- Add `--help` to any command for detailed info
- Use `--mode=interactive` for conversational help
- Check token estimates to manage API costs
- Run `/workflows css-safety-check` before major CSS changes

## 📊 Token Usage Guide

- 🟢 **Low** (<1,500 tokens): Quick commands like help
- 🟡 **Medium** (1,500-3,000 tokens): Single agent tasks
- 🔴 **High** (>3,000 tokens): Multi-agent workflows

## 🆕 New in v2.1

- Visual Designer for CSS and animations
- Enhanced Automation Engineer with visual regression
- CSS Safety Check workflow
- Visual Testing workflow
- Token count estimates for all commands