import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Variáveis de configuração de e-mail
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email_service(to, subject, body):
    """
    Função para enviar um e-mail utilizando o protocolo SMTP.
    Parâmetros:
    - to (str): Endereço de e-mail do destinatário.
    - subject (str): Assunto do e-mail.
    - body (str): Corpo do e-mail.
    """
    # Cria a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to
    msg['Subject'] = subject

    # Anexa o corpo do e-mail na mensagem
    msg.attach(MIMEText(body, 'plain'))

    # Conecta ao servidor SMTP e envia o e-mail
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Inicializa o TLS para segurança
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Faz login no servidor
            server.sendmail(EMAIL_ADDRESS, to, msg.as_string())  # Envia o e-mail
            print(f"E-mail enviado com sucesso para {to}")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")