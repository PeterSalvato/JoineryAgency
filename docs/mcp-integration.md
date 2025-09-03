# MCP Setup Guide

*Instructions for setting up Model Context Protocol servers for the design consultancy AI agent ecosystem.*

## **🛠️ MCP Dependencies**

This project uses five MCP servers installed globally to enhance AI agent capabilities:

### **Required Global Installations**
```bash
# Install all MCP servers globally
npm install -g @playwright/mcp@^0.0.36
npm install -g @upstash/context7-mcp@^1.0.16  
npm install -g sourcegraph-mcp-server@^1.4.2
npm install -g @modelcontextprotocol/server-sequential-thinking@^2025.7.1
npm install -g sequential-thinking-mcp@^1.0.0
```

### **Verification Commands**
```bash
# Verify installations
npm list -g --depth=0 | grep -E "(playwright|context7|sourcegraph|sequential|thinking)"

# Expected output:
# ├── @modelcontextprotocol/server-sequential-thinking@2025.7.1
# ├── @playwright/mcp@0.0.36
# ├── @upstash/context7-mcp@1.0.16
# ├── sequential-thinking-mcp@1.0.0
# └── sourcegraph-mcp-server@1.4.2
```

## **📦 Why Global Installation?**

**MCP servers run independently** from the project and are shared across:
- Multiple projects and codespaces
- Different AI assistant sessions  
- Various development environments

**Local installation** would limit MCP capabilities to this project only.

## **🔄 New Environment Setup**

When setting up in a new codespace or environment:

### **1. Install Project Dependencies**
```bash
npm install  # Installs sass, playwright (local)
```

### **2. Install MCP Servers**  
```bash
npm install -g @playwright/mcp @upstash/context7-mcp sourcegraph-mcp-server @modelcontextprotocol/server-sequential-thinking sequential-thinking-mcp
```

### **3. Verify MCP Integration**
Check that agents can access MCP tools through their integrated guidance sections.

## **📋 MCP Server Details**

### **@playwright/mcp** - Interactive Browser Automation
- **Purpose**: Real-time design validation and cross-device testing
- **Used by**: UX, web design, user research, photography agents
- **Capabilities**: Live browser control, accessibility auditing, visual testing

### **@upstash/context7-mcp** - Project Memory & Continuity
- **Purpose**: Session continuity and project history tracking  
- **Used by**: Project management, client success, sales, discovery agents
- **Capabilities**: Context preservation, relationship history, decision tracking

### **sourcegraph-mcp-server** - Code Intelligence
- **Purpose**: Advanced code analysis and pattern discovery
- **Used by**: Architecture, design system, competitive analysis agents  
- **Capabilities**: Semantic search, pattern analysis, architectural insights

### **@modelcontextprotocol/server-sequential-thinking** - Multi-Step Problem Solving
- **Purpose**: Structured approach to complex problem solving and decision making
- **Used by**: All agents for systematic thinking and complex analysis
- **Capabilities**: Step-by-step reasoning, problem breakdown, solution planning

### **sequential-thinking-mcp** - Alternative Sequential Reasoning
- **Purpose**: Problem solving with branching thoughts and adaptive thinking
- **Used by**: Strategic agents for complex business decisions and analysis
- **Capabilities**: Branching thoughts, thought revision, reflective analysis

## **🔧 Troubleshooting**

### **MCP Tools Not Found**
```bash
# Reinstall globally
npm install -g @playwright/mcp @upstash/context7-mcp sourcegraph-mcp-server @modelcontextprotocol/server-sequential-thinking sequential-thinking-mcp

# Verify global installation path
npm root -g
```

### **Permission Issues**
```bash
# Fix npm global permissions (Linux/Mac)
sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
```

### **Version Updates**
```bash
# Update to latest versions
npm update -g @playwright/mcp @upstash/context7-mcp sourcegraph-mcp-server @modelcontextprotocol/server-sequential-thinking sequential-thinking-mcp
```

## **📊 Integration Status**

| Tool | Status | Agents Using | Primary Benefit |
|------|--------|--------------|-----------------|
| **Playwright MCP** | ✅ Installed | 6 agents | Real-time validation |
| **Context7 MCP** | ✅ Installed | 5 agents | Project continuity |  
| **Sourcegraph MCP** | ✅ Installed | 5 agents | Code intelligence |
| **Sequential Thinking (Official)** | ✅ Installed | All 28 agents | Multi-step reasoning |
| **Sequential Thinking (Alt)** | ✅ Installed | Strategic agents | Adaptive problem solving |

**Total Enhanced Agents**: All 28 agents now have access to systematic multi-step thinking capabilities

---

*This setup enables world-class AI consultancy capabilities with memory, intelligence, and interactive testing.*