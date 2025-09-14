#!/usr/bin/env python3
"""
Script para crear usuarios de prueba que se mantengan entre despliegues
"""
import os
from __init__ import create_app, db
from models import User, UserProfile
from werkzeug.security import generate_password_hash

def create_test_users():
    """Crea usuarios de prueba para testing"""
    app = create_app()
    
    with app.app_context():
        try:
            # Usuarios de prueba
            test_users = [
                {
                    "username": "testuser1",
                    "email": "test1@edurecom.com",
                    "password": "test123",
                    "role": "profesor",
                    "digital_skills": 2,  # Básico
                    "expected_group": "Alfabetización Digital Básica"
                },
                {
                    "username": "testuser2", 
                    "email": "test2@edurecom.com",
                    "password": "test123",
                    "role": "director",
                    "digital_skills": 4,  # Avanzado
                    "expected_group": "Habilidades Digitales Avanzadas"
                },
                {
                    "username": "testuser3",
                    "email": "test3@edurecom.com", 
                    "password": "test123",
                    "role": "profesor",
                    "digital_skills": 3,
                    "interest_leadership": True,
                    "expected_group": "Fortalecimiento Institucional"
                }
            ]
            
            users_created = 0
            
            for user_data in test_users:
                # Verificar si el usuario ya existe
                existing_user = User.query.filter_by(username=user_data["username"]).first()
                if existing_user:
                    print(f"👤 Usuario {user_data['username']} ya existe")
                    continue
                
                # Crear usuario
                user = User(
                    username=user_data["username"],
                    email=user_data["email"],
                    password_hash=generate_password_hash(user_data["password"])
                )
                db.session.add(user)
                db.session.flush()  # Para obtener el ID
                
                # Crear perfil
                profile = UserProfile(
                    user_id=user.id,
                    role=user_data["role"],
                    school_type='urbana',
                    dependency='municipal',
                    age_range='31-40',
                    digital_tools_skill=user_data["digital_skills"],
                    advanced_tic_skill=user_data["digital_skills"],
                    digital_citizenship_skill=user_data["digital_skills"],
                    teaching_tech_skill=user_data["digital_skills"],
                    leadership_support=3,
                    resource_support=3,
                    interest_digital_literacy=False,
                    interest_educational_innovation=user_data.get("interest_leadership", False),
                    interest_leadership=user_data.get("interest_leadership", False),
                    learning_format='en-linea',
                    assigned_group=user_data["expected_group"]
                )
                db.session.add(profile)
                users_created += 1
                
                print(f"✅ Usuario de prueba creado: {user_data['username']} (Grupo esperado: {user_data['expected_group']})")
            
            db.session.commit()
            print(f"🎯 {users_created} usuarios de prueba creados")
            
            # Mostrar resumen
            total_users = User.query.count()
            total_profiles = UserProfile.query.count()
            print(f"📊 Total usuarios: {total_users}, Total perfiles: {total_profiles}")
            
        except Exception as e:
            db.session.rollback()
            print(f"❌ Error creando usuarios de prueba: {e}")
            raise

if __name__ == "__main__":
    create_test_users()
