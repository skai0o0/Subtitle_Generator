@echo off
echo ================================================
echo   Subtitle Generator Ver 2 - Setup Script
echo ================================================
echo.

echo [1/4] Checking Python...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found! Please install Python 3.8+ first.
    pause
    exit /b 1
)
echo.

echo [2/4] Creating virtual environment...
echo Trying to use Python 3.11...
py -3.11 -m venv .venv
if %ERRORLEVEL% NEQ 0 (
    echo Python 3.11 not found, using default Python...
    python -m venv .venv
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Failed to create virtual environment!
        pause
        exit /b 1
    )
)
echo.

echo [3/4] Activating virtual environment...
call .venv\Scripts\activate.bat
echo.

echo [4/4] Installing dependencies...
echo This may take several minutes...
python -m pip install --upgrade pip
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install dependencies!
    pause
    exit /b 1
)
echo.

echo ================================================
echo   Setup Complete!
echo ================================================
echo.
echo Next steps:
echo   1. Make sure FFmpeg is installed: ffmpeg -version
echo      If not: choco install ffmpeg
echo.
echo   2. Test the setup: python test_setup.py
echo.
echo   3. Run the app: python main.py
echo.
echo ================================================
pause
