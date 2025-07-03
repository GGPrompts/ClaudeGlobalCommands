# Claude Global Commands Migration Checklist

## Pre-Migration Steps

### 1. Backup Current System
- [ ] Create full backup of current prompt files
- [ ] Document current token usage baseline
- [ ] Export any custom configurations
- [ ] Tag current version in git

### 2. Validate Infrastructure
- [ ] Verify `/setup/` directory is complete
- [ ] Test all utility scripts function correctly
- [ ] Confirm shared-components.yaml is accessible
- [ ] Check template references resolve properly

## Migration Process

### 3. Command Files Migration
- [ ] Replace `prompt-engineer.md` with optimized version
- [ ] Replace `documentation.md` with optimized version
- [ ] Replace `senior-engineer.md` with optimized version
- [ ] Replace `agents.md` with optimized version
- [ ] Replace `cicd-orchestrator.md` with optimized version
- [ ] Replace `incident-commander.md` with optimized version
- [ ] Replace `workflows.md` with optimized version
- [ ] Replace `guide.md` with optimized version

### 4. Workflow Files Migration
- [ ] Replace `documentation-update.md` with hierarchical version
- [ ] Replace `css-safety-check.md` with optimized version
- [ ] Replace `visual-testing.md` with optimized version

### 5. Testing Phase
- [ ] Test each command individually
- [ ] Verify output quality maintained
- [ ] Check token usage reduction
- [ ] Validate all references resolve
- [ ] Test workflow handoffs function correctly

## Post-Migration Validation

### 6. Performance Verification
- [ ] Measure actual token usage vs estimates
- [ ] Compare response times (should be faster)
- [ ] Verify memory usage improvements
- [ ] Check for any errors in logs

### 7. Quality Assurance
- [ ] A/B test outputs against original prompts
- [ ] Collect user feedback on changes
- [ ] Document any issues found
- [ ] Create rollback plan if needed

### 8. Documentation Updates
- [ ] Update main README.md with new architecture
- [ ] Add optimization notes to CONTRIBUTING.md
- [ ] Update any API documentation
- [ ] Create user migration guide

## Monitoring & Maintenance

### 9. Set Up Monitoring
- [ ] Configure token usage tracking
- [ ] Set up performance dashboards
- [ ] Create alerts for anomalies
- [ ] Schedule regular optimization reviews

### 10. Establish Maintenance Process
- [ ] Create template for adding new commands
- [ ] Document shared component update process
- [ ] Set up quarterly optimization reviews
- [ ] Train team on new architecture

## Sign-Off

- [ ] Technical Lead Approval
- [ ] Quality Assurance Approval
- [ ] Documentation Complete
- [ ] Rollback Plan Tested
- [ ] Migration Complete

**Migration Date**: ___________
**Completed By**: ___________
**Token Reduction Achieved**: ___________