from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix
import os
import logging

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    # Configurar la base de datos
    database_url = os.environ.get("DATABASE_URL")
    
    if database_url:
        # Si hay DATABASE_URL (Railway o producción), usarla
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url
        print(f"Usando base de datos: {database_url[:50]}...")
    else:
        # Para Railway, usar SQLite en directorio persistente
        if os.environ.get("RAILWAY_ENVIRONMENT"):
            # En Railway, usar directorio /tmp que es más persistente
            db_path = "/tmp/edurecom.db"
            app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
            print(f"Usando SQLite persistente en Railway: {db_path}")
        else:
            # Para desarrollo local, usar SQLite
            app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/edurecom.db"
            print("Usando SQLite para desarrollo local")
    
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
        "pool_size": 10,
        "max_overflow": 20,
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message = 'Por favor inicia sesión para acceder a esta página.'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))

    # Configurar el registro de logs
    try:
        from logging_config import setup_logging
        setup_logging(app)
        app.logger.info("Logging configurado exitosamente")
    except Exception as e:
        app.logger.error(f"Error configurando logging: {e}")

    # Importar y registrar rutas
    try:
        from routes import register_routes
        register_routes(app)
        app.logger.info("Rutas registradas exitosamente")
    except Exception as e:
        app.logger.error(f"Error registrando rutas: {e}")
        raise

    return app 