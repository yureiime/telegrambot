@echo off
setlocal

set CONDA_ENV_NAME=telebot

where conda >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Conda is not found in your system's PATH.
    echo Please ensure Anaconda or Miniconda is installed and configured correctly.
    pause
    exit /b 1
)

echo Checking for Conda environment: %CONDA_ENV_NAME%

set ENV_EXISTS=false
for /f "delims=" %%i in ('conda env list') do (
    echo %%i | findstr /b /c:"%CONDA_ENV_NAME% " >nul
    if not errorlevel 1 (
        set ENV_EXISTS=true
    )
)

if "%ENV_EXISTS%"=="true" (
    echo Environment '%CONDA_ENV_NAME%' already exists. Updating it with prune...
    conda env update -f environment.yml --prune
    if %errorlevel% neq 0 (
        echo Warning: Error updating Conda environment. Proceeding with existing environment.
    )
) else (
    echo Environment '%CONDA_ENV_NAME%' not found. Creating it now...
    conda env create -f environment.yml
    if %errorlevel% neq 0 (
        echo Error creating Conda environment. Please check environment.yml.
        pause
        exit /b 1
    )
    echo Environment '%CONDA_ENV_NAME%' created successfully.
)

echo Activating Conda environment: %CONDA_ENV_NAME%
call conda activate %CONDA_ENV_NAME%
if %errorlevel% neq 0 (
    echo Error activating Conda environment.
    pause
    exit /b 1
)

@REM echo Running the chatbot application...
@REM python main.py

echo Chatbot script finished.
pause
endlocal