# System Overview

## Architecture Vision
The Mockup-to-Site AI Agency is a complete design consultancy system that transforms design concepts into production-ready websites through specialized AI agents working in coordination.

## Two-Layer Architecture

### Layer 1: Consultation System
**28 Specialist Consultant Agents** provide expert domain knowledge across:

#### Business Strategy & Sales (8 agents)
- sales-specialist, proposal-specialist, client-discovery-specialist
- pricing-strategist, negotiation-specialist, client-relationship-manager
- business-development-specialist, revenue-optimization-specialist

#### Design & Visual (6 agents)  
- visual-design-specialist, brand-designer, brand-strategist
- photographer, illustrator, graphic-designer

#### Technical & Architecture (5 agents)
- frontend-architecture-specialist, responsive-design-specialist
- performance-specialist, accessibility-specialist, technical-infrastructure-specialist

#### Content & Communication (5 agents)
- copywriting-specialist, content-strategy-specialist, seo-specialist
- social-media-specialist, email-marketing-specialist

#### Analysis & Operations (4 agents)
- market-research-specialist, competitive-analyst, user-research-specialist
- project-manager

### Layer 2: Production Department
**Production Manager + 6 Production Agents** execute consultant recommendations:

- **Production Manager**: Central coordination, task routing, workflow management
- **code-producer**: HTML, CSS, JavaScript, framework implementation
- **design-producer**: Mockups, assets, visual elements, brand materials
- **content-producer**: Copy, documentation, marketing materials
- **data-producer**: Research, analysis, reporting, insights
- **deployment-producer**: Hosting, CI/CD, domains, infrastructure
- **integration-producer**: APIs, databases, third-party services

## Information Flow

```
Client Request
      ↓
Consultant Agent(s) ← Domain Expertise & Methodologies
      ↓
Recommendations/Specifications
      ↓
Production Manager ← Task Routing & Coordination
      ↓
Production Agents ← Standardized YAML Interfaces
      ↓
Deliverables ← Quality Assurance & Integration
      ↓
Client Delivery
```

## Key Design Principles

### Separation of Concerns
- **Consultants**: Provide expert advice, strategic thinking, proven methodologies
- **Production**: Execute tasks, handle tools, create deliverables
- **Coordination**: Production Manager handles routing, dependencies, quality

### Standardized Interfaces
- All production agents accept identical YAML task format
- Consistent input/output protocols across all agents
- Error handling and status reporting uniformity

### Expert Methodologies
Each consultant agent embodies proven methodologies from industry leaders:
- **Chris Do (The Futur)**: Value-based selling, business strategy
- **Don Norman**: Human-centered design, usability principles  
- **Becca Luna**: Menu-based pricing, service packaging
- **Paula Scher**: Visual identity systems, brand development
- **Massimo Vignelli**: Systematic design, typography

### Scalability & Modularity
- Stateless production agents enable horizontal scaling
- Function-like behavior with modular routines and subroutines
- Independent agent development and testing
- Composable workflows for complex projects

## Quality Assurance Framework

### Input Validation
- Consultant recommendations validated for completeness
- Production task specifications checked for accuracy
- Dependencies verified before execution

### Process Standards
- Standardized YAML task format ensures consistency
- Production Manager coordinates multi-agent workflows  
- Error handling and retry mechanisms built-in

### Output Quality
- Performance optimization (Core Web Vitals, loading speed)
- Accessibility compliance (WCAG AA standards)
- Security best practices (SSL, input validation, secure headers)
- Cross-browser compatibility and responsive design

## Integration Capabilities

### MCP (Model Context Protocol) Integration
- **@playwright/mcp**: Real-time design validation and testing
- **@upstash/context7-mcp**: Project memory and session continuity
- **sourcegraph-mcp-server**: Code intelligence and pattern analysis
- **sequential-thinking-mcp**: Multi-step problem solving and analysis

### External Service Integration
- **Payment Processing**: Stripe, PayPal, Square
- **Email & Communication**: Mailchimp, SendGrid, Twilio
- **Analytics**: Google Analytics, Mixpanel, Hotjar
- **Hosting & Deployment**: Netlify, Vercel, AWS, DigitalOcean
- **Version Control**: GitHub, GitLab integration with CI/CD

## Operational Model

### Session Persistence
- `CURRENT_PLANNING.md` maintains state between sessions
- Git-based persistence ensures planning continuity
- Active planning documentation prevents context loss

### Documentation Standards
- Self-documenting agent definitions with clear triggers and use cases
- Comprehensive production workflows with examples
- Quality standards and best practices documentation
- Test scenarios and validation procedures

### Continuous Improvement
- Agent methodologies based on proven industry practices
- Production processes refined through practical implementation
- Quality standards updated based on performance metrics
- System architecture evolved based on operational feedback

## Success Metrics

### Consultation Quality
- Expert-level advice based on proven methodologies  
- Clear, actionable recommendations
- Appropriate agent selection for challenges
- Strategic thinking and business value focus

### Production Efficiency  
- Fast task routing and execution coordination
- High-quality deliverables meeting standards
- Successful multi-agent workflow coordination
- Complete end-to-end project delivery

### System Reliability
- Consistent standardized interfaces across all agents
- Robust error handling and recovery mechanisms
- Quality assurance validation at each stage
- Scalable architecture supporting growth