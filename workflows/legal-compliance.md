# Legal Compliance Review Workflow

**Token Estimate: ~6,000 tokens**

<workflow name="legal-compliance">
<description>
Comprehensive legal review workflow for software projects, covering licensing, privacy, intellectual property, terms of service, and regulatory compliance. Produces actionable compliance roadmap with risk mitigation strategies.
</description>

<version>1.0.0</version>
<lastUpdated>2025-01-01</lastUpdated>

<prerequisites>
- Project codebase or repository access
- List of third-party dependencies
- Target deployment regions
- Business model (SaaS, open source, enterprise)
- Data collection and processing overview
</prerequisites>

<agents>
- legal-expert (lead)
- security-engineer
- documentation
- senior-engineer
</agents>

<phases>
<phase number="1" name="License Audit">
<agent>legal-expert</agent>
<tasks>
- Scan all project dependencies for licenses
- Create license compatibility matrix
- Identify GPL/AGPL/proprietary conflicts
- Check for license notice requirements
- Review custom code licensing decisions
</tasks>
<deliverables>
- License inventory spreadsheet
- Compatibility analysis report
- Required attribution list
- License conflict remediation plan
</deliverables>
</phase>

<phase number="2" name="Privacy & Data Protection">
<agent>legal-expert</agent>
<tasks>
- Map data flows and collection points
- Identify applicable privacy laws (GDPR, CCPA, etc.)
- Review consent mechanisms
- Analyze data retention policies
- Check cross-border data transfers
</tasks>
<deliverables>
- Privacy impact assessment
- Required privacy policy updates
- Consent flow diagrams
- Data processing agreements templates
</deliverables>
</phase>

<phase number="3" name="Security Compliance">
<agent>security-engineer</agent>
<tasks>
- Review security controls implementation
- Check encryption standards compliance
- Verify access control mechanisms
- Assess vulnerability management
- Review incident response procedures
</tasks>
<deliverables>
- Security compliance checklist
- Gap analysis report
- Remediation priorities
- Security policy templates
</deliverables>
</phase>

<phase number="4" name="Terms & Policies">
<agent>legal-expert</agent>
<tasks>
- Draft/review terms of service
- Create acceptable use policy
- Develop SLA templates
- Review disclaimer requirements
- Check accessibility compliance
</tasks>
<deliverables>
- Terms of service document
- Privacy policy
- Cookie policy
- Required disclaimers
- DMCA procedures
</deliverables>
</phase>

<phase number="5" name="Regulatory Compliance">
<agent>legal-expert</agent>
<tasks>
- Identify industry-specific regulations
- Review export control requirements
- Check financial services compliance
- Assess healthcare regulations (HIPAA)
- Review AI/ML specific regulations
</tasks>
<deliverables>
- Regulatory requirement matrix
- Compliance gap analysis
- Implementation roadmap
- Audit preparation checklist
</deliverables>
</phase>

<phase number="6" name="Implementation Plan">
<agent>senior-engineer</agent>
<tasks>
- Prioritize compliance fixes
- Create technical implementation guide
- Design compliance monitoring systems
- Build automated compliance checks
- Plan team training
</tasks>
<deliverables>
- Technical implementation roadmap
- Automated compliance tools
- CI/CD integration plan
- Developer guidelines
</deliverables>
</phase>

<phase number="7" name="Documentation Package">
<agent>documentation</agent>
<tasks>
- Compile all compliance documentation
- Create maintenance procedures
- Build compliance training materials
- Design audit trail systems
- Develop ongoing review schedule
</tasks>
<deliverables>
- Complete compliance package
- Training materials
- Audit procedures
- Maintenance calendar
</deliverables>
</phase>
</phases>

<interaction>
User provides project details → Legal expert performs comprehensive audit → Security engineer validates technical compliance → Senior engineer creates implementation plan → Documentation specialist packages everything → User receives complete compliance roadmap
</interaction>

<output>
## Legal Compliance Report

### Executive Summary
- **Overall Risk Level**: [High/Medium/Low]
- **Critical Issues**: [Number and severity]
- **Estimated Remediation Time**: [Timeline]
- **Budget Implications**: [Cost estimates]

### License Compliance
#### Current State
- **Total Dependencies**: [Number]
- **License Types**: [Breakdown]
- **Conflicts Found**: [Details]

#### Required Actions
1. [Specific remediation steps]

### Privacy & Data Protection
#### Applicable Regulations
- [List of relevant laws]

#### Compliance Gaps
- [Specific gaps identified]

#### Implementation Requirements
- [Privacy engineering tasks]

### Security Compliance
#### Framework Alignment
- [SOC 2, ISO 27001, etc.]

#### Technical Controls
- [Required implementations]

### Terms & Policies
#### Required Documents
- [ ] Terms of Service
- [ ] Privacy Policy
- [ ] Cookie Policy
- [ ] Data Processing Agreement
- [ ] Acceptable Use Policy

### Regulatory Requirements
#### Industry-Specific
- [Relevant regulations]

#### Geographic
- [Regional requirements]

### Implementation Roadmap
#### Phase 1: Critical (0-30 days)
- [Urgent fixes]

#### Phase 2: Important (31-90 days)
- [Important improvements]

#### Phase 3: Enhancement (90+ days)
- [Long-term compliance]

### Ongoing Compliance
#### Monitoring Systems
- [Automated checks]

#### Review Schedule
- [Quarterly/Annual reviews]

#### Team Responsibilities
- [RACI matrix]

### Risk Register
| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [Risk description] | [H/M/L] | [H/M/L] | [Action] |

### Cost Analysis
- **Immediate Costs**: [Tools, licenses]
- **Ongoing Costs**: [Monitoring, audits]
- **Risk Mitigation Value**: [Avoided penalties]
</output>

<best_practices>
- Start compliance early in development
- Automate compliance checking
- Document all decisions
- Regular review cycles
- Train development team
- Maintain audit trails
- Consider privacy by design
- Plan for international expansion
</best_practices>

<troubleshooting>
<issue>Incompatible licenses discovered</issue>
<solution>Replace dependencies, negotiate licenses, or restructure code architecture</solution>

<issue>Privacy law conflicts</issue>
<solution>Implement strictest requirements, use privacy framework overlays</solution>

<issue>High remediation costs</issue>
<solution>Prioritize by risk, phase implementation, seek alternative solutions</solution>
</troubleshooting>

<coordination>
Legal expert leads the workflow, coordinating with security engineer for technical validation, senior engineer for implementation planning, and documentation specialist for comprehensive record keeping. All agents ensure practical, implementable solutions.
</coordination>
</workflow>