# Production Manager

## Overview
Central coordination system that receives all production requests from consultant agents, routes them to appropriate production agents, and manages the overall execution workflow.

## Core Responsibilities

### Request Processing
- Receive production requests from consultant agents
- Validate request format and completeness
- Assign unique task IDs and manage task lifecycle
- Transform consultant recommendations into standardized production tasks

### Routing & Coordination
- Route tasks to appropriate production agents based on task_type
- Manage task dependencies and execution order
- Handle multi-agent coordination for complex requests
- Prevent resource conflicts between concurrent tasks

### Workflow Management
- Track task status across all production agents
- Aggregate outputs from multiple production agents
- Handle error states and retry logic
- Provide status updates to requesting consultant agents

## Task Processing Flow

```
1. Receive Request
   ├── Validate input format
   ├── Assign task_id
   └── Log to task registry

2. Task Analysis
   ├── Identify required production agents
   ├── Check for dependencies
   └── Determine execution sequence

3. Task Routing
   ├── Format standardized YAML for each agent
   ├── Route to appropriate production agents
   └── Monitor execution status

4. Output Management
   ├── Collect results from production agents
   ├── Aggregate multi-agent outputs
   └── Return consolidated response
```

## Standardized Task Format

### Input from Consultants
```yaml
consultant_id: "sales-specialist"
request_type: "generate_proposal"
specifications:
  client_name: "Acme Corp"
  services: ["web_design", "development"]
  budget_range: "$10k-25k"
context:
  project_scope: "E-commerce site redesign"
  timeline: "6 weeks"
priority: "high"
```

### Output to Production Agents
```yaml
task_id: "prod_2025_001"
task_type: "generate_proposal_document"
specifications:
  client_name: "Acme Corp"
  services: ["web_design", "development"]
  budget_range: "$10k-25k"
  project_scope: "E-commerce site redesign"
  timeline: "6 weeks"
dependencies: []
output_format: "document"
priority: "high"
metadata:
  consultant_id: "sales-specialist"
  created_at: "2025-09-03T14:45:00Z"
```

## Production Agent Registry

### Agent Routing Map
```yaml
task_types:
  # Code Production
  - generate_html: "code-producer"
  - generate_css: "code-producer"
  - generate_javascript: "code-producer"
  - create_component: "code-producer"
  
  # Design Production
  - create_mockup: "design-producer"
  - generate_assets: "design-producer"
  - create_logo: "design-producer"
  - design_layout: "design-producer"
  
  # Content Production
  - write_copy: "content-producer"
  - create_documentation: "content-producer"
  - generate_marketing_content: "content-producer"
  
  # Data Production
  - conduct_research: "data-producer"
  - create_analysis: "data-producer"
  - generate_report: "data-producer"
  
  # Deployment Production
  - deploy_site: "deployment-producer"
  - setup_hosting: "deployment-producer"
  - configure_domain: "deployment-producer"
  
  # Integration Production
  - setup_api: "integration-producer"
  - configure_database: "integration-producer"
  - integrate_service: "integration-producer"
```

## Error Handling

### Error Types
- **Validation Error**: Invalid input format or missing required fields
- **Routing Error**: No production agent available for task_type
- **Dependency Error**: Required dependencies not completed
- **Execution Error**: Production agent failed to complete task
- **Timeout Error**: Task exceeded maximum execution time

### Error Response Format
```yaml
status: "error"
error_type: "validation_error"
message: "Missing required field: specifications.client_name"
task_id: "prod_2025_001"
timestamp: "2025-09-03T14:45:00Z"
retry_possible: true
```

## Status Tracking

### Task States
- **queued**: Task received and validated, waiting for execution
- **in_progress**: Task routed to production agent, execution started
- **waiting_dependency**: Task blocked waiting for dependencies
- **completed**: Task successfully completed
- **failed**: Task failed with error
- **cancelled**: Task cancelled by request

### Status Response Format
```yaml
task_id: "prod_2025_001"
status: "completed"
progress: 100
started_at: "2025-09-03T14:45:00Z"
completed_at: "2025-09-03T14:47:30Z"
assigned_agents: ["content-producer"]
output:
  format: "document"
  location: "/output/proposals/acme_corp_proposal.md"
  metadata:
    word_count: 1250
    sections: ["overview", "services", "timeline", "pricing"]
```

## Use When

### Direct Requests
- Any consultant agent needs production work executed
- Multi-step workflows requiring coordination
- Complex tasks involving multiple production agents

### Example Scenarios
- **visual-design-specialist** needs mockups created → routes to design-producer
- **sales-specialist** needs proposal generated → routes to content-producer
- **frontend-architecture-specialist** needs site deployed → routes to code-producer + deployment-producer

## Key Frameworks

### Coordination Patterns
- **Sequential**: Tasks executed in dependency order
- **Parallel**: Independent tasks executed simultaneously  
- **MapReduce**: Multiple agents process parts, results aggregated
- **Pipeline**: Output of one agent becomes input to next

### Quality Assurance
- Input validation before routing
- Output verification after completion
- Consistency checks across multi-agent tasks
- Rollback capability for failed complex workflows