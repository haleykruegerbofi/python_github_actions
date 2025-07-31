#!/bin/bash
# Run all validation checks locally before pushing

echo "==================================="
echo "Running Local Validation Suite"
echo "==================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track failures
FAILED=0

echo -e "\n${YELLOW}1. Running Black Formatter${NC}"
if black --check src/ tests/; then
    echo -e "${GREEN}✓ Black formatter check passed${NC}"
else
    echo -e "${RED}✗ Black formatter check failed${NC}"
    echo "  Run 'black src/ tests/' to fix"
    FAILED=1
fi

echo -e "\n${YELLOW}2. Running isort${NC}"
if isort --check-only src/ tests/; then
    echo -e "${GREEN}✓ Import sorting check passed${NC}"
else
    echo -e "${RED}✗ Import sorting check failed${NC}"
    echo "  Run 'isort src/ tests/' to fix"
    FAILED=1
fi

echo -e "\n${YELLOW}3. Running Flake8${NC}"
if flake8 src/ tests/; then
    echo -e "${GREEN}✓ Flake8 check passed${NC}"
else
    echo -e "${RED}✗ Flake8 check failed${NC}"
    FAILED=1
fi

echo -e "\n${YELLOW}4. Running MyPy Type Checker${NC}"
if mypy src/; then
    echo -e "${GREEN}✓ Type checking passed${NC}"
else
    echo -e "${RED}✗ Type checking failed${NC}"
    FAILED=1
fi

echo -e "\n${YELLOW}5. Running SDLC Standards Check${NC}"
if python scripts/check_sdlc_standards.py; then
    echo -e "${GREEN}✓ SDLC standards check passed${NC}"
else
    echo -e "${RED}✗ SDLC standards check failed${NC}"
    FAILED=1
fi

echo -e "\n${YELLOW}6. Running Security Scan${NC}"
if bandit -r src/ -ll; then
    echo -e "${GREEN}✓ Security scan passed${NC}"
else
    echo -e "${RED}✗ Security scan failed${NC}"
    FAILED=1
fi

echo -e "\n${YELLOW}7. Running Unit Tests with Coverage${NC}"
if pytest --cov=src --cov-fail-under=80; then
    echo -e "${GREEN}✓ Unit tests passed with sufficient coverage${NC}"
else
    echo -e "${RED}✗ Unit tests failed or coverage below 80%${NC}"
    FAILED=1
fi

echo -e "\n==================================="
if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All validation checks passed!${NC}"
    echo "Your code is ready to push."
    exit 0
else
    echo -e "${RED}✗ Some validation checks failed!${NC}"
    echo "Please fix the issues before pushing."
    exit 1
fi 