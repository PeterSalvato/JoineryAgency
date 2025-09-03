# AI Agency Development Conventions

## 🤖 Agent Development Standards

This document defines development conventions for AI agent systems working on client projects. These standards ensure consistency, quality, and maintainability across all agency deliverables.

### **Universal Agent Standards**
- **Consistent Naming**: Use consistent naming conventions across all generated code (PascalCase recommended)
- **Mathematical Design Systems**: Use systematic proportional scales rather than arbitrary measurements
- **Documentation**: MANDATORY updates to project symbol index for all new code
- **Component Architecture**: Standardized data patterns and consistent interfaces
- **Build Process Discipline**: Never edit compiled output directly - always edit source files
- **Security Standards**: Always sanitize output using appropriate language-specific methods
- **Responsive Design**: Mobile-first approach with systematic breakpoint implementations
- **Source Control**: Maintain source → compile → output workflows

## Naming Standards

### **Agency Standard: PascalCase System**
Our agency standard uses PascalCase for maximum clarity and consistency across projects:

- **Classes/Components**: CSS classes, component names, UI elements
- **Functions**: All function names regardless of language
- **Variables**: All variable names for consistency
- **Files**: Use kebab-case for file names only

### **Cross-Language Application**
```
File: component-card.js
CSS: .CardPrimary
Function: RenderCard() / renderCard() (language appropriate)
Variable: CardData / cardData (language appropriate)
Component: <CardPrimary>
```

### **Agent Validation Checklist**
- [ ] Consistent naming convention applied throughout
- [ ] File names use kebab-case
- [ ] No mixed naming conventions within single project
- [ ] Language-appropriate adaptations (camelCase for JavaScript, etc.)

## SCSS Architecture

### **Agent Development Pattern**
- **Structure**: Single `assets/scss/` folder with modular files
- **Import Flow**: All files → `main.scss` → compiled CSS
- **Component Rule**: One SCSS file per component
- **Agent Workflow**: Edit SCSS → Run compile → Never touch CSS

### **File Organization for Agents**
```
assets/scss/
├── variables.scss    # Golden ratio system, design tokens
├── responsive.scss   # Breakpoint mixins (use these, not raw media queries)
├── base.scss        # Global resets and base styles
├── layout.scss      # Grid system, Container() mixin
├── fonts.scss       # Typography system + Material Symbols
└── components/
    ├── header.scss
    ├── card.scss
    └── [component].scss
```

### **Agent Quick Actions**
- **New Component**: Create `[name].scss` → Import in `main.scss`
- **Styling**: Use golden ratio variables, never hardcode measurements
- **Responsive**: Always use `Respond()` mixin from `responsive.scss`

## Mathematical Design Systems

### **Agency Standard: Proportional Scaling**
All agency projects use systematic proportional scales rather than arbitrary measurements:

- **Base Unit**: Define consistent base measurement (typically 1rem/16px)
- **Systematic Ratios**: Use mathematical relationships (golden ratio, modular scale, etc.)
- **Scale Consistency**: Apply scale across typography, spacing, layout, and components
- **No Arbitrary Values**: Eliminate random pixel values and inconsistent measurements

### **Example: Golden Ratio Implementation**
```scss
// Define systematic scale
$Scale: (
  'xs':   0.382rem,  // Base ÷ 1.618²
  'sm':   0.618rem,  // Base ÷ 1.618
  'base': 1rem,      // Base unit
  'lg':   1.618rem,  // Base × 1.618
  'xl':   2.618rem,  // Base × 1.618²
  'xxl':  4.236rem   // Base × 1.618³
);

// Usage pattern:
padding: map-get($Scale, 'lg');
margin: var(--scale-base); /* CSS custom properties alternative */
```

### **Agent Implementation Requirements**
- [ ] All measurements use defined scale values
- [ ] No hardcoded arbitrary measurements
- [ ] Typography follows systematic hierarchy
- [ ] Consistent proportional relationships maintained
- [ ] Scale system documented for project team

## Component Architecture

### **Agent Component Creation Pattern**
- **Location**: `assets/components/` directory only
- **Data Contract**: All components expect standardized `$Data` object
- **Output Method**: Components `echo` HTML directly (never `return` strings)

### **Standardized Data Structure for Agents**
```php
$Data = [
  'Title'   => 'Component title',
  'Content' => 'Main content/description', 
  'Classes' => 'additional-css-classes',
  'Image'   => 'path/to/image.jpg',
  'Url'     => 'https://link-destination.com'
];
```

### **Agent Development Requirements**
- **Error Handling**: Check `isset()` for all data keys
- **Sanitization**: Use `htmlspecialchars()` for all output
- **Accessibility**: Include ARIA attributes and semantic HTML
- **Icons**: Use semantic icon component with proper labels

### **Agent Component Checklist**
- [ ] Component file in `assets/components/`
- [ ] Accepts standardized `$Data` object
- [ ] Handles missing data gracefully
- [ ] Uses `htmlspecialchars()` for output
- [ ] Includes proper accessibility attributes
- [ ] Has corresponding SCSS file
- [ ] Documentation updated in symbol-index.md

## PHP Standards
- **File Organization**: One component per file
- **Data Sanitization**: Always use `htmlspecialchars()` for output
- **Includes**: Use `require_once` for critical files
- **Functions**: PascalCase naming (e.g., `LoadPortfolioData()`)
- **Variables**: PascalCase naming (e.g., `$CardData`)

## Responsive Design

### **Agent Implementation Requirements**
- **Approach**: Mobile-first design (start small, enhance upward)
- **CRITICAL RULE**: Use `Respond()` mixin only - NO raw media queries

### **Breakpoint System for Agents**
```scss
// Agent usage pattern:
@include Respond('medium') {
  // Styles for 768px and up
}

@include Respond('large') {
  // Styles for 992px and up
}
```

### **Available Breakpoints**
- `small`: 576px+
- `medium`: 768px+
- `large`: 992px+
- `xlarge`: 1200px+

### **Agent Layout System**
```scss
// Use Container() mixin for consistent layouts:
@include Container();
// Provides max-width and proper padding
```

### **Agent Responsive Checklist**
- [ ] Mobile-first approach (base styles for mobile)
- [ ] Uses `Respond()` mixin, not raw media queries
- [ ] Uses `Container()` mixin for layout
- [ ] Tests at all breakpoints
- [ ] No horizontal overflow on mobile

## Data Management
- **Portfolio**: Single JSON file (`assets/data/portfolio.json`)
- **Blog Posts**: Markdown files in (`assets/blog/posts/`) with YAML frontmatter
- **Structure**: Standardized schema with required fields
- **Contact Forms**: JSON logging + email notifications
- **File Handling**: Always check file existence before reading

## Blog System Architecture
- **Storage**: File-based markdown with YAML frontmatter
- **Location**: `/assets/blog/posts/` directory
- **File Naming**: `YYYY-MM-DD-post-slug.md` format
- **Frontmatter**: Required fields: `title`, `date`, `author`, `excerpt`, `slug`
- **Optional Fields**: `tags` (array), custom metadata
- **Content**: Markdown below frontmatter delimiter (`---`)
- **Routing**: `blog.php` for listing, `post.php?slug=name` for individual posts
- **Parsing**: Custom frontmatter parser, basic markdown to HTML conversion
- **Sorting**: Automatic date-based sorting (newest first)

## SEO Implementation
- **Current Phase**: Basic meta tags, semantic HTML, Open Graph
- **Meta Data**: Dynamic per-page title/description via `$PageData`
- **Structure**: Proper heading hierarchy (h1 → h2 → h3)
- **Future**: Advanced SEO techniques post-launch

## Build Process

### **Agent Workflow Commands**
- **Development**: `npm run css:watch` (use this while coding)
- **Single Compile**: `npm run css`
- **Production**: `npm run css:compressed`

### **Agent Development Workflow**
1. **Start**: `npm run css:watch`
2. **Edit**: SCSS files only (never CSS directly)
3. **Validate**: Check compiled CSS output
4. **Commit**: Include both SCSS and compiled CSS

### **Critical Agent Rules**
- ❌ **NEVER edit CSS files directly**
- ✅ **Always use `npm run css:watch` during development**
- ✅ **Edit SCSS sources only**
- ✅ **Commit both SCSS and compiled CSS**

### **Agent Setup (if needed)**
```bash
npm install                    # Install dependencies
chmod +x init.sh && ./init.sh  # Initialize structure (new projects only)
npm run css:watch              # Start development
```

## File Organization Rules
- **Assets**: All assets in `assets/` subdirectories
- **Components**: Reusable PHP components in `assets/components/`
- **Data**: JSON files in `assets/data/`
- **Documentation**: All docs in `docs/` directory
- **Clean Structure**: No loose files in root except main pages
- **Full Structure**:
  ```
  assets/
  ├── components/     # PHP components (header, nav, card, footer, icon)
  ├── scss/          # SCSS source files  
  ├── css/           # Compiled CSS output
  ├── data/          # JSON data files (portfolio.json)
  ├── blog/          # Blog system
  │   └── posts/     # Markdown blog posts with frontmatter
  ├── js/            # JavaScript files (main.js, navigation.js)
  └── images/        # Static images
  docs/              # Project documentation
  blog.php           # Blog listing page
  post.php           # Individual blog post page
  case-study.php     # Individual project case study page
  ```

## Version Control
- **Documentation**: Update conventions.md for any architectural changes
- **Symbol Index**: Update symbol-index.md for every new component/function
- **Commits**: Document convention changes in commit messages
- **Living Documents**: Both convention and symbol files evolve with project

## Quality Standards
- **Validation**: HTML5 semantic markup with W3C compliance
- **Accessibility**: WCAG 2.1 AA compliance with proper semantic structure
- **Performance**: Core Web Vitals optimization and efficient resource loading
- **Browser Support**: Modern browsers with progressive enhancement
- **Code Quality**: Consistent patterns, semantic naming, maintainable architecture

## Development Workflow
1. Edit source files (SCSS, component templates, etc.)
2. Run build processes for live compilation and validation
3. Structure data contracts before implementing components
4. Use mathematical scale values for all measurements
5. Follow mobile-first responsive design principles
6. Update project documentation for architectural changes
7. Update symbol index for new components/functions
8. Test across devices and accessibility standards

## Typography & Design Systems
- **Typography Hierarchy**: Systematic font sizing using mathematical ratios
- **Monospace Applications**: Code, technical content, data display
- **Icon Systems**: Semantic iconography with accessibility compliance
- **Icon Implementation**: Context-aware labeling and ARIA support
- **Font Loading**: Performance optimization with appropriate loading strategies
- **Visual Consistency**: Systematic approach to all visual elements

## Important Development Rules

### **🚨 CRITICAL AGENT REQUIREMENTS**

#### **BLOCKING RULES (Project will fail if violated)**
1. **CSS Editing**: Never edit CSS files directly - only SCSS sources
2. **Golden Ratio**: All measurements must use scale values (no hardcoded px/rem)
3. **Documentation**: MANDATORY updates to `symbol-index.md` for new code
4. **Data Sanitization**: Always use `htmlspecialchars()` for output
5. **Build Process**: Use `npm run css:watch` - never skip compilation

#### **NAMING ENFORCEMENT**
- **PascalCase**: All CSS classes, PHP functions, variables
- **kebab-case**: File names only
- **Consistency**: Apply across all agent-generated code

#### **COMPONENT REQUIREMENTS**
- **Data Structure**: Components expect standardized `$Data` object
- **Error Handling**: Check `isset()` for all data keys
- **Accessibility**: Include ARIA attributes and semantic HTML
- **Icons**: Use semantic icon component with proper labels

#### **RESPONSIVE REQUIREMENTS**
- **Mobile-First**: Start with mobile, enhance upward
- **Mixins Only**: Use `Respond()` mixin, never raw media queries
- **Container System**: Use `Container()` mixin for layouts

### **Agent Pre-Flight Checklist**
Before any code generation:
- [ ] Will use golden ratio scale values
- [ ] Will use PascalCase naming
- [ ] Will sanitize all output
- [ ] Will use `Respond()` mixin for responsive
- [ ] Will update documentation
- [ ] Will compile SCSS (never edit CSS)
- [ ] Will include accessibility attributes

---

*This document is updated whenever architectural decisions are made or conventions are established.*