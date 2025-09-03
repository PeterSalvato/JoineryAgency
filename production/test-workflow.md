# Production System Test Workflow

## Test Scenario: Homepage Creation
Testing the complete flow from consultant recommendation to production execution.

### 1. Consultant Input
```yaml
# From visual-design-specialist
consultant_id: "visual-design-specialist"
request_type: "create_homepage"
specifications:
  business_type: "web_design_agency"
  target_audience: "small_business_owners"
  brand_colors: ["#FF6B35", "#004E89", "#FFFFFF"]
  sections: ["hero", "services", "portfolio", "testimonials", "contact"]
  conversion_goal: "consultation_booking"
context:
  company_name: "Joinery Agency"
  unique_value_prop: "AI-powered design consultancy"
  preferred_style: "modern_professional"
priority: "high"
```

### 2. Production Manager Processing
```yaml
# Production Manager converts to standardized tasks

# Task 1: Content Creation
task_id: "content_001"
task_type: "write_copy"
specifications:
  content_type: "homepage"
  target_audience:
    demographics: "small_business_owners"
    pain_points: ["need_professional_website", "limited_budget", "time_constraints"]
  brand_voice:
    tone: "professional"
    personality: ["trustworthy", "innovative", "approachable"]
  sections: ["hero", "services", "portfolio", "testimonials", "contact"]
dependencies: []
output_format: "document"
priority: "high"

# Task 2: Design Creation  
task_id: "design_001"
task_type: "create_mockup"
specifications:
  page_type: "homepage"
  viewport_sizes: ["mobile", "tablet", "desktop"]
  content_sections:
    - type: "hero"
      content: "AI-Powered Design Consultancy"
      cta: "Book Consultation"
    - type: "services"
      items: 3
    - type: "portfolio"
      items: 6
    - type: "testimonials"
      items: 3
  color_scheme: ["#FF6B35", "#004E89", "#FFFFFF"]
dependencies: ["content_001"]
output_format: "files"
priority: "high"

# Task 3: Code Generation
task_id: "code_001" 
task_type: "generate_html"
specifications:
  content_structure:
    sections: ["hero", "services", "portfolio", "testimonials", "contact"]
    navigation: ["home", "services", "portfolio", "about", "contact"]
  design_system:
    colors: ["#FF6B35", "#004E89", "#FFFFFF"]
    typography: "Inter, system-ui, sans-serif"
  layout_requirements:
    breakpoints: ["mobile: 320px", "tablet: 768px", "desktop: 1024px"]
    grid_system: "12-column"
  accessibility_level: "AA"
dependencies: ["content_001", "design_001"]
output_format: "files"
priority: "high"

# Task 4: Integration Setup
task_id: "integration_001"
task_type: "setup_api"
specifications:
  api_requirements:
    type: "rest"
    endpoints:
      - path: "/api/contact"
        method: "POST"
        authentication: "none"
        validation: ["name", "email", "message"]
    rate_limiting: "10_requests_per_minute"
dependencies: ["code_001"]
output_format: "integration"
priority: "normal"

# Task 5: Deployment
task_id: "deploy_001"
task_type: "deploy_site"
specifications:
  site_type: "static"
  source_location: "/output/code/code_001/"
  environment: "production"
  hosting_requirements:
    platform: "netlify"
    performance_tier: "professional"
  domain_info:
    domain_name: "joinery-agency-demo.com"
    ssl_required: true
dependencies: ["code_001", "integration_001"]
output_format: "deployment"
priority: "high"
```

### 3. Expected Production Agent Outputs

#### Content Producer Output
```yaml
status: "completed"
task_id: "content_001"
output:
  format: "document"
  files:
    - "homepage-hero-copy.md"
    - "services-section-copy.md"
    - "testimonials-copy.md"
  metadata:
    word_count: 850
    reading_level: "grade_8"
    seo_keywords: ["web design", "AI consultancy", "professional websites"]
```

#### Design Producer Output
```yaml
status: "completed" 
task_id: "design_001"
output:
  format: "files"
  files:
    - "homepage-mockup-desktop.png"
    - "homepage-mockup-mobile.png"
    - "design-system.json"
  metadata:
    design_style: "modern_professional"
    responsive_breakpoints: ["320px", "768px", "1024px"]
```

#### Code Producer Output
```yaml
status: "completed"
task_id: "code_001"
output:
  format: "files"
  files:
    - "index.html"
    - "styles/main.css"
    - "scripts/main.js"
  metadata:
    framework: "vanilla"
    accessibility_score: "AA"
    performance_score: 95
```

#### Integration Producer Output
```yaml
status: "completed"
task_id: "integration_001"
output:
  format: "integration"
  endpoints:
    - "https://api.joinery-demo.com/contact"
  metadata:
    api_version: "v1"
    security_level: "production_ready"
```

#### Deployment Producer Output
```yaml
status: "completed"
task_id: "deploy_001"
output:
  format: "deployment"
  location: "https://joinery-agency-demo.com"
  metadata:
    hosting_platform: "netlify"
    performance_score: 95
    ssl_grade: "A+"
```

## Test Validation

### System Integration Checks
- [ ] Production Manager correctly routes tasks to appropriate agents
- [ ] Dependencies are handled in proper sequence
- [ ] Standardized YAML format accepted by all agents
- [ ] Error handling works across the system
- [ ] Outputs from one agent properly consumed by dependent agents

### Quality Assurance
- [ ] Content matches brand voice and target audience
- [ ] Design mockups reflect specifications and responsive requirements
- [ ] Generated code is semantic, accessible, and performant
- [ ] API endpoints function correctly with proper validation
- [ ] Deployed site loads quickly with all features working

### End-to-End Verification
- [ ] Complete homepage created from single consultant input
- [ ] All specified sections present and functional
- [ ] Contact form working with API integration
- [ ] Site deployed and accessible at specified URL
- [ ] Performance and accessibility scores meet targets

## Success Criteria
✅ Production system successfully transforms consultant recommendations into live website
✅ All 6 production agents execute their tasks with standardized interfaces
✅ Production Manager coordinates multi-agent workflow effectively
✅ Final output meets quality standards and client specifications