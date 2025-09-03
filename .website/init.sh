#!/bin/bash

echo "🚀 Initializing Design & Development Consultancy Website..."
echo "================================================="

# Create main directory structure
echo "📁 Creating directory structure..."

mkdir -p assets/{scss,css,js,images,components,data}
mkdir -p docs

# Create main PHP files
echo "📄 Creating main PHP files..."

# Index page
cat > index.php << 'EOF'
<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

$PageData = [
    'Title' => 'Design & Development Consultancy',
    'Description' => 'Visual Design, UX Design & System Architecture',
    'Classes' => 'HomePage'
];
?>

<main class="Main HomePage">
    <section class="Hero">
        <div class="Container">
            <h1 class="Hero__Title">Design & Development Consultancy</h1>
            <p class="Hero__Subtitle">Visual Design, UX Design & System Architecture</p>
        </div>
    </section>
    
    <section class="Services">
        <div class="Container">
            <h2>Our Services</h2>
            <!-- Services content will go here -->
        </div>
    </section>
</main>

<?php require_once 'assets/components/footer.php'; ?>
EOF

# About page
cat > about.php << 'EOF'
<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

$PageData = [
    'Title' => 'About Us - Design & Development Consultancy',
    'Description' => 'Learn about our approach to visual design, UX, and system architecture',
    'Classes' => 'AboutPage'
];
?>

<main class="Main AboutPage">
    <section class="About">
        <div class="Container">
            <h1>About Us</h1>
            <p>We specialize in three core areas: Visual Design, UX Design, and System Architecture & Development.</p>
        </div>
    </section>
</main>

<?php require_once 'assets/components/footer.php'; ?>
EOF

# Contact page
cat > contact.php << 'EOF'
<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

$PageData = [
    'Title' => 'Contact Us - Design & Development Consultancy',
    'Description' => 'Get in touch to discuss your next project',
    'Classes' => 'ContactPage'
];
?>

<main class="Main ContactPage">
    <section class="Contact">
        <div class="Container">
            <h1>Contact Us</h1>
            <form class="ContactForm" method="POST" action="contact-handler.php">
                <div class="FormGroup">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="FormGroup">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="FormGroup">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" required></textarea>
                </div>
                <button type="submit" class="Button Primary">Send Message</button>
            </form>
        </div>
    </section>
</main>

<?php require_once 'assets/components/footer.php'; ?>
EOF

# Portfolio page
cat > portfolio.php << 'EOF'
<?php
require_once 'assets/components/header.php';
require_once 'assets/components/nav.php';

$PageData = [
    'Title' => 'Portfolio - Design & Development Consultancy',
    'Description' => 'View our recent work in visual design, UX, and development',
    'Classes' => 'PortfolioPage'
];

function LoadPortfolioData() {
    $JsonFile = 'assets/data/portfolio.json';
    if (file_exists($JsonFile)) {
        $JsonData = file_get_contents($JsonFile);
        return json_decode($JsonData, true);
    }
    return ['projects' => []];
}

$PortfolioData = LoadPortfolioData();
?>

<main class="Main PortfolioPage">
    <section class="Portfolio">
        <div class="Container">
            <h1>Our Work</h1>
            <div class="PortfolioGrid">
                <?php foreach ($PortfolioData['projects'] as $Project): ?>
                    <?php
                    $CardData = [
                        'Title' => $Project['title'],
                        'Content' => $Project['description'],
                        'Image' => $Project['image'],
                        'Url' => $Project['url'] ?? '#',
                        'Classes' => 'PortfolioCard'
                    ];
                    require 'assets/components/card.php';
                    ?>
                <?php endforeach; ?>
            </div>
        </div>
    </section>
</main>

<?php require_once 'assets/components/footer.php'; ?>
EOF

# Create components
echo "🧩 Creating component files..."

# Header component
cat > assets/components/header.php << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $PageData['Title'] ?? 'Design & Development Consultancy'; ?></title>
    <meta name="description" content="<?php echo $PageData['Description'] ?? 'Professional design and development services'; ?>">
    
    <!-- Open Graph -->
    <meta property="og:title" content="<?php echo $PageData['Title'] ?? 'Design & Development Consultancy'; ?>">
    <meta property="og:description" content="<?php echo $PageData['Description'] ?? 'Professional design and development services'; ?>">
    <meta property="og:type" content="website">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="assets/css/main.css">
</head>
<body class="<?php echo $PageData['Classes'] ?? ''; ?>">
EOF

# Navigation component
cat > assets/components/nav.php << 'EOF'
<nav class="Navigation">
    <div class="Container">
        <a href="index.php" class="Logo">
            <span class="Logo__Text">Consultancy</span>
        </a>
        <ul class="Navigation__Menu">
            <li><a href="index.php" class="Navigation__Link">Home</a></li>
            <li><a href="about.php" class="Navigation__Link">About</a></li>
            <li><a href="portfolio.php" class="Navigation__Link">Portfolio</a></li>
            <li><a href="contact.php" class="Navigation__Link">Contact</a></li>
            <li><a href="blog/" class="Navigation__Link">Blog</a></li>
        </ul>
    </div>
</nav>
EOF

# Card component
cat > assets/components/card.php << 'EOF'
<?php
// Card component - Renders cards with standardized data structure
// Usage: Set $CardData array with Title, Content, Image, Url, Classes before including

$Title = $CardData['Title'] ?? '';
$Content = $CardData['Content'] ?? '';
$Image = $CardData['Image'] ?? '';
$Url = $CardData['Url'] ?? '#';
$Classes = $CardData['Classes'] ?? 'Card';
?>

<article class="Card <?php echo $Classes; ?>">
    <?php if ($Image): ?>
        <div class="Card__Image">
            <img src="<?php echo htmlspecialchars($Image); ?>" alt="<?php echo htmlspecialchars($Title); ?>">
        </div>
    <?php endif; ?>
    
    <div class="Card__Content">
        <?php if ($Title): ?>
            <h3 class="Card__Title"><?php echo htmlspecialchars($Title); ?></h3>
        <?php endif; ?>
        
        <?php if ($Content): ?>
            <p class="Card__Description"><?php echo htmlspecialchars($Content); ?></p>
        <?php endif; ?>
        
        <?php if ($Url !== '#'): ?>
            <a href="<?php echo htmlspecialchars($Url); ?>" class="Card__Link">View Project</a>
        <?php endif; ?>
    </div>
</article>
EOF

# Footer component
cat > assets/components/footer.php << 'EOF'
    <footer class="Footer">
        <div class="Container">
            <div class="Footer__Content">
                <div class="Footer__Section">
                    <h4>Design & Development Consultancy</h4>
                    <p>Visual Design, UX Design & System Architecture</p>
                </div>
                <div class="Footer__Section">
                    <h4>Services</h4>
                    <ul>
                        <li>Visual Design</li>
                        <li>UX Design</li>
                        <li>System Architecture</li>
                        <li>Development</li>
                    </ul>
                </div>
                <div class="Footer__Section">
                    <h4>Contact</h4>
                    <p>Ready to start your next project?</p>
                    <a href="contact.php" class="Button Secondary">Get In Touch</a>
                </div>
            </div>
            <div class="Footer__Bottom">
                <p>&copy; <?php echo date('Y'); ?> Design & Development Consultancy. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>
EOF

# Create SCSS files
echo "🎨 Creating SCSS files..."

# Main SCSS file
cat > assets/scss/main.scss << 'EOF'
// Main SCSS File - Imports all components
// Golden Ratio Design System

@import 'variables';
@import 'responsive';
@import 'base';
@import 'layout';
@import 'header';
@import 'footer';
@import 'card';
EOF

# Variables with Golden Ratio system
cat > assets/scss/variables.scss << 'EOF'
// Design Token System - Golden Ratio Foundation
// =============================================

// Golden Ratio Base
$GoldenRatio: 1.618;
$BaseUnit: 1rem; // 16px base

// Golden Ratio Scale
$Scale: (
  'xs': $BaseUnit / ($GoldenRatio * $GoldenRatio),    // ~0.382rem
  'sm': $BaseUnit / $GoldenRatio,                     // ~0.618rem  
  'base': $BaseUnit,                                  // 1rem
  'lg': $BaseUnit * $GoldenRatio,                     // ~1.618rem
  'xl': $BaseUnit * ($GoldenRatio * $GoldenRatio),    // ~2.618rem
  'xxl': $BaseUnit * ($GoldenRatio * $GoldenRatio * $GoldenRatio) // ~4.236rem
);

// Color System
$ColorPrimary: #1a1a1a;
$ColorSecondary: #f5f5f5;
$ColorAccent: #0066cc;
$ColorSuccess: #22c55e;
$ColorWarning: #f59e0b;
$ColorError: #ef4444;

// Typography using Golden Ratio
$FontPrimary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
$FontSecondary: 'JetBrains Mono', 'SF Mono', Consolas, monospace;

$FontSizes: (
  'small': map-get($Scale, 'sm'),      // 0.618rem
  'body': map-get($Scale, 'base'),     // 1rem
  'h3': map-get($Scale, 'lg'),         // 1.618rem
  'h2': map-get($Scale, 'xl'),         // 2.618rem
  'h1': map-get($Scale, 'xxl')         // 4.236rem
);

// Spacing using Golden Ratio
$Spacing: $Scale;

// Component Tokens
$BorderRadius: map-get($Scale, 'xs');
$BoxShadow: 0 1px 3px rgba(0,0,0,0.12);
$Transition: all 0.2s ease;
EOF

# Responsive mixins
cat > assets/scss/responsive.scss << 'EOF'
// Responsive Design System
// ========================

// Breakpoint System
$Breakpoints: (
  'small': 576px,
  'medium': 768px,
  'large': 992px,
  'xlarge': 1200px
);

// Responsive Mixin
@mixin Respond($breakpoint) {
  @if map-has-key($Breakpoints, $breakpoint) {
    @media (min-width: map-get($Breakpoints, $breakpoint)) {
      @content;
    }
  }
}

// Container Mixin
@mixin Container($maxWidth: 1200px) {
  width: 100%;
  max-width: $maxWidth;
  margin: 0 auto;
  padding: 0 map-get($Spacing, 'base');
  
  @include Respond('medium') {
    padding: 0 map-get($Spacing, 'lg');
  }
}
EOF

# Base styles
cat > assets/scss/base.scss << 'EOF'
// Base Styles & Reset
// ===================

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 16px;
  line-height: 1.6;
}

body {
  font-family: $FontPrimary;
  color: $ColorPrimary;
  background-color: white;
  font-size: map-get($FontSizes, 'body');
}

h1, h2, h3, h4, h5, h6 {
  font-weight: 600;
  line-height: 1.2;
  margin-bottom: map-get($Spacing, 'sm');
}

h1 { font-size: map-get($FontSizes, 'h1'); }
h2 { font-size: map-get($FontSizes, 'h2'); }
h3 { font-size: map-get($FontSizes, 'h3'); }

p {
  margin-bottom: map-get($Spacing, 'base');
}

a {
  color: $ColorAccent;
  text-decoration: none;
  transition: $Transition;
  
  &:hover {
    text-decoration: underline;
  }
}

img {
  max-width: 100%;
  height: auto;
}

// Container Class
.Container {
  @include Container();
}
EOF

# Layout styles
cat > assets/scss/layout.scss << 'EOF'
// Layout Components
// =================

.Main {
  min-height: calc(100vh - 200px); // Account for header/footer
}

// Button System
.Button {
  display: inline-block;
  padding: map-get($Spacing, 'sm') map-get($Spacing, 'base');
  border: none;
  border-radius: $BorderRadius;
  font-family: $FontPrimary;
  font-size: map-get($FontSizes, 'body');
  font-weight: 500;
  text-decoration: none;
  cursor: pointer;
  transition: $Transition;
  
  &.Primary {
    background-color: $ColorAccent;
    color: white;
    
    &:hover {
      background-color: darken($ColorAccent, 10%);
      text-decoration: none;
    }
  }
  
  &.Secondary {
    background-color: transparent;
    color: $ColorAccent;
    border: 1px solid $ColorAccent;
    
    &:hover {
      background-color: $ColorAccent;
      color: white;
      text-decoration: none;
    }
  }
}

// Grid System
.Grid {
  display: grid;
  gap: map-get($Spacing, 'lg');
  
  &.TwoColumn {
    @include Respond('medium') {
      grid-template-columns: 1fr 1fr;
    }
  }
  
  &.ThreeColumn {
    @include Respond('medium') {
      grid-template-columns: repeat(2, 1fr);
    }
    
    @include Respond('large') {
      grid-template-columns: repeat(3, 1fr);
    }
  }
}

// Form Elements
.FormGroup {
  margin-bottom: map-get($Spacing, 'base');
}

label {
  display: block;
  margin-bottom: map-get($Spacing, 'xs');
  font-weight: 500;
}

input, textarea {
  width: 100%;
  padding: map-get($Spacing, 'sm');
  border: 1px solid #ddd;
  border-radius: $BorderRadius;
  font-family: $FontPrimary;
  font-size: map-get($FontSizes, 'body');
  
  &:focus {
    outline: none;
    border-color: $ColorAccent;
    box-shadow: 0 0 0 2px rgba($ColorAccent, 0.1);
  }
}

textarea {
  min-height: 120px;
  resize: vertical;
}
EOF

# Header styles
cat > assets/scss/header.scss << 'EOF'
// Header Component Styles
// =======================

.Navigation {
  background-color: white;
  border-bottom: 1px solid #eee;
  position: sticky;
  top: 0;
  z-index: 100;
  
  .Container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: map-get($Spacing, 'base');
    padding-bottom: map-get($Spacing, 'base');
  }
}

.Logo {
  &__Text {
    font-size: map-get($FontSizes, 'h3');
    font-weight: 600;
    color: $ColorPrimary;
  }
}

.Navigation {
  &__Menu {
    display: flex;
    list-style: none;
    gap: map-get($Spacing, 'lg');
  }
  
  &__Link {
    font-weight: 500;
    color: $ColorPrimary;
    
    &:hover {
      color: $ColorAccent;
      text-decoration: none;
    }
  }
}

// Hero Section
.Hero {
  background-color: $ColorSecondary;
  padding: map-get($Spacing, 'xxl') 0;
  text-align: center;
  
  &__Title {
    margin-bottom: map-get($Spacing, 'base');
  }
  
  &__Subtitle {
    font-size: map-get($FontSizes, 'h3');
    color: lighten($ColorPrimary, 20%);
  }
}
EOF

# Footer styles
cat > assets/scss/footer.scss << 'EOF'
// Footer Component Styles
// =======================

.Footer {
  background-color: $ColorPrimary;
  color: white;
  margin-top: map-get($Spacing, 'xxl');
  
  &__Content {
    display: grid;
    gap: map-get($Spacing, 'xl');
    padding: map-get($Spacing, 'xxl') 0 map-get($Spacing, 'xl') 0;
    
    @include Respond('medium') {
      grid-template-columns: repeat(3, 1fr);
    }
  }
  
  &__Section {
    h4 {
      color: white;
      margin-bottom: map-get($Spacing, 'base');
    }
    
    ul {
      list-style: none;
      
      li {
        margin-bottom: map-get($Spacing, 'xs');
      }
    }
    
    a {
      color: rgba(white, 0.8);
      
      &:hover {
        color: white;
      }
    }
  }
  
  &__Bottom {
    border-top: 1px solid rgba(white, 0.2);
    padding: map-get($Spacing, 'base') 0;
    text-align: center;
    color: rgba(white, 0.6);
  }
}
EOF

# Card styles
cat > assets/scss/card.scss << 'EOF'
// Card Component Styles
// =====================

.Card {
  background: white;
  border-radius: $BorderRadius;
  box-shadow: $BoxShadow;
  transition: $Transition;
  overflow: hidden;
  
  &:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    transform: translateY(-2px);
  }
  
  &__Image {
    img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }
  }
  
  &__Content {
    padding: map-get($Spacing, 'base');
  }
  
  &__Title {
    margin-bottom: map-get($Spacing, 'sm');
    color: $ColorPrimary;
  }
  
  &__Description {
    color: lighten($ColorPrimary, 20%);
    margin-bottom: map-get($Spacing, 'base');
  }
  
  &__Link {
    font-weight: 500;
    color: $ColorAccent;
  }
}

// Portfolio specific cards
.PortfolioCard {
  // Additional styles for portfolio cards
}

// Services specific cards  
.ServiceCard {
  text-align: center;
  
  .Card__Content {
    padding: map-get($Spacing, 'lg');
  }
}
EOF

# Create data files
echo "📊 Creating data files..."

# Portfolio JSON
cat > assets/data/portfolio.json << 'EOF'
{
  "projects": [
    {
      "id": "sample-project-1",
      "title": "E-commerce Website Redesign",
      "client": "Sample Client",
      "services": ["Visual Design", "UX Design", "Development"],
      "description": "Complete redesign and development of a modern e-commerce platform with focus on conversion optimization and user experience.",
      "image": "/assets/images/portfolio/project-1.jpg",
      "gallery": ["detail-1.jpg", "detail-2.jpg"],
      "url": "https://example.com",
      "featured": true,
      "date": "2024-12-15"
    },
    {
      "id": "sample-project-2", 
      "title": "SaaS Dashboard Interface",
      "client": "Tech Startup",
      "services": ["UX Design", "System Architecture"],
      "description": "Design and architecture of a complex dashboard interface for data visualization and user management.",
      "image": "/assets/images/portfolio/project-2.jpg",
      "gallery": ["detail-3.jpg", "detail-4.jpg"],
      "url": "https://example2.com",
      "featured": true,
      "date": "2024-11-20"
    }
  ]
}
EOF

# Create package.json for SCSS compilation
echo "📦 Creating package.json..."

cat > package.json << 'EOF'
{
  "name": "design-development-consultancy",
  "version": "1.0.0",
  "description": "Professional consultancy website with golden ratio design system",
  "scripts": {
    "css": "sass assets/scss/main.scss assets/css/main.css",
    "css:watch": "sass --watch assets/scss/main.scss:assets/css/main.css",
    "css:compressed": "sass assets/scss/main.scss assets/css/main.css --style=compressed"
  },
  "dependencies": {},
  "devDependencies": {
    "sass": "^1.69.0"
  }
}
EOF

# Create .htaccess for clean URLs
echo "⚙️ Creating .htaccess..."

cat > .htaccess << 'EOF'
# Clean URLs and Performance
RewriteEngine On

# Remove .php extension
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^([^\.]+)$ $1.php [NC,L]

# Cache static assets
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType image/png "access plus 1 month"
    ExpiresByType image/jpg "access plus 1 month"
    ExpiresByType image/jpeg "access plus 1 month"
    ExpiresByType image/gif "access plus 1 month"
</IfModule>

# Compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>
EOF

# Create JavaScript file
echo "🎯 Creating JavaScript files..."

cat > assets/js/main.js << 'EOF'
// Main JavaScript File
// ====================

document.addEventListener('DOMContentLoaded', function() {
    console.log('Design & Development Consultancy - Site Loaded');
    
    // Add any interactive functionality here
});
EOF

# Create documentation files
echo "📚 Creating documentation..."

# Conventions documentation
cat > docs/conventions.md << 'EOF'
# Project Conventions & Rules

## Naming Standards
- **PascalCase**: CSS classes, functions, component references, variables
- **kebab-case**: File names only
- **Examples**: 
  - `card.php` file
  - `.CardPrimary` CSS class  
  - `RenderCard()` function
  - `$CardData` variable

## SCSS Architecture
- **Structure**: Single `assets/scss/` folder with modular files
- **Imports**: All files imported through `main.scss`
- **Components**: Separate SCSS file for each component
- **Organization**: 
  - `variables.scss` - Design tokens and golden ratio system
  - `responsive.scss` - Breakpoint mixins and utilities  
  - `base.scss` - Global styles and resets
  - `layout.scss` - Grid, flexbox, and layout utilities
  - Component files - `header.scss`, `card.scss`, etc.

## Golden Ratio Design System
- **Base Unit**: 1rem (16px)
- **Scale Calculation**: Base unit multiplied/divided by golden ratio (1.618)
- **Usage Rule**: All measurements must use predefined scale values
- **Scale Values**:
  - `xs`: ~0.382rem
  - `sm`: ~0.618rem  
  - `base`: 1rem
  - `lg`: ~1.618rem
  - `xl`: ~2.618rem
  - `xxl`: ~4.236rem
- **Implementation**: Use `map-get($Scale, 'value')` or `map-get($FontSizes, 'value')`

## Component Architecture
- **Location**: `assets/components/` directory
- **Data Pattern**: All components receive standardized `$Data` object
- **Required Keys**: Components should handle `Title`, `Content`, `Classes`, `Image`, `Url`
- **Error Handling**: Components should gracefully handle missing data keys
- **Output Method**: Components echo HTML directly (not return strings)
- **Separation**: PHP handles structure/logic, SCSS handles presentation

## PHP Standards
- **File Organization**: One component per file
- **Data Sanitization**: Always use `htmlspecialchars()` for output
- **Includes**: Use `require_once` for critical files
- **Functions**: PascalCase naming (e.g., `LoadPortfolioData()`)
- **Variables**: PascalCase naming (e.g., `$CardData`)

## Responsive Design
- **Approach**: Mobile-first with min-width breakpoints
- **Breakpoints**: 
  - Small: 576px
  - Medium: 768px  
  - Large: 992px
  - XLarge: 1200px
- **Usage**: Always use `Respond()` mixin, never raw media queries
- **Container**: Use `Container()` mixin for consistent max-width and padding

## Data Management
- **Portfolio**: Single JSON file (`assets/data/portfolio.json`)
- **Structure**: Standardized schema with required fields
- **Contact Forms**: JSON logging + email notifications
- **File Handling**: Always check file existence before reading

## SEO Implementation
- **Current Phase**: Basic meta tags, semantic HTML, Open Graph
- **Meta Data**: Dynamic per-page title/description via `$PageData`
- **Structure**: Proper heading hierarchy (h1 → h2 → h3)
- **Future**: Advanced SEO techniques post-launch

## Build Process
- **SCSS Compilation**: Node.js Sass CLI
- **Commands**: 
  - `npm run css` - Single compile
  - `npm run css:watch` - Watch mode
  - `npm run css:compressed` - Production build
- **Workflow**: Develop in SCSS, compile to CSS, never edit CSS directly

## File Organization Rules
- **Assets**: All assets in `assets/` subdirectories
- **Components**: Reusable PHP components in `assets/components/`
- **Data**: JSON files in `assets/data/`
- **Documentation**: All docs in `docs/` directory
- **Clean Structure**: No loose files in root except main pages

## Version Control
- **Documentation**: Update conventions.md for any architectural changes
- **Symbol Index**: Update symbol-index.md for every new component/function
- **Commits**: Document convention changes in commit messages
- **Living Documents**: Both convention and symbol files evolve with project

## Quality Standards
- **Validation**: HTML5 semantic markup
- **Accessibility**: Proper alt tags, labels, semantic elements
- **Performance**: Optimize images, minimize HTTP requests
- **Browser Support**: Modern browsers (IE11+ if required)
- **Code Quality**: Consistent indentation, meaningful names, comments for complex logic

---

*This document is updated whenever architectural decisions are made or conventions are established.*
EOF

# Symbol Index documentation
cat > docs/symbol-index.md << 'EOF'
# Symbol Index - Functional Context Map

*This document maps all components, functions, and relationships in the system.*

## PHP Functions

### LoadPortfolioData()
- **Location**: `portfolio.php`
- **Purpose**: Loads and parses portfolio JSON data
- **Dependencies**: `assets/data/portfolio.json`
- **Returns**: Array with 'projects' key or empty array if file missing
- **Called By**: `portfolio.php` main logic
- **Error Handling**: Returns empty projects array if JSON file doesn't exist

### Component Data Pattern
- **Standard**: All components expect `$Data` associative array
- **Required Keys**: 
  - `Title` (string) - Component heading
  - `Content` (string) - Main content text
  - `Classes` (string) - CSS class additions
- **Optional Keys**:
  - `Image` (string) - Image path
  - `Url` (string) - Link destination
- **Usage Pattern**: Set `$CardData` array, then include component file

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
- **Used By**: `portfolio.php` for project display

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

## SCSS System

### Golden Ratio Variables
- **Location**: `assets/scss/variables.scss`
- **Core Values**:
  - `$GoldenRatio: 1.618` - Mathematical constant
  - `$BaseUnit: 1rem` - Base measurement unit
- **Scale Map**: `$Scale` with calculated proportional values
- **Font Scale**: `$FontSizes` using golden ratio proportions
- **Usage**: `map-get($Scale, 'lg')` returns `~1.618rem`
- **Dependencies**: Used throughout all component SCSS files

### Responsive System
- **Location**: `assets/scss/responsive.scss`
- **Breakpoint Map**: `$Breakpoints` with standard mobile-first values
- **Primary Mixin**: `@include Respond('medium') { ... }`
- **Container Mixin**: `@include Container()` for max-width layouts
- **Dependencies**: Used in layout.scss, header.scss, footer.scss, card.scss
- **Mobile-First**: All breakpoints use min-width media queries

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

## Data Structures

### Portfolio JSON Schema
- **Location**: `assets/data/portfolio.json`
- **Root Structure**: Object with `projects` array
- **Project Object Fields**:
  - `id` (string) - Unique identifier
  - `title` (string) - Project name
  - `client` (string) - Client name
  - `services` (array) - Service types provided
  - `description` (string) - Project summary
  - `image` (string) - Thumbnail image path
  - `gallery` (array) - Additional image paths
  - `url` (string) - Live project URL
  - `featured` (boolean) - Homepage display flag
  - `date` (string) - Completion date (YYYY-MM-DD)
- **Dependencies**: Read by `LoadPortfolioData()` function
- **Usage**: Filtered and displayed by `portfolio.php`

### Page Data Structure
- **Usage**: `$PageData` array in all main PHP pages
- **Standard Fields**:
  - `Title` (string) - Page title for <title> tag
  - `Description` (string) - Meta description
  - `Classes` (string) - Body CSS classes
- **Dependencies**: Used by `header.php` for meta tags and body classes
- **SEO Impact**: Direct mapping to HTML meta elements

## File Dependencies

### SCSS Import Chain
- **Entry Point**: `assets/scss/main.scss`
- **Import Order**: 
  1. `variables.scss` - Must be first (defines tokens)
  2. `responsive.scss` - Mixins used by other files
  3. `base.scss` - Global styles
  4. `layout.scss` - Layout utilities
  5. `header.scss`, `footer.scss`, `card.scss` - Components
- **Build Output**: `assets/css/main.css`
- **Watch Command**: `npm run css:watch`

### PHP Include Chain
- **Page Structure**: 
  1. Main page (index.php, about.php, etc.)
  2. `require_once 'assets/components/header.php'`
  3. `require_once 'assets/components/nav.php'`
  4. Page content with component includes
  5. `require_once 'assets/components/footer.php'`
- **Component Includes**: Use relative paths from page location
- **Data Flow**: Set data arrays before including components

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
EOF

echo ""
echo "📁 Creating placeholder directories..."
mkdir -p assets/images/portfolio

echo ""
echo "✅ Initialization complete!"
echo ""
echo "🚀 Next Steps:"
echo "1. Run 'npm install' to install Sass"
echo "2. Run 'npm run css:watch' to start SCSS compilation"
echo "3. Start developing your content and customizing styles"
echo "4. Update docs/symbol-index.md as you add new components"
echo ""
echo "📋 File Structure Created:"
echo "├── Main Pages: index.php, about.php, contact.php, portfolio.php"
echo "├── Components: header.php, nav.php, card.php, footer.php"  
echo "├── SCSS System: Complete golden ratio design system"
echo "├── Documentation: conventions.md, symbol-index.md"
echo "├── Sample Data: portfolio.json with example projects"
echo "└── Build System: package.json with Sass compilation"
echo ""
echo "Happy coding! 🎉"