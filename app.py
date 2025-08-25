import logging
import sys
from __init__ import create_app, db

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('edurecom.log')
    ]
)

logger = logging.getLogger(__name__)

# Crear la aplicación
try:
    app = create_app()
    logger.info("Aplicación creada exitosamente")
    
    with app.app_context():
        # Crear tablas
        db.create_all()
        logger.info("Base de datos inicializada")
        
        # Inicializar datos
        from init_data import init_courses
        init_courses()
        logger.info("Datos inicializados")
        
except Exception as e:
    logger.error(f"Error inicializando la aplicación: {e}")
    raise

if __name__ == '__main__':
    try:
        logger.info("Iniciando servidor EduRecom...")
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        logger.error(f"Error iniciando servidor: {e}")
        sys.exit(1)
