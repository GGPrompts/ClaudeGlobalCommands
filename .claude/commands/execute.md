---
description: "Execute - quick task routing to the best specialist or workflow"
---

# Execute Command

A lightweight router that quickly connects you to the right specialist or workflow.

---

## Workflow

### Step 1: Get the Task

If the user didn't provide a task, ask:

"What would you like to accomplish?"

---

### Step 2: Analyze and Route

Analyze the task and determine the best destination:

| Task Pattern | Route To |
|--------------|----------|
| Code review, architecture, bugs | `/senior-engineer` |
| UI, CSS, design, accessibility | `/visual-designer` |
| Incident, outage, P1/P2 | `/incident-commander` |
| Deploy, pipeline, CI/CD | `/cicd-orchestrator` |
| Docs, README, API docs | `/documentation` |
| Prompt, instruction design | `/prompt-engineer` |
| Cloud, AWS, Azure, GCP, infra | `/cloud-architect` |
| Legal, license, compliance, GDPR | `/legal-expert` |
| Marketing, content, campaign | `/marketing-expert` |

---

### Step 3: Confirm Route

Use `AskUserQuestion`:

**Question**: "I'll route this to [agent]. Sound good?"
**Header**: "Route"
**Multi-select**: false

**Options**:
1. **"Yes, proceed"** - "Route to recommended agent"
2. **"Show me options"** - "List all available agents to choose from"
3. **"Just do it directly"** - "Handle the task yourself without specialist routing"

---

### Step 4: Execute

#### If "Yes, proceed"
Invoke the selected agent's workflow with the user's task as context.

#### If "Show me options"
Display available agents:

```
## Available Agents

**Engineering:**
- /senior-engineer - Code review, architecture, security
- /visual-designer - UI/UX, CSS, accessibility

**Operations:**
- /incident-commander - Incident response, post-mortems
- /cicd-orchestrator - Deployments, pipelines

**Infrastructure:**
- /cloud-architect - AWS/Azure/GCP, IaC, scaling

**Business:**
- /legal-expert - Licensing, compliance, privacy
- /marketing-expert - Campaigns, content, SEO

**Support:**
- /documentation - Docs, README, API docs
- /prompt-engineer - Prompt design and optimization
```

Then ask which one to use.

#### If "Just do it directly"
Handle the task yourself using your general capabilities.

---

## Quick Examples

```bash
/execute review the auth module      → routes to /senior-engineer
/execute fix the navbar spacing      → routes to /visual-designer
/execute we have a P1 outage         → routes to /incident-commander
/execute deploy to staging           → routes to /cicd-orchestrator
/execute update the API docs         → routes to /documentation
```

---

Execute this workflow now. If the user provided a task, analyze it and suggest the best route.
