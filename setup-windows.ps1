#!/usr/bin/env powershell

# CCGlobalCommands Windows Installation Script
# Adapted for Windows Claude Code setup

Write-Host "🚀 CCGlobalCommands Windows Installation" -ForegroundColor Green
Write-Host "=======================================" -ForegroundColor Green

# Get the current user's profile directory
$ClaudeDir = "$env:USERPROFILE\.claude"
$CommandsDir = "$ClaudeDir\commands"
$WorkflowsDir = "$ClaudeDir\workflows"
$ArchiveDir = "$ClaudeDir\archive"

# Create directories if they don't exist
Write-Host "📁 Creating Claude directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Path $CommandsDir -Force | Out-Null
New-Item -ItemType Directory -Path $WorkflowsDir -Force | Out-Null
New-Item -ItemType Directory -Path $ArchiveDir -Force | Out-Null

# Copy command files
Write-Host "📦 Installing commands..." -ForegroundColor Yellow
$SourceCommandsDir = "D:\ClaudeWindows\ClaudeGlobalCommands\commands"
$SourceWorkflowsDir = "D:\ClaudeWindows\ClaudeGlobalCommands\workflows"
$SourceArchiveDir = "D:\ClaudeWindows\ClaudeGlobalCommands\_archive"

if (Test-Path $SourceCommandsDir) {
    Copy-Item "$SourceCommandsDir\*.md" $CommandsDir -Force
    Write-Host "✅ Commands installed to: $CommandsDir" -ForegroundColor Green
}

if (Test-Path $SourceWorkflowsDir) {
    Copy-Item "$SourceWorkflowsDir\*.md" $WorkflowsDir -Force
    Write-Host "✅ Workflows installed to: $WorkflowsDir" -ForegroundColor Green
}

if (Test-Path $SourceArchiveDir) {
    Copy-Item "$SourceArchiveDir\*" $ArchiveDir -Recurse -Force
    Write-Host "✅ Archive installed to: $ArchiveDir" -ForegroundColor Green
}

Write-Host ""
Write-Host "🎉 Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Available commands:" -ForegroundColor Cyan
Write-Host "  /guide     - Show help and all commands" -ForegroundColor White
Write-Host "  /agents    - List all AI specialists" -ForegroundColor White
Write-Host "  /execute   - Quick task execution" -ForegroundColor White
Write-Host "  /workflows - See available workflows" -ForegroundColor White
Write-Host "  /senior-engineer - Code reviews and architecture" -ForegroundColor White
Write-Host "  /documentation - Technical documentation generation" -ForegroundColor White
Write-Host ""
Write-Host "Try running '/guide' in Claude Code to get started!" -ForegroundColor Yellow

# List installed files for verification
Write-Host ""
Write-Host "📋 Installed files:" -ForegroundColor Cyan
Get-ChildItem $CommandsDir -Name "*.md" | ForEach-Object { 
    Write-Host "  Commands: $_" -ForegroundColor Gray 
}
Get-ChildItem $WorkflowsDir -Name "*.md" | ForEach-Object { 
    Write-Host "  Workflows: $_" -ForegroundColor Gray 
}