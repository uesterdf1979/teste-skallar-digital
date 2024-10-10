import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_send_email(client):
    response = client.post('/send-email', json={
        "to": "ujlacerda@gmail.com",
        "subject": "Teste de E-mail",
        "body": "Este é um e-mail de teste."
    })
    assert response.status_code == 200
    assert response.get_json()["message"] == "E-mail enviado com sucesso!"