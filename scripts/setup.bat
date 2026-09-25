@echo off
REM Setup automático do projeto DevShowcase API (Windows).
REM Uso: scripts\setup.bat

cd /d "%~dp0.."

echo ==> Verificando se o Python esta instalado...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao foi encontrado. Instale o Python em https://python.org e marque a opcao "Add Python to PATH" durante a instalacao.
    pause
    exit /b 1
)

echo ==> Criando ambiente virtual (venv)...
python -m venv venv
if errorlevel 1 (
    echo [ERRO] Falha ao criar o ambiente virtual.
    pause
    exit /b 1
)

echo ==> Ativando ambiente virtual e instalando dependencias...
call venv\Scripts\activate.bat
pip install --upgrade pip -q
pip install -r requirements.txt -q
if errorlevel 1 (
    echo [ERRO] Falha ao instalar as dependencias. Verifique sua conexao com a internet.
    pause
    exit /b 1
)

echo ==> Populando banco de dados com dados de exemplo...
python scripts\seed_data.py
if errorlevel 1 (
    echo [ERRO] Falha ao popular o banco de dados.
    pause
    exit /b 1
)

echo.
echo Tudo pronto! Para iniciar a API, rode:
echo   scripts\run.bat
echo (ou diretamente: uvicorn app.main:app --reload)
echo.
pause
