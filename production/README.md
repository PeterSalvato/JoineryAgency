# Production Department

The production department executes recommendations from the 28 consultant agents through a coordinated system.

## Architecture

- **Production Manager** (`/manager/`) - Routes and coordinates all production requests
- **6 Production Agents** (`/agents/`) - Execute tasks with standardized interfaces

## Flow

1. **Consultant Agents** → provide recommendations/specifications
2. **Production Manager** → receives requests, routes and coordinates
3. **Production Manager** → formats uniform input for production agents
4. **Production Agents** → receive standardized YAML input, execute tasks
5. **Production Manager** → aggregates outputs, handles sequencing

## Production Agents

- **code-producer** - HTML, CSS, JS, frameworks
- **design-producer** - Images, layouts, assets, visual elements
- **content-producer** - Copy, docs, marketing materials
- **data-producer** - Research, analysis, reports
- **deployment-producer** - Hosting, CI/CD, domains, infrastructure
- **integration-producer** - APIs, databases, third-party services

## Standardized Input Format

```yaml
task_id: "unique-identifier"
task_type: "generate_css" | "create_image" | "deploy_site" | etc
specifications: { /* task-specific details */ }
dependencies: [ /* other tasks this depends on */ ]
output_format: "files" | "data" | "deployment"
priority: "high" | "normal" | "low"
```