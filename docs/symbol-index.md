# Symbol Index - Agent Reference Map

*Comprehensive system mapping optimized for AI agent consumption and cross-reference.*

## 🤖 Quick Agent Lookup

### **Critical System Patterns**
- **Component Data Pattern**: All components expect `$Data` array with keys: `Title`, `Content`, `Classes`, `Image`, `Url`
- **Security Pattern**: Always use `htmlspecialchars()` for output sanitization
- **Golden Ratio Pattern**: All measurements via `map-get($Scale, 'size')` - never hardcode
- **Responsive Pattern**: Use `@include Respond('breakpoint')` - never raw media queries
- **Documentation Pattern**: Update this file for ANY new functions/components/pages

### **Agent File Location Matrix**
```
Components: assets/components/[name].php + assets/scss/classes/[name]-classes.scss
Pages: [name].php + functions within
Data: assets/data/[name].json OR assets/blog/posts/[date]-[slug].md
Styles: Organized in assets/scss/elements/, classes/, pages/ folders
Build: npm run css:watch (development) | npm run css:compressed (production)
```

### **Agent Integration Checkpoints**
- [ ] Component follows data pattern
- [ ] SCSS uses golden ratio variables
- [ ] PHP sanitizes output with htmlspecialchars()
- [ ] Responsive uses Respond() mixin
- [ ] Documentation updated in this file

## AI Agent System Integration

### **AI Production Agents** (From main repository)
- **design-producer**: Generates SCSS and visual assets following golden ratio system
- **code-producer**: Creates PHP components and responsive implementations
- **content-producer**: Generates copy and content following brand voice
- **data-producer**: Handles research, analytics, and data processing
- **deployment-producer**: Manages hosting, CI/CD, and infrastructure
- **integration-producer**: Handles APIs, databases, and third-party services

### **Integration Points**
- **SCSS Generation**: AI agents must follow golden ratio scale and Respond() mixins
- **Component Creation**: AI agents must use standardized $Data object pattern
- **Content Generation**: AI agents must apply htmlspecialchars() sanitization
- **Responsive Implementation**: AI agents must use mobile-first with Respond() mixins

## PHP Functions (Website Components)

### LoadPortfolioData()
- **Location**: `portfolio.php:5-12`, `case-study.php:5-12`
- **Purpose**: Loads and parses portfolio JSON data
- **Dependencies**: `assets/data/portfolio.json`
- **Returns**: Array with 'projects' key or empty array if file missing
- **Called By**: `portfolio.php` main logic
- **Error Handling**: Returns empty projects array if JSON file doesn't exist

### RenderPortfolioItem()
- **Location**: `portfolio.php:20-34`
- **Purpose**: Renders appropriate template based on project template type
- **Parameters**: `$Project` (array) - Portfolio project data structure
- **Dependencies**: 
  - `assets/components/portfolio-gallery.php`
  - `assets/components/portfolio-case-study.php`
- **Logic**: Switch statement based on `template` field (defaults to 'gallery')
- **Template Types**: 'case-study' or 'gallery' (default)
- **Called By**: `portfolio.php` main rendering loop

### LoadBlogData()
- **Location**: `blog.php:5-18`
- **Purpose**: Scans and loads blog posts from markdown files
- **Dependencies**: `assets/blog/posts/` directory
- **Returns**: Array of post objects with metadata and content
- **Processing**: Parses YAML frontmatter, extracts content, sorts by date
- **Error Handling**: Skips invalid files, continues processing

### ParseBlogPost()
- **Location**: `blog.php:20-45`, `post.php:20-45`
- **Purpose**: Parses individual markdown blog post with YAML frontmatter
- **Parameters**: `$FilePath` (string) - Path to markdown file
- **Returns**: Associative array with post data and content
- **Processing**: Separates frontmatter from content, converts markdown to HTML
- **Required Fields**: `title`, `date`, `author`, `excerpt`, `slug`

## PHP Components

### Header Component
- **File**: `assets/components/header.php`
- **SCSS**: `assets/scss/classes/header-classes.scss`
- **Purpose**: Site header with navigation and branding
- **Data Required**: None (standalone component)
- **Dependencies**: Navigation component
- **Structure**: Logo, navigation menu, responsive hamburger menu

### Navigation Component  
- **File**: `assets/components/navigation.php`
- **SCSS**: `assets/scss/classes/navigation-classes.scss`
- **Purpose**: Primary site navigation menu
- **Data Required**: None (hardcoded menu items)
- **Structure**: Responsive navigation with mobile hamburger menu
- **JavaScript**: `assets/js/navigation.js` for mobile menu toggle

### Card Component
- **File**: `assets/components/card.php`
- **SCSS**: `assets/scss/classes/card-classes.scss`
- **Purpose**: Reusable content card for various content types
- **Data Pattern**: 
  ```php
  $Data = [
    'Title' => 'Card title',
    'Content' => 'Card description',
    'Classes' => 'additional-css-classes',
    'Image' => 'path/to/image.jpg',
    'Url' => 'https://link-destination.com'
  ];
  ```
- **Usage**: Portfolio items, blog posts, service descriptions

### Footer Component
- **File**: `assets/components/footer.php`
- **SCSS**: `assets/scss/classes/footer-classes.scss`
- **Purpose**: Site footer with contact info and links
- **Data Required**: None (standalone component)
- **Structure**: Contact information, social links, copyright

### Icon Component
- **File**: `assets/components/icon.php`
- **SCSS**: `assets/scss/classes/icon-classes.scss`
- **Purpose**: Semantic Material Symbols icons with accessibility
- **Data Pattern**:
  ```php
  $Data = [
    'Icon' => 'material-symbol-name',
    'Label' => 'Accessible label text',
    'Classes' => 'additional-css-classes'
  ];
  ```
- **Features**: ARIA labels, semantic meaning, multiple variants

### Portfolio Components
- **Gallery**: `assets/components/portfolio-gallery.php`
- **Case Study**: `assets/components/portfolio-case-study.php`
- **Purpose**: Display portfolio items in different formats
- **Data Pattern**: Expects full project object from portfolio.json
- **Usage**: Called by RenderPortfolioItem() based on template type

## SCSS Architecture

### Variables System
- **File**: `assets/scss/variables.scss`
- **Purpose**: Golden ratio scale, color system, typography
- **Key Variables**:
  - `$Scale`: Golden ratio spacing scale (xs, sm, base, lg, xl, xxl)
  - `$FontSizes`: Typography scale following golden ratio
  - `$Colors`: Brand color palette and semantic colors
  - `$Breakpoints`: Responsive breakpoint definitions

### Responsive System
- **File**: `assets/scss/responsive.scss`
- **Purpose**: Breakpoint mixins and responsive utilities
- **Key Mixins**:
  - `Respond($size)`: Media query mixin (small, medium, large, xlarge)
  - `Container()`: Consistent layout container with max-width and padding
- **Usage**: Always use mixins, never raw media queries

### Component Classes
- **Location**: `assets/scss/classes/`
- **Pattern**: One SCSS file per component type
- **Files**:
  - `layout-classes.scss`: Grid system, containers, utilities
  - `button-classes.scss`: Button variants and states
  - `form-classes.scss`: Form styling and validation states
  - `card-classes.scss`: Card component variations
  - `navigation-classes.scss`: Navigation and menu styling
  - `footer-classes.scss`: Footer layout and styling

## Data Structures

### Portfolio Data Schema
- **File**: `assets/data/portfolio.json`
- **Structure**:
  ```json
  {
    "projects": [
      {
        "id": "project-slug",
        "title": "Project Title",
        "description": "Brief description",
        "template": "gallery|case-study",
        "images": ["image1.jpg", "image2.jpg"],
        "url": "https://project-url.com",
        "tags": ["tag1", "tag2"]
      }
    ]
  }
  ```

### Blog Post Schema
- **Location**: `assets/blog/posts/YYYY-MM-DD-slug.md`
- **Frontmatter**:
  ```yaml
  ---
  title: "Post Title"
  date: "YYYY-MM-DD"
  author: "Author Name"
  excerpt: "Brief description"
  slug: "url-slug"
  tags: ["tag1", "tag2"]
  ---
  Markdown content here...
  ```

## Build System

### NPM Scripts
- **Development**: `npm run css:watch` - Live SCSS compilation
- **Single Build**: `npm run css` - One-time compilation
- **Production**: `npm run css:compressed` - Minified output
- **Documentation**: `npm run docs:check` - Validate documentation

### File Processing
- **Input**: `assets/scss/main.scss` (imports all partials)
- **Output**: `assets/css/main.css` (compiled CSS)
- **Watch Mode**: Automatically recompiles on SCSS changes
- **Dependencies**: Sass compiler via npm

## Pages & Routing

### Main Pages
- **Homepage**: `index.php` - Main landing page with services and portfolio
- **About**: `about.php` - Company information and team
- **Portfolio**: `portfolio.php` - Project gallery using LoadPortfolioData()
- **Blog**: `blog.php` - Blog post listing using LoadBlogData()
- **Contact**: `contact.php` - Contact form and information

### Dynamic Pages
- **Blog Post**: `post.php?slug=name` - Individual blog posts
- **Case Study**: `case-study.php?id=project-id` - Portfolio project details

### Page Data Pattern
```php
$PageData = [
  'Title' => 'Page Title - Site Name',
  'Description' => 'Meta description for SEO',
  'CanonicalUrl' => 'https://site.com/page',
  'OpenGraph' => [...] // Social media metadata
];
```

## Testing & Quality

### Playwright Testing
- **Config**: `playwright.config.js`
- **Tests**: `tests/*.spec.js`
- **Coverage**: Cross-browser compatibility, Core Web Vitals, accessibility
- **Command**: `npx playwright test`

### Quality Standards
- **HTML**: Valid HTML5, semantic markup
- **CSS**: BEM-like naming (PascalCase), no hardcoded values
- **PHP**: Sanitized output, error handling, proper includes
- **Accessibility**: WCAG 2.1 AA compliance
- **Performance**: Optimized images, efficient CSS, minimal HTTP requests

---

*This index is updated whenever new functions, components, or architectural elements are added to maintain comprehensive system mapping for AI agents.*