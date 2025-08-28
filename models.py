from __init__ import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with profile
    profile = db.relationship('UserProfile', backref='user', uselist=False, cascade='all, delete-orphan')

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Información básica
    role = db.Column(db.String(50), nullable=False)  # profesor, director, asistente
    school_type = db.Column(db.String(50), nullable=False)  # rural, urbana, cientifico-humanista, tecnico-profesional
    dependency = db.Column(db.String(50), nullable=False)  # municipal, privada-subvencionada, privada-pagada
    age_range = db.Column(db.String(20), nullable=False)  # 20-30, 31-40, 41-50, 51+
    
    # Digital skills (1-5 scale)
    digital_tools_skill = db.Column(db.Integer, nullable=False)  # Herramientas TI básicas
    advanced_tic_skill = db.Column(db.Integer, nullable=False)  # TIC avanzadas
    digital_citizenship_skill = db.Column(db.Integer, nullable=False)  # Ciudadanía digital
    teaching_tech_skill = db.Column(db.Integer, nullable=False)  # Uso de tecnología en enseñanza
    
    # Institutional support (1-5 scale)
    leadership_support = db.Column(db.Integer, nullable=False)  # Liderazgo institucional
    resource_support = db.Column(db.Integer, nullable=False)  # Recursos disponibles
    
    # Interests (multiple choice)
    interest_digital_literacy = db.Column(db.Boolean, default=False)
    interest_educational_innovation = db.Column(db.Boolean, default=False)
    interest_leadership = db.Column(db.Boolean, default=False)
    
    # Learning format preference
    learning_format = db.Column(db.String(50), nullable=False)  # en-linea, talleres, autoaprendizaje
    
    # Assigned group
    assigned_group = db.Column(db.String(100), nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CourseView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    viewed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    course = db.relationship('Course', backref='views')
    user = db.relationship('User', backref='course_views')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=False)
    group = db.Column(db.String(100), nullable=False)  # Group this course belongs to
    duration = db.Column(db.String(50), nullable=True)
    format = db.Column(db.String(50), nullable=True)
    views_count = db.Column(db.Integer, default=0)  # Contador de visualizaciones
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
