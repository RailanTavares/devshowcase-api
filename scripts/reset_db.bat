@echo off
REM Apaga o banco SQLite e recria os dados de exemplo do zero.
REM Útil para "resetar" o estado antes de gravar o vídeo de novo.
REM Uso: scripts\reset_db.bat
cd /d "%~dp0.."

if not exist venv\Scripts\activate.bat (
    echo [ERRO] Ambiente virtual nao encontrado. Rode primeiro: scripts\setup.bat
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
del /f devshowcase.db 2>nul
python scripts\seed_data.py --force
if errorlevel 1 (
    echo [ERRO] Falha ao popular o banco. Veja a mensagem acima.
    pause
    exit /b 1
)

echo.
echo Banco resetado e populado com dados de exemplo novamente.
pause
