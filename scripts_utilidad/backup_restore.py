#!/usr/bin/env python3
"""
Script para hacer backup y restore de la base de datos SQLite
"""
import os
import shutil
import json
from datetime import datetime
from __init__ import create_app, db
from models import User, UserProfile, Course, CourseView

def backup_database():
    """Hace backup de la base de datos"""
    app = create_app()
    
    with app.app_context():
        try:
            # Obtener ruta de la base de datos
            db_uri = app.config.get('SQLALCHEMY_DATABASE_URI', '')
            if db_uri.startswith('sqlite:///'):
                db_path = db_uri.replace('sqlite:///', '')
            else:
                print("❌ Solo se puede hacer backup de bases de datos SQLite")
                return
            
            # Crear directorio de backup si no existe
            backup_dir = "backups"
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            # Crear nombre de archivo con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"{backup_dir}/edurecom_backup_{timestamp}.db"
            
            # Copiar archivo de base de datos
            if os.path.exists(db_path):
                shutil.copy2(db_path, backup_file)
                print(f"✅ Backup creado: {backup_file}")
                
                # También crear backup en JSON
                backup_json = f"{backup_dir}/edurecom_data_{timestamp}.json"
                export_to_json(backup_json)
                print(f"✅ Datos exportados a JSON: {backup_json}")
            else:
                print(f"❌ Base de datos no encontrada en: {db_path}")
                
        except Exception as e:
            print(f"❌ Error creando backup: {e}")

def export_to_json(filename):
    """Exporta todos los datos a JSON"""
    try:
        data = {
            "users": [],
            "profiles": [],
            "courses": [],
            "course_views": []
        }
        
        # Exportar usuarios
        users = User.query.all()
        for user in users:
            data["users"].append({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "created_at": user.created_at.isoformat() if user.created_at else None
            })
        
        # Exportar perfiles
        profiles = UserProfile.query.all()
        for profile in profiles:
            data["profiles"].append({
                "id": profile.id,
                "user_id": profile.user_id,
                "role": profile.role,
                "school_type": profile.school_type,
                "dependency": profile.dependency,
                "age_range": profile.age_range,
                "digital_tools_skill": profile.digital_tools_skill,
                "advanced_tic_skill": profile.advanced_tic_skill,
                "digital_citizenship_skill": profile.digital_citizenship_skill,
                "teaching_tech_skill": profile.teaching_tech_skill,
                "leadership_support": profile.leadership_support,
                "resource_support": profile.resource_support,
                "interest_digital_literacy": profile.interest_digital_literacy,
                "interest_educational_innovation": profile.interest_educational_innovation,
                "interest_leadership": profile.interest_leadership,
                "learning_format": profile.learning_format,
                "assigned_group": profile.assigned_group,
                "created_at": profile.created_at.isoformat() if profile.created_at else None
            })
        
        # Exportar cursos
        courses = Course.query.all()
        for course in courses:
            data["courses"].append({
                "id": course.id,
                "title": course.title,
                "description": course.description,
                "link": course.link,
                "group": course.group,
                "duration": course.duration,
                "format": course.format,
                "views_count": course.views_count,
                "created_at": course.created_at.isoformat() if course.created_at else None
            })
        
        # Guardar JSON
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print(f"❌ Error exportando a JSON: {e}")

def restore_from_json(filename):
    """Restaura datos desde JSON"""
    app = create_app()
    
    with app.app_context():
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Limpiar tablas existentes
            CourseView.query.delete()
            UserProfile.query.delete()
            Course.query.delete()
            User.query.delete()
            db.session.commit()
            
            # Restaurar usuarios
            for user_data in data.get("users", []):
                user = User(
                    id=user_data["id"],
                    username=user_data["username"],
                    email=user_data["email"],
                    password_hash="restored_user"  # Contraseña temporal
                )
                db.session.add(user)
            
            db.session.commit()
            
            # Restaurar perfiles
            for profile_data in data.get("profiles", []):
                profile = UserProfile(
                    id=profile_data["id"],
                    user_id=profile_data["user_id"],
                    role=profile_data["role"],
                    school_type=profile_data["school_type"],
                    dependency=profile_data["dependency"],
                    age_range=profile_data["age_range"],
                    digital_tools_skill=profile_data["digital_tools_skill"],
                    advanced_tic_skill=profile_data["advanced_tic_skill"],
                    digital_citizenship_skill=profile_data["digital_citizenship_skill"],
                    teaching_tech_skill=profile_data["teaching_tech_skill"],
                    leadership_support=profile_data["leadership_support"],
                    resource_support=profile_data["resource_support"],
                    interest_digital_literacy=profile_data["interest_digital_literacy"],
                    interest_educational_innovation=profile_data["interest_educational_innovation"],
                    interest_leadership=profile_data["interest_leadership"],
                    learning_format=profile_data["learning_format"],
                    assigned_group=profile_data["assigned_group"]
                )
                db.session.add(profile)
            
            # Restaurar cursos
            for course_data in data.get("courses", []):
                course = Course(
                    id=course_data["id"],
                    title=course_data["title"],
                    description=course_data["description"],
                    link=course_data["link"],
                    group=course_data["group"],
                    duration=course_data["duration"],
                    format=course_data["format"],
                    views_count=course_data["views_count"]
                )
                db.session.add(course)
            
            db.session.commit()
            print(f"✅ Datos restaurados desde: {filename}")
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error restaurando datos: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "backup":
            backup_database()
        elif sys.argv[1] == "restore" and len(sys.argv) > 2:
            restore_from_json(sys.argv[2])
        else:
            print("Uso: python backup_restore.py [backup|restore <archivo>]")
    else:
        backup_database()
