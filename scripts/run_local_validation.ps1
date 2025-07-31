# Run all validation checks locally before pushing
# PowerShell version for Windows

Write-Host "===================================" -ForegroundColor Yellow
Write-Host "Running Local Validation Suite" -ForegroundColor Yellow
Write-Host "===================================" -ForegroundColor Yellow

# Track failures
$failed = 0

Write-Host "`n1. Running Black Formatter" -ForegroundColor Yellow
$blackResult = python -m black --check src/ tests/ 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Black formatter check passed" -ForegroundColor Green
} else {
    Write-Host "✗ Black formatter check failed" -ForegroundColor Red
    Write-Host "  Run 'black src/ tests/' to fix" -ForegroundColor Red
    $failed = 1
}

Write-Host "`n2. Running isort" -ForegroundColor Yellow
$isortResult = python -m isort --check-only src/ tests/ 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Import sorting check passed" -ForegroundColor Green
} else {
    Write-Host "✗ Import sorting check failed" -ForegroundColor Red
    Write-Host "  Run 'isort src/ tests/' to fix" -ForegroundColor Red
    $failed = 1
}

Write-Host "`n3. Running Flake8" -ForegroundColor Yellow
$flake8Result = python -m flake8 src/ tests/ 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Flake8 check passed" -ForegroundColor Green
} else {
    Write-Host "✗ Flake8 check failed" -ForegroundColor Red
    Write-Host $flake8Result
    $failed = 1
}

Write-Host "`n4. Running MyPy Type Checker" -ForegroundColor Yellow
$mypyResult = python -m mypy src/ 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Type checking passed" -ForegroundColor Green
} else {
    Write-Host "✗ Type checking failed" -ForegroundColor Red
    Write-Host $mypyResult
    $failed = 1
}

Write-Host "`n5. Running SDLC Standards Check" -ForegroundColor Yellow
$sdlcResult = python scripts/check_sdlc_standards.py 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ SDLC standards check passed" -ForegroundColor Green
} else {
    Write-Host "✗ SDLC standards check failed" -ForegroundColor Red
    $failed = 1
}

Write-Host "`n6. Running Security Scan" -ForegroundColor Yellow
$banditResult = python -m bandit -r src/ -ll 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Security scan passed" -ForegroundColor Green
} else {
    Write-Host "✗ Security scan failed" -ForegroundColor Red
    Write-Host $banditResult
    $failed = 1
}

Write-Host "`n7. Running Unit Tests with Coverage" -ForegroundColor Yellow
$pytestResult = python -m pytest --cov=src --cov-fail-under=80 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Unit tests passed with sufficient coverage" -ForegroundColor Green
} else {
    Write-Host "✗ Unit tests failed or coverage below 80%" -ForegroundColor Red
    Write-Host $pytestResult
    $failed = 1
}

Write-Host "`n===================================" -ForegroundColor Yellow
if ($failed -eq 0) {
    Write-Host "✓ All validation checks passed!" -ForegroundColor Green
    Write-Host "Your code is ready to push." -ForegroundColor Green
    exit 0
} else {
    Write-Host "✗ Some validation checks failed!" -ForegroundColor Red
    Write-Host "Please fix the issues before pushing." -ForegroundColor Red
    exit 1
} 