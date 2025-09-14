import os
import argparse
from werkzeug.security import generate_password_hash
from __init__ import create_app, db
from models import User, UserProfile

def create_admin_user(username, email, password):
    """Crea un usuario administrador."""
    app = create_app()
    with app.app_context():
        print("Creando usuario administrador...")

        # Validar que no existan
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            print("El usuario o email ya existe.")
            return

        # Hashear la contraseña
        password_hash = generate_password_hash(password)

        # Crear el nuevo usuario y su perfil
        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )
        
        new_profile = UserProfile(
            user=new_user,
            role='admin',  # Asignar rol de administrador
            school_type='urbana',
            dependency='municipal',
            age_range='31-40',
            digital_tools_skill=5,
            advanced_tic_skill=5,
            digital_citizenship_skill=5,
            teaching_tech_skill=5,
            leadership_support=5,
            resource_support=5,
            learning_format='en-linea'
        )

        try:
            db.session.add(new_user)
            db.session.add(new_profile)
            db.session.commit()
            print(f"Usuario administrador '{username}' creado exitosamente.")
        except Exception as e:
            db.session.rollback()
            print(f"Error al crear el usuario administrador: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crear un usuario administrador.')
    parser.add_argument('username', type=str, help='Nombre de usuario del administrador')
    parser.add_argument('email', type=str, help='Email del administrador')
    parser.add_argument('password', type=str, help='Contraseña del administrador')
    args = parser.parse_args()
    
    create_admin_user(args.username, args.email, args.password)
