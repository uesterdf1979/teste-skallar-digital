from flask import Blueprint, request, jsonify
from flasgger import swag_from
from controllers.email_controller import send_email

# Define o Blueprint para as rotas de e-mail
email_blueprint = Blueprint('email_blueprint', __name__)

# Rota para envio de e-mails
@email_blueprint.route('/send-email', methods=['POST'])
@swag_from('../docs/email_send.yml')  # Carrega a documentação a partir do arquivo YAML
def send():
    data = request.get_json()
    to = data.get("to")
    subject = data.get("subject")
    body = data.get("body")
    
    # Chama o controlador para enviar o e-mail
    result = send_email(to, subject, body)
    
    return jsonify({"message": result})