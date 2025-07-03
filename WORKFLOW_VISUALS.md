# Workflow Visual Documentation
## Graphical Representations of All Claude Global Commands Workflows

**Date**: July 2, 2025  
**Version**: 1.0  
**Purpose**: Visual diagrams to understand workflow architectures and step flows

---

## Table of Contents

1. [Optimized Hierarchical Workflows](#optimized-hierarchical-workflows)
2. [Standard Multi-Agent Workflows](#standard-multi-agent-workflows)  
3. [Development & Quality Workflows](#development--quality-workflows)
4. [Planning & Analysis Workflows](#planning--analysis-workflows)
5. [Infrastructure & Deployment Workflows](#infrastructure--deployment-workflows)
6. [Architecture Patterns](#architecture-patterns)

---

## Optimized Hierarchical Workflows

### 1. Start Workflow (`/execute` command)
**Token Usage**: 3k-5k base + execution  
**Architecture**: Progressive enhancement with parallel burst

```mermaid
graph TD
    A["/execute command"] --> B{Plan.md exists?}
    B -->|Yes| C[Task Discovery]
    B -->|No| Z[Create plan.md template]
    
    C --> D{Tasks found?}
    D -->|No| E[Brainstorming Session]
    D -->|Yes| F[Prompt Engineering]
    
    F --> G[Task Enhancement]
    G --> H[Agent Assignment]
    H --> I[Parallel Execution]
    
    I --> J[Frontend Tasks]
    I --> K[Backend Tasks] 
    I --> L[Documentation Tasks]
    I --> M[Testing Tasks]
    
    J --> N[Results Compilation]
    K --> N
    L --> N
    M --> N
    
    N --> O[Update plan.md]
    O --> P[Execution Report]
    
    E --> Q[Feature Planning]
    Q --> R[New Tasks Created]
    R --> F
    
    style A fill:#e1f5fe
    style E fill:#fff3e0
    style I fill:#f3e5f5
    style P fill:#e8f5e8
```

**Step-by-Step Flow**:
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  1. Discovery   │ ──▶│ 2. Enhancement  │ ──▶│ 3. Assignment   │
│  ~1000 tokens   │    │  ~1500 tokens   │    │   ~500 tokens   │
│                 │    │                 │    │                 │
│ • Read plan.md  │    │ • Clarify tasks │    │ • Match agents  │
│ • Parse tasks   │    │ • Query user    │    │ • Plan parallel │
│ • Categorize    │    │ • Optimize      │    │ • Set budgets   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ 4. Execution    │    │ 5. Compilation  │    │  6. Reporting   │
│  Variable tokens│    │  ~1000 tokens   │    │   Generated     │
│                 │    │                 │    │                 │
│ • Run parallel  │    │ • Collect       │    │ • Summary       │
│ • Monitor       │ ──▶│ • Update plan   │ ──▶│ • Next steps    │
│ • Handle deps   │    │ • Check off     │    │ • Metrics       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 2. Documentation Update Workflow
**Token Usage**: 12k total (40% reduction from 20k)  
**Architecture**: Hierarchical orchestration

```mermaid
graph TD
    A[Documentation Update Request] --> B[Orchestrator Agent]
    B --> C{Analysis Mode}
    
    C -->|Quick| D[Quick Analysis - 2k tokens]
    C -->|Full| E[Full Analysis - 5k tokens]
    C -->|Archive| F[Archive Mode - 8k tokens]
    
    D --> G[Content Analyzer]
    E --> G
    F --> G
    
    G --> H[Format Specialist]
    H --> I[Quality Reviewer]
    I --> J[Final Report]
    
    subgraph "Phase 1: Orchestration"
        B
        direction TB
        B1[Assess Project] --> B2[Plan Strategy]
        B2 --> B3[Select Mode]
    end
    
    subgraph "Phase 2: Content Analysis"
        G
        direction TB
        G1[Scan Documentation] --> G2[Find Outdated Content]
        G2 --> G3[Check Accuracy]
    end
    
    subgraph "Phase 3: Format Optimization"
        H
        direction TB
        H1[Reduce File Sizes] --> H2[Archive Old Content]
        H2 --> H3[Optimize Structure]
    end
    
    subgraph "Phase 4: Quality Review"
        I
        direction TB
        I1[Validate Examples] --> I2[Check Links]
        I2 --> I3[Final Approval]
    end
    
    style B fill:#e3f2fd
    style G fill:#f1f8e9
    style H fill:#fff8e1
    style I fill:#fce4ec
```

**Token Flow Diagram**:
```
Orchestrator (5k)
    │
    ├─ Quick Mode ────────┐
    ├─ Full Mode ─────────┤
    └─ Archive Mode ──────┘
                          │
                          ▼
              Content Analyzer (3k)
                          │
                          ▼ 
              Format Specialist (2k)
                          │
                          ▼
              Quality Reviewer (2k)
                          │
                          ▼
                Total: 12k tokens
```

### 3. CSS Safety Check Workflow  
**Token Usage**: 2.1k total (40% reduction)  
**Architecture**: Sequential validation pipeline

```mermaid
graph LR
    A[CSS Files Input] --> B[Orchestrator]
    
    B --> C[Performance Analyzer]
    C --> D[Compatibility Specialist]
    D --> E[Accessibility Validator]
    E --> F[Optimizer]
    F --> G[Safety Report]
    
    subgraph "Performance Analysis"
        C --> C1[Selector Efficiency]
        C --> C2[Redundancy Detection]
        C --> C3[Bundle Size Analysis]
    end
    
    subgraph "Compatibility Check"
        D --> D1[Browser Support]
        D --> D2[Vendor Prefixes]
        D --> D3[Feature Detection]
    end
    
    subgraph "Accessibility Validation"
        E --> E1[WCAG Compliance]
        E --> E2[Color Contrast]
        E --> E3[Focus Indicators]
    end
    
    subgraph "Optimization"
        F --> F1[Critical CSS]
        F --> F2[Unused Code]
        F --> F3[Minification]
    end
    
    style B fill:#e8eaf6
    style C fill:#e0f2f1
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#f3e5f5
```

**Sequential Flow**:
```
Input CSS Files
       │
       ▼
┌─────────────────┐  300 tokens
│  Orchestrator   │ ─────────────┐
│  • Plan checks  │              │
│  • Set strategy │              │
└─────────────────┘              │
       │                         │
       ▼                         │
┌─────────────────┐  500 tokens  │
│ Performance     │ ─────────────┤
│ • Selectors     │              │
│ • Redundancy    │              │
└─────────────────┘              │
       │                         │
       ▼                         │
┌─────────────────┐  450 tokens  │  Total:
│ Compatibility   │ ─────────────┤  2,100 tokens
│ • Browsers      │              │  (vs 3,500 original)
│ • Prefixes      │              │
└─────────────────┘              │
       │                         │
       ▼                         │
┌─────────────────┐  400 tokens  │
│ Accessibility   │ ─────────────┤
│ • WCAG          │              │
│ • Contrast      │              │
└─────────────────┘              │
       │                         │
       ▼                         │
┌─────────────────┐  450 tokens  │
│ Optimizer       │ ─────────────┘
│ • Critical CSS  │
│ • Cleanup       │
└─────────────────┘
       │
       ▼
   Safety Report
```

### 4. Visual Testing Workflow
**Token Usage**: 2.4k total (40% reduction)  
**Architecture**: Staged testing pipeline

```mermaid
graph TD
    A[Visual Test Request] --> B[Test Orchestrator]
    
    B --> C{Test Type}
    C -->|Regression| D[Regression Setup]
    C -->|Cross-browser| E[Browser Setup]
    C -->|Responsive| F[Viewport Setup]
    
    D --> G[Setup Specialist]
    E --> G
    F --> G
    
    G --> H[Capture Controller]
    H --> I[Comparison Engine]
    I --> J[Report Generator]
    
    subgraph "Setup Phase"
        G --> G1[Install Tools]
        G --> G2[Configure Viewports]
        G --> G3[Prepare Environment]
    end
    
    subgraph "Capture Phase"
        H --> H1[Batch Screenshots]
        H --> H2[Stabilize Content]
        H --> H3[Handle Dynamic Elements]
    end
    
    subgraph "Comparison Phase"
        I --> I1[Intelligent Diffing]
        I --> I2[Threshold Analysis]
        I --> I3[Change Detection]
    end
    
    subgraph "Reporting Phase"
        J --> J1[HTML Report]
        J --> J2[Side-by-side Views]
        J --> J3[Summary Metrics]
    end
    
    style B fill:#e1f5fe
    style G fill:#e8f5e8
    style H fill:#fff3e0
    style I fill:#fce4ec
    style J fill:#f3e5f5
```

**Resource Flow**:
```
Test Request
     │
     ▼
┌─────────────────────────────────────────┐
│          Test Orchestrator              │
│         (500 tokens)                    │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │Regression│ │Browser  │ │Viewport │   │
│  │  Mode    │ │  Mode   │ │  Mode   │   │
│  └─────────┘ └─────────┘ └─────────┘   │
└─────────────────────────────────────────┘
     │
     ▼
┌─────────────────┐ → ┌─────────────────┐ → ┌─────────────────┐
│ Setup Specialist│   │Capture Controller│   │Comparison Engine│
│   (600 tokens) │   │   (700 tokens)  │   │   (600 tokens)  │
│                 │   │                 │   │                 │
│ • Tool install  │   │ • Screenshots   │   │ • Diff analysis │
│ • Configuration │   │ • Stabilization │   │ • Thresholds    │
│ • Environment   │   │ • Batch process │   │ • Change detect │
└─────────────────┘   └─────────────────┘   └─────────────────┘
                                              │
                                              ▼
                                    ┌─────────────────┐
                                    │Report Generator │
                                    │   (500 tokens)  │
                                    │                 │
                                    │ • HTML reports  │
                                    │ • Comparisons   │
                                    │ • Metrics       │
                                    └─────────────────┘
```

---

## Standard Multi-Agent Workflows

### 5. Legal Compliance Workflow
**Token Usage**: ~6k tokens  
**Architecture**: Sequential validation with parallel implementation

```mermaid
graph TD
    A[Legal Compliance Request] --> B[Legal Expert]
    
    B --> C[License Audit]
    B --> D[Privacy Review]
    B --> E[Security Compliance]
    
    C --> F[Implementation Planning]
    D --> F
    E --> F
    
    F --> G[Parallel Implementation]
    
    G --> H[Terms & Policies]
    G --> I[Privacy Controls]
    G --> J[Security Measures]
    
    H --> K[Documentation Package]
    I --> K
    J --> K
    
    subgraph "Audit Phase (2k tokens)"
        C --> C1[Dependency Scan]
        C --> C2[License Compatibility]
        C --> C3[Risk Assessment]
        
        D --> D1[GDPR Analysis]
        D --> D2[CCPA Compliance]
        D --> D3[Data Mapping]
        
        E --> E1[Security Controls]
        E --> E2[Encryption Review]
        E --> E3[Access Controls]
    end
    
    subgraph "Implementation Phase (3k tokens)"
        H --> H1[Terms of Service]
        H --> H2[Privacy Policy]
        
        I --> I1[Data Controls]
        I --> I2[User Rights]
        
        J --> J1[Technical Controls]
        J --> J2[Monitoring Setup]
    end
    
    style B fill:#fff8e1
    style F fill:#e8f5e8
    style K fill:#e3f2fd
```

### 6. Social Media Campaign Workflow  
**Token Usage**: ~5.5k tokens  
**Architecture**: Creative pipeline with legal validation

```mermaid
graph LR
    A[Campaign Brief] --> B[Marketing Expert]
    
    B --> C[Strategy Development]
    C --> D[Content Creation]
    D --> E[Visual Design]
    E --> F[Legal Review]
    F --> G[Performance Setup]
    G --> H[Campaign Package]
    
    subgraph "Strategy (1.5k tokens)"
        C --> C1[Audience Research]
        C --> C2[Platform Selection]
        C --> C3[Content Pillars]
        C --> C4[Success Metrics]
    end
    
    subgraph "Content (2k tokens)"
        D --> D1[Platform Copy]
        D --> D2[Hashtag Strategy]
        D --> D3[Call-to-Actions]
        D --> D4[Content Calendar]
    end
    
    subgraph "Design (1k tokens)"
        E --> E1[Graphics Creation]
        E --> E2[Brand Consistency]
        E --> E3[Template Library]
    end
    
    subgraph "Legal (500 tokens)"
        F --> F1[Compliance Check]
        F --> F2[Disclosure Review]
    end
    
    subgraph "Analytics (500 tokens)"
        G --> G1[Tracking Setup]
        G --> G2[Performance KPIs]
    end
    
    style B fill:#e1f5fe
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#fff8e1
    style G fill:#f3e5f5
```

---

## Development & Quality Workflows

### 7. Code Review Workflow
**Architecture**: Quality-focused analysis pipeline

```mermaid
graph TD
    A[Code Review Request] --> B[Senior Engineer]
    
    B --> C[Security Analysis]
    B --> D[Quality Assessment]
    B --> E[Performance Review]
    B --> F[Best Practices Check]
    
    C --> G[Consolidated Report]
    D --> G
    E --> G
    F --> G
    
    G --> H[Recommendations]
    H --> I[Implementation Plan]
    
    subgraph "Security Focus"
        C --> C1[Vulnerability Scan]
        C --> C2[Injection Patterns]
        C --> C3[Authentication Review]
        C --> C4[Data Protection]
    end
    
    subgraph "Quality Metrics"
        D --> D1[Complexity Analysis]
        D --> D2[Test Coverage]
        D --> D3[Code Duplication]
        D --> D4[Maintainability]
    end
    
    subgraph "Performance"
        E --> E1[Bottleneck Analysis]
        E --> E2[Resource Usage]
        E --> E3[Optimization Opportunities]
    end
    
    subgraph "Standards"
        F --> F1[Coding Standards]
        F --> F2[Documentation Quality]
        F --> F3[Error Handling]
    end
    
    style B fill:#e3f2fd
    style C fill:#ffebee
    style D fill:#e8f5e8
    style E fill:#fff3e0
    style F fill:#f3e5f5
```

### 8. Test Generation Workflow  
**Architecture**: Comprehensive test creation pipeline

```mermaid
graph LR
    A[Test Request] --> B[QA Engineer]
    
    B --> C[Code Analysis]
    C --> D[Test Case Identification]
    D --> E[Test Generation]
    E --> F[Coverage Validation]
    
    subgraph "Analysis Phase"
        C --> C1[Function Mapping]
        C --> C2[Edge Case Discovery]
        C --> C3[Dependency Analysis]
    end
    
    subgraph "Identification Phase"
        D --> D1[Unit Test Cases]
        D --> D2[Integration Scenarios]
        D --> D3[Error Conditions]
    end
    
    subgraph "Generation Phase"
        E --> E1[Test Code Creation]
        E --> E2[Mock Setup]
        E --> E3[Assertion Building]
    end
    
    subgraph "Validation Phase"
        F --> F1[Coverage Measurement]
        F --> F2[Quality Assessment]
        F --> F3[Gap Analysis]
    end
    
    style B fill:#e1f5fe
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#f3e5f5
```

---

## Planning & Analysis Workflows

### 9. Migration Planner Workflow
**Architecture**: Risk assessment and planning pipeline

```mermaid
graph TD
    A[Migration Request] --> B[Technical Analyst]
    
    B --> C[Current State Assessment]
    C --> D[Target State Definition]
    D --> E[Gap Analysis]
    E --> F[Risk Assessment]
    F --> G[Migration Roadmap]
    
    subgraph "Assessment (1k tokens)"
        C --> C1[System Architecture]
        C --> C2[Data Dependencies]
        C --> C3[Integration Points]
        C --> C4[Performance Baseline]
    end
    
    subgraph "Target Definition (800 tokens)"
        D --> D1[Technology Stack]
        D --> D2[Architecture Goals]
        D --> D3[Performance Targets]
        D --> D4[Success Criteria]
    end
    
    subgraph "Gap Analysis (1k tokens)"
        E --> E1[Feature Gaps]
        E --> E2[Technical Debt]
        E --> E3[Skill Requirements]
        E --> E4[Resource Needs]
    end
    
    subgraph "Risk Assessment (800 tokens)"
        F --> F1[Technical Risks]
        F --> F2[Business Risks]
        F --> F3[Mitigation Strategies]
    end
    
    subgraph "Roadmap (1.2k tokens)"
        G --> G1[Phase Planning]
        G --> G2[Timeline Estimation]
        G --> G3[Resource Allocation]
        G --> G4[Milestone Definition]
    end
    
    style B fill:#e3f2fd
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#ffebee
    style G fill:#f3e5f5
```

### 10. API Designer Workflow
**Architecture**: Specification-driven design process

```mermaid
graph LR
    A[API Requirements] --> B[Backend Engineer]
    
    B --> C[Requirements Analysis]
    C --> D[Schema Design]
    D --> E[Endpoint Definition]
    E --> F[Security Design]
    F --> G[Documentation]
    
    subgraph "Analysis"
        C --> C1[Use Case Mapping]
        C --> C2[Data Flow Analysis]
        C --> C3[Performance Requirements]
    end
    
    subgraph "Schema"
        D --> D1[Data Models]
        D --> D2[Validation Rules]
        D --> D3[Relationship Mapping]
    end
    
    subgraph "Endpoints"
        E --> E1[REST Design]
        E --> E2[HTTP Methods]
        E --> E3[Response Formats]
    end
    
    subgraph "Security"
        F --> F1[Authentication]
        F --> F2[Authorization]
        F --> F3[Rate Limiting]
    end
    
    subgraph "Documentation"
        G --> G1[OpenAPI Spec]
        G --> G2[Usage Examples]
        G --> G3[Integration Guide]
    end
    
    style B fill:#e1f5fe
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#ffebee
    style G fill:#f3e5f5
```

---

## Infrastructure & Deployment Workflows

### 11. Containerization Workflow
**Architecture**: Progressive containerization approach

```mermaid
graph TD
    A[Application Analysis] --> B[Cloud Architect]
    
    B --> C[Environment Analysis]
    C --> D[Dockerfile Creation]
    D --> E[Docker Compose Setup]
    E --> F[Orchestration Planning]
    F --> G[Deployment Package]
    
    subgraph "Analysis Phase"
        C --> C1[Dependencies Mapping]
        C --> C2[Runtime Requirements]
        C --> C3[Configuration Needs]
        C --> C4[Data Persistence]
    end
    
    subgraph "Containerization"
        D --> D1[Base Image Selection]
        D --> D2[Layer Optimization]
        D --> D3[Security Hardening]
        D --> D4[Multi-stage Build]
    end
    
    subgraph "Composition"
        E --> E1[Service Definition]
        E --> E2[Network Configuration]
        E --> E3[Volume Management]
        E --> E4[Environment Variables]
    end
    
    subgraph "Orchestration"
        F --> F1[Kubernetes Manifests]
        F --> F2[Helm Charts]
        F --> F3[CI/CD Integration]
        F --> F4[Monitoring Setup]
    end
    
    style B fill:#e3f2fd
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#f3e5f5
    style G fill:#e1f5fe
```

### 12. Monitoring Setup Workflow
**Architecture**: Comprehensive observability implementation

```mermaid
graph LR
    A[Monitoring Requirements] --> B[Cloud Architect]
    
    B --> C[Metrics Planning]
    C --> D[Logging Strategy]
    D --> E[Alerting Design]
    E --> F[Dashboard Creation]
    
    subgraph "Metrics (1k tokens)"
        C --> C1[Application Metrics]
        C --> C2[Infrastructure Metrics]
        C --> C3[Business Metrics]
        C --> C4[Custom Metrics]
    end
    
    subgraph "Logging (800 tokens)"
        D --> D1[Log Aggregation]
        D --> D2[Structured Logging]
        D --> D3[Log Retention]
        D --> D4[Search & Analysis]
    end
    
    subgraph "Alerting (600 tokens)"
        E --> E1[Threshold Definition]
        E --> E2[Notification Channels]
        E --> E3[Escalation Rules]
        E --> E4[Alert Fatigue Prevention]
    end
    
    subgraph "Dashboards (800 tokens)"
        F --> F1[Executive Dashboards]
        F --> F2[Operational Views]
        F --> F3[Developer Metrics]
        F --> F4[Real-time Monitoring]
    end
    
    style B fill:#e1f5fe
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#f3e5f5
```

---

## Architecture Patterns

### Hierarchical vs Parallel Execution

#### Before Optimization (Parallel)
```
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│ Agent 1 │  │ Agent 2 │  │ Agent 3 │  │ Agent 4 │  │ Agent 5 │
│  5k tok │  │  5k tok │  │  5k tok │  │  5k tok │  │  5k tok │
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
     │            │            │            │            │
     └────────────┼────────────┼────────────┼────────────┘
                  │            │            │
                  ▼            ▼            ▼
              ┌─────────────────────────────────┐
              │        Compilation Agent        │
              │          2k tokens              │
              └─────────────────────────────────┘

Total: 27k tokens (25k + 2k compilation)
```

#### After Optimization (Hierarchical)
```
         ┌─────────────────┐
         │  Orchestrator   │ ← 1k tokens
         │   Agent         │
         └─────────────────┘
                 │
                 ▼
         ┌─────────────────┐
         │   Specialist    │ ← 3k tokens
         │   Agent 1       │
         └─────────────────┘
                 │
                 ▼
         ┌─────────────────┐
         │   Specialist    │ ← 2k tokens
         │   Agent 2       │
         └─────────────────┘
                 │
                 ▼
         ┌─────────────────┐
         │   Specialist    │ ← 2k tokens
         │   Agent 3       │
         └─────────────────┘

Total: 8k tokens (70% reduction)
```

### Progressive Enhancement Pattern

```mermaid
graph LR
    A[Base Request] --> B{Enhancement Level}
    
    B -->|Quick| C[Base Response - 1k tokens]
    B -->|Detailed| D[Enhanced Response - 3k tokens]
    B -->|Comprehensive| E[Full Response - 5k tokens]
    
    C --> F[User Satisfaction Check]
    D --> F
    E --> F
    
    F -->|Need More| G[Add Enhancement Layer]
    F -->|Satisfied| H[Complete]
    
    G --> I[Additional Analysis - +2k tokens]
    I --> F
    
    style A fill:#e1f5fe
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style H fill:#f3e5f5
```

### Context Layering Strategy

```
┌─────────────────────────────────────────────┐
│                Core Layer                   │ ← Always included (500 tokens)
│  • Project basics • Current task • Goals   │
├─────────────────────────────────────────────┤
│              Context Layer                  │ ← Added when needed (1k tokens)
│  • Code context • Standards • History      │
├─────────────────────────────────────────────┤
│              Detail Layer                   │ ← Full analysis only (2k tokens)
│  • Detailed specs • Examples • References  │
├─────────────────────────────────────────────┤
│              Archive Layer                  │ ← Specialized tasks (3k tokens)
│  • Full documentation • Legacy code        │
└─────────────────────────────────────────────┘

Smart Loading:
• Quick tasks: Core only (500 tokens)
• Standard tasks: Core + Context (1.5k tokens)
• Complex tasks: Core + Context + Detail (3.5k tokens)
• Comprehensive: All layers (6.5k tokens vs 15k original)
```

---

## Token Optimization Summary

### Before vs After Comparison

| Workflow Type | Original Tokens | Optimized Tokens | Reduction | Method |
|---------------|-----------------|------------------|-----------|---------|
| **Documentation Update** | 20,000 | 12,000 | 40% | Hierarchical |
| **CSS Safety Check** | 3,500 | 2,100 | 40% | Sequential |
| **Visual Testing** | 4,000 | 2,400 | 40% | Staged |
| **Start Workflow** | N/A (new) | 3,000-5,000 | N/A | Optimized design |
| **Legal Compliance** | 8,000 | 6,000 | 25% | Parallel → Sequential |
| **Social Media** | 7,000 | 5,500 | 21% | Pipeline optimization |

### Architecture Benefits

```
Parallel Architecture Issues:
❌ Context duplication across agents
❌ Redundant analysis 
❌ Complex coordination overhead
❌ Higher token usage
❌ Difficult to debug

Hierarchical Architecture Benefits:
✅ Minimal context passing
✅ Specialized agent roles
✅ Clear execution flow
✅ Significant token savings
✅ Easier maintenance
```

This visual documentation provides clear understanding of how each workflow operates, the token savings achieved through optimization, and the architectural patterns that make them efficient.