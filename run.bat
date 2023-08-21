@echo off

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed.
    echo Please follow these steps to install Python:
    echo 1. Download the latest version of Python from https://www.python.org/downloads/
    echo 2. Run the installer and follow the instructions, make sure to check the box that says "Add Python to PATH".
    echo 3. Restart your computer.
    echo After following these steps, please run this script again.
    pause
    goto :eof
)

REM Check if pip is installed
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed. Installing now...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    del get-pip.py
)

REM Define your required packages
set packages=PyQt5 PyQt5-tools logging

REM Loop over the packages and check if they are installed
for %%p in (%packages%) do (
    echo Checking for %%p
    python -c "import %%p" 2>nul
    if errorlevel 1 (
        echo Installing %%p
        python -m pip install %%p
    ) else (
        echo Updating %%p
        python -m pip install --upgrade %%p
    )
)

REM Start the main script
python main.py

echo If you encountered any issues while running this script, please ensure the following:
echo 1. You have the latest version of Python and pip installed.
echo 2. You have added Python to your system's PATH. You can do this by checking the relevant box during Python's installation.
echo 3. You have the necessary permissions to install Python packages. If you are on a managed computer, you may need to ask your system administrator for help.
pause
