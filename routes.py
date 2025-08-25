from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
from models import User, UserProfile, Course
from forms import RegistrationForm, LoginForm, ProfileForm, AdminConfigForm
from utils import assign_group
from functools import wraps
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import json
import os

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Debes iniciar sesión para acceder a esta página.', 'danger')
            return redirect(url_for('login'))
        
        if not current_user.profile:
            flash('Debes completar tu perfil para acceder a esta página.', 'warning')
            return redirect(url_for('profile_form'))
        
        if not hasattr(current_user.profile, 'role') or current_user.profile.role != 'admin':
            flash('Acceso restringido solo para administradores.', 'danger')
            return redirect(url_for('index'))
        
        return f(*args, **kwargs)
    return decorated_function

def register_routes(app):
    @app.route('/')
    def index():
        if current_user.is_authenticated:
            if current_user.profile:
                return redirect(url_for('recommendations'))
            else:
                return redirect(url_for('profile_form'))
        return render_template('index.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        
        form = RegistrationForm()
        if form.validate_on_submit():
            # Verificar si el nombre de usuario o email ya existe
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                flash('El nombre de usuario ya está en uso. Elige otro.', 'danger')
                return render_template('register.html', form=form)
            
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                flash('El correo electrónico ya está registrado.', 'danger')
                return render_template('register.html', form=form)
            
            # Crear nuevo usuario
            user = User(
                username=form.username.data,
                email=form.email.data,
                password_hash=generate_password_hash(form.password.data)
            )
            db.session.add(user)
            db.session.commit()
            
            flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        
        return render_template('register.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash(f'¡Bienvenido/a, {user.username}!', 'success')
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('index'))
            else:
                flash('Nombre de usuario o contraseña incorrectos.', 'danger')
        
        return render_template('login.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Has cerrado sesión exitosamente.', 'info')
        return redirect(url_for('index'))

    @app.route('/profile', methods=['GET', 'POST'])
    @login_required
    def profile_form():
        # Cargar preguntas dinámicas
        questions_path = 'questions_admin.json'
        if os.path.exists(questions_path):
            with open(questions_path, 'r', encoding='utf-8') as f:
                questions = json.load(f)
        else:
            questions = []
        # Crear formulario dinámico
        class DynamicProfileForm(FlaskForm):
            pass
        for q in questions:
            if q['type'] == 'select':
                choices_data = q.get('choices', [])
                if choices_data and isinstance(choices_data[0], dict):
                    choices = [(c['value'], c['label']) for c in choices_data]
                else:
                    choices = [(c, c) for c in choices_data]
                setattr(DynamicProfileForm, q['name'], SelectField(q['label'], choices=choices, validators=[DataRequired()]))
            elif q['type'] == 'text':
                setattr(DynamicProfileForm, q['name'], StringField(q['label'], validators=[DataRequired()]))
            elif q['type'] == 'boolean':
                setattr(DynamicProfileForm, q['name'], BooleanField(q['label']))
        setattr(DynamicProfileForm, 'submit', SubmitField('Obtener recomendaciones'))
        form = DynamicProfileForm()
        # Si el usuario ya tiene perfil, poblar el formulario
        if current_user.profile and request.method == 'GET':
            profile = current_user.profile
            for q in questions:
                if hasattr(form, q['name']) and hasattr(profile, q['name']):
                    getattr(form, q['name']).data = getattr(profile, q['name'])
        if form.validate_on_submit():
            if current_user.profile:
                profile = current_user.profile
            else:
                profile = UserProfile(user_id=current_user.id)
            
            # Procesar cada pregunta y asignar valores con validación
            for q in questions:
                if hasattr(form, q['name']):
                    # Si el usuario es admin y ya tiene perfil, no actualizar el rol
                    if current_user.profile and hasattr(current_user.profile, 'role') and current_user.profile.role == 'admin' and q['name'] == 'role':
                        continue

                    field_value = getattr(form, q['name']).data
                    
                    # Convertir valores según el tipo de campo
                    if q['type'] == 'select':
                        if q['name'] in ['digital_tools_skill', 'advanced_tic_skill', 'digital_citizenship_skill', 
                                       'teaching_tech_skill', 'leadership_support', 'resource_support']:
                            # Convertir a entero para campos numéricos
                            field_value = int(field_value) if field_value else 3
                        else:
                            # Para campos de texto, usar valor por defecto si está vacío
                            field_value = field_value or 'profesor' if q['name'] == 'role' else \
                                        field_value or 'urbana' if q['name'] == 'school_type' else \
                                        field_value or 'municipal' if q['name'] == 'dependency' else \
                                        field_value or '31-40' if q['name'] == 'age_range' else \
                                        field_value or 'en-linea' if q['name'] == 'learning_format' else field_value
                    elif q['type'] == 'boolean':
                        # Para campos booleanos, usar False si es None
                        field_value = field_value if field_value is not None else False
                    
                    setattr(profile, q['name'], field_value)
            
            # Asignar grupo y guardar
            try:
                profile.assigned_group = assign_group(profile)
                if not current_user.profile:
                    db.session.add(profile)
                db.session.commit()
                
                # Verificar que el perfil se haya guardado correctamente
                if profile.assigned_group:
                    flash('Perfil actualizado exitosamente. Aquí tienes tus recomendaciones personalizadas.', 'success')
                    return redirect(url_for('recommendations'))
                else:
                    flash('Error: No se pudo asignar un grupo de formación. Por favor, intenta nuevamente.', 'danger')
                    return render_template('profile_form.html', form=form, questions=questions)
                    
            except Exception as e:
                db.session.rollback()
                print(f"Error guardando perfil: {e}")
                flash('Error al guardar el perfil. Por favor, intenta nuevamente.', 'danger')
                return render_template('profile_form.html', form=form, questions=questions)
        return render_template('profile_form.html', form=form, questions=questions)

    @app.route('/recommendations')
    @login_required
    def recommendations():
        try:
            # Verificar que el usuario tenga un perfil
            if not current_user.profile:
                flash('Primero debes completar tu perfil para recibir recomendaciones.', 'warning')
                return redirect(url_for('profile_form'))
            
            # Verificar que el perfil tenga un grupo asignado
            if not hasattr(current_user.profile, 'assigned_group') or not current_user.profile.assigned_group:
                flash('Error: No se pudo asignar un grupo de formación. Por favor, actualiza tu perfil.', 'danger')
                return redirect(url_for('profile_form'))
            
            # Get courses for the user's assigned group
            try:
                courses = Course.query.filter_by(group=current_user.profile.assigned_group).all()
                
                if not courses:
                    flash(f'No se encontraron cursos para el grupo "{current_user.profile.assigned_group}". Contacta al administrador.', 'warning')
                    # Fallback: mostrar cursos de todos los grupos
                    courses = Course.query.limit(10).all()
                    
            except Exception as e:
                print(f"Error al consultar cursos: {e}")
                flash('Error al cargar los cursos. Mostrando cursos disponibles.', 'warning')
                courses = Course.query.limit(10).all()
            
            return render_template('recommendations.html', 
                                 courses=courses, 
                                 group=current_user.profile.assigned_group,
                                 profile=current_user.profile)
                             
        except Exception as e:
            print(f"Error en recomendaciones: {e}")
            flash('Ocurrió un error inesperado. Por favor, intenta nuevamente.', 'danger')
            return redirect(url_for('profile_form'))

    @app.route('/admin/dashboard')
    @login_required
    @admin_required
    def admin_dashboard():
        # Métricas: número de usuarios, clusters activos, recomendaciones más vistas
        num_usuarios = User.query.count()
        num_clusters = db.session.query(UserProfile.assigned_group).distinct().count()
        # Top recomendaciones (cursos más vistos por grupo)
        top_recomendaciones = db.session.query(Course.group, db.func.count(Course.id)).group_by(Course.group).all()
        return render_template('admin_dashboard.html', num_usuarios=num_usuarios, num_clusters=num_clusters, top_recomendaciones=top_recomendaciones)

    @app.route('/admin/users')
    @login_required
    @admin_required
    def admin_users():
        users = User.query.all()
        return render_template('admin_users.html', users=users)

    @app.route('/admin/users/<int:user_id>/make_admin', methods=['POST'])
    @login_required
    @admin_required
    def make_admin(user_id):
        user = User.query.get_or_404(user_id)
        if user.profile:
            user.profile.role = 'admin'
            db.session.commit()
            flash('Rol de administrador asignado correctamente.', 'success')
        else:
            flash('El usuario no tiene perfil para asignar rol.', 'danger')
        return redirect(url_for('admin_users'))

    @app.route('/admin/config', methods=['GET', 'POST'])
    @login_required
    @admin_required
    def admin_config():
        # Configuración simplificada sin archivos externos
        default_config = {'n_clusters': 4, 'confidence_threshold': 0.7}
        form = AdminConfigForm(data=default_config)
        
        if form.validate_on_submit():
            # Aquí podrías implementar la lógica para guardar en base de datos
            flash('Configuración actualizada correctamente.', 'success')
            return redirect(url_for('admin_config'))
            
        return render_template('admin_config.html', form=form, config=default_config)

    @app.route('/admin/questions', methods=['GET', 'POST'])
    @login_required
    @admin_required
    def admin_questions():
        questions_path = 'questions_admin.json'
        # Estructura: lista de preguntas, cada una con tipo, label, opciones (si aplica)
        if os.path.exists(questions_path):
            with open(questions_path, 'r', encoding='utf-8') as f:
                questions = json.load(f)
        else:
            # Preguntas por defecto (ejemplo)
            questions = [
                {"name": "role", "type": "select", "label": "¿Cuál es tu rol en el establecimiento educativo?", "choices": ["profesor", "director", "asistente"]},
                {"name": "age_range", "type": "select", "label": "¿En qué rango de edad te encuentras?", "choices": ["20-30", "31-40", "41-50", "51+"]},
                {"name": "digital_tools_skill", "type": "select", "label": "Herramientas TI básicas", "choices": ["1", "2", "3", "4", "5"]}
            ]
        if request.method == 'POST':
            # Recibir cambios desde el formulario (agregar, editar, eliminar preguntas)
            action = request.form.get('action')
            if action == 'add':
                questions.append({"name": request.form['name'], "type": request.form['type'], "label": request.form['label'], "choices": request.form.get('choices', '').split(',') if request.form.get('choices') else []})
            elif action == 'edit':
                idx = int(request.form['idx'])
                questions[idx] = {"name": request.form['name'], "type": request.form['type'], "label": request.form['label'], "choices": request.form.get('choices', '').split(',') if request.form.get('choices') else []}
            elif action == 'delete':
                idx = int(request.form['idx'])
                questions.pop(idx)
            with open(questions_path, 'w', encoding='utf-8') as f:
                json.dump(questions, f, ensure_ascii=False, indent=2)
            flash('Preguntas actualizadas correctamente.', 'success')
            return redirect(url_for('admin_questions'))
        return render_template('admin_questions.html', questions=questions)
