# Claude Command System v3.0 Help

## Command: /guide

```yaml
meta:
  name: guide
  description: Master help system for Claude Command Framework v3.0 with Hooks
  version: 3.0.0
  updated: 2025-01-01
  token_estimate: ~4k

overview: |
  Enterprise-ready framework for specialized AI assistance with comprehensive hooks support.
  Features structured commands, workflows, specialized agents, and lifecycle management.

features:
  - {name: "Claude Code Hooks", desc: "Enterprise-grade lifecycle management"}
  - {name: "Security First", desc: "Automated security scanning via hooks"}
  - {name: "Real-time Monitoring", desc: "Performance profiling and resource tracking"}
  - {name: "Error Recovery", desc: "Automatic rollback and incident creation"}
  - {name: "VS Code Integration", desc: "Browser dev tools and visual testing"}
  - {name: "Token Estimates", desc: "All commands include usage estimates"}
  - {name: "Visual Designer", desc: "Specialist for UI/UX tasks"}
  - {name: "Enhanced Workflows", desc: "CSS safety, visual testing, and more"}
  - {name: "Infrastructure Specialists", desc: "Cloud, K8s, and IaC specialists"}
  - {name: "Smart Coordination", desc: "Enhanced XML structure with coordination"}

categories:
  core:
    desc: Essential system commands
    commands:
      - {cmd: go, desc: "Quick start interactive workflow selector and executor"}
      - {cmd: guide, desc: "Comprehensive help system with all commands"}
      - {cmd: agents, desc: "Lists all available specialist agents"}
      - {cmd: prompt-engineer, desc: "Optimizes prompts for clarity and effectiveness"}
      - {cmd: senior-engineer, desc: "Expert technical guidance with 20+ years"}
      - {cmd: documentation, desc: "Creates and improves technical documentation"}
      - {cmd: workflows, desc: "Shows available multi-step workflows"}
      - {cmd: cicd-orchestrator, desc: "Manages CI/CD pipelines"}
      - {cmd: incident-commander, desc: "Coordinates incident response"}
  
  engineering:
    location: _archive/engineering/
    commands:
      - {cmd: performance-optimizer, desc: "Analyzes and optimizes application performance"}
      - {cmd: qa-automation, desc: "Creates comprehensive test suites"}
      - {cmd: automation-engineer, desc: "Builds automation scripts and CI/CD"}
      - {cmd: visual-designer, desc: "Creates UI/UX designs with accessibility"}
      - {cmd: frontend-engineer, desc: "Develops modern web applications"}
      - {cmd: backend-engineer, desc: "Builds scalable APIs and microservices"}
      - {cmd: security-engineer, desc: "Implements security best practices"}
      - {cmd: data-engineer, desc: "Designs data pipelines and ETL"}
  
  analysis:
    location: _archive/analysis/
    commands:
      - {cmd: business-analyst, desc: "Analyzes requirements and process flows"}
      - {cmd: technical-analyst, desc: "System design and integration planning"}
      - {cmd: security-analyst, desc: "Security audits and threat modeling"}
      - {cmd: data-analyst, desc: "Data insights and visualizations"}
  
  business:
    location: _archive/business/
    commands:
      - {cmd: project-manager, desc: "Manages timelines and resources"}
      - {cmd: product-manager, desc: "Defines strategy and roadmaps"}
      - {cmd: stakeholder-communicator, desc: "Crafts clear communications"}
      - {cmd: legal-expert, desc: "Legal analysis and compliance"}
      - {cmd: marketing-expert, desc: "Marketing materials and campaigns"}
  
  infrastructure:
    location: _archive/infrastructure/
    commands:
      - {cmd: cloud-architect, desc: "Designs scalable cloud architectures"}
      - {cmd: kubernetes-specialist, desc: "Manages K8s clusters"}
      - {cmd: terraform-engineer, desc: "Creates infrastructure as code"}

workflow_categories:
  development:
    - {name: start-workflow, flow: "select → configure → execute → monitor → complete"}
    - {name: debug-assistant, flow: "analyze → identify → fix → test → implement"}
    - {name: code-review, flow: "security → quality → performance → practices → report"}
    - {name: test-generation, flow: "analyze → identify → generate → coverage"}
    - {name: refactoring-guide, flow: "analyze → improve → plan → test"}
  
  planning:
    - {name: migration-planner, flow: "assess → target → gap → risk → roadmap"}
    - {name: api-designer, flow: "requirements → schema → endpoints → security → docs"}
    - {name: documentation-generator, flow: "scan → extract → api_docs → guides"}
  
  performance_security:
    - {name: performance-audit, flow: "profile → bottlenecks → metrics → optimize → verify"}
    - {name: security-audit, flow: "scan → threat_model → pentest → compliance → remediate"}
    - {name: dependency-analyzer, flow: "scan → vulnerabilities → licenses → updates"}
  
  frontend_ux:
    - {name: css-safety-check, flow: "validate → compatibility → performance → report"}
    - {name: visual-testing, flow: "baseline → regression → compare → report"}
    - {name: accessibility-audit, flow: "wcag → screen_reader → keyboard → fixes"}
  
  infrastructure:
    - {name: containerization, flow: "analyze → dockerfile → compose → orchestration"}
    - {name: monitoring-setup, flow: "metrics → logging → alerts → dashboards"}
  
  business:
    - {name: social-media-campaign, flow: "strategy → content → design → legal → performance"}
    - {name: legal-compliance, flow: "license → privacy → security → terms → implement"}

usage:
  basic: |
    /execute                # Quick start - interactive workflow selector
    /guide                  # Show this help
    /agents                 # List all available agents
    /senior-engineer        # Activate senior engineer
    /workflows              # Show available workflows
  
  specialists: |
    # Core commands work directly
    /senior-engineer
    
    # Archive specialists also work directly
    /visual-designer
    /legal-expert
    /cloud-architect
  
  workflows: |
    /workflow code-review
    /workflow social-media-campaign
    /workflow legal-compliance
  
  hooks: |
    # Commands automatically trigger hooks:
    /senior-engineer        # Pre: Security scan, Post: Quality report
    /cicd-orchestrator     # Pre: Pipeline validation, Post: Deployment verify
    
    # Hook execution flow:
    1. Pre-execution hooks (validation, security)
    2. Main command execution
    3. Post-execution hooks (reporting, cleanup)
    4. Error hooks if needed (recovery, rollback)
  
  token_mgmt:
    small_commands: 1k-3k
    specialists: 2k-5k
    workflows: 3k-8k
    with_hooks: +1k-2k

best_practices:
  - Start with /execute for interactive workflow selection or /guide to understand all options
  - Check token estimates before complex workflows
  - Use specialists for domain-specific tasks
  - Chain commands for multi-step operations
  - Monitor coordination sections
  - Use /clear after /guide to free context

troubleshooting:
  - {issue: "Command not found", solution: "Check name. Archive commands work directly."}
  - {issue: "High token usage", solution: "Review estimates. Break large tasks down."}
  - {issue: "Workflow fails", solution: "Check prerequisites and specialist availability."}

examples:
  - {title: "Get Started", code: "/execute\n# Interactive workflow selection\n\n# Or explore manually:\n/guide\n/agents\n/workflows"}
  - {title: "Visual Design", code: "/visual-designer\n# Design a modern dashboard UI"}
  - {title: "Legal Review", code: "/workflow legal-compliance\n# Review for licensing"}
  - {title: "Marketing", code: "/workflow social-media-campaign\n# Create content"}

changelog:
  - {version: "3.0.0", date: "2025-01-01", changes: "Hooks system, enterprise security, VS Code"}
  - {version: "2.1.0", date: "2024-12-27", changes: "Token estimates, visual tools, infrastructure"}
  - {version: "2.0.0", date: "2024-12-01", changes: "Major refactor with archive structure"}
  - {version: "1.0.0", date: "2024-11-01", changes: "Initial release"}

related: [agents, workflows, prompt-engineer]
```