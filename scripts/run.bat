@echo off
REM Sobe o servidor da API. Uso: scripts\run.bat
cd /d "%~dp0.."

if not exist venv\Scripts\activate.bat (
    echo [ERRO] Ambiente virtual nao encontrado. Rode primeiro: scripts\setup.bat
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
uvicorn app.main:app --reload
pause
