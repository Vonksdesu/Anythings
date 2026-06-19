@echo off
setlocal enabledelayedexpansion

:: 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to your system PATH!
    echo.
    echo To run this tool, please install Python 3:
    echo 1. Download it from: https://www.python.org/downloads/
    echo 2. IMPORTANT: Make sure to check the box "Add Python to PATH" during installation.
    echo.
    pause
    exit /b
)

:: 2. If the user DID NOT drag-and-drop a file (just double-clicked)
:: We change the working directory (CWD) to the PARENT folder (which is ZZMI/Mods/)
if "%~1"=="" (
    cd /d "%~dp0.."
    echo [INFO] Working directory changed to parent folder: !cd!
)

:: 3. Run the python script from its absolute path, passing any arguments
python "%~dp0zzz-mod-fixer.py" %*

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] The fixer encountered an error during execution.
    pause
)
