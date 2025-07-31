# Quick Start Guide

## 🚀 Developer Quick Reference

### Initial Setup (One-time)
```bash
# Clone repo
git clone <repo-url>
cd python-cicd-demo

# Setup environment
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements-dev.txt
```

### Daily Development Flow

#### 1. Start New Feature
```bash
git checkout main
git pull origin main
git checkout -b feature/PBI-XXX-description
```

#### 2. Before Committing

**Windows (PowerShell):**
```powershell
# Run all validation checks
.\scripts\run_local_validation.ps1
```

**Mac/Linux:**
```bash
# Run all validation checks
./scripts/run_local_validation.sh
```

**Or run individually:**
```bash
# Format code
black src/ tests/

# Run tests with coverage
pytest --cov=src --cov-fail-under=80

# Check standards
python scripts/check_sdlc_standards.py
```

#### 3. Push and Create PR
```bash
git add .
git commit -m "feat: Your feature description"
git push origin feature/PBI-XXX-description
```

Then create PR to `development` branch on GitHub.

### Branch Strategy
```
main (production)
  ↑
uat (staging)
  ↑
development (integration)
  ↑
feature/* (your work)
```

### Common Commands

| Task | Command |
|------|---------|
| Run tests | `pytest` |
| Run specific test | `pytest tests/test_calculator.py::TestCalculator::test_add` |
| Check coverage | `pytest --cov=src` |
| Format code | `black src/ tests/` |
| Sort imports | `isort src/ tests/` |
| Type check | `mypy src/` |
| Security scan | `bandit -r src/` |
| SDLC check | `python scripts/check_sdlc_standards.py` |

### Workflow Status Badges

Add these to your README:

```markdown
![Developer Workflow](https://github.com/YOUR_ORG/REPO/workflows/Developer%20Workflow/badge.svg)
![QA/UAT Workflow](https://github.com/YOUR_ORG/REPO/workflows/QA%2FUAT%20Workflow/badge.svg)
![Production Release](https://github.com/YOUR_ORG/REPO/workflows/Production%20Release/badge.svg)
```

### Emergency Procedures

#### Rollback Production
1. Go to Actions → Production Release
2. Run workflow with `release_type: hotfix`
3. Or manually: `git checkout <previous-tag>`

#### Skip Tests (Emergency Only)
1. Go to Actions → Production Release
2. Check "Skip tests" option
3. Document reason in PR

### Useful Links
- [Complete Workflow Guide](docs/WORKFLOW_GUIDE.md) - Detailed step-by-step process
- [Full Implementation Guide](docs/IMPLEMENTATION_GUIDE.md)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)

### Need Help?
1. Check workflow logs in Actions tab
2. Review error messages carefully
3. Consult team documentation
4. Ask in team chat

---
Remember: **Always test locally before pushing!** 🧪 