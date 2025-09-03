#!/usr/bin/env node
/**
 * Documentation Compliance Validator
 * Enforces mandatory documentation requirements for JoinerySystemworks
 * 
 * BLOCKING VALIDATION: This script will exit with code 1 (failure) if any
 * documentation requirements are not met, preventing git commits.
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Colors for terminal output
const colors = {
    red: '\x1b[31m',
    green: '\x1b[32m',
    yellow: '\x1b[33m',
    blue: '\x1b[34m',
    reset: '\x1b[0m'
};

class DocumentationValidator {
    constructor() {
        this.errors = [];
        this.warnings = [];
        this.symbolIndex = '';
        this.conventions = '';
        this.phpFiles = [];
        this.scssFiles = [];
        this.componentFiles = [];
    }

    // Load documentation files
    loadDocumentation() {
        try {
            this.symbolIndex = fs.readFileSync('docs/symbol-index.md', 'utf8');
            this.conventions = fs.readFileSync('docs/conventions.md', 'utf8');
        } catch (error) {
            this.errors.push('❌ CRITICAL: Documentation files missing or unreadable');
            return false;
        }
        return true;
    }

    // Scan codebase for files that need documentation
    scanCodebase() {
        // Get all PHP files
        this.phpFiles = this.getAllFiles('.', '.php')
            .filter(file => !file.includes('vendor/') && !file.includes('node_modules/'));

        // Get component files specifically
        this.componentFiles = this.getAllFiles('assets/components', '.php');

        // Get SCSS files
        this.scssFiles = this.getAllFiles('assets/scss', '.scss');
    }

    // Utility to get all files with specific extension
    getAllFiles(dir, ext) {
        if (!fs.existsSync(dir)) return [];
        
        const files = [];
        const items = fs.readdirSync(dir);
        
        for (const item of items) {
            const fullPath = path.join(dir, item);
            if (fs.statSync(fullPath).isDirectory()) {
                files.push(...this.getAllFiles(fullPath, ext));
            } else if (item.endsWith(ext)) {
                files.push(fullPath);
            }
        }
        return files;
    }

    // Extract PHP functions from file content
    extractPHPFunctions(filePath) {
        const content = fs.readFileSync(filePath, 'utf8');
        const functions = [];
        
        // Match function definitions
        const functionRegex = /function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(/g;
        let match;
        
        while ((match = functionRegex.exec(content)) !== null) {
            const functionName = match[1];
            const lineNumber = content.substring(0, match.index).split('\n').length;
            functions.push({
                name: functionName,
                file: filePath,
                line: lineNumber
            });
        }
        
        return functions;
    }

    // Validate that all PHP functions are documented
    validatePHPFunctions() {
        const allFunctions = [];
        
        // Scan all PHP files for functions
        for (const file of this.phpFiles) {
            const functions = this.extractPHPFunctions(file);
            allFunctions.push(...functions);
        }

        // Check each function is documented in symbol-index.md
        for (const func of allFunctions) {
            const isDocumented = this.symbolIndex.includes(`### ${func.name}()`);
            const hasLocation = this.symbolIndex.includes(`**Location**: \`${func.file}:`);
            
            if (!isDocumented) {
                this.errors.push(
                    `❌ UNDOCUMENTED FUNCTION: ${func.name}() in ${func.file}:${func.line}\n` +
                    `   Required: Add to docs/symbol-index.md with location, purpose, dependencies`
                );
            } else if (!hasLocation) {
                this.warnings.push(
                    `⚠️  INCOMPLETE DOCS: ${func.name}() documented but missing accurate location reference`
                );
            }
        }
    }

    // Validate that all components are documented
    validateComponents() {
        for (const componentFile of this.componentFiles) {
            const componentName = path.basename(componentFile);
            const isDocumented = this.symbolIndex.includes(`### ${componentName}`);
            
            if (!isDocumented) {
                this.errors.push(
                    `❌ UNDOCUMENTED COMPONENT: ${componentFile}\n` +
                    `   Required: Add to docs/symbol-index.md with location, purpose, dependencies`
                );
            }
        }
    }

    // Validate that all SCSS files are documented
    validateSCSSFiles() {
        for (const scssFile of this.scssFiles) {
            const fileName = path.basename(scssFile, '.scss');
            const isInIndex = this.symbolIndex.includes(fileName);
            const isInConventions = this.conventions.includes(fileName);
            
            if (!isInIndex && !isInConventions) {
                this.errors.push(
                    `❌ UNDOCUMENTED SCSS: ${scssFile}\n` +
                    `   Required: Add to docs/symbol-index.md or docs/conventions.md`
                );
            }
        }
    }

    // Validate PHP pages are documented
    validatePHPPages() {
        const mainPages = this.phpFiles.filter(file => 
            !file.includes('assets/components/') && 
            !file.includes('vendor/') &&
            file.match(/^[^\/]*\.php$/) // Root level PHP files
        );

        for (const page of mainPages) {
            const pageName = path.basename(page);
            const isDocumented = this.symbolIndex.includes(`### ${pageName}`);
            
            if (!isDocumented) {
                this.errors.push(
                    `❌ UNDOCUMENTED PAGE: ${page}\n` +
                    `   Required: Add to docs/symbol-index.md with purpose, dependencies, URL structure`
                );
            }
        }
    }

    // Check for recent git changes that might need documentation
    validateRecentChanges() {
        try {
            // Get files changed in the last commit
            const changedFiles = execSync('git diff --name-only HEAD~1 HEAD', { encoding: 'utf8' })
                .split('\n')
                .filter(file => file.length > 0);

            const needsDocumentation = changedFiles.filter(file => 
                file.endsWith('.php') || 
                file.endsWith('.scss') ||
                file.startsWith('assets/components/')
            );

            if (needsDocumentation.length > 0) {
                this.warnings.push(
                    `⚠️  RECENT CHANGES: The following files were recently modified:\n` +
                    needsDocumentation.map(file => `   - ${file}`).join('\n') +
                    `\n   Verify documentation is up to date`
                );
            }
        } catch (error) {
            // Ignore git errors - might be initial commit
        }
    }

    // Main validation runner
    validate() {
        console.log(`${colors.blue}🔍 Validating documentation compliance...${colors.reset}`);
        
        if (!this.loadDocumentation()) {
            return false;
        }

        this.scanCodebase();
        this.validatePHPFunctions();
        this.validateComponents();
        this.validateSCSSFiles();
        this.validatePHPPages();
        this.validateRecentChanges();

        // Report results
        if (this.warnings.length > 0) {
            console.log(`\n${colors.yellow}WARNINGS:${colors.reset}`);
            this.warnings.forEach(warning => console.log(warning));
        }

        if (this.errors.length > 0) {
            console.log(`\n${colors.red}BLOCKING ERRORS - COMMIT PREVENTED:${colors.reset}`);
            this.errors.forEach(error => console.log(error));
            
            console.log(`\n${colors.red}🚫 DOCUMENTATION COMPLIANCE FAILED${colors.reset}`);
            console.log(`${colors.yellow}Fix all errors above before committing.${colors.reset}`);
            return false;
        } else {
            console.log(`\n${colors.green}✅ Documentation compliance verified${colors.reset}`);
            return true;
        }
    }
}

// Run validation
const validator = new DocumentationValidator();
const isValid = validator.validate();

// Exit with appropriate code
process.exit(isValid ? 0 : 1);