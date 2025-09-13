import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'WTF_CSRF_ENABLED': False, # Desactiva CSRF para las pruebas
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:' # Usa una base de datos en memoria
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_login_page(client):
    """Prueba que la página de login se cargue correctamente."""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Iniciar Sesi\xc3\xb3n' in response.data # Verifica que el título esté presente

# Para ejecutar las pruebas, usa el comando `pytest` en la terminal.
