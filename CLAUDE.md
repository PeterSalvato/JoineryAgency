# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Mockup-to-Site AI Agency** - An AI-powered design consultancy staffed with specialized agents that transform design mockups into professional, production-ready websites. Each agent embodies proven expert methodologies from industry leaders to provide domain-specific consultation and guidance.

## Architecture & Structure

### Agent System
- **28 specialized AI agents** organized by domain expertise
- **Consultation model** - agents provide focused advice when specifically requested
- **Expert methodologies** - each agent based on proven practitioners (Chris Do, Don Norman, etc.)
- **Stateless design** - agents are persona-based consultants, not persistent systems

### Directory Structure
- `/agents/` - 28 specialist agent definitions with proven methodologies
- `/production/` - Production department with manager and 6 production agents
- `/docs/` - System documentation and implementation guides
- `/research/` - Research materials and planning documents
- `/sessions/` - Session persistence and planning continuity

### Agent Categories
1. **Business Strategy & Sales** (8 agents) - Sales, pricing, proposals, client management
2. **Design & Visual** (6 agents) - Visual design, branding, photography, illustration
3. **Technical & Architecture** (5 agents) - Frontend, responsive design, performance, accessibility
4. **Content & Communication** (5 agents) - Copywriting, content strategy, marketing
5. **Analysis & Operations** (4 agents) - User research, competitive analysis, project management

## Development Status

**Current Phase**: Complete consultation and production system operational
**Consultation Layer**: 28 specialist agents providing expert methodologies
**Production Department**: 6 production agents executing recommendations through coordinated workflows

## Key Expert Methodologies

### Chris Do (The Futur)
- **Agents**: sales-specialist, proposal-specialist, client-discovery-specialist  
- **Focus**: Value-based selling, client psychology, business strategy

### Don Norman (Human-Centered Design)
- **Agents**: ux-interaction-specialist
- **Focus**: Usability principles, cognitive psychology, accessibility

### Becca Luna (Menu-Based Pricing)
- **Agents**: pricing-strategist
- **Focus**: Service packaging, pricing psychology, conversion optimization

### Paula Scher (Pentagram)
- **Agents**: brand-designer
- **Focus**: Visual identity systems, brand development

### Massimo Vignelli (Systematic Design)
- **Agents**: visual-design-specialist
- **Focus**: Typography, grid systems, mathematical proportions

## MCP Integration

This project integrates with Model Context Protocol (MCP) servers to enhance agent capabilities:

### Available MCP Tools
- **@playwright/mcp** - Real-time design validation and interactive testing
- **@upstash/context7-mcp** - Project memory and session continuity  
- **sourcegraph-mcp-server** - Code intelligence and pattern analysis
- **@modelcontextprotocol/server-sequential-thinking** - Multi-step problem solving
- **sequential-thinking-mcp** - Adaptive reasoning and complex analysis

### MCP Setup
```bash
# Install globally
npm install -g @playwright/mcp @upstash/context7-mcp sourcegraph-mcp-server
npm install -g @modelcontextprotocol/server-sequential-thinking sequential-thinking-mcp

# Verify installation
npm list -g --depth=0 | grep -E "(playwright|context7|sourcegraph|sequential|thinking)"
```

## Usage Guidelines

### Consultation and Production Workflow
1. **Consultation Phase**
   - User identifies specific challenge or domain expertise required
   - Select appropriate specialist consultant agent
   - Agent provides actionable advice using proven methodology
2. **Production Phase** 
   - User requests production implementation of consultant recommendations
   - Production Manager receives request and routes to appropriate production agents
   - Production agents execute tasks with standardized YAML interfaces
3. **Delivery**
   - Production system delivers complete implementation from code to deployment
   - Quality assurance and performance optimization included

### How to Request Services

#### Consultation Requests
- Be specific about the challenge or domain you need guidance on
- Request individual specialists rather than multiple agents at once
- Implement recommendations selectively based on your specific context
- Follow up with additional specialists as needed for complex projects

#### Production Requests
- Provide consultant recommendations or detailed specifications
- Production Manager automatically routes to appropriate production agents
- System handles multi-agent coordination and standardized interfaces
- Expect complete deliverables from concept to deployment

### Agent Selection Examples
- **Pricing challenges**: pricing-strategist (Becca Luna methodology)
- **Sales issues**: sales-specialist (Chris Do methodology) 
- **Design problems**: visual-design-specialist (Massimo Vignelli approach)
- **UX concerns**: ux-interaction-specialist (Don Norman principles)
- **Brand development**: brand-strategist or brand-designer
- **Technical architecture**: frontend-architecture-specialist

## Agent File Structure

Each agent file includes:
- **Overview**: Agent purpose and methodology basis
- **Triggers**: When to consult this specialist
- **Core Expertise**: Key knowledge areas and capabilities
- **Use When**: Specific scenarios and example requests
- **Methodology**: Underlying framework and approach
- **Key Frameworks**: Specific tools and techniques

## Development Principles

### Agent Development
- Base agents on proven expert methodologies, not generic AI advice
- Define clear triggers and use cases for each specialist
- Maintain focus on specific domain expertise
- Test with real consultation scenarios

### Planning & Session Continuity
- **CRITICAL**: When planning or strategy sessions begin, immediately document the context in `CURRENT_PLANNING.md`
- Update planning documentation continuously throughout the session
- Always read existing planning files at session start to maintain continuity
- Document decisions, next steps, and current state to prevent loss of progress
- Use git commits to preserve planning milestones and major decisions

### Quality Standards
- Professional consultation quality in all agent responses
- Actionable, specific recommendations based on established frameworks
- Clear delineation between different specialist domains
- Consistency with expert methodologies and approaches

## Future Roadmap

### Phase 1: Consultation System (Complete)
- ✅ 28 specialist agent definitions with expert methodologies
- ✅ On-demand consultation model established
- ✅ MCP integration for enhanced capabilities

### Phase 2: Production System (Complete)
- ✅ Production Manager with task routing and coordination
- ✅ 6 specialized production agents with standardized interfaces
- ✅ End-to-end workflow from consultation to deployment
- ✅ Quality assurance and performance optimization

### Phase 3: System Integration (Complete)
- ✅ Seamless mockup-to-site pipeline operational
- ✅ Multi-agent coordination for complex projects
- ✅ Professional output standards automation
- ✅ Complete consultation and execution system

### Future Enhancements
- Advanced image processing for mockup analysis
- Real-time design validation and testing
- Enhanced AI capabilities integration
- Expanded service offerings and specializations

## Implementation Notes

This is a **complete AI-powered design consultancy** combining consultation and execution capabilities. The system provides expert domain knowledge through specialized consultant agents, then executes recommendations through a coordinated production department.

### System Architecture
- **Consultation Layer**: 28 specialist agents provide expert methodologies and strategic guidance
- **Production Layer**: Production Manager coordinates 6 production agents for execution
- **Integration**: Standardized YAML interfaces ensure seamless consultant-to-production workflows

When working with this system, prioritize:
1. Clear identification of domain expertise needed for consultation
2. Selection of appropriate specialist agents for advice
3. Production requests with detailed specifications or consultant recommendations
4. Quality assurance through standardized production processes