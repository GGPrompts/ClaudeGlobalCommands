#!/bin/bash

# CCGlobalCommands Installation Script
# This script helps you set up the commands for Claude Code

echo "🚀 CCGlobalCommands Installation"
echo "================================"

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -d "commands" ]; then
    echo "❌ Error: Please run this script from the CCGlobalCommands directory"
    exit 1
fi

# Option 1: Copy everything
echo ""
echo "Choose installation method:"
echo "1) Install all commands and workflows (recommended)"
echo "2) Install core commands only"
echo "3) Custom installation"
read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo "📦 Installing all commands and workflows..."
        mkdir -p ~/.claude/commands ~/.claude/workflows ~/.claude/archive
        cp commands/*.md ~/.claude/commands/ 2>/dev/null
        cp workflows/*.md ~/.claude/workflows/ 2>/dev/null
        cp -r _archive/* ~/.claude/archive/ 2>/dev/null
        echo "✅ Complete installation finished!"
        ;;
    2)
        echo "📦 Installing core commands only..."
        mkdir -p ~/.claude/commands
        cp commands/{guide,agents,execute,workflows,senior-engineer,documentation}.md ~/.claude/commands/ 2>/dev/null
        echo "✅ Core commands installed!"
        ;;
    3)
        echo "📦 Custom installation - copy the files you need to ~/.claude/"
        echo "   Example: cp commands/guide.md ~/.claude/commands/"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "🎉 Installation complete!"
echo ""
echo "Quick start:"
echo "  /guide     - Show help and all commands"
echo "  /agents    - List all AI specialists"
echo "  /execute   - Quick task execution"
echo "  /workflows - See available workflows"
echo ""
echo "Enjoy CCGlobalCommands!"