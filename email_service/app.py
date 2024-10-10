from flask import Flask
from flasgger import Swagger
from routes.email_routes import email_blueprint

# Inicializa a aplicação Flask
app = Flask(__name__)

# Inicializa o Swagger e define algumas informações básicas
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Microserviço de Envio de E-mails",
        "description": "Documentação para a API de envio de e-mails utilizando Flask",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ]
})

# Registra o Blueprint da rota de e-mail
app.register_blueprint(email_blueprint)

# Ponto de entrada da aplicação
if __name__ == "__main__":
    app.run(debug=True)