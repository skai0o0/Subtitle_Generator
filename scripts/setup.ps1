# Subtitle Generator Ver 2 - Setup Script (PowerShell)

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Subtitle Generator Ver 2 - Setup Script" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "[1/5] Checking Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  ✅ $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "  ❌ Python not found! Please install Python 3.8+" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Check FFmpeg
Write-Host "[2/5] Checking FFmpeg..." -ForegroundColor Yellow
try {
    $ffmpegVersion = ffmpeg -version 2>&1 | Select-Object -First 1
    Write-Host "  ✅ FFmpeg installed" -ForegroundColor Green
} catch {
    Write-Host "  ⚠️  FFmpeg not found!" -ForegroundColor Yellow
    Write-Host "  Please install: choco install ffmpeg" -ForegroundColor Yellow
    Write-Host "  You can continue setup and install FFmpeg later" -ForegroundColor Yellow
}
Write-Host ""

# Create virtual environment
Write-Host "[3/5] Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path ".venv") {
    Write-Host "  ℹ️  Virtual environment already exists, skipping..." -ForegroundColor Cyan
} else {
    # Try Python 3.11 first, fallback to default python
    $python311 = Get-Command "py" -ErrorAction SilentlyContinue
    if ($python311) {
        Write-Host "  Using Python 3.11..." -ForegroundColor Cyan
        py -3.11 -m venv .venv
    } else {
        Write-Host "  Using default Python..." -ForegroundColor Cyan
        python -m venv .venv
    }
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✅ Virtual environment created" -ForegroundColor Green
    } else {
        Write-Host "  ❌ Failed to create virtual environment" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}
Write-Host ""

# Activate and install
Write-Host "[4/5] Installing dependencies..." -ForegroundColor Yellow
Write-Host "  This may take several minutes..." -ForegroundColor Cyan

& ".\.venv\Scripts\Activate.ps1"

python -m pip install --upgrade pip --quiet

# Check for NVIDIA GPU
Write-Host "  Checking for NVIDIA GPU..." -ForegroundColor Cyan
$hasGPU = $false
try {
    $nvidiaSmi = nvidia-smi 2>&1
    if ($LASTEXITCODE -eq 0) {
        $hasGPU = $true
        Write-Host "  🎮 NVIDIA GPU detected! Installing PyTorch with CUDA..." -ForegroundColor Green
    }
} catch {
    Write-Host "  💻 No NVIDIA GPU detected. Installing CPU version..." -ForegroundColor Yellow
}

if ($hasGPU) {
    # Install with CUDA support
    pip install -r requirements-cuda.txt
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
} else {
    # Install CPU version
    pip install -r requirements.txt
}

if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✅ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "  ❌ Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Test setup
Write-Host "[5/5] Testing installation..." -ForegroundColor Yellow
python test_setup.py

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To run the app:" -ForegroundColor Yellow
Write-Host "  .\run.ps1" -ForegroundColor White
Write-Host ""
Write-Host "Or manually:" -ForegroundColor Yellow
Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "  python main.py" -ForegroundColor White
Write-Host ""

Read-Host "Press Enter to exit"
