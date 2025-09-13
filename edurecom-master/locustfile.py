from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    """Define el comportamiento de un usuario general del sitio."""
    wait_time = between(1, 5)  # Tiempo de espera aleatorio entre 1 y 5 segundos entre tareas

    def on_start(self):
        """Se ejecuta cuando un usuario simulado inicia."""
        print("Iniciando un nuevo usuario virtual")

    @task(1)
    def index_page(self):
        """Prueba de Rendimiento Base: Carga la página de inicio."""
        self.client.get("/")

    @task(2)
    def login_page_load(self):
        """Prueba de Carga: Simula usuarios que visitan la página de login."""
        self.client.get("/login")

class StressTestUser(HttpUser):
    """Define el comportamiento de un usuario para pruebas de estrés en el login."""
    wait_time = between(1, 3)

    @task
    def attempt_login(self):
        """
        Prueba de Estrés: Intenta iniciar sesión con credenciales inválidas.
        Esto prueba la validación del formulario y la respuesta del servidor bajo estrés.
        """
        self.client.post(
            "/login",
            json={"email": "test@example.com", "password": "wrongpassword"}
        )
