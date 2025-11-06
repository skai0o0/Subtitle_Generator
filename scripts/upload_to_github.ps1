# Git Upload Script - Simple version without special characters
# Configuration
$USERNAME = "skai0o0"
$REPO = "Subtitle_Generator"

Write-Host "Git Upload Script" -ForegroundColor Cyan
Write-Host "Repository: $USERNAME/$REPO" -ForegroundColor Yellow
Write-Host ""

# Init if needed
if (-not (Test-Path ".git")) {
    git init
}

# Add remote
$remote = git remote get-url origin 2>$null
if (-not $remote) {
    git remote add origin "https://github.com/$USERNAME/$REPO.git"
}

# Stage and commit
git add .
$files = (git ls-files | Measure-Object).Count
Write-Host "Staging $files files..." -ForegroundColor Yellow

$confirm = Read-Host "Commit and push? (y/n)"
if ($confirm -eq "y") {
    git commit -m "Initial commit: Subtitle Generator v2.0"
    git branch -M main
    git push -u origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "SUCCESS!" -ForegroundColor Green
        Write-Host "https://github.com/$USERNAME/$REPO" -ForegroundColor Cyan
    } else {
        Write-Host "FAILED - Check errors above" -ForegroundColor Red
    }
}
