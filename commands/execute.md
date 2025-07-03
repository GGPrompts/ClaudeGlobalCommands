# Execute Command

**Command**: `/execute`  
**Aliases**: `/start`  
**Tokens**: ~500

```yaml
type: workflow-launcher
target: start-workflow
desc: Execute tasks from plan.md with auto agent assignment

usage:
  "/execute": Execute all tasks
  "/execute security": Priority filter
  "/execute brainstorm": Force planning

flow:
  1. Read plan.md tasks
  2. Enhance prompts
  3. Assign best agents
  4. Parallel execute
  5. Update progress

features:
  - No config needed
  - Auto agent selection
  - Parallel execution
  - Progress tracking
  - Fallback brainstorming
```