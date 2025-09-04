# Internal Partner Dashboard Planning

**Session Date**: September 4, 2025  
**Context**: Planning internal dashboard for 2-partner agency operations  
**Status**: Initial requirements gathering - on hold for further discussion

## Core Dashboard Requirements (First Principles)

### Primary Function
**Project visibility and time management for daily partner operations**

### Core Information Needs
- **Projects in motion** - what's currently active
- **Project stages** - where each project sits in the workflow
- **Upcoming deadlines** - what's due when
- **Deliverables** - what specific things need to be delivered
- **Calendar integration** - scheduling and time management
- **Individual project drill-down** - click through for detailed project views

## Dashboard Architecture (Two-Level)

### Level 1: Overview Dashboard
- **Gantt chart view** showing all active projects (partner specifically requested)
- **Project-level timelines** - each project as one bar
- **Both partners shown** - workload distribution and assignments visible
- **Upcoming deadlines** and milestones marked on timeline
- **Calendar integration** - meetings, deadlines, key dates

### Level 2: Individual Project View (Click-through)
- **Project-specific Gantt** with task-level breakdown
- **Project details** - timeline, deliverables, client info, notes
- **Project history** - completed work and next steps
- **Files/assets** - project resources and deliverables
- **Client communication** history and contact info

## Project Workflow Stages (Working Framework)

### Current Planning Stages
1. **Discovery** - Understanding client needs and requirements
2. **Strategy** - Planning and approach development
3. **Production** - Creating/building actual deliverables
4. **Delivery** - Client presentation and project completion

**Note**: These stages are flexible starting points to be refined as actual processes develop

## 3-Systems Integration Challenge

### Business Model Connection
**Core Insight**: Dashboard should reflect "systems of systems" business approach

### The Challenge: Systems + Phases Matrix
**3 Systems** (Core Business Model):
- **Design System** - visual design, branding, assets
- **UX System** - user experience, interactions, flows
- **Dev System** - development, implementation, deployment

**4 Phases** (Project Workflow):
- Discovery → Strategy → Production → Delivery

### Visualization Questions (Unresolved)
**Two-Dimensional Problem**: How to show both system progress AND phase progress

#### Visualization Options Considered

**Option 1: Stacked Bars**
- Each project = 3 stacked bars (one per system)
- Each bar divided into 4 phase segments
- Shows system progress within each phase

**Option 2: Grid View**  
- Each project = 3x4 grid (systems × phases)
- Progress/status shown in each grid cell
- More detailed but potentially complex

**Option 3: Nested Gantt**
- Project bar expands to show 3 system bars
- Each system bar shows its 4 phases
- Hierarchical drill-down approach

### Key Questions Needing Resolution
1. **Phase Consistency**: Do all three systems go through all four phases?
   - Does Design have Discovery/Strategy/Production/Delivery?
   - Does UX follow same phase progression?
   - Does Dev system align with same phases?

2. **Timing Relationships**: Do phases happen sequentially or overlap?
   - Can UX Discovery happen while Design is in Production?
   - When does Dev system start relative to Design/UX?
   - How do systems coordinate across phases?

3. **Progress Granularity**: How detailed should progress tracking be?
   - Simple status (Not Started/In Progress/Complete)?
   - Percentage completion within each system/phase?
   - Task-level tracking within each system?

4. **Partner Workflow**: How do partners interact with this complexity?
   - Which partner manages which systems?
   - How are system handoffs coordinated?
   - What approval gates exist between phases?

## Dashboard Benefits (Anticipated)

### Operational Advantages
- **Project Oversight**: Clear visibility of all active work
- **Deadline Management**: Visual timeline of upcoming deliverables
- **Partner Coordination**: Workload distribution and scheduling
- **Client Communication**: Project status ready for client updates
- **Capacity Planning**: See availability for new projects

### Business Model Alignment
- **3-Systems Visualization**: Dashboard reinforces core methodology
- **Integration Tracking**: Monitor how systems work together
- **Quality Control**: Ensure balanced progress across all systems
- **Client Value**: Demonstrate systematic approach in project management

## Implementation Considerations

### Technical Requirements
- **Gantt Chart Library**: Need robust timeline visualization component
- **Two-Level Navigation**: Overview + drill-down functionality
- **Calendar Integration**: Sync with existing calendar systems
- **Progress Tracking**: System for updating project/task status
- **Partner Access**: Authentication and role-based permissions

### User Experience Goals
- **Simple Overview**: Not overwhelming with too much detail
- **Quick Updates**: Easy status changes and progress tracking
- **Mobile Friendly**: Access dashboard from anywhere
- **Visual Clarity**: Information hierarchy that supports decision-making

### Future Considerations
- **AI Integration**: How might AI system tasks appear on dashboard?
- **Client Access**: Separate client portal vs. internal dashboard views
- **Reporting**: Business analytics and performance tracking
- **Scalability**: Support for growing project volume

## Current Status: ON HOLD

### Next Steps (When Resumed)
1. **Clarify Systems/Phases Relationship**: Define how 3 systems progress through 4 phases
2. **Choose Visualization Approach**: Select best option for showing systems + phases
3. **Partner Workflow Design**: Define how partners interact with dashboard daily
4. **Technical Specification**: Document specific features and requirements
5. **Prototype Development**: Create basic dashboard mockup for testing

### Key Decisions Needed
- **Phase Alignment**: Do all systems follow same phase progression?
- **Visual Complexity**: How much detail to show on overview vs. drill-down?
- **Update Workflow**: How do partners maintain project status?
- **Calendar Integration**: Which calendar system and what events?

---

**Session Status**: Requirements gathering complete, complex visualization questions identified  
**Next Phase**: Systems/phases relationship clarification with both partners  
**Key Challenge**: Balancing 3-systems business model with practical project timeline visualization