"""
Configuración de logging para EduRecom
"""
import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    """
    Configura el sistema de logging para la aplicación
    """
    if not app.debug:
        # Crear directorio de logs si no existe
        if not os.path.exists('logs'):
            os.mkdir('logs')
        
        # Handler para archivo
        file_handler = RotatingFileHandler(
            'logs/edurecom.log', 
            maxBytes=10240000,  # 10MB
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        
        # Handler para consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        app.logger.addHandler(console_handler)
        
        app.logger.setLevel(logging.INFO)
        app.logger.info('EduRecom startup')
    
    # Logging específico para errores de clustering
    clustering_logger = logging.getLogger('clustering')
    clustering_logger.setLevel(logging.DEBUG)
    
    # Handler para archivo de clustering
    clustering_handler = RotatingFileHandler(
        'logs/clustering.log',
        maxBytes=10240000,
        backupCount=5
    )
    clustering_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    clustering_logger.addHandler(clustering_handler)
    
    return app.logger

