# CI/CD Orchestrator Command

## Command: /cicd-orchestrator

```yaml
meta:
  name: cicd-orchestrator
  description: Enterprise CI/CD orchestration with intelligent automation
  version: 3.0.0
  token_estimate: 5k-10k

hooks:
  pre_execution:
    - {name: pipeline_validator, priority: 1, validate: [syntax, dependencies, permissions, resources]}
    - {name: environment_checker, priority: 2, verify: [staging_ready, prod_frozen, backup_available]}
    - {name: approval_workflow, priority: 3, required: {staging: 1, production: 2}}
  
  execution:
    - name: progressive_deployment
      config: {strategy: canary, initial: 10%, increment: 20%, health_check: 60s}
    - name: real_time_monitoring
      metrics: [error_rate, response_time, cpu_usage, memory]
      thresholds: {error_rate: 0.05, response_time: 2000ms}
  
  post_execution:
    - {name: deployment_verifier, checks: [health_endpoints, smoke_tests, integration_tests]}
    - {name: notification_dispatcher, channels: [slack, email, pagerduty]}
  
  error_handling:
    - name: automatic_rollback
      triggers: [health_check_fail, error_spike, manual]
      strategy: blue_green
    - {name: incident_creator, severity: {production_down: P1, degraded: P2, partial: P3}}

config:
  deployment_strategy: progressive
  rollback_enabled: true
  monitoring_level: comprehensive
  compliance_mode: sox_compliant

capabilities:
  - Multi-environment pipeline orchestration
  - Automated rollback with data preservation
  - Progressive deployment strategies (canary, blue-green)
  - Real-time monitoring and alerting
  - Compliance and audit trail generation
  - Self-healing pipeline capabilities

instructions:
  role: Expert CI/CD Orchestrator managing enterprise deployment pipelines
  
  safety_protocols: &safety_ref
    - Progressive rollout strategies
    - Automated health checks at each stage
    - Immediate rollback on failure detection
    - Zero-downtime deployment patterns
  
  pipeline_mgmt: &pipeline_ref
    - Validate configurations before execution
    - Implement proper secret management
    - Use infrastructure as code principles
    - Maintain immutable deployment artifacts
  
  monitoring: &monitoring_ref
    - Real-time metrics collection
    - Automated anomaly detection
    - Comprehensive audit logging
    - Performance baseline comparisons
  
  process:
    1: Validate pipeline syntax and dependencies
    2: Check environment readiness and approvals
    3: Create backup points for rollback
    4: Execute progressive deployment
    5: Monitor health metrics continuously
    6: Generate deployment reports

advanced:
  features: [auto_scaling, chaos_engineering, ab_testing, feature_flags, db_migration]

templates:
  microservice:
    stages: [build_test, security_scan, registry_push, staging_deploy, prod_canary, full_rollout]
  database_migration:
    stages: [schema_validate, backup, dry_run, staged_migration, data_verify, perf_validate]

examples:
  - scenario: Production Deployment
    trigger: /cicd-orchestrator deploy api-service to production
    flow: [validate_config, get_approvals, backup, canary_10%, monitor_5min, scale_100%]
  
  - scenario: Emergency Hotfix
    trigger: /cicd-orchestrator hotfix security-patch --expedite
    flow: [fast_track_approval, direct_deploy, enhanced_monitoring, incident_update]

coordination:
  handoff_to: [security-engineer, incident-commander, performance-optimizer]
```