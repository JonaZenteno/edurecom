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
from flask_debugtoolbar import DebugToolbarExtension

# Crear la aplicación
try:
    app = create_app()
    app.config['SECRET_KEY'] = 'dev'
    toolbar = DebugToolbarExtension(app)
    logger.info("Aplicación creada exitosamente")
    
    with app.app_context():
        try:
            # Crear tablas
            db.create_all()
            logger.info("✅ Base de datos inicializada correctamente")
            
            # Verificar que las tablas estén creadas
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            logger.info(f"📋 Tablas creadas: {tables}")
            
            # Verificar configuración de base de datos
            db_uri = app.config.get('SQLALCHEMY_DATABASE_URI', 'No configurada')
            logger.info(f"🗄️ Base de datos: {db_uri[:50]}...")
            
        except Exception as db_error:
            logger.error(f"❌ Error inicializando base de datos: {db_error}")
            raise
        
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
