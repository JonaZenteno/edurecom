#!/usr/bin/env python3
"""
Script para verificar y cargar cursos en la base de datos
"""
import json
from __init__ import create_app, db
from models import Course

def check_and_load_courses():
    """Verifica y carga cursos en la base de datos"""
    app = create_app()
    
    with app.app_context():
        try:
            # Verificar cursos existentes
            course_count = Course.query.count()
            print(f"📚 Cursos actuales en la base de datos: {course_count}")
            
            if course_count > 0:
                # Mostrar grupos disponibles
                groups = db.session.query(Course.group).distinct().all()
                groups = [g[0] for g in groups]
                print(f"🎯 Grupos disponibles: {groups}")
                
                # Mostrar algunos cursos de ejemplo
                sample_courses = Course.query.limit(5).all()
                print("\n📋 Ejemplos de cursos:")
                for course in sample_courses:
                    print(f"  - {course.title} (Grupo: {course.group})")
            else:
                print("🔄 No hay cursos, cargando desde JSON...")
                load_courses_from_json()
                
                # Verificar nuevamente
                course_count = Course.query.count()
                print(f"📚 Cursos cargados: {course_count}")
                
                if course_count > 0:
                    # Mostrar grupos disponibles
                    groups = db.session.query(Course.group).distinct().all()
                    groups = [g[0] for g in groups]
                    print(f"🎯 Grupos disponibles: {groups}")
                    
                    # Mostrar algunos cursos de ejemplo
                    sample_courses = Course.query.limit(5).all()
                    print("\n📋 Ejemplos de cursos:")
                    for course in sample_courses:
                        print(f"  - {course.title} (Grupo: {course.group})")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            raise

def load_courses_from_json():
    """Carga los cursos desde un archivo JSON a la base de datos."""
    try:
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

if __name__ == "__main__":
    check_and_load_courses()
