# Repository Structure

*Clean, professional organization for the design consultancy website.*

## **📁 Root Directory**

```
JoinerySystemworks/
├── .git/                      # Git version control
├── assets/                    # Website assets & components
├── docs/                      # Project documentation
├── scripts/                   # Build & utility scripts
├── tests/                     # Testing files
├── test-results/              # Test execution results
│
├── *.php                      # Main website pages
├── package.json               # Node.js dependencies
├── README.md                  # Project overview
├── .htaccess                  # Apache configuration
└── .gitignore                 # Ignored files configuration
```

## **🎨 Website Assets (/assets/)**

```
assets/
├── components/                # PHP components
├── scss/                      # SCSS source files
├── css/                       # Compiled CSS output
├── data/                      # JSON data files
├── blog/                      # Blog system
├── js/                        # JavaScript files
└── images/                    # Static images
```

## **📚 Documentation (/docs/)**

```
docs/
├── conventions.md             # Coding standards & patterns
└── symbol-index.md            # System mapping & references
```


## **🧪 Testing (/tests/ & /test-results/)**

```
tests/                        # Test specifications
├── *.spec.js                 # Playwright test files

test-results/                 # Test execution results
├── playwright-report/        # Test reports
└── execution-data/           # Test run data
```

## **⚙️ Configuration Files**

- **package.json** - Node.js dependencies & build scripts
- **.gitignore** - Files excluded from version control
- **.htaccess** - Apache server configuration
- **playwright.config.js** - Testing configuration
- **init.sh** - Project initialization script

## **🎯 Organization Benefits**

### **Clean Root Directory**
- Only essential files at root level
- Clear separation of concerns
- Professional appearance

### **Logical Grouping**
- **Development**: Assets, docs, scripts in organized directories  
- **Website Code**: PHP pages and components cleanly separated
- **Testing**: All testing infrastructure contained
- **Documentation**: Clear project documentation and conventions

### **Version Control Optimization**
- Private files properly gitignored
- Testing artifacts excluded from commits
- Only production-ready code tracked

### **Professional Structure**
- Industry-standard directory organization
- Clear file naming conventions  
- Scalable architecture for growth

---

*This structure supports clean PHP website development with professional standards and maintainable architecture.*