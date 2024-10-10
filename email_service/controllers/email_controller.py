from services.email_service import send_email_service

def send_email(to, subject, body):
    try:
        # Chama o serviço de envio de e-mail
        send_email_service(to, subject, body)
        return "E-mail enviado com sucesso!"
    except Exception as e:
        return f"Erro ao enviar o e-mail: {str(e)}"
