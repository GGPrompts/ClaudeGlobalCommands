# Documentation Update Workflow - Optimized v3.0

**Description**: Hierarchical documentation maintenance workflow using orchestrator pattern for efficient token usage.

**Architecture**: Orchestrator → Content Analyzer → Format Specialist → Quality Reviewer

**Token Usage**: ~12,000 tokens (40% reduction from v2.0)

```yaml
workflow:
  name: documentation-update-optimized
  version: 3.0.0
  pattern: hierarchical-orchestration
  
  activation:
    - "Update Documentation"
    - "Run Documentation Update"
    - "Documentation maintenance"
  
  # Phase 1: Orchestration Layer (5k tokens)
  orchestrator:
    role: documentation-orchestrator
    context: minimal
    tokens: 5000
    
    responsibilities:
      - Analyze documentation structure
      - Plan update strategy
      - Delegate specific tasks
      - Coordinate agent handoffs
      - Compile final report
    
    initial_analysis:
      - File inventory and sizes
      - Last update timestamps
      - Documentation health metrics
      - Dependency mapping
    
    delegation_strategy:
      content_analysis:
        agent: content-analyzer
        scope: [README.md, CLAUDE.md, technical docs]
        context: file paths + metrics only
        
      format_optimization:
        agent: format-specialist
        scope: files exceeding size limits
        context: specific sections needing work
        
      quality_review:
        agent: quality-reviewer
        scope: updated content only
        context: change summaries
    
    handoff_protocol:
      - Provide minimal context
      - Include specific tasks
      - Set clear success criteria
      - Define return format

  # Phase 2: Content Analysis (3k tokens)
  content_analyzer:
    role: technical-content-specialist
    tokens: 3000
    
    tasks:
      - Scan for outdated content
      - Identify missing sections
      - Check technical accuracy
      - Find redundancies
      
    analysis_criteria:
      staleness:
        - Version references
        - Deprecated features
        - Completed TODOs
        - Old timestamps
        
      accuracy:
        - Code examples validity
        - API documentation sync
        - Configuration correctness
        - Link validation
    
    output_format:
      findings:
        - file: path
          issues: [list of specific issues]
          priority: high|medium|low
          suggested_fixes: [actionable items]
          
    handoff_to_orchestrator:
      - Prioritized issue list
      - Specific update recommendations
      - Content dependencies

  # Phase 3: Format Optimization (2k tokens)
  format_specialist:
    role: documentation-formatter
    tokens: 2000
    
    focus_areas:
      - Files exceeding size limits
      - Archive candidates
      - Structure improvements
      
    optimization_tasks:
      size_reduction:
        - Extract verbose sections
        - Consolidate duplicates
        - Move examples to separate files
        
      archival:
        - Identify completed phases
        - Package historical content
        - Update references
        
      structure:
        - Improve navigation
        - Update TOCs
        - Add cross-references
    
    constraints:
      - README.md: <500 lines
      - CLAUDE.md: <400 lines
      - PLAN.md: <1000 lines
      - Individual guides: <1000 lines
    
    output:
      - Optimized file versions
      - Archive manifest
      - Structure improvements

  # Phase 4: Quality Review (2k tokens)
  quality_reviewer:
    role: documentation-qa
    tokens: 2000
    
    validation_checks:
      - Example functionality
      - Link integrity
      - Format consistency
      - Completeness verification
      
    review_process:
      code_examples:
        - Syntax validation
        - Execution testing
        - Output verification
        
      user_experience:
        - Clarity assessment
        - Navigation flow
        - Quick start validation
        
      compliance:
        - Style guide adherence
        - Version consistency
        - Terminology standards
    
    final_output:
      - Quality score
      - Issue list
      - Approval status

  # Execution Flow
  execution:
    phases:
      - name: initialization
        agent: orchestrator
        duration: ~1min
        output: strategy document
        
      - name: content_analysis
        agent: content-analyzer
        duration: ~2min
        output: findings report
        
      - name: optimization
        agent: format-specialist
        duration: ~2min
        output: optimized files
        
      - name: quality_assurance
        agent: quality-reviewer
        duration: ~1min
        output: validation report
        
      - name: finalization
        agent: orchestrator
        duration: ~1min
        output: summary + metrics

  # Progressive Enhancement
  enhancements:
    quick_mode:
      tokens: ~6000
      phases: [orchestrator, content-analyzer]
      use_case: "Quick health check"
      
    full_mode:
      tokens: ~12000
      phases: all
      use_case: "Complete maintenance"
      
    archive_only:
      tokens: ~4000
      phases: [orchestrator, format-specialist]
      use_case: "Archive old content"

  # Success Metrics
  metrics:
    efficiency:
      - Token usage vs v2.0: -40%
      - Execution time: -30%
      - Coverage: 100%
      
    quality:
      - Documentation health score
      - Update completeness
      - Error reduction
      
    maintenance:
      - File size compliance
      - Archive organization
      - Link integrity

  # Output Structure
  outputs:
    health_report:
      format: markdown
      includes:
        - Current state summary
        - Size metrics
        - Staleness indicators
        - Quality scores
        
    update_log:
      format: markdown
      includes:
        - Changes by file
        - Archive movements
        - Link updates
        - Action items
        
    metrics_dashboard:
      format: yaml
      includes:
        - Token usage
        - Time taken
        - Files processed
        - Issues resolved
```

## Benefits of Hierarchical Architecture

1. **Token Efficiency**: 40% reduction through focused context sharing
2. **Parallel Prevention**: Sequential phases eliminate redundant work
3. **Clear Accountability**: Each agent has specific, non-overlapping responsibilities
4. **Progressive Enhancement**: Can scale down for quick checks or up for thorough reviews
5. **Better Error Handling**: Failures isolated to specific phases

## Migration Guide from v2.0

```yaml
migration:
  from: parallel-multi-agent
  to: hierarchical-orchestration
  
  key_changes:
    - Replace 4 parallel agents with phased execution
    - Reduce context sharing to essential information
    - Implement progressive enhancement options
    - Add explicit handoff protocols
    
  benefits:
    - 8,000 fewer tokens per run
    - Clearer execution flow
    - Better error isolation
    - Flexible execution modes
```