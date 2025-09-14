# Estructura del Proyecto EduRecom

## 📁 Organización de Archivos

### **Archivos Principales (Raíz)**
```
EduRecom/
├── app.py                      # 🚀 Aplicación principal
├── routes.py                   # 🛣️ Rutas y controladores
├── models.py                   # 🗄️ Modelos de base de datos
├── forms.py                    # 📝 Formularios WTForms
├── utils.py                    # 🔧 Utilidades y clustering
├── init_db.py                  # 🗃️ Inicialización de BD
├── requirements.txt            # 📦 Dependencias Python
├── railway.json               # 🚂 Configuración Railway
├── questions_admin.json       # ❓ Preguntas del formulario
└── README.md                  # 📖 Documentación principal
```

### **Carpetas Organizadas**

#### **📁 documentacion/**
Contiene toda la documentación del proyecto:
- `FICHA_TECNICA_PRESENTACION.md` - Ficha técnica completa
- `GUIA_PRESENTACION_COMISION.md` - Guía para la presentación
- `ESTRUCTURA_PROYECTO.md` - Este archivo
- `SISTEMA_TECNICO.md` - Documentación técnica
- `DIAGRAMAS_SISTEMA.md` - Diagramas y arquitectura
- `RESUMEN_EJECUTIVO.md` - Resumen ejecutivo
- `SOLUCION_REDIRECCION.md` - Solución de problemas
- `SOLUCION_ADMIN_QUESTIONS.md` - Solución admin
- `MEJORAS_IMPLEMENTADAS.md` - Mejoras realizadas
- `DIAGNOSTICO_CURSOS.md` - Diagnóstico de cursos
- `railway_setup.md` - Configuración Railway

#### **📁 scripts_utilidad/**
Scripts de utilidad y mantenimiento:
- `backup_restore.py` - Backup y restauración de BD
- `check_courses.py` - Verificación de cursos
- `create_test_users.py` - Creación de usuarios de prueba
- `setup_questions.py` - Configuración de preguntas

#### **📁 clustering/**
Algoritmos de machine learning:
- `auto_assignment.py` - Asignación automática de grupos
- `feature_engineering.py` - Ingeniería de características

#### **📁 templates/**
Templates HTML de la aplicación:
- `base.html` - Template base
- `index.html` - Página principal
- `login.html` - Página de login
- `register.html` - Página de registro
- `profile_form.html` - Formulario de perfil
- `recommendations.html` - Página de recomendaciones
- `admin_dashboard.html` - Dashboard de administración
- `admin_users.html` - Gestión de usuarios
- `admin_questions.html` - Gestión de preguntas
- `admin_courses.html` - Gestión de cursos
- `admin_config.html` - Configuración del sistema

#### **📁 static/**
Archivos estáticos:
- `css/style.css` - Estilos CSS
- `images/` - Imágenes y iconos

#### **📁 MDS/**
Datos de cursos:
- `cursos.json` - Catálogo de cursos

#### **📁 tests/**
Pruebas unitarias:
- `test_auth.py` - Pruebas de autenticación

#### **📁 instance/**
Base de datos local:
- `edurecom.db` - Base de datos SQLite

#### **📁 logs/**
Archivos de log:
- `edurecom.log` - Logs de la aplicación
- `clustering.log` - Logs de clustering

## 🔧 Archivos de Configuración

### **requirements.txt**
```txt
Flask==2.3.3
Flask-Login==0.6.3
Flask-WTF==1.1.1
Flask-SQLAlchemy==3.0.5
Werkzeug==2.3.7
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
joblib==1.3.2
gunicorn==21.2.0
```

### **railway.json**
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python init_db.py && python check_courses.py && python create_test_users.py && python setup_questions.py && gunicorn --bind 0.0.0.0:$PORT app:app",
    "healthcheckPath": "/",
    "healthcheckTimeout": 100,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

## 🗄️ Modelo de Datos

### **User (Usuario)**
```python
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile = db.relationship('UserProfile', backref='user', uselist=False)
```

### **UserProfile (Perfil de Usuario)**
```python
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    school_type = db.Column(db.String(50), nullable=False)
    dependency = db.Column(db.String(50), nullable=False)
    age_range = db.Column(db.String(20), nullable=False)
    digital_tools_skill = db.Column(db.Integer, nullable=False)
    advanced_tic_skill = db.Column(db.Integer, nullable=False)
    digital_citizenship_skill = db.Column(db.Integer, nullable=False)
    teaching_tech_skill = db.Column(db.Integer, nullable=False)
    leadership_support = db.Column(db.Integer, nullable=False)
    resource_support = db.Column(db.Integer, nullable=False)
    interest_digital_literacy = db.Column(db.Boolean, default=False)
    interest_educational_innovation = db.Column(db.Boolean, default=False)
    interest_leadership = db.Column(db.Boolean, default=False)
    learning_format = db.Column(db.String(50), nullable=False)
    assigned_group = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

### **Course (Curso)**
```python
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=False)
    group = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=True)
    format = db.Column(db.String(50), nullable=True)
    views_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

### **CourseView (Visualización de Curso)**
```python
class CourseView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    viewed_at = db.Column(db.DateTime, default=datetime.utcnow)
    course = db.relationship('Course', backref='views')
    user = db.relationship('User', backref='course_views')
```

## 🛣️ Rutas de la Aplicación

### **Rutas Públicas**
- `/` - Página principal
- `/register` - Registro de usuarios
- `/login` - Inicio de sesión
- `/logout` - Cerrar sesión

### **Rutas de Usuario**
- `/profile` - Formulario de perfil
- `/recommendations` - Recomendaciones personalizadas
- `/course/<id>/view` - Visualización de curso

### **Rutas de Administración**
- `/admin/dashboard` - Dashboard de administración
- `/admin/users` - Gestión de usuarios
- `/admin/questions` - Gestión de preguntas
- `/admin/courses` - Gestión de cursos
- `/admin/config` - Configuración del sistema

## 🔧 Scripts de Utilidad

### **init_db.py**
- Inicializa la base de datos
- Crea tablas
- Carga cursos desde JSON
- Crea usuario administrador

### **check_courses.py**
- Verifica cursos en la base de datos
- Carga cursos si es necesario
- Muestra estadísticas

### **create_test_users.py**
- Crea usuarios de prueba
- Diferentes perfiles para testing
- Grupos de formación variados

### **setup_questions.py**
- Configura preguntas del formulario
- Crea archivo questions_admin.json
- Verifica integridad

### **backup_restore.py**
- Hace backup de la base de datos
- Exporta datos a JSON
- Restaura desde backup

## 🚀 Flujo de Despliegue

### **1. Inicialización**
```bash
python init_db.py
```

### **2. Verificación**
```bash
python check_courses.py
```

### **3. Usuarios de Prueba**
```bash
python create_test_users.py
```

### **4. Configuración**
```bash
python setup_questions.py
```

### **5. Aplicación**
```bash
gunicorn --bind 0.0.0.0:$PORT app:app
```

## 📊 Métricas y Logs

### **Logs de la Aplicación**
- `logs/edurecom.log` - Logs generales
- `logs/clustering.log` - Logs de clustering
- `edurecom.log` - Log principal

### **Métricas del Sistema**
- Total de usuarios registrados
- Número de clusters activos
- Cursos más visualizados
- Estadísticas de uso

## 🔒 Seguridad

### **Autenticación**
- Hash de contraseñas con Werkzeug
- Sesiones seguras con Flask-Login
- Protección CSRF con Flask-WTF

### **Autorización**
- Roles diferenciados (Usuario/Administrador)
- Protección de rutas con decoradores
- Validación de permisos

### **Validación**
- Validación de formularios en servidor
- Sanitización de datos
- Manejo seguro de errores

---

*Esta estructura está optimizada para mantenimiento, escalabilidad y presentación profesional.*
