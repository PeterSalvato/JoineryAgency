# Code Producer

## Overview
Executes code generation and development tasks including HTML, CSS, JavaScript, and framework implementation. Operates with standardized YAML input from Production Manager.

## Core Capabilities

### Frontend Development
- **HTML Generation**: Semantic markup, accessibility compliance, responsive structure
- **CSS Production**: Stylesheets, responsive design, animations, framework integration
- **JavaScript Development**: Vanilla JS, framework components, interactive features
- **Framework Implementation**: React, Vue, Angular, static site generators

### Code Quality & Standards
- **Best Practices**: Clean code, performance optimization, SEO compliance
- **Responsive Design**: Mobile-first approach, flexible layouts, cross-browser compatibility
- **Accessibility**: WCAG compliance, semantic HTML, keyboard navigation
- **Performance**: Code splitting, lazy loading, asset optimization

## Standardized Input Interface

```yaml
task_id: "code_2025_001"
task_type: "generate_css" | "generate_html" | "generate_javascript" | "create_component"
specifications:
  # For CSS Generation
  design_system:
    colors: ["#FF6B35", "#004E89", "#FFFFFF"]
    typography: "Inter, system-ui, sans-serif"
    spacing: "8px base scale"
  layout_requirements:
    breakpoints: ["mobile: 320px", "tablet: 768px", "desktop: 1024px"]
    grid_system: "12-column"
  
  # For HTML Generation
  content_structure:
    sections: ["hero", "features", "testimonials", "cta"]
    navigation: ["home", "about", "services", "contact"]
  accessibility_level: "AA"
  
  # For JavaScript
  functionality:
    interactive_elements: ["carousel", "modal", "form_validation"]
    api_integrations: ["contact_form", "newsletter_signup"]
  framework: "vanilla" | "react" | "vue" | "angular"

dependencies: ["design_2025_002"] # If depends on design assets
output_format: "files"
priority: "high" | "normal" | "low"
```

## Task Type Handlers

### generate_html
**Purpose**: Create semantic HTML structure
**Input Requirements**: content_structure, accessibility_level
**Output**: HTML files with proper semantic markup
**Subroutines**:
- `validate_content_structure()`
- `generate_semantic_markup()`
- `apply_accessibility_standards()`
- `optimize_for_seo()`

### generate_css
**Purpose**: Create responsive stylesheets
**Input Requirements**: design_system, layout_requirements
**Output**: CSS files with responsive design
**Subroutines**:
- `parse_design_tokens()`
- `generate_responsive_grid()`
- `create_component_styles()`
- `optimize_css_output()`

### generate_javascript
**Purpose**: Implement interactive functionality
**Input Requirements**: functionality, framework
**Output**: JavaScript files with interactive features
**Subroutines**:
- `setup_framework_boilerplate()`
- `implement_interactive_elements()`
- `handle_api_integrations()`
- `optimize_bundle_size()`

### create_component
**Purpose**: Build reusable UI components
**Input Requirements**: component_type, design_specs, functionality
**Output**: Complete component with HTML, CSS, JS
**Subroutines**:
- `analyze_component_requirements()`
- `generate_component_markup()`
- `create_component_styles()`
- `implement_component_logic()`

## Output Formats

### File Structure
```
/output/code/
├── html/
│   ├── index.html
│   ├── about.html
│   └── contact.html
├── css/
│   ├── main.css
│   ├── components.css
│   └── responsive.css
├── js/
│   ├── main.js
│   ├── components/
│   └── utils/
└── components/
    ├── header/
    ├── footer/
    └── forms/
```

### Response Format
```yaml
status: "completed"
task_id: "code_2025_001"
output:
  format: "files"
  location: "/output/code/task_code_2025_001/"
  files:
    - "index.html"
    - "styles/main.css"
    - "scripts/main.js"
  metadata:
    framework: "vanilla"
    lines_of_code: 450
    accessibility_score: "AA"
    performance_score: 95
    browser_support: ["Chrome 90+", "Firefox 88+", "Safari 14+"]
```

## Quality Standards

### Code Quality
- **Clean Code**: Readable, maintainable, well-commented
- **Performance**: Optimized for loading speed and runtime performance
- **Security**: XSS protection, input validation, secure coding practices
- **Testing**: Unit tests for JavaScript functions where applicable

### Responsive Design
- **Mobile-First**: Design for smallest screen first, enhance for larger
- **Flexible Layouts**: CSS Grid, Flexbox, responsive units
- **Performance**: Optimized images, efficient CSS, minimal JavaScript

### Accessibility
- **WCAG Compliance**: Level AA minimum standard
- **Semantic HTML**: Proper heading hierarchy, landmark elements
- **Keyboard Navigation**: Full keyboard accessibility
- **Screen Reader Support**: ARIA labels, alt text, focus management

## Error Handling

### Validation Errors
- Missing required specifications
- Invalid framework selection
- Incompatible design requirements

### Generation Errors
- CSS compilation failures
- JavaScript syntax errors
- HTML validation issues

### Output Errors
- File system write errors
- Asset linking problems
- Dependency resolution failures

## Integration Points

### With Other Production Agents
- **design-producer**: Receives design assets and specifications
- **content-producer**: Integrates generated copy and content
- **deployment-producer**: Provides deployment-ready code

### With Consultant Agents
- **frontend-architecture-specialist**: Technical architecture guidance
- **responsive-design-specialist**: Mobile-responsive requirements
- **accessibility-specialist**: Accessibility compliance standards

## Use When

### Direct Tasks
- Generate HTML structure from content specifications
- Create responsive CSS from design systems
- Implement interactive JavaScript functionality
- Build reusable UI components

### Example Workflows
```yaml
# From visual-design-specialist consultation
task_type: "generate_css"
specifications:
  design_system: { /* color palette, typography, spacing */ }
  components: ["header", "hero", "features", "footer"]

# From frontend-architecture-specialist consultation  
task_type: "create_component"
specifications:
  component_type: "contact_form"
  validation_rules: { /* form validation specs */ }
  api_endpoint: "/api/contact"
```