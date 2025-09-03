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

## PHP Functions

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

### parseFrontmatter()
- **Location**: `blog.php:12-44`, `post.php:14-46`
- **Purpose**: Extracts YAML frontmatter and content from markdown files
- **Parameters**: `$content` (string) - Raw markdown file content
- **Returns**: Array with 'metadata' and 'content' keys
- **Logic**: Regex pattern matching for `---` delimited frontmatter
- **Handles**: String values, quoted strings, array syntax for tags
- **Error Handling**: Returns empty metadata array if no frontmatter found

### getBlogData()
- **Location**: `blog.php:46-81`
- **Purpose**: Scans posts directory and returns all blog post data
- **Dependencies**: `/assets/blog/posts/*.md` files
- **Returns**: Array with 'posts' key containing sorted post arrays
- **Logic**: 
  1. Scans directory with `glob()` for `.md` files
  2. Parses each file with `parseFrontmatter()`
  3. Adds file-based metadata (id, slug generation)
  4. Sorts by date (newest first)
- **Error Handling**: Returns empty posts array if directory doesn't exist

### findPostBySlug()
- **Location**: `post.php:48-78`
- **Purpose**: Locates single blog post by slug identifier
- **Parameters**: `$slug` (string) - Post slug to find
- **Dependencies**: `/assets/blog/posts/*.md` files
- **Returns**: Post array or null if not found
- **Logic**: Iterates through markdown files, matches slug from frontmatter or filename
- **Used By**: `post.php` for individual post display
- **Error Handling**: Returns null for non-existent posts

### convertMarkdownToHtml()
- **Location**: `post.php:81-98`
- **Purpose**: Basic markdown to HTML conversion
- **Parameters**: `$content` (string) - Markdown content
- **Returns**: HTML string with basic formatting
- **Conversions**:
  - `# text` → `<h1>text</h1>`
  - `## text` → `<h2>text</h2>` 
  - `**text**:` → `<strong>text</strong>:`
  - `- item` → `<li>item</li>` (wrapped in `<ul>`)
  - Double newlines → `<p>` tags
- **Security**: Uses `htmlspecialchars()` before processing

### isCurrentPage()
- **Location**: `assets/components/nav.php:3-7`
- **Purpose**: Determines if current page matches navigation link
- **Parameters**: `$href` (string) - Link href to compare against current page
- **Returns**: Boolean true if current page matches link
- **Logic**: Compares basename of current PHP_SELF with basename of href
- **Used By**: Navigation component for active state detection
- **Dependencies**: $_SERVER['PHP_SELF'] global variable

### getCurrentPageInfo()
- **Location**: `assets/components/nav.php:10-25`
- **Purpose**: Returns breadcrumb information for current page
- **Returns**: Array with 'title' and 'parent' keys
- **Logic**: Maps current page to navigation hierarchy structure
- **Page Mapping**: index→Home, about→About, portfolio→Portfolio, contact→Contact, blog→Blog
- **Used By**: Navigation component for breadcrumb generation
- **Dependencies**: $_SERVER['PHP_SELF'] global variable

### FindProjectById()
- **Location**: `case-study.php:14-21`
- **Purpose**: Finds portfolio project by ID from project array
- **Parameters**: `$projects` (array), `$id` (string) - Project collection and target ID
- **Returns**: Project array or null if not found
- **Logic**: Linear search through projects array matching ID field
- **Used By**: `case-study.php` for individual project display
- **Error Handling**: Returns null for non-existent projects

### renderBlogPost()
- **Location**: `blog.php:84-110`
- **Purpose**: Renders single blog post preview for listing page
- **Parameters**: `$post` (array) - Blog post data structure
- **Returns**: HTML string for blog post preview
- **Features**: Title linking, date formatting, tag display, excerpt with "Read More"
- **Used By**: `blog.php` listing loop
- **Dependencies**: Post data structure with title, date, slug, excerpt, tags

### Component Data Pattern (MANDATORY FOR AGENTS)

### **Universal Component Interface**
All components MUST follow this pattern:
```php
$ComponentData = [
  'Title'   => 'Component heading',     // Required
  'Content' => 'Main content text',      // Required  
  'Classes' => 'additional-css-classes', // Required (can be empty string)
  'Image'   => '/path/to/image.jpg',     // Optional
  'Url'     => 'https://destination',    // Optional
];
```

### **Agent Implementation Rules**
1. **Set data BEFORE including component**
2. **Always check isset() for optional keys in component logic**  
3. **Use htmlspecialchars() for all output**
4. **Components echo HTML directly (never return strings)**

### **Component Naming Convention**
- Data Variable: `$[ComponentName]Data` (e.g., `$ButtonData`, `$CardData`)
- File Path: `assets/components/[component-name].php`
- CSS Classes: `.ComponentName` with BEM methodology

## PHP Components

### card.php
- **Location**: `assets/components/card.php`
- **Purpose**: Renders article cards with standardized markup
- **Dependencies**: 
  - `$CardData` global variable with component data
  - `.Card` CSS classes for styling
- **Output**: HTML article element with BEM-style classes
- **Variants**: Supports additional CSS classes via `Classes` key
- **Related CSS**: `assets/scss/card.scss`
- **Used By**: General card display (legacy)

### portfolio-gallery.php
- **Location**: `assets/components/portfolio-gallery.php`
- **Purpose**: Template for portfolio items focused on visual showcase
- **Dependencies**: 
  - `$PortfolioData` global variable with project data
  - Portfolio CSS classes for styling
- **Features**: Hero image, meta info, services list, image gallery grid
- **Template Type**: 'gallery' - Used for visual/design-focused projects
- **Used By**: `RenderPortfolioItem()` when `template: "gallery"`

### portfolio-case-study.php
- **Location**: `assets/components/portfolio-case-study.php`
- **Purpose**: Template for detailed project case studies
- **Dependencies**: 
  - `$PortfolioData` global variable with project data
  - Portfolio CSS classes for styling
- **Features**: Challenge/Solution/Results sections, technologies, detailed content
- **Template Type**: 'case-study' - Used for development/strategic projects
- **Used By**: `RenderPortfolioItem()` when `template: "case-study"`

### header.php
- **Location**: `assets/components/header.php`
- **Purpose**: Renders HTML document head and opening body tag
- **Dependencies**: 
  - `$PageData` global variable for meta information
  - `assets/css/main.css` stylesheet
- **SEO Features**: Dynamic title, description, Open Graph tags
- **Related Components**: Must be paired with `footer.php`
- **CSS Classes**: Applies `$PageData['Classes']` to body element

### nav.php
- **Location**: `assets/components/nav.php`
- **Purpose**: Renders main site navigation
- **Dependencies**: 
  - `.Navigation` CSS classes
  - `.Container` layout class
- **Structure**: Logo + horizontal menu list
- **Related CSS**: `assets/scss/header.scss`
- **Responsive**: Styles adapt via responsive mixins

### footer.php
- **Location**: `assets/components/footer.php`
- **Purpose**: Renders site footer and closes HTML document
- **Dependencies**: 
  - `.Footer` CSS classes
  - `.Container` layout class
- **Structure**: Three-column grid with company info, services, contact
- **Related CSS**: `assets/scss/footer.scss`
- **Pairs With**: `header.php` (must be included together)

### icon.php
- **Location**: `assets/components/icon.php`
- **Purpose**: Semantic Material Symbols icon component with accessibility
- **Dependencies**: 
  - `$IconData` global variable with icon configuration
  - Material Symbols fonts (outlined, rounded, filled)
  - Icon-specific CSS classes
- **Required Keys**: `name` (Material Symbol name), `semantic` (meaning context)
- **Optional Keys**: `label`, `size`, `style`, `color`, `decorative`
- **Features**: Auto-generated accessibility labels, size variants, color themes
- **Output**: Styled `<span>` with proper ARIA attributes
- **Related CSS**: `assets/scss/fonts.scss`

### button.php
- **Location**: `assets/components/button.php`
- **Purpose**: Professional button component with multiple variants and states
- **Dependencies**: 
  - `$ButtonData` global variable with button configuration
  - `.Button` CSS classes for styling
- **Required Keys**: `text` (button label), `href` or `onclick` (action)
- **Optional Keys**: `style` (primary/secondary/ghost), `size` (small/large), `icon`, `classes`
- **Features**: Icon support, multiple styling variants, accessibility compliance
- **Output**: Styled `<a>` or `<button>` element with proper ARIA attributes
- **Related CSS**: `assets/scss/button.scss`

### form-field.php
- **Location**: `assets/components/form-field.php`
- **Purpose**: Standardized form field component with validation support
- **Dependencies**: 
  - `$FieldData` global variable with field configuration
  - `.FormField` CSS classes for styling
- **Required Keys**: `name` (field identifier), `label` (field label)
- **Optional Keys**: `type`, `placeholder`, `required`, `validation`, `value`, `classes`
- **Features**: Multiple input types, validation states, accessibility labels
- **Output**: Complete form field with label, input, and validation markup
- **Related CSS**: `assets/scss/forms.scss`

### process-step.php
- **Location**: `assets/components/process-step.php`
- **Purpose**: Process visualization step component for methodology showcase
- **Dependencies**: 
  - `$StepData` global variable with step configuration
  - `.ProcessStep` CSS classes for styling
- **Required Keys**: `number` (step number), `title` (step title), `description`
- **Optional Keys**: `icon`, `status` (active/completed), `classes`
- **Features**: Step numbering, status indicators, icon integration
- **Output**: Styled process step with proper semantic markup
- **Related CSS**: `assets/scss/process.scss`

### team-member.php
- **Location**: `assets/components/team-member.php`
- **Purpose**: Team member profile component with social links and skills
- **Dependencies**: 
  - `$MemberData` global variable with member configuration
  - `.TeamMember` CSS classes for styling
- **Required Keys**: `name` (member name), `role` (position title)
- **Optional Keys**: `avatar`, `bio`, `skills`, `social`, `featured`, `classes`
- **Features**: Avatar placeholders, social media integration, skill tags
- **Output**: Complete team member profile with structured data
- **Related CSS**: `assets/scss/team.scss`

### testimonial.php
- **Location**: `assets/components/testimonial.php`
- **Purpose**: Client testimonial component with ratings and attribution
- **Dependencies**: 
  - `$TestimonialData` global variable with testimonial configuration
  - `.Testimonial` CSS classes for styling
- **Required Keys**: `quote` (testimonial text), `author` (client name)
- **Optional Keys**: `role`, `company`, `avatar`, `rating`, `featured`, `classes`
- **Features**: Star ratings, client avatars, multiple layout variants
- **Output**: Styled testimonial with proper attribution markup
- **Related CSS**: `assets/scss/testimonial.scss`

## PHP Pages

### blog.php
- **Location**: `blog.php`
- **Purpose**: Blog listing page with post previews
- **Dependencies**: 
  - `/assets/blog/posts/*.md` files
  - `parseFrontmatter()`, `getBlogData()`, `renderBlogPost()` functions
  - `header.php`, `nav.php`, `footer.php` components
- **Features**: Automatic post loading, date sorting, excerpt display
- **URL Structure**: `/blog.php` - main blog listing
- **Related CSS**: `assets/scss/blog.scss`

### post.php
- **Location**: `post.php`
- **Purpose**: Individual blog post display
- **Parameters**: `$_GET['slug']` - Post slug identifier
- **Dependencies**:
  - `/assets/blog/posts/*.md` files
  - `parseFrontmatter()`, `findPostBySlug()`, `convertMarkdownToHtml()` functions
  - `header.php`, `nav.php`, `footer.php` components
- **Features**: Single post display, markdown conversion, 404 handling
- **URL Structure**: `/post.php?slug=post-name`
- **Error Handling**: Shows 404 page for non-existent posts

### case-study.php
- **Location**: `case-study.php`
- **Purpose**: Individual project case study display
- **Parameters**: `$_GET['project']` - Project ID identifier
- **Dependencies**:
  - `assets/data/portfolio.json`
  - `LoadPortfolioData()`, `FindProjectById()` functions
  - `header.php`, `nav.php`, `footer.php`, `icon.php` components
- **Features**: Project hero, challenge/solution sections, gallery, navigation
- **URL Structure**: `/case-study.php?project=project-id`
- **Error Handling**: Shows 404 page for non-existent projects
- **Related CSS**: `assets/scss/case-study.scss`

### index.php
- **Location**: `index.php`
- **Purpose**: Homepage with hero section, services, and featured portfolio
- **Dependencies**:
  - `header.php`, `nav.php`, `footer.php`, `icon.php` components
  - Portfolio data integration for featured projects
- **Features**: Hero section, service cards, featured work showcase
- **URL Structure**: `/` - Site homepage
- **Related CSS**: `assets/scss/main.scss`, responsive design system

### about.php
- **Location**: `about.php`
- **Purpose**: About page showcasing company expertise and approach
- **Dependencies**:
  - `header.php`, `nav.php`, `footer.php`, `icon.php` components
- **Features**: Company story, team information, service methodology
- **URL Structure**: `/about.php`
- **Related CSS**: Standard design system styling

### contact.php
- **Location**: `contact.php`
- **Purpose**: Contact form and company contact information
- **Dependencies**:
  - `header.php`, `nav.php`, `footer.php`, `icon.php` components
- **Features**: Contact form, office information, call-to-action
- **URL Structure**: `/contact.php`
- **Related CSS**: Form styling and layout components

### portfolio.php
- **Location**: `portfolio.php`
- **Purpose**: Portfolio listing page displaying all projects
- **Dependencies**:
  - `assets/data/portfolio.json`
  - `LoadPortfolioData()`, `RenderPortfolioItem()` functions
  - `header.php`, `nav.php`, `footer.php` components
  - `portfolio-gallery.php`, `portfolio-case-study.php` templates
- **Features**: Project filtering, template-based rendering, responsive grid
- **URL Structure**: `/portfolio.php`
- **Related CSS**: Portfolio-specific styling and card layouts

## SCSS System (Agent Quick Reference)

### **Agent Development Workflow**
1. Edit SCSS files only (never CSS directly)
2. Run `npm run css:watch` for development
3. Use golden ratio variables for ALL measurements
4. Use `Respond()` mixin for responsive breakpoints
5. Import new files through `main.scss`

### **Required Import Order (Critical for Agents)**
```scss
// main.scss structure - DO NOT CHANGE ORDER
@import 'variables';        // MUST BE FIRST - defines tokens
@import 'responsive';       // MUST BE SECOND - defines mixins  
@import 'fonts';            // Typography system & Material Icons

// HTML Element Styles
@import 'elements/base-elements';     // html, body, h1-h6, p, a, etc.
@import 'elements/form-elements';     // input, textarea, select, button, etc.

// CSS Class Styles - organized by purpose
@import 'classes/layout-classes';             // .Container, .Grid, etc.
@import 'classes/component-classes';          // Basic component utilities
@import 'classes/button-classes';             // .Button system
@import 'classes/form-classes';               // .FormField system
@import 'classes/card-classes';               // .Card system
@import 'classes/navigation-classes';         // .Navigation system
@import 'classes/footer-classes';             // .Footer system
@import 'classes/testimonial-classes';        // .Testimonial system
@import 'classes/team-classes';               // .TeamMember system
@import 'classes/process-classes';            // .ProcessStep system
@import 'classes/brand-enhancement-classes';  // Brand polish enhancements
@import 'classes/touch-target-classes';       // Touch target standards
@import 'classes/visual-sophistication-classes'; // Museum-quality visual enhancements

// Page-Specific Styles
@import 'pages/blog-page';           // Blog listing and post styles
@import 'pages/case-study-page';     // Case study display styles
```

### Golden Ratio Variables (MANDATORY AGENT USAGE)
- **Location**: `assets/scss/variables.scss`
- **Critical Agent Rule**: NEVER use hardcoded measurements

#### **Agent Reference Syntax**
```scss
// Spacing scale (ALWAYS USE THESE)
padding: map-get($Scale, 'lg');        // 1.618rem
margin: map-get($Scale, 'sm');         // 0.618rem
width: map-get($Scale, 'xxl');         // 4.236rem

// Typography scale
font-size: map-get($FontSizes, 'lg');  // Golden ratio typography

// NEVER DO THIS:
padding: 20px;  // ❌ BLOCKED - Use scale only
```

#### **Available Scale Values**
- `xs`: 0.382rem, `sm`: 0.618rem, `base`: 1rem, `lg`: 1.618rem, `xl`: 2.618rem, `xxl`: 4.236rem
- Dependencies: Used in ALL component SCSS - agents must follow this pattern

### Responsive System (MANDATORY AGENT PATTERN)
- **Location**: `assets/scss/responsive.scss`
- **Critical Agent Rule**: Use `Respond()` mixin only - NEVER raw media queries

#### **Agent Implementation Syntax**
```scss
// Mobile-first pattern (ALWAYS USE THIS)
.ComponentName {
  // Mobile styles first (no mixin needed)
  padding: map-get($Scale, 'sm');
  
  @include Respond('medium') {
    // Tablet styles (768px+)
    padding: map-get($Scale, 'base');
  }
  
  @include Respond('large') {
    // Desktop styles (992px+)
    padding: map-get($Scale, 'lg');
  }
}

// Container system
@include Container(); // Max-width + padding system
```

#### **Available Breakpoints**
- `small`: 576px+, `medium`: 768px+, `large`: 992px+, `xlarge`: 1200px+
- Dependencies: ALL responsive styling must use these mixins

### Component CSS Classes

#### .Card System
- **Location**: `assets/scss/card.scss`
- **Base Class**: `.Card` with hover effects and shadows
- **Child Elements**: 
  - `.Card__Image` - Image container with object-fit
  - `.Card__Content` - Text content wrapper
  - `.Card__Title` - Heading element
  - `.Card__Description` - Body text
  - `.Card__Link` - Action link
- **Variants**: 
  - `.PortfolioCard` - Additional portfolio-specific styles
  - `.ServiceCard` - Centered text for service cards
- **Related PHP**: `assets/components/card.php`

#### .Navigation System
- **Location**: `assets/scss/header.scss`
- **Structure**: 
  - `.Navigation` - Main nav container with sticky positioning
  - `.Navigation__Menu` - Flexbox menu list
  - `.Navigation__Link` - Individual menu items
- **Logo Classes**: `.Logo` and `.Logo__Text`
- **Responsive**: Menu layout adapts via Respond mixin
- **Related PHP**: `assets/components/nav.php`

#### .Footer System
- **Location**: `assets/scss/footer.scss`
- **Structure**:
  - `.Footer` - Main footer container
  - `.Footer__Content` - Grid layout for sections
  - `.Footer__Section` - Individual footer columns
  - `.Footer__Bottom` - Copyright area
- **Grid**: Responsive three-column layout
- **Related PHP**: `assets/components/footer.php`

#### .Button System
- **Location**: `assets/scss/button.scss`
- **Base Class**: `.Button` with comprehensive styling framework
- **Variants**:
  - `.Button--primary` - Main call-to-action styling
  - `.Button--secondary` - Secondary action styling
  - `.Button--ghost` - Minimal outline style
- **Sizes**: `.Button--small`, `.Button--large` for different contexts
- **Features**: Icon integration, hover states, focus accessibility
- **Related PHP**: `assets/components/button.php`

#### .FormField System
- **Location**: `assets/scss/forms.scss`
- **Structure**:
  - `.FormField` - Field container with golden ratio spacing
  - `.FormField__Label` - Accessible label styling
  - `.FormField__Input` - Input element with states
  - `.FormField__Error` - Validation error display
- **States**: Focus, error, disabled state management
- **Related PHP**: `assets/components/form-field.php`

#### .ProcessStep System
- **Location**: `assets/scss/process.scss`
- **Structure**:
  - `.ProcessStep` - Step container with numbering
  - `.ProcessStep__Number` - Visual step indicator
  - `.ProcessStep__Content` - Step description area
  - `.ProcessStep__Icon` - Optional icon display
- **Features**: Sequential numbering, progress indicators, responsive layout
- **Related PHP**: `assets/components/process-step.php`

#### .TeamMember System
- **Location**: `assets/scss/team.scss`
- **Base Class**: `.TeamMember` with hover effects and social overlays
- **Child Elements**:
  - `.TeamMember__Avatar` - Avatar container with placeholders
  - `.TeamMember__Content` - Member information section
  - `.TeamMember__Social` - Social media overlay
  - `.TeamMember__Skills` - Skill tag display
- **Variants**: `.TeamMember--featured`, `.TeamMember--compact` for different layouts
- **Related PHP**: `assets/components/team-member.php`

#### .Testimonial System
- **Location**: `assets/scss/testimonial.scss`
- **Structure**:
  - `.Testimonial` - Main testimonial container
  - `.Testimonial__Quote` - Quote text with styling
  - `.Testimonial__Attribution` - Author and rating section
  - `.Testimonial__Rating` - Star rating display
- **Variants**: `.Testimonial--featured`, `.Testimonial--compact`
- **Features**: Quote icons, rating systems, responsive layouts
- **Related PHP**: `assets/components/testimonial.php`

#### .Brand Enhancement System
- **Location**: `assets/scss/brand-enhancements.scss`
- **Purpose**: Professional polish and mathematical precision using golden ratio
- **Structure**:
  - `.Section-Header` - Consistent brand hierarchy with golden ratio spacing
  - `.Philosophy-Stats` - Mathematical emphasis with hover effects
  - `.Process-Steps` - Enhanced visual hierarchy with connection lines
  - `.ProcessStep` - Individual step with numbered circles and accent rings
  - `.Philosophy` - Enhanced philosophy section with gradient backgrounds
  - `.FeaturedWork` - Grid enhancement with golden ratio spacing
  - `.Approach` - Section enhancement with optimal content width
- **Features**: Golden ratio proportions, gradient backgrounds, hover effects, responsive layouts
- **Mathematical Design**: All spacing based on φ^n scale progression

#### .Touch Target System
- **Location**: `assets/scss/touch-targets.scss`
- **Purpose**: Professional touch target standards for optimal accessibility and UX
- **Features**: 44x44px minimum touch areas, invisible expansion technique, comprehensive interactive element coverage
- **Structure**:
  - `@mixin TouchTarget()` - Universal touch target mixin with invisible expansion
  - Form element enhancements with comfortable padding and explicit heights
  - Navigation link optimizations with responsive touch areas
  - Button group spacing and touch feedback systems
- **Coverage**: All interactive elements (links, buttons, form controls, navigation, icons)
- **Accessibility**: WCAG compliance with proper touch target sizing and visual feedback
- **Dependencies**: Golden ratio scale variables, responsive mixins

#### .Visual Sophistication System
- **Location**: `assets/scss/visual-sophistication.scss`
- **Purpose**: Museum-quality design with subtle depth, micro-interactions, and professional polish
- **Features**: Enhanced shadows, hover animations, entrance effects, loading states
- **Structure**:
  - `$SophisticatedShadows` - Professional shadow scale with depth layering
  - `@mixin HoverLift()` - Consistent hover elevation effects
  - Keyframe animations: `fadeInUp`, `fadeInScale`, `shimmer`
  - Component enhancements: Navigation backdrop blur, card hover effects, button ripples
  - Form field focus states with visual feedback
  - Typography refinements with accent animations
- **Accessibility**: Focus indicators, selection styling, print optimizations
- **Performance**: Smooth transitions, hardware acceleration, minimal reflow triggers
- **Dependencies**: Color variables, transition tokens, responsive system

## Data Structures

### Portfolio JSON Schema
- **Location**: `assets/data/portfolio.json`
- **Root Structure**: Object with `projects` array
- **Project Object Fields**:
  - `id` (string) - Unique identifier
  - `title` (string) - Project name
  - `client` (string) - Client name
  - `template` (string) - Template type: 'gallery' or 'case-study'
  - `services` (array) - Service types provided
  - `description` (string) - Project summary
  - `challenge` (string) - Client challenge (case studies)
  - `solution` (string) - Solution provided (case studies)
  - `results` (array) - Measurable outcomes (case studies)
  - `technologies` (array) - Technologies used (case studies)
  - `image` (string) - Thumbnail/hero image path
  - `gallery` (array) - Additional image paths
  - `url` (string) - Live project URL
  - `featured` (boolean) - Homepage display flag
  - `date` (string) - Completion date (YYYY-MM-DD)
- **Template Logic**: `template` field determines which component renders the project
- **Dependencies**: Read by `LoadPortfolioData()`, used by `RenderPortfolioItem()`
- **Usage**: Template-based rendering in `portfolio.php`

### Blog Post Markdown Structure
- **Location**: `/assets/blog/posts/YYYY-MM-DD-slug.md`
- **Format**: YAML frontmatter + markdown content
- **Frontmatter Fields**:
  - `title` (string) - Post title
  - `date` (string) - Publication date (YYYY-MM-DD)
  - `author` (string) - Author name
  - `tags` (array) - Category tags
  - `excerpt` (string) - Post summary for listings
  - `slug` (string) - URL identifier
- **Content**: Markdown below `---` delimiter
- **File Naming**: Date prefix for chronological sorting
- **Dependencies**: Parsed by `parseFrontmatter()` function
- **Usage**: Displayed by `blog.php` and `post.php`

### Blog Post Data Structure
- **Usage**: Internal format after parsing markdown files
- **Generated Fields**:
  - `id` (string) - Filename without extension
  - `content` (string) - Markdown content from file
  - All frontmatter fields are preserved as-is
- **Processing**: 
  - Slugs auto-generated from filename if missing
  - Tags handled as arrays
  - Content converted to HTML for display
- **Dependencies**: Created by `getBlogData()` and `findPostBySlug()`

### Page Data Structure
- **Usage**: `$PageData` array in all main PHP pages
- **Standard Fields**:
  - `Title` (string) - Page title for <title> tag
  - `Description` (string) - Meta description
  - `Classes` (string) - Body CSS classes
- **Dependencies**: Used by `header.php` for meta tags and body classes
- **SEO Impact**: Direct mapping to HTML meta elements
- **Example Structure**:
  ```php
  $PageData = [
      'Title' => 'Page Title',           // For <title> tag
      'Description' => 'Meta description', // For meta description
      'Classes' => 'PageSpecificClass'    // Body CSS classes
  ];
  ```

### Component Data Structure
- **Usage**: Standard pattern for all components (e.g., `$CardData`)
- **Standard Fields**:
  - `Title` (string) - Component title/heading
  - `Content` (string) - Main content text
  - `Image` (string) - Image path
  - `Url` (string) - Link destination
  - `Classes` (string) - Additional CSS classes
- **Example Structure**:
  ```php
  $CardData = [
      'Title' => 'Card Title',
      'Content' => 'Card content text',
      'Image' => '/path/to/image.jpg',
      'Url' => 'https://example.com',
      'Classes' => 'AdditionalCSSClasses'
  ];
  ```

## File Dependencies

### Typography System
- **Location**: `assets/scss/fonts.scss`
- **Primary Font**: Inter - Modern sans-serif for UI and body text
- **Monospace Fonts**: JetBrains Mono, Space Mono, IBM Plex Mono
- **Icon System**: Material Symbols (outlined, rounded variants)
- **Font Loading**: Google Fonts CDN with display=swap
- **Icon Classes**: `.material-symbols-outlined`, `.material-symbols-rounded`
- **Size Variants**: `.small`, `.large` for different icon contexts

### SCSS Import Chain
- **Entry Point**: `assets/scss/main.scss`
- **Import Order**: 
  1. `variables.scss` - Must be first (defines tokens)
  2. `responsive.scss` - Mixins used by other files
  3. `base.scss` - Global styles and responsive typography
  4. `layout.scss` - Layout utilities
  5. `fonts.scss` - Typography and icon systems
  6. `header.scss`, `footer.scss`, `card.scss`, `case-study.scss` - Core components
  7. `button.scss`, `forms.scss`, `testimonial.scss`, `team.scss` - Enhanced components
  8. `brand-enhancements.scss` - Professional polish and mathematical precision
  9. `touch-targets.scss` - Accessibility and UX touch target standards
  10. `visual-sophistication.scss` - Museum-quality design enhancements and micro-interactions
- **Build Output**: `assets/css/main.css`
- **Watch Command**: `npm run css:watch`

### PHP Include Chain
- **Page Structure**: 
  1. Main page (index.php, about.php, blog.php, post.php, etc.)
  2. `require_once 'assets/components/header.php'`
  3. `require_once 'assets/components/nav.php'`
  4. Page content with component includes
  5. `require_once 'assets/components/footer.php'`
- **Component Includes**: Use relative paths from page location
- **Data Flow**: Set data arrays before including components
- **Blog Pages**: Additional data loading via markdown parsing functions
- **Case Study Pages**: Project data loading and individual project display

### JavaScript Assets
- **Location**: `assets/js/` directory
- **Files**:
  - `main.js` - Basic JavaScript functionality
  - `navigation.js` - Navigation interaction handling
- **Loading**: Included in footer for optimal page performance

## Build System

### NPM Scripts
- **Location**: `package.json`
- **Commands**:
  - `npm run css` - Single SCSS compilation
  - `npm run css:watch` - Development watch mode
  - `npm run css:compressed` - Production minification
- **Dependencies**: Requires `sass` package
- **Workflow**: Edit SCSS → Run command → CSS updates

### Asset Pipeline
- **Source**: `assets/scss/` directory
- **Output**: `assets/css/` directory
- **Linked**: `header.php` links to compiled CSS
- **Development**: Use watch mode for live updates
- **Production**: Use compressed mode for deployment

---

*This index is updated every time components, functions, or relationships are added or modified.*
