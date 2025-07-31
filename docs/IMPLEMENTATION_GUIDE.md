# Step-by-Step Implementation Guide

## Overview

This guide provides detailed instructions for implementing the Python CI/CD pipeline with GitHub Actions. Total estimated time: **6-8 hours**.

## Prerequisites

- GitHub account with Actions enabled
- Python 3.8+ installed locally
- Git installed and configured
- Basic knowledge of Python and Git

---

## Phase 1: Repository Setup (30-45 minutes)

### Step 1: Create GitHub Repository (10 minutes)

1. Go to GitHub and create a new repository
2. Name it appropriately (e.g., `python-cicd-demo`)
3. Initialize with a README (optional, we'll replace it)
4. Set repository visibility (public or private)

### Step 2: Clone and Setup Local Environment (10 minutes)

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/python-cicd-demo.git
cd python-cicd-demo

# Copy all the files from this implementation
# The file structure should match what was created

# Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt
```

### Step 3: Configure Repository Settings (15 minutes)

1. Go to Settings → Secrets and variables → Actions
2. Add the following secrets:
   - `SLACK_WEBHOOK_URL` (optional)
   - `TEAMS_WEBHOOK_URL` (optional)
   - `EMAIL_SERVER` (optional)
   - `EMAIL_USERNAME` (optional)
   - `EMAIL_PASSWORD` (optional)

3. Add the following variables:
   - `PYTHON_VERSION`: `3.9`
   - `MIN_COVERAGE`: `80`

4. Configure branch protection rules:
   - **[See detailed Branch Protection Setup Guide](BRANCH_PROTECTION_SETUP.md)**
   - Quick summary:
     - Protect `main`: 2 reviews, all checks must pass
     - Protect `development`: 1 review, all checks must pass  
     - Protect `uat`: 1 review, QA checks must pass

### Step 4: Create Initial Branches (10 minutes)

```bash
# Create development branch
git checkout -b development
git push -u origin development

# Create UAT branch
git checkout -b uat
git push -u origin uat

# Return to main
git checkout main
```

---

## Phase 2: Implement SDLC Standards (1.5-2 hours)

### Step 1: Test the SDLC Checker (15 minutes)

```bash
# Run the SDLC standards checker
python scripts/check_sdlc_standards.py

# Fix any issues reported
```

### Step 2: Run Linting Tools (20 minutes)

```bash
# Format code with Black
black src/ tests/

# Sort imports
isort src/ tests/

# Check with flake8
flake8 src/ tests/

# Type checking
mypy src/

# Security scan
bandit -r src/
```

### Step 3: Run Tests Locally (15 minutes)

```bash
# Run tests with coverage
pytest

# Generate HTML coverage report
pytest --cov=src --cov-report=html

# Open htmlcov/index.html to view coverage
```

### Step 4: Commit Standards-Compliant Code (10 minutes)

```bash
git add .
git commit -m "Initial implementation with SDLC standards"
git push origin main
```

---

## Phase 3: Developer Workflow Testing (2-3 hours)

### Step 1: Create Feature Branch (10 minutes)

```bash
# Create a feature branch from main
git checkout main
git pull origin main
git checkout -b feature/PBI-001-add-power-function
```

### Step 2: Implement New Feature (30 minutes)

Add a power function to `src/calculator.py`:

```python
def power(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Raise a to the power of b.
    
    Args:
        a: Base number
        b: Exponent
        
    Returns:
        a raised to power b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numeric")
    
    result = a ** b
    self._record_operation(f"{a} ^ {b} = {result}")
    return result
```

### Step 3: Add Tests (20 minutes)

Add tests to `tests/test_calculator.py`:

```python
def test_power_positive_numbers(self):
    """Test power operation with positive numbers."""
    assert self.calc.power(2, 3) == 8
    assert self.calc.power(5, 0) == 1
    assert self.calc.power(10, 2) == 100

def test_power_negative_exponent(self):
    """Test power operation with negative exponent."""
    assert self.calc.power(2, -1) == 0.5
    assert self.calc.power(4, -2) == 0.0625
```

### Step 4: Push and Create PR (15 minutes)

```bash
# Run all checks locally first
black src/ tests/
pytest
python scripts/check_sdlc_standards.py

# Commit and push
git add .
git commit -m "feat: Add power function to calculator

- Implement power method with type checking
- Add comprehensive unit tests
- Update documentation"

git push origin feature/PBI-001-add-power-function
```

1. Go to GitHub and create a Pull Request to `development`
2. Fill out the PR template
3. Watch the GitHub Actions workflow run
4. Address any failures

### Step 5: Code Review and Merge (20 minutes)

1. Have a colleague review the PR (or self-review)
2. Check that all automated tests pass
3. Merge the PR to development
4. Delete the feature branch

---

## Phase 4: QA/UAT Workflow Testing (1-1.5 hours)

### Step 1: Create PR from Development to UAT (10 minutes)

```bash
git checkout development
git pull origin development
```

1. Create PR from `development` to `uat` on GitHub
2. Verify QA workflow triggers
3. Monitor test execution

### Step 2: Manual QA Testing (20 minutes)

While automated tests run:
1. Review test reports in Actions
2. Check artifact uploads
3. Verify scheduled job configuration

### Step 3: Merge to UAT (10 minutes)

1. Approve and merge PR to UAT
2. Verify UAT deployment job runs
3. Check deployment status

### Step 4: Trigger Manual Test Run (15 minutes)

1. Go to Actions → QA/UAT Workflow
2. Click "Run workflow"
3. Select test suite type
4. Monitor execution

---

## Phase 5: Production Release (30-45 minutes)

### Step 1: Prepare Release (10 minutes)

```bash
git checkout uat
git pull origin uat

# Update release notes
# Edit RELEASE_NOTES.md with new version info
```

### Step 2: Create PR to Main (10 minutes)

1. Create PR from `uat` to `main`
2. Ensure RELEASE_NOTES.md is updated
3. Verify pre-release validation passes

### Step 3: Merge and Deploy (10 minutes)

1. Approve and merge PR
2. Watch automatic:
   - Version tagging
   - GitHub Release creation
   - Production deployment
   - Notifications

### Step 4: Verify Production (10 minutes)

1. Check GitHub Releases page
2. Verify deployment status
3. Review scheduled job configuration
4. Check rollback plan creation

---

## Phase 6: Scheduled Jobs Testing (15-20 minutes)

### Step 1: Modify Cron Schedule (5 minutes)

For testing, temporarily modify the schedule in `.github/workflows/production-release.yml`:

```yaml
schedule:
  - cron: '*/5 * * * *'  # Every 5 minutes for testing
```

### Step 2: Monitor Execution (10 minutes)

1. Wait for scheduled job to trigger
2. Check Actions tab for execution
3. Review job logs
4. Restore original schedule

---

## Troubleshooting Guide

### Common Issues and Solutions

1. **Permission Denied on Scripts**
   ```bash
   chmod +x scripts/check_sdlc_standards.py
   ```

2. **Import Errors**
   ```bash
   # Ensure you're in the project root
   export PYTHONPATH="${PYTHONPATH}:${PWD}"
   ```

3. **Coverage Below Threshold**
   - Add more tests
   - Check for untested edge cases
   - Review coverage report

4. **Linting Failures**
   ```bash
   # Auto-fix with Black
   black src/ tests/
   
   # Auto-fix imports
   isort src/ tests/
   ```

5. **Type Checking Errors**
   - Add type hints to functions
   - Use `typing` module imports
   - Add `# type: ignore` sparingly

---

## Best Practices

1. **Branch Naming**
   - Feature: `feature/PBI-XXX-description`
   - Bugfix: `bugfix/ISSUE-XXX-description`
   - Hotfix: `hotfix/ISSUE-XXX-description`

2. **Commit Messages**
   - Use conventional commits
   - Examples:
     - `feat: Add new calculation method`
     - `fix: Correct division by zero handling`
     - `docs: Update API documentation`
     - `test: Add edge case tests`

3. **PR Management**
   - Always fill out PR template
   - Link to related issues/PBIs
   - Include screenshots if UI changes
   - Request appropriate reviewers

4. **Testing**
   - Write tests before pushing
   - Aim for >80% coverage
   - Test edge cases
   - Use meaningful test names

5. **Documentation**
   - Update docs with code changes
   - Keep README current
   - Document breaking changes
   - Include examples

---

## Maintenance Tasks

### Weekly
- Review and merge dependabot PRs
- Check for security vulnerabilities
- Review failed scheduled jobs

### Monthly
- Update dependencies
- Review and optimize workflows
- Clean up old branches
- Archive old deployments

### Quarterly
- Major dependency updates
- Performance optimization
- Security audit
- Workflow efficiency review

---

## Additional Resources

- [Complete Workflow Guide](WORKFLOW_GUIDE.md) - Detailed step-by-step workflow
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Testing Best Practices](https://docs.pytest.org/en/latest/goodpractices.html)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)

---

## Support

For questions or issues:
1. Check the troubleshooting guide
2. Review GitHub Actions logs
3. Consult team documentation
4. Reach out to DevOps team 