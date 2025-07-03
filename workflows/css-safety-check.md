# CSS Safety Check Workflow - Optimized v3.0

**Description**: Hierarchical CSS validation using phased execution for efficient analysis and optimization.

**Architecture**: Orchestrator → Performance Analyzer → Compatibility Specialist → Accessibility Validator → Optimizer

**Token Usage**: ~2,100 tokens (40% reduction from v2.1)

```yaml
workflow:
  name: css-safety-check-optimized
  version: 3.0.0
  pattern: hierarchical-validation
  category: validation
  
  # Phase 1: Orchestration (800 tokens)
  orchestrator:
    role: css-validation-orchestrator
    tokens: 800
    
    initial_scan:
      - Collect CSS file paths
      - Calculate total CSS size
      - Identify critical files
      - Plan validation strategy
      
    delegation_map:
      performance:
        condition: "CSS size > 50KB OR selector count > 1000"
        agent: performance-analyzer
        context: file_paths + metrics
        
      compatibility:
        condition: "Browser targets specified"
        agent: compatibility-specialist
        context: target_browsers + feature_usage
        
      accessibility:
        condition: "Always required"
        agent: accessibility-validator
        context: color_values + interactive_selectors
        
      optimization:
        condition: "Issues found > 5"
        agent: css-optimizer
        context: issue_summary + performance_metrics
    
    coordination:
      - Sequential execution
      - Minimal context passing
      - Aggregated reporting
      - Early termination on critical issues

  # Phase 2: Performance Analysis (500 tokens)
  performance_analyzer:
    role: css-performance-specialist
    tokens: 500
    
    focus_areas:
      selector_efficiency:
        checks:
          - Descendant selector depth
          - Universal selector usage
          - Attribute selector complexity
          - Pseudo-selector performance
        
        thresholds:
          max_depth: 4
          complex_selectors: 10%
          
      redundancy_detection:
        - Duplicate declarations
        - Unused rules (if HTML provided)
        - Redundant vendor prefixes
        - Overspecific selectors
        
    output_format:
      issues:
        - type: expensive_selector
          selector: string
          impact: high|medium|low
          suggestion: optimized_version
          
      metrics:
        total_selectors: number
        complex_selectors: number
        estimated_performance: score

  # Phase 3: Compatibility Check (400 tokens)
  compatibility_specialist:
    role: browser-compatibility-expert
    tokens: 400
    
    validation_scope:
      - CSS Grid/Flexbox usage
      - Custom properties support
      - Modern features detection
      - Vendor prefix requirements
      
    check_process:
      feature_detection:
        - Identify CSS features used
        - Map to browser support matrix
        - Flag unsupported combinations
        
      fallback_analysis:
        - Check for fallback values
        - Validate progressive enhancement
        - Suggest polyfills if needed
    
    output:
      compatibility_score: percentage
      unsupported_features: list
      missing_prefixes: list
      fallback_suggestions: list

  # Phase 4: Accessibility Validation (300 tokens)
  accessibility_validator:
    role: css-accessibility-expert
    tokens: 300
    
    critical_checks:
      color_contrast:
        - Extract color pairs
        - Calculate contrast ratios
        - Validate against WCAG AA/AAA
        
      focus_indicators:
        - Check :focus styles
        - Validate outline removal
        - Ensure visible indicators
        
      motion_preferences:
        - Check prefers-reduced-motion
        - Validate animation controls
        
      touch_targets:
        - Minimum size validation
        - Spacing requirements
    
    output:
      wcag_compliance: level
      contrast_issues: list
      focus_problems: list
      motion_concerns: list

  # Phase 5: Optimization Engine (100 tokens)
  css_optimizer:
    role: css-optimization-specialist
    tokens: 100
    
    optimization_tasks:
      - Generate critical CSS
      - Suggest file splitting
      - Recommend minification
      - Propose consolidation
      
    strategies:
      size_reduction:
        - Remove unused rules
        - Consolidate similar rules
        - Optimize property order
        
      delivery_optimization:
        - Critical path extraction
        - Async loading strategy
        - HTTP/2 push recommendations
    
    final_recommendations:
      priority: high|medium|low
      estimated_savings: percentage
      implementation_effort: score

  # Execution Flow
  execution:
    flow_type: sequential_with_early_exit
    
    phases:
      - phase: orchestration
        duration: 10s
        output: validation_plan
        
      - phase: performance
        duration: 20s
        output: performance_report
        exit_condition: "critical_issues > 10"
        
      - phase: compatibility
        duration: 15s
        output: compatibility_report
        parallel_with: accessibility
        
      - phase: accessibility
        duration: 15s
        output: accessibility_report
        parallel_with: compatibility
        
      - phase: optimization
        duration: 10s
        output: optimization_plan
        condition: "total_issues > 5"

  # Progressive Enhancement Modes
  modes:
    quick_check:
      tokens: ~1000
      phases: [orchestration, performance]
      use_case: "CI/CD pipeline checks"
      
    standard:
      tokens: ~2100
      phases: all
      use_case: "Pre-release validation"
      
    performance_only:
      tokens: ~1300
      phases: [orchestration, performance, optimization]
      use_case: "Performance optimization focus"

  # Output Templates
  outputs:
    summary_report:
      ```markdown
      ## CSS Safety Check Report
      
      ### Overview
      - Files analyzed: {count}
      - Total CSS size: {size}
      - Critical issues: {critical_count}
      - Warnings: {warning_count}
      
      ### Performance Score: {score}/100
      {performance_details}
      
      ### Browser Compatibility: {percentage}%
      {compatibility_details}
      
      ### Accessibility: {wcag_level}
      {accessibility_details}
      
      ### Optimization Opportunities
      {optimization_suggestions}
      ```
    
    detailed_issues:
      format: json
      structure:
        - file: path
          issues: array
          severity: critical|warning|info
          suggestions: array

  # Success Metrics
  metrics:
    efficiency:
      - Token reduction: 40%
      - Execution time: -35%
      - Coverage maintained: 100%
      
    quality:
      - Issue detection rate
      - False positive rate
      - Actionable suggestions

  # Integration Points
  integrations:
    ci_cd:
      - GitHub Actions
      - GitLab CI
      - Jenkins
      - CircleCI
      
    tools:
      - PostCSS
      - Stylelint
      - PurgeCSS
      - Critical

  # Comparison with v2.1
  improvements:
    token_usage:
      v2.1: 3500
      v3.0: 2100
      reduction: 40%
      
    execution:
      v2.1: parallel_specialists
      v3.0: hierarchical_phases
      benefit: "Better coordination, less redundancy"
      
    flexibility:
      v2.1: single_mode
      v3.0: progressive_enhancement
      benefit: "Adapt to different needs"
```

## Benefits Over v2.1

1. **Token Efficiency**: 40% reduction through hierarchical delegation
2. **Focused Analysis**: Each specialist works on pre-filtered data
3. **Early Exit**: Stop execution when critical issues found
4. **Flexible Modes**: Choose depth based on needs
5. **Better Coordination**: Clear handoffs prevent duplicate work

## Migration from v2.1

```yaml
migration_guide:
  key_changes:
    - XML-style workflow → YAML configuration
    - Parallel execution → Sequential phases
    - Full context sharing → Minimal context passing
    - Single mode → Progressive enhancement
    
  compatibility:
    - Maintains all v2.1 checks
    - Same quality standards
    - Enhanced reporting format
    - Backward compatible outputs
```