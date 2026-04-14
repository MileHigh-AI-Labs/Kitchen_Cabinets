@echo off
cd /d "%~dp0"
echo Starting email save server...
python email_server.py
pause
