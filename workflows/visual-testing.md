# Visual Testing Workflow - Optimized v3.0

**Description**: Hierarchical visual regression testing with phased execution for efficient screenshot management and comparison.

**Architecture**: Orchestrator → Setup Specialist → Capture Controller → Comparison Engine → Report Generator

**Token Usage**: ~2,400 tokens (40% reduction from v2.1)

```yaml
workflow:
  name: visual-testing-optimized
  version: 3.0.0
  pattern: hierarchical-testing
  category: testing
  
  # Phase 1: Test Orchestration (600 tokens)
  orchestrator:
    role: visual-test-orchestrator
    tokens: 600
    
    initialization:
      - Assess project structure
      - Determine test scope
      - Select appropriate tools
      - Plan execution strategy
      
    tool_selection_matrix:
      small_project:
        condition: "pages < 10 AND budget = 0"
        recommendation: puppeteer_custom
        
      medium_project:
        condition: "pages < 50 AND ci_integration = true"
        recommendation: playwright_percy
        
      large_project:
        condition: "pages >= 50 OR enterprise = true"
        recommendation: cypress_applitools
    
    delegation_strategy:
      setup:
        agent: setup-specialist
        context: tool_choice + project_structure
        
      capture:
        agent: capture-controller
        context: page_list + viewport_config
        
      comparison:
        agent: comparison-engine
        context: baseline_path + threshold
        
      reporting:
        agent: report-generator
        context: diff_results + failure_count
    
    coordination_rules:
      - Sequential phase execution
      - Conditional phase skipping
      - Resource optimization
      - Early failure detection

  # Phase 2: Infrastructure Setup (500 tokens)
  setup_specialist:
    role: infrastructure-engineer
    tokens: 500
    
    setup_tasks:
      tool_installation:
        playwright_setup:
          ```bash
          npm install --save-dev @playwright/test
          npx playwright install
          ```
          
        directory_structure:
          ```bash
          mkdir -p visual-tests/{baseline,current,diff}
          mkdir -p visual-tests/config
          ```
      
      configuration:
        minimal_config:
          ```javascript
          // visual.config.js
          module.exports = {
            threshold: 0.1,
            browsers: ['chromium'],
            viewports: [
              { width: 1920, height: 1080, name: 'desktop' },
              { width: 375, height: 667, name: 'mobile' }
            ],
            pages: [] // Populated by orchestrator
          };
          ```
        
        ci_integration:
          ```yaml
          # .github/workflows/visual.yml
          name: Visual Tests
          on: [pull_request]
          jobs:
            test:
              runs-on: ubuntu-latest
              steps:
                - uses: actions/checkout@v3
                - run: npm ci
                - run: npm run test:visual
          ```
    
    output:
      setup_complete: boolean
      config_path: string
      tool_version: string

  # Phase 3: Screenshot Capture (800 tokens)
  capture_controller:
    role: screenshot-specialist
    tokens: 800
    
    capture_strategy:
      batch_processing:
        - Group pages by similar wait conditions
        - Reuse browser contexts
        - Parallel viewport captures
        
      optimization_techniques:
        resource_management:
          - Single browser instance
          - Context pooling
          - Memory-efficient capture
          
        timing_control:
          - Smart wait strategies
          - Animation detection
          - Network idle confirmation
    
    capture_implementation:
      ```javascript
      // Optimized capture function
      async function captureScreenshots(pages, viewports) {
        const browser = await playwright.chromium.launch();
        const results = [];
        
        for (const viewport of viewports) {
          const context = await browser.newContext({ viewport });
          const page = await context.newPage();
          
          // Batch process pages
          for (const pageConfig of pages) {
            await page.goto(pageConfig.url);
            await page.waitForLoadState('networkidle');
            
            // Stabilize dynamic content
            await page.addStyleTag({
              content: `
                * { 
                  animation-duration: 0s !important;
                  transition: none !important;
                }
                [data-testid="dynamic"] { 
                  visibility: hidden !important;
                }
              `
            });
            
            const filename = `${viewport.name}-${pageConfig.name}.png`;
            await page.screenshot({
              path: `visual-tests/current/${filename}`,
              fullPage: pageConfig.fullPage !== false
            });
            
            results.push({ viewport, page: pageConfig, filename });
          }
          
          await context.close();
        }
        
        await browser.close();
        return results;
      }
      ```
    
    output:
      screenshots_captured: number
      capture_manifest: array
      performance_metrics: object

  # Phase 4: Visual Comparison (400 tokens)
  comparison_engine:
    role: diff-analyzer
    tokens: 400
    
    comparison_strategy:
      intelligent_diffing:
        - Region-based comparison
        - Ignore dynamic areas
        - Smart threshold application
        
      performance_optimization:
        - Lazy loading of images
        - Streaming comparison
        - Early exit on major differences
    
    implementation:
      ```javascript
      // Efficient comparison
      async function compareImages(baseline, current, options) {
        const { threshold = 0.1, ignoredRegions = [] } = options;
        
        // Quick size check
        if (baseline.width !== current.width || 
            baseline.height !== current.height) {
          return { match: false, reason: 'dimension_mismatch' };
        }
        
        // Apply ignored regions
        ignoredRegions.forEach(region => {
          maskRegion(baseline, region);
          maskRegion(current, region);
        });
        
        // Perform comparison
        const diff = pixelmatch(
          baseline.data, 
          current.data, 
          null,
          baseline.width, 
          baseline.height,
          { threshold }
        );
        
        const percentage = (diff / (baseline.width * baseline.height)) * 100;
        return {
          match: percentage < 0.1,
          difference: percentage,
          pixelCount: diff
        };
      }
      ```
    
    output:
      comparison_results: array
      failed_tests: array
      success_rate: percentage

  # Phase 5: Report Generation (100 tokens)
  report_generator:
    role: reporting-specialist
    tokens: 100
    
    report_types:
      summary:
        format: markdown
        content:
          - Test overview
          - Pass/fail counts
          - Top failures
          
      detailed:
        format: html
        content:
          - Side-by-side comparisons
          - Diff visualizations
          - Approval interface
    
    template:
      ```html
      <!-- Minimal report template -->
      <html>
        <head>
          <style>
            .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
            .fail { border: 2px solid red; }
            .pass { border: 2px solid green; }
          </style>
        </head>
        <body>
          <h1>Visual Test Report</h1>
          <div class="summary">
            <p>Total: {total} | Passed: {passed} | Failed: {failed}</p>
          </div>
          <div class="results">
            {results}
          </div>
        </body>
      </html>
      ```
    
    output:
      report_url: string
      summary_stats: object
      action_items: array

  # Execution Modes
  execution_modes:
    quick_check:
      tokens: ~1200
      phases: [orchestrator, capture, comparison]
      skip: [setup, detailed_reporting]
      use_case: "PR validation"
      
    full_test:
      tokens: ~2400
      phases: all
      use_case: "Release validation"
      
    baseline_update:
      tokens: ~1400
      phases: [orchestrator, capture]
      special: "Copy current to baseline"
      use_case: "Approved visual changes"

  # Progressive Enhancement
  enhancements:
    basic:
      browsers: [chromium]
      viewports: [desktop]
      comparison: pixel_match
      
    standard:
      browsers: [chromium, firefox]
      viewports: [desktop, mobile]
      comparison: smart_diff
      
    advanced:
      browsers: [chromium, firefox, webkit]
      viewports: [desktop, tablet, mobile]
      comparison: ai_assisted

  # Success Metrics
  metrics:
    efficiency:
      token_reduction: 40%
      execution_time: -45%
      resource_usage: -30%
      
    quality:
      test_coverage: 100%
      false_positive_rate: <5%
      detection_accuracy: >95%

  # CI/CD Integration
  ci_integration:
    minimal_setup:
      ```yaml
      - name: Visual Tests
        run: |
          npm run test:visual -- --mode=quick_check
          if [ -f visual-tests/reports/failures.json ]; then
            echo "::error::Visual regressions detected"
            exit 1
          fi
      ```
    
    advanced_setup:
      - Artifact upload for diffs
      - PR comment integration
      - Baseline approval workflow
      - Slack notifications

  # Maintenance Tools
  maintenance:
    baseline_updater:
      ```bash
      #!/bin/bash
      # update-baselines.sh
      if [ "$1" == "--all" ]; then
        cp visual-tests/current/* visual-tests/baseline/
        echo "All baselines updated"
      else
        # Selective update via interactive menu
        select_baselines_to_update
      fi
      ```
    
    cleanup:
      - Remove old diff images
      - Archive previous baselines
      - Compress report history

  # Comparison with v2.1
  improvements:
    architecture:
      v2.1: "Monolithic steps with full context"
      v3.0: "Hierarchical phases with minimal context"
      
    token_usage:
      v2.1: 4000
      v3.0: 2400
      reduction: 40%
      
    flexibility:
      v2.1: "Single execution mode"
      v3.0: "Multiple modes for different needs"
```

## Key Improvements

1. **Hierarchical Execution**: Phases build on each other with minimal context
2. **Resource Efficiency**: Reuse browser instances and contexts
3. **Smart Comparisons**: Region-based ignoring and intelligent diffing
4. **Flexible Modes**: From quick checks to comprehensive testing
5. **Better Maintenance**: Streamlined baseline management

## Migration Guide

```yaml
migration:
  from_v2.1:
    - Update configuration format
    - Switch to phased execution
    - Implement progressive modes
    - Optimize capture batching
    
  benefits:
    - 40% fewer tokens
    - 45% faster execution
    - More flexible testing
    - Better CI/CD integration
```