@echo off
REM Define o diretório do projeto (substitua conforme o caminho do seu projeto)
cd /d "C:\teste-skallar-digital\email_service"

REM Ativa o ambiente virtual
call venv\Scripts\activate

REM Instala as dependências (opcional, pode ser comentado se já estiverem instaladas)
pip install -r requirements.txt

REM Executa a aplicação Flask
python app.py

REM Mantém o terminal aberto após a execução
pause