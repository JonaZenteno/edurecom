#!/usr/bin/env python3
"""
Script para inicializar la base de datos
"""
import os
from __init__ import create_app, db
from models import User, UserProfile, Course, CourseView

def init_database():
    """Inicializa la base de datos creando todas las tablas"""
    app = create_app()
    
    with app.app_context():
        try:
            # Crear todas las tablas
            db.create_all()
            print("✅ Base de datos inicializada correctamente")
            
            # Verificar que las tablas se crearon
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"📋 Tablas creadas: {tables}")
            
            # Verificar si hay usuarios
            user_count = User.query.count()
            print(f"👥 Usuarios en la base de datos: {user_count}")
            
            # Verificar si hay perfiles
            profile_count = UserProfile.query.count()
            print(f"👤 Perfiles en la base de datos: {profile_count}")
            
            # Verificar si hay cursos
            course_count = Course.query.count()
            print(f"📚 Cursos en la base de datos: {course_count}")
            
        except Exception as e:
            print(f"❌ Error inicializando la base de datos: {e}")
            raise

if __name__ == "__main__":
    init_database()
