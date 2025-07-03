# Agents Command v2.1

**Token Estimate: ~600 tokens**

<command name="agents">
<description>
Lists available agents by category. Use /help <agent> for details.
</description>

<version>2.1.0</version>
<lastUpdated>2024-12-27</lastUpdated>

<output>
## Available Agents (47 total)

### Core Commands (/commands/)
```yaml
guide:         Help system         ~3k
agents:        This command        ~600
prompt-engineer: Prompt design     ~3.5k
senior-engineer: Architecture      ~4k
documentation: Docs specialist     ~3.5k
workflows:     Workflow catalog    ~2.5k
cicd-orchestrator: CI/CD pipes    ~4k
incident-commander: Incident mgmt  ~3.5k
```

### Engineering (/_archive/engineering/)
```yaml
visual-designer:    UI/UX design      ~4.5k ✅
frontend-engineer:  Frontend dev      ~4k
backend-engineer:   Backend APIs      ~4k
automation-engineer: Test automation  ~4.5k 🔄
qa-automation:      QA processes      ~3.5k
performance-optimizer: Perf tuning   ~4k
security-engineer:  Security impl     ~4.5k
data-engineer:      Data pipelines    ~4k
```

### Analysis (/_archive/analysis/)
```yaml
business-analyst:  Requirements  ~3.5k
technical-analyst: Systems      ~3.5k
security-analyst:  Threats       ~4k
data-analyst:      Analytics     ~3.5k
```

### Business (/_archive/business/)
```yaml
project-manager:    Planning     ~3.5k
product-manager:    Strategy     ~3.5k
stakeholder-comm:   Comms        ~3k
```

### Infrastructure (/_archive/infrastructure/) ✅
```yaml
cloud-architect:    AWS/Azure/GCP  ~4k
kubernetes-spec:    K8s deploy     ~4.5k
terraform-engineer: IaC impl       ~4k
```

### Workflows (/workflows/)
```yaml
debug-assistant:    Debug helper      ~3.5k
code-review:        Review process    ~4k
test-generation:    Auto tests        ~3.5k
migration-planner:  Migrations        ~4.5k
api-designer:       REST APIs         ~4k
performance-audit:  Perf analysis     ~4.5k
security-audit:     Security check    ~5k
refactoring-guide:  Refactor help     ~4k
dependency-analyzer: Deps analysis    ~3.5k
documentation-gen:  Auto docs         ~3.5k
css-safety-check:   CSS validation    ~3.5k ✅
visual-testing:     Visual regression ~4k ✅
accessibility-audit: A11y check       ~4k
containerization:   Docker/K8s        ~4.5k
monitoring-setup:   Observability     ~4k
```

### Quick Usage
```bash
/load _archive/engineering/visual-designer
/workflow css-safety-check
/help <agent-name>
```

### Task Recommendations
- **UI/UX**: visual-designer, frontend-engineer, css-safety-check
- **Cloud**: cloud-architect, kubernetes-spec, terraform-engineer
- **Quality**: senior-engineer, code-review, security-audit
- **Planning**: project-manager, technical-analyst, migration-planner

**Legend**: ✅ New | 🔄 Enhanced | ~Xk = ~X,000 tokens
</output>

<relatedCommands>
- guide: System documentation
- workflows: Workflow details
- prompt-engineer: Optimize usage
</relatedCommands>
</command>