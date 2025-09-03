# MCP Setup Guide

*Instructions for setting up Model Context Protocol servers for the design consultancy AI agent ecosystem.*

## **🛠️ MCP Dependencies**

This project uses three MCP servers installed globally to enhance AI agent capabilities:

### **Required Global Installations**
```bash
# Install all MCP servers globally
npm install -g @playwright/mcp@^0.0.36
npm install -g @upstash/context7-mcp@^1.0.16  
npm install -g sourcegraph-mcp-server@^1.4.2
```

### **Verification Commands**
```bash
# Verify installations
npm list -g --depth=0 | grep -E "(playwright|context7|sourcegraph)"

# Expected output:
# ├── @playwright/mcp@0.0.36
# ├── @upstash/context7-mcp@1.0.16
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
npm install -g @playwright/mcp @upstash/context7-mcp sourcegraph-mcp-server
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

## **🔧 Troubleshooting**

### **MCP Tools Not Found**
```bash
# Reinstall globally
npm install -g @playwright/mcp @upstash/context7-mcp sourcegraph-mcp-server

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
npm update -g @playwright/mcp @upstash/context7-mcp sourcegraph-mcp-server
```

## **📊 Integration Status**

| Tool | Status | Agents Using | Primary Benefit |
|------|--------|--------------|-----------------|
| **Playwright MCP** | ✅ Installed | 6 agents | Real-time validation |
| **Context7 MCP** | ✅ Installed | 5 agents | Project continuity |  
| **Sourcegraph MCP** | ✅ Installed | 5 agents | Code intelligence |

**Total Enhanced Agents**: 14 of 24 agents have MCP integration guidance

---

*This setup enables world-class AI consultancy capabilities with memory, intelligence, and interactive testing.*