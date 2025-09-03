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
- `/docs/` - System documentation and implementation guides
- `/research/` - Research materials and planning documents

### Agent Categories
1. **Business Strategy & Sales** (8 agents) - Sales, pricing, proposals, client management
2. **Design & Visual** (6 agents) - Visual design, branding, photography, illustration
3. **Technical & Architecture** (5 agents) - Frontend, responsive design, performance, accessibility
4. **Content & Communication** (5 agents) - Copywriting, content strategy, marketing
5. **Analysis & Operations** (4 agents) - User research, competitive analysis, project management

## Development Status

**Current Phase**: Persona-based consultation using expert methodologies
**Future**: Enhanced with genuine capabilities (image processing, code generation, validation tools)

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

### Agent Consultation Model
1. **User identifies need** - Specific challenge or domain expertise required
2. **Agent selection** - Choose the most relevant specialist for the challenge
3. **Focused consultation** - Agent provides actionable advice using proven methodology
4. **User implementation** - User decides which recommendations to apply
5. **Follow-up available** - Additional specialists can be consulted as needed

### How to Request Agent Consultation
- Be specific about the challenge or domain you need guidance on
- Request individual specialists rather than multiple agents at once
- Implement recommendations selectively based on your specific context
- Follow up with additional specialists as needed for complex projects

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

### Quality Standards
- Professional consultation quality in all agent responses
- Actionable, specific recommendations based on established frameworks
- Clear delineation between different specialist domains
- Consistency with expert methodologies and approaches

## Future Roadmap

### Phase 1: Persona Consultation (Current)
- ✅ 28 specialist agent definitions complete
- ✅ On-demand consultation model established
- ✅ MCP integration for enhanced capabilities

### Phase 2: Enhanced Capabilities
- Image processing for mockup analysis
- Code generation capabilities  
- Real-time validation tools
- Automated quality assurance

### Phase 3: Integration
- Seamless mockup-to-site pipeline
- Multi-agent coordination for complex projects
- Professional output standards automation

## Implementation Notes

This is a **consultation-based AI agency**, not a code generation system. The focus is on providing expert domain knowledge and strategic guidance through specialized agent personas, enhanced with MCP capabilities for deeper analysis and systematic thinking.

When working with this system, prioritize:
1. Clear identification of domain expertise needed
2. Selection of appropriate specialist agents
3. Implementation of proven methodologies
4. User-directed decision making on recommendations