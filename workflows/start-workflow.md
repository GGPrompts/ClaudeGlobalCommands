# Start Workflow - Automated Task Execution

**Command**: `/workflow start` or `/execute`  
**Token Usage**: ~3,000 base + task execution
**Architecture**: Hierarchical with parallel burst

```yaml
metadata:
  name: start-workflow
  aliases: [go, start]
  version: 1.0.0

orchestration:
  mode: progressive
  phases: 5
  parallelism: dynamic

phases:
  discovery:
    agent: orchestrator
    tokens: ~1000
    tasks:
      - read plan.md
      - extract unchecked items
      - categorize by type
      - branch: tasks_found ? enhance : brainstorm

  enhancement:
    agent: prompt-engineer  
    tokens: ~1500
    tasks:
      - clarify ambiguous tasks
      - query user for context
      - optimize prompts
      - prepare execution plan

  assignment:
    agent: orchestrator
    tokens: ~500
    strategy:
      code: [senior-engineer, backend, frontend]
      docs: [documentation, technical-writer]
      test: [qa-automation, test-engineer]
      security: [security-engineer, analyst]
      infra: [cloud-architect, k8s, terraform]

  execution:
    mode: parallel
    max_concurrent: 5
    monitor: real-time
    collect: streaming

  compilation:
    agent: orchestrator
    tokens: ~1000
    outputs:
      - update plan.md
      - execution summary
      - next steps

fallback_brainstorm:
  agent: feature-planner
  tokens: ~2000
  trigger: no_tasks_found
```

## Quick Examples

```bash
/start                    # Execute all tasks
/execute security first   # Prioritize security tasks  
/start brainstorm        # Force brainstorming mode
```

## Task Recognition

```yaml
patterns:
  implement|code|build: engineering
  document|write: documentation
  test|verify: quality
  optimize|improve: performance
  deploy|infrastructure: devops
```

## Execution Report

```markdown
🚀 **Execution Summary**
- Tasks: 8/10 completed
- Tokens: 15,500 used
- Time: 4.2 minutes

✅ Completed:
- Task 1.1: Setup shared components (@senior-engineer)
- Task 1.2: Create templates (@documentation)

⚠️ Blocked:
- Task 1.3: Needs API key
```