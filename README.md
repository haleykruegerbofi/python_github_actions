# Simple GitHub Actions CI/CD Demo

This repository demonstrates a basic CI/CD pipeline using GitHub Actions for a Python project.

## 🚀 What This Demo Shows

- **Automated Testing**: Every push and PR triggers automated tests
- **Code Quality Checks**: Automatic formatting and linting validation
- **Simple Python Project**: Basic calculator with unit tests

## 📋 How It Works

1. **Push Code** → GitHub Actions automatically runs
2. **Checks Run** → Formatting, linting, and tests execute
3. **Status Shows** → Green ✅ or Red ❌ on your PR

## 🔧 Local Development

### Setup
```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements-dev.txt
```

### Run Tests Locally
```bash
# Format code
python -m black src/ tests/

# Check linting
python -m flake8 src/ tests/

# Run tests
python -m pytest tests/ -v
```

## 🌲 Workflow

1. Create a feature branch
2. Make changes
3. Push to GitHub
4. Create a Pull Request
5. Watch GitHub Actions run automatically!

## 📝 Files

- `src/calculator.py` - Simple calculator implementation
- `tests/test_calculator.py` - Unit tests
- `.github/workflows/simple-ci.yml` - GitHub Actions workflow