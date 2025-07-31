# Python CI/CD Pipeline with GitHub Actions

This repository demonstrates a complete CI/CD pipeline using GitHub Actions for a Python project with multiple environment stages and comprehensive testing.

## 🚀 Features

- **Multi-branch workflow**: Feature → Development → UAT → Production
- **Automated testing**: Unit tests, linting, SDLC standards
- **Code review process**: Pull request templates and automated checks
- **Environment-specific deployments**: Dev, QA/UAT, and Production
- **Comprehensive notifications**: Alerts for failures and successful deployments

## 📋 Prerequisites

- Python 3.8+
- GitHub account with Actions enabled
- Repository secrets configured (see below)

## 🔧 Repository Setup

### Required Secrets

Configure these in your GitHub repository settings:

1. `SLACK_WEBHOOK_URL` - For notifications
2. `TEAMS_WEBHOOK_URL` - For Microsoft Teams notifications
3. `EMAIL_SERVER` - SMTP server for email alerts
4. `EMAIL_USERNAME` - Email authentication
5. `EMAIL_PASSWORD` - Email password

### Required Variables

1. `PYTHON_VERSION` - Default: 3.9
2. `MIN_COVERAGE` - Minimum test coverage (default: 80%)
3. `ENVIRONMENT` - Current environment (dev/uat/prod)

## 🌲 Branch Structure

```
main (production)
├── uat (user acceptance testing)
├── development (integration)
└── feature/* (individual features)
```

## 🔄 Workflow Overview

1. **Developer Workflow**: Create feature branch → Code → Test → Push → PR
2. **QA Workflow**: Test in UAT → Approve → Merge
3. **Release Workflow**: Deploy to production → Monitor

## 📝 Development Process

1. Fork from main branch
2. Create feature branch: `feature/PBI-123-description`
3. Write code following SDLC standards
4. Write unit tests (minimum 80% coverage)
5. Update documentation
6. Create pull request to development branch
7. Pass automated checks
8. Code review approval
9. Merge to development

📖 **[See detailed workflow guide](docs/WORKFLOW_GUIDE.md)** for step-by-step instructions

## 🧪 Testing Standards

- **Linting**: Black, flake8, mypy
- **Unit Tests**: pytest with coverage
- **SDLC Compliance**: Naming conventions, code structure
- **Security**: bandit for security checks

## 📊 Metrics

- Code coverage reports
- Build time statistics
- Deployment success rates
- Test execution reports 