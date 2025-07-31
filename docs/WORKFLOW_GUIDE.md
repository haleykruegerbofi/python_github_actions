# Complete CI/CD Workflow Guide

This guide explains every step of the CI/CD pipeline from initial development to production deployment.

## Table of Contents
1. [Overview](#overview)
2. [Local Development Phase](#local-development-phase)
3. [GitHub Actions Automation Phase](#github-actions-automation-phase)
4. [Environment Progression](#environment-progression)
5. [Workflow Diagrams](#workflow-diagrams)

---

## Overview

This CI/CD pipeline implements a structured flow:

```
Local Development → GitHub Push → Automated Testing → Code Review → Development → QA/UAT → Production
```

### Key Principles
- **No direct commits** to protected branches (development, uat, main)
- **All changes** go through pull requests
- **Automated quality gates** at every step
- **Human approval** required for production

> 🛡️ **Branch Protection Enforces These Rules** - [See Branch Protection Setup](BRANCH_PROTECTION_SETUP.md)

---

## Local Development Phase

> **Note**: This phase happens on the developer's machine - NO GitHub Actions involved yet!

### Step 1: Create Feature Branch

```bash
# Always start from main to get latest code
git checkout main
git pull origin main

# Create your feature branch
git checkout -b feature/PBI-123-add-new-feature
```

**Naming Convention**: `feature/PBI-XXX-description` or `bugfix/ISSUE-XXX-description`

### Step 2: Write Code

Make your changes to the codebase. For example:

```python
# src/calculator.py
def new_function(self, x: float) -> float:
    """Add your new functionality."""
    # Implementation here
    return result
```

### Step 3: Write Tests

Add corresponding tests:

```python
# tests/test_calculator.py
def test_new_function(self):
    """Test the new functionality."""
    assert calc.new_function(5) == expected_result
```

### Step 4: Local Validation (Optional but Recommended)

Run the validation script to catch issues early:

```bash
# Windows
.\scripts\run_local_validation.ps1

# Mac/Linux
./scripts/run_local_validation.sh
```

This runs locally:
1. Black formatter check
2. Import sorting (isort)  
3. Flake8 linting
4. Type checking (mypy)
5. SDLC standards check
6. Security scan (bandit)
7. Unit tests with coverage

**Why do this?**
- Immediate feedback (seconds vs minutes)
- Fix issues before pushing
- Save GitHub Actions minutes
- Avoid failed builds in your PR

### Step 5: Commit and Push

```bash
# Stage your changes
git add .

# Commit with conventional commit message
git commit -m "feat: Add new calculation function

- Implement new_function for advanced calculations
- Add comprehensive unit tests
- Update documentation"

# Push to GitHub (THIS TRIGGERS GITHUB ACTIONS!)
git push origin feature/PBI-123-add-new-feature
```

---

## GitHub Actions Automation Phase

> **Note**: Everything below happens automatically on GitHub's servers!

### Step 6: Push Triggers Initial Workflow

When you push, `developer-workflow.yml` triggers:

```yaml
on:
  push:
    branches:
      - 'feature/**'
```

**What happens:**
1. GitHub spins up Ubuntu virtual machine
2. Checks out your code
3. Sets up Python environment
4. Runs ALL the same checks from Step 4
5. Posts status to your branch

### Step 7: Create Pull Request

On GitHub:
1. Navigate to your repository
2. Click "Compare & pull request"
3. Fill out the PR template:
   - Description of changes
   - Related issue/PBI number
   - Type of change
   - Testing performed
   - Checklist items

### Step 8: PR Triggers Enhanced Workflow

Creating a PR triggers `developer-workflow.yml` again:

```yaml
on:
  pull_request:
    branches:
      - development
```

**Additional PR-specific checks:**
- PR validation
- Coverage commenting
- Status checks for merge requirements

### Step 9: Automated Check Results

GitHub shows status on your PR:

```
✅ lint-and-format       Success - 45s
✅ sdlc-standards        Success - 30s  
✅ security-scan         Success - 20s
✅ unit-tests           Success - 1m 10s
✅ build-validation      Success - 35s
```

If any fail:
```
❌ unit-tests           Failed - 1m 10s
   View details → "AssertionError: Expected 10 but got 11"
```

### Step 10: Code Review Process

**If all checks pass:**
1. Automated comment: "All checks passed! Ready for review"
2. Reviewer examines code changes
3. Reviewer may request changes
4. After approval, PR can be merged

**If checks fail:**
1. Fix issues locally
2. Push fixes (returns to Step 6)
3. Checks run again automatically

> 🛡️ **Branch Protection in Action Here:**
> - ❌ Cannot merge until ALL status checks pass
> - ❌ Cannot merge without required reviews (1 for dev, 2 for main)
> - ❌ Merge button is physically disabled by GitHub until requirements met

---

## Environment Progression

### Step 11: Development Integration

After PR approval and merge to `development`:
- Code is now in integration environment
- Other features may also be here
- Ready for QA testing

### Step 12: QA/UAT Promotion

QA Lead creates PR: `development` → `uat`

This triggers `qa-uat-workflow.yml`:

```yaml
jobs:
  qa-validation:     # Smoke tests
  integration-tests: # Full integration suite
  performance-tests: # Performance benchmarks
  security-validation: # Security scanning
  uat-deployment:    # Deploy to UAT
```

**UAT-Specific Features:**
- Scheduled test runs (daily at 2 AM)
- Manual test suite selection
- Extended integration testing
- Performance benchmarking

### Step 13: Production Release

Release Manager creates PR: `uat` → `main`

This triggers `production-release.yml`:

```yaml
jobs:
  pre-release-validation:  # Verify PR from UAT
  final-tests:            # Last test run
  create-release:         # Version tagging
  production-deployment:  # Deploy to prod
  release-notification:   # Notify stakeholders
```

**Production-Specific Features:**
- Automatic version tagging (v1.0.0, v1.0.1, etc.)
- GitHub Release creation
- Changelog generation
- Deployment status tracking
- Rollback plan preparation
- Scheduled production jobs

---

## Workflow Diagrams

### Developer Workflow
```
Developer Machine                    GitHub
     |                                |
  Write Code                          |
     ↓                                |
  Run Tests Locally                   |
     ↓                                |
  Fix Issues                          |
     ↓                                |
  git push ----------------------→ Push triggers workflow
     |                                ↓
     |                          Run automated checks
     |                                ↓
  Create PR ------------------→ PR triggers workflow again
                                     ↓
                              All checks must pass
                                     ↓
                              Code Review Required
                                     ↓
                              Merge to Development
```

### Environment Flow
```
feature/branch
     ↓ (PR + Reviews)
development
     ↓ (PR + QA Tests)
uat
     ↓ (PR + Final Checks)
main (production)
     ↓
Tagged Release (v1.0.0)
```

### Check Execution Timeline
```
Time →
00s: Workflow starts
05s: Environment setup
10s: Dependencies installed
15s: |-- Black formatter --|
20s: |-- isort check -----|
25s: |-- Flake8 ---------|
30s: |-- MyPy -----------|
35s: |-- SDLC Standards --|
40s: |-- Security Scan ---|
45s: |-- Unit Tests ------|-------|
90s:                              |-- Coverage Report
95s: Build validation
100s: ✅ All checks complete
```

---

## Common Scenarios

### Scenario 1: Quick Bug Fix
1. Create `bugfix/ISSUE-456-fix-calculation`
2. Fix bug (5 min)
3. Run local validation (30 sec)
4. Push and create PR (1 min)
5. Automated checks (2 min)
6. Quick review and merge (5 min)
**Total: ~15 minutes to development**

### Scenario 2: Failed PR Checks
1. Push code
2. ❌ Linting fails - Black wants reformatting
3. Run `black src/ tests/` locally
4. Push fix
5. ✅ All checks pass
6. Proceed with review

### Scenario 3: Production Hotfix
1. Create `hotfix/critical-bug` from `main`
2. Fix issue
3. Create PR directly to `main` (with justification)
4. Emergency review process
5. Deploy with `skip_tests: true` if critical
6. Follow up with proper testing

---

## Key Automation Points

### What's Automated
- ✅ Code formatting validation
- ✅ Linting and style checks
- ✅ Type checking
- ✅ Security scanning
- ✅ Unit test execution
- ✅ Coverage calculation
- ✅ Build validation
- ✅ Version tagging
- ✅ Release notes generation
- ✅ Deployment (simulated)

### What's NOT Automated
- ❌ Writing code
- ❌ Writing tests
- ❌ Code review approval
- ❌ PR merge decision
- ❌ Release timing decision
- ❌ Rollback decision

---

## Best Practices

1. **Always run local validation** before pushing
2. **Write tests** for all new code
3. **Keep PRs small** and focused
4. **Use meaningful commit messages**
5. **Fill out PR templates** completely
6. **Don't skip code reviews**
7. **Monitor GitHub Actions** for failures
8. **Maintain 80%+ test coverage**

---

## Troubleshooting

### "My PR checks are failing"
1. Click "Details" on the failed check
2. Read the error message
3. Fix locally and push again

### "Local validation passes but GitHub fails"
- Check Python version matches
- Ensure all dependencies are in requirements.txt
- Verify no hardcoded paths

### "Coverage dropped below 80%"
- Add tests for new code
- Check coverage report for untested lines
- Focus on critical business logic first

---

## Summary

The pipeline ensures:
1. **Quality** - Nothing broken reaches production
2. **Consistency** - Same standards for everyone
3. **Visibility** - Clear status at every step
4. **Automation** - Reduce manual work
5. **Safety** - Multiple gates before production

Remember: The automation is there to help you ship quality code faster, not to slow you down! 