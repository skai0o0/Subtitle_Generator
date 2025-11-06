# 🚀 Git Upload Script - Automated GitHub Setup
# PowerShell script để tự động setup và upload project lên GitHub

# ============================================
# CONFIGURATION - ĐỔI CÁC GIÁ TRỊ NÀY
# ============================================
$GITHUB_USERNAME = "skai0o0"      # Thay bằng username GitHub của bạn
$REPO_NAME = "Subtitle_Generator"
$REPO_DESCRIPTION = "🎬 AI-powered subtitle generator using Whisper & NLLB-200"

# ============================================
# SCRIPT START
# ============================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "🚀 Git Setup & Upload Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
Write-Host "📋 Checking Git installation..." -ForegroundColor Yellow
$gitVersion = git --version 2>$null
if (-not $gitVersion) {
    Write-Host "❌ Git is not installed!" -ForegroundColor Red
    Write-Host "   Install with: winget install --id Git.Git" -ForegroundColor Yellow
    exit 1
}
Write-Host "✅ Git found: $gitVersion" -ForegroundColor Green
Write-Host ""

# Check if already a git repo
if (Test-Path ".git") {
    Write-Host "⚠️  This is already a Git repository!" -ForegroundColor Yellow
    $response = Read-Host "Do you want to continue? (y/n)"
    if ($response -ne "y") {
        Write-Host "Aborted." -ForegroundColor Red
        exit 0
    }
    Write-Host ""
} else {
    # Initialize Git
    Write-Host "📦 Initializing Git repository..." -ForegroundColor Yellow
    git init
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Git repository initialized" -ForegroundColor Green
    } else {
        Write-Host "❌ Failed to initialize Git" -ForegroundColor Red
        exit 1
    }
    Write-Host ""
}

# Configure Git user (if not set)
Write-Host "👤 Checking Git configuration..." -ForegroundColor Yellow
$userName = git config user.name
$userEmail = git config user.email

if (-not $userName) {
    Write-Host "⚠️  Git user.name not set" -ForegroundColor Yellow
    $inputName = Read-Host "Enter your name"
    git config --global user.name "$inputName"
    Write-Host "✅ User name set to: $inputName" -ForegroundColor Green
}

if (-not $userEmail) {
    Write-Host "⚠️  Git user.email not set" -ForegroundColor Yellow
    $inputEmail = Read-Host "Enter your email"
    git config --global user.email "$inputEmail"
    Write-Host "✅ User email set to: $inputEmail" -ForegroundColor Green
}
Write-Host ""

# Check .gitignore exists
Write-Host "📝 Checking .gitignore file..." -ForegroundColor Yellow
if (-not (Test-Path ".gitignore")) {
    Write-Host "❌ .gitignore not found!" -ForegroundColor Red
    Write-Host "   Creating default .gitignore..." -ForegroundColor Yellow
    
    $gitignoreContent = @"
# Python
__pycache__/
*.py[cod]
*`$py.class
*.so
.Python
build/
dist/
*.egg-info/

# Virtual Environment
venv/
.venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Model caches
~/.cache/whisper/
~/.cache/huggingface/
*.bin
*.safetensors

# User data
playlist_history.json
*.srt
*.vtt
temp_audio_*.wav
*.tmp
*.temp

# Test files
test_*.py
demo_*.py
changelogs/
"@
    
    $gitignoreContent | Out-File -FilePath ".gitignore" -Encoding UTF8
    Write-Host "✅ .gitignore created" -ForegroundColor Green
} else {
    Write-Host "✅ .gitignore found" -ForegroundColor Green
}
Write-Host ""

# Add remote if not exists
Write-Host "🌐 Setting up GitHub remote..." -ForegroundColor Yellow
$remoteUrl = git remote get-url origin 2>$null
if (-not $remoteUrl) {
    if ($GITHUB_USERNAME -eq "YOUR_GITHUB_USERNAME") {
        Write-Host "⚠️  Please edit this script and set your GitHub username!" -ForegroundColor Red
        $GITHUB_USERNAME = Read-Host "Enter your GitHub username"
    }
    
    $repoUrl = "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
    Write-Host "   Adding remote: $repoUrl" -ForegroundColor Cyan
    git remote add origin $repoUrl
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Remote added successfully" -ForegroundColor Green
    } else {
        Write-Host "❌ Failed to add remote" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✅ Remote already exists: $remoteUrl" -ForegroundColor Green
}
Write-Host ""

# Stage all files
Write-Host "📦 Staging files..." -ForegroundColor Yellow
git add .
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Files staged" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to stage files" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Show status
Write-Host "📊 Files to be committed:" -ForegroundColor Yellow
git status --short
Write-Host ""

# Check for unwanted files
Write-Host "🔍 Checking for unwanted files..." -ForegroundColor Yellow
$unwantedPatterns = @("venv", "__pycache__", ".cache", "*.pyc", "*.bin")
$foundUnwanted = $false

foreach ($pattern in $unwantedPatterns) {
    $found = git status --short | Select-String $pattern
    if ($found) {
        Write-Host "⚠️  Found unwanted files matching: $pattern" -ForegroundColor Red
        $found | ForEach-Object { Write-Host "   $_" -ForegroundColor Red }
        $foundUnwanted = $true
    }
}

if ($foundUnwanted) {
    Write-Host ""
    Write-Host "⚠️  WARNING: Unwanted files detected!" -ForegroundColor Red
    Write-Host "   Please check your .gitignore and run:" -ForegroundColor Yellow
    Write-Host "   git rm -r --cached ." -ForegroundColor Cyan
    Write-Host "   git add ." -ForegroundColor Cyan
    Write-Host ""
    $response = Read-Host "Continue anyway? (y/n)"
    if ($response -ne "y") {
        Write-Host "Aborted." -ForegroundColor Red
        exit 0
    }
} else {
    Write-Host "✅ No unwanted files detected" -ForegroundColor Green
}
Write-Host ""

# Count files
$fileCount = (git ls-files | Measure-Object).Count
Write-Host "📊 Total files to upload: $fileCount" -ForegroundColor Cyan
Write-Host ""

# Confirm before commit
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Ready to commit and push to GitHub!" -ForegroundColor Green
Write-Host "Repository: $GITHUB_USERNAME/$REPO_NAME" -ForegroundColor Cyan
Write-Host "Files: $fileCount files" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$confirm = Read-Host "Proceed with commit and push? (y/n)"
if ($confirm -ne "y") {
    Write-Host "Aborted." -ForegroundColor Red
    exit 0
}
Write-Host ""

# Commit
Write-Host "💾 Creating commit..." -ForegroundColor Yellow
$commitMessage = "Initial commit: Subtitle Generator v2.0 with Whisper & NLLB-200

Features:
- AI transcription with OpenAI Whisper (5 models)
- Multi-language translation with Meta NLLB-200 (200+ languages)
- Fullscreen mode with overlay controls
- Playlist management
- Subtitle editor
- GPU acceleration (CUDA)
- Context-aware translation with sliding window
- Auto VRAM cleanup"

git commit -m "$commitMessage"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Commit created successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to create commit" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Set main branch
Write-Host "🌿 Setting main branch..." -ForegroundColor Yellow
git branch -M main
Write-Host "✅ Branch set to main" -ForegroundColor Green
Write-Host ""

# Push to GitHub
Write-Host "🚀 Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "   This may take a few moments..." -ForegroundColor Cyan
Write-Host ""

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "✅ SUCCESS! Project uploaded to GitHub" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "📍 Repository URL:" -ForegroundColor Cyan
    Write-Host "   https://github.com/$GITHUB_USERNAME/$REPO_NAME" -ForegroundColor White
    Write-Host "📘 Description:" -ForegroundColor Cyan
    Write-Host "   $REPO_DESCRIPTION" -ForegroundColor White
    Write-Host ""
    Write-Host "🎯 Next Steps:" -ForegroundColor Yellow
    Write-Host "   1. Visit your repository on GitHub" -ForegroundColor White
    Write-Host "   2. Add topics/tags (python, ai, subtitles, whisper, nllb)" -ForegroundColor White
    Write-Host "   3. Enable Issues and Discussions" -ForegroundColor White
    Write-Host "   4. Create a Release (optional)" -ForegroundColor White
    Write-Host "   5. Share with the world! 🌍" -ForegroundColor White
    Write-Host ""
    
    # Offer to open in browser
    $openBrowser = Read-Host "Open repository in browser? (y/n)"
    if ($openBrowser -eq "y") {
        Start-Process "https://github.com/$GITHUB_USERNAME/$REPO_NAME"
    }
    
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "❌ FAILED to push to GitHub" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Possible causes:" -ForegroundColor Yellow
    Write-Host "   1. Repository doesn't exist on GitHub" -ForegroundColor White
    Write-Host "      → Create it first at: https://github.com/new" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "   2. Authentication failed" -ForegroundColor White
    Write-Host "      → Use Personal Access Token as password" -ForegroundColor Cyan
    Write-Host "      → Get token at: https://github.com/settings/tokens" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "   3. Remote URL incorrect" -ForegroundColor White
    Write-Host "      → Check: git remote get-url origin" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "   4. Network issues" -ForegroundColor White
    Write-Host "      → Check internet connection" -ForegroundColor Cyan
    Write-Host ""
    
    exit 1
}

Write-Host ""
Write-Host "🎉 Done! Happy coding!" -ForegroundColor Green
Write-Host ""
