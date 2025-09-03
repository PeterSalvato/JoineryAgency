# Documentation Enforcement System

## 🔒 ACTIVE ENFORCEMENT MECHANISMS

### 1. Git Pre-Commit Hook
- **Location**: `.git/hooks/pre-commit`
- **Function**: Automatically blocks commits that don't meet documentation requirements
- **Bypass**: Use `git commit --no-verify` (NOT RECOMMENDED - violates project policy)

### 2. Validation Script  
- **Location**: `scripts/validate-docs.js`
- **Function**: Scans codebase for undocumented functions, components, and pages
- **Usage**: Run `npm run docs:check` before commits

### 3. NPM Scripts
- `npm run docs:check` - Validate documentation compliance
- `npm run docs:setup` - Initialize enforcement mechanisms
- `npm run commit:safe` - Safe commit with documentation validation
- `npm run commit:force` - Force commit bypassing checks (DISCOURAGED)

## ⚠️ BLOCKING CONDITIONS

The system will BLOCK commits when:

1. **New PHP Functions** found without symbol-index.md documentation
2. **New Components** in `assets/components/` without documentation  
3. **New PHP Pages** without symbol-index.md entries
4. **New SCSS Files** without mention in documentation
5. **Inaccurate Line References** in symbol-index.md

## ✅ COMPLIANCE REQUIREMENTS

To pass validation, ensure:

1. **Every PHP function** has an entry in `docs/symbol-index.md` with:
   - Location (file:line)
   - Purpose description
   - Parameters and return values
   - Dependencies

2. **Every component** documented with:
   - File location
   - Data requirements
   - CSS dependencies
   - Usage patterns

3. **Every page** documented with:
   - Purpose and features
   - Dependencies
   - URL structure
   - Related CSS

4. **Architecture changes** reflected in `docs/conventions.md`

## 🚫 NO BYPASS POLICY

- Documentation updates are MANDATORY, not optional
- "I'll update docs later" is not acceptable
- All changes must include documentation in the same commit
- Use of `--no-verify` violates project standards

## 🔧 TROUBLESHOOTING

**If validation fails:**
1. Read error messages carefully
2. Update required documentation files
3. Ensure line numbers are accurate
4. Run `npm run docs:check` to verify fixes
5. Commit with updated documentation

**If hooks aren't working:**
- Run `npm run docs:setup` to reinitialize
- Check file permissions with `ls -la .git/hooks/pre-commit`
- Ensure Node.js is available in PATH