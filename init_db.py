#!/usr/bin/env python3
"""
Script para inicializar la base de datos
"""
import os
from __init__ import create_app, db
from models import User, UserProfile, Course, CourseView

def init_database():
    """Inicializa la base de datos creando todas las tablas y cargando cursos"""
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
            
            # Crear usuario administrador si no existe
            create_admin_user_if_needed()
            
            # Verificar si hay perfiles
            profile_count = UserProfile.query.count()
            print(f"👤 Perfiles en la base de datos: {profile_count}")
            
            # Verificar si hay cursos
            course_count = Course.query.count()
            print(f"📚 Cursos en la base de datos: {course_count}")
            
            # Si no hay cursos, cargarlos desde el JSON
            if course_count == 0:
                print("🔄 No hay cursos en la base de datos, cargando desde JSON...")
                load_courses_from_json()
                
                # Verificar nuevamente
                course_count = Course.query.count()
                print(f"📚 Cursos cargados: {course_count}")
                
                # Mostrar grupos disponibles
                groups = db.session.query(Course.group).distinct().all()
                print(f"🎯 Grupos de formación disponibles: {[g[0] for g in groups]}")
            else:
                # Mostrar grupos disponibles
                groups = db.session.query(Course.group).distinct().all()
                print(f"🎯 Grupos de formación disponibles: {[g[0] for g in groups]}")
            
        except Exception as e:
            print(f"❌ Error inicializando la base de datos: {e}")
            raise

def load_courses_from_json():
    """Carga los cursos desde un archivo JSON a la base de datos."""
    try:
        import json
        from models import Course
        
        # Intentar cargar desde MDS/cursos.json
        json_paths = ['MDS/cursos.json', 'scripts/cursos.json', 'cursos.json']
        courses_data = None
        
        for path in json_paths:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    courses_data = json.load(f)
                print(f"📁 Cursos cargados desde: {path}")
                break
            except FileNotFoundError:
                continue
        
        if not courses_data:
            print("❌ No se encontró archivo de cursos JSON")
            return
        
        courses_loaded = 0
        for course_info in courses_data:
            # Mapeo flexible de claves JSON a los atributos del modelo Course
            title = course_info.get('titulo', course_info.get('title'))
            description = course_info.get('descripcion', course_info.get('description'))
            link = course_info.get('enlace', course_info.get('link'))
            group = course_info.get('grupo_formacion', course_info.get('group'))
            duration = course_info.get('duration')
            course_format = course_info.get('format')

            # Validar que los campos esenciales no sean nulos
            if not all([title, description, link, group]):
                print(f"⚠️ Omitiendo curso por falta de datos esenciales: {title}")
                continue

            # Crear instancia del curso si no existe
            if not Course.query.filter_by(title=title).first():
                new_course = Course(
                    title=title,
                    description=description,
                    link=link,
                    group=group,
                    duration=duration,
                    format=course_format
                )
                db.session.add(new_course)
                courses_loaded += 1
        
        db.session.commit()
        print(f"✅ {courses_loaded} cursos cargados exitosamente")

    except Exception as e:
        db.session.rollback()
        print(f"❌ Error al cargar los cursos: {e}")
        raise

def create_admin_user_if_needed():
    """Crea un usuario administrador si no existe"""
    try:
        from werkzeug.security import generate_password_hash
        
        # Verificar si ya existe un usuario administrador
        admin_user = User.query.join(UserProfile).filter(UserProfile.role == 'admin').first()
        
        if admin_user:
            print(f"👑 Usuario administrador ya existe: {admin_user.username}")
            return
        
        # Crear usuario administrador
        admin_username = "admin"
        admin_email = "admin@edurecom.com"
        admin_password = "admin123"  # Cambiar en producción
        
        # Verificar si el usuario ya existe
        existing_user = User.query.filter_by(username=admin_username).first()
        if existing_user:
            print(f"👤 Usuario {admin_username} ya existe, asignando rol de administrador...")
            # Crear perfil de administrador si no existe
            if not existing_user.profile:
                admin_profile = UserProfile(
                    user_id=existing_user.id,
                    role='admin',
                    school_type='urbana',
                    dependency='municipal',
                    age_range='31-40',
                    digital_tools_skill=5,
                    advanced_tic_skill=5,
                    digital_citizenship_skill=5,
                    teaching_tech_skill=5,
                    leadership_support=5,
                    resource_support=5,
                    interest_digital_literacy=True,
                    interest_educational_innovation=True,
                    interest_leadership=True,
                    learning_format='en-linea',
                    assigned_group='Administrador'
                )
                db.session.add(admin_profile)
                db.session.commit()
                print(f"👑 Rol de administrador asignado a {admin_username}")
            return
        
        # Crear nuevo usuario administrador
        admin_user = User(
            username=admin_username,
            email=admin_email,
            password_hash=generate_password_hash(admin_password)
        )
        db.session.add(admin_user)
        db.session.flush()  # Para obtener el ID
        
        # Crear perfil de administrador
        admin_profile = UserProfile(
            user_id=admin_user.id,
            role='admin',
            school_type='urbana',
            dependency='municipal',
            age_range='31-40',
            digital_tools_skill=5,
            advanced_tic_skill=5,
            digital_citizenship_skill=5,
            teaching_tech_skill=5,
            leadership_support=5,
            resource_support=5,
            interest_digital_literacy=True,
            interest_educational_innovation=True,
            interest_leadership=True,
            learning_format='en-linea',
            assigned_group='Administrador'
        )
        db.session.add(admin_profile)
        db.session.commit()
        
        print(f"👑 Usuario administrador creado:")
        print(f"   Usuario: {admin_username}")
        print(f"   Email: {admin_email}")
        print(f"   Contraseña: {admin_password}")
        print(f"   ⚠️  IMPORTANTE: Cambiar la contraseña en producción")
        
    except Exception as e:
        db.session.rollback()
        print(f"❌ Error creando usuario administrador: {e}")

if __name__ == "__main__":
    init_database()
