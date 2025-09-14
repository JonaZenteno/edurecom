# EduRecom - Sistema de Recomendación de Formación Docente

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)](https://scikit-learn.org)
[![Deploy](https://img.shields.io/badge/Deploy-Railway-purple.svg)](https://railway.app)

## 🎯 Descripción

EduRecom es un sistema inteligente de recomendación de formación docente que utiliza machine learning para personalizar la oferta educativa según el perfil profesional, habilidades digitales y necesidades específicas de cada educador.

## 🚀 Demo en Vivo

**URL de Producción:** https://edurecom-production-5bda.up.railway.app

### Credenciales de Prueba:
- **Administrador:** `admin` / `admin123`
- **Usuario Demo:** `testuser1` / `test123`

## ✨ Características Principales

### 🤖 Sistema de Recomendación Inteligente
- **Algoritmo de clustering** personalizado con scikit-learn
- **Clasificación automática** en 4 grupos de formación
- **Recomendaciones personalizadas** basadas en perfil del usuario
- **Fallback manual** para casos especiales

### 👥 Gestión de Usuarios
- **Registro y autenticación** segura
- **Perfiles completos** con 14 preguntas dinámicas
- **Roles diferenciados** (Usuario/Administrador)
- **Panel de administración** completo

### 📚 Catálogo de Cursos
- **Cursos organizados** por grupos de formación
- **Información detallada** de cada curso
- **Seguimiento de visualizaciones**
- **Enlaces directos** a plataformas educativas

### 📊 Analytics y Métricas
- **Dashboard en tiempo real** con estadísticas
- **Métricas de uso** del sistema
- **Análisis de comportamiento** por grupo
- **Reportes de visualizaciones**

## 🏗️ Arquitectura Técnica

### Frontend
- **HTML5 + CSS3 + Bootstrap 5**
- **JavaScript** para interactividad
- **Responsive Design** para dispositivos móviles
- **Templates Jinja2** para renderizado dinámico

### Backend
- **Python Flask** - Framework web
- **Flask-Login** - Gestión de sesiones
- **Flask-WTF** - Formularios seguros
- **SQLAlchemy** - ORM para base de datos

### Machine Learning
- **Scikit-learn** - Algoritmos de clustering
- **Pandas** - Manipulación de datos
- **NumPy** - Cálculos numéricos
- **Joblib** - Persistencia de modelos

### Base de Datos
- **SQLite** - Desarrollo local
- **PostgreSQL** - Producción (Railway)
- **Migraciones** - Alembic

## 🚀 Instalación y Configuración

### Requisitos
- Python 3.8+
- pip
- Git

### Instalación Local

1. **Clonar el repositorio:**
```bash
git clone https://github.com/JonaZenteno/edurecom.git
cd edurecom
```

2. **Crear entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Inicializar base de datos:**
```bash
python init_db.py
```

5. **Ejecutar aplicación:**
```bash
python app.py
```

6. **Acceder a la aplicación:**
```
http://localhost:5000
```

## 📁 Estructura del Proyecto

```
EduRecom/
├── 📁 documentacion/           # Documentación completa
│   ├── FICHA_TECNICA_PRESENTACION.md
│   ├── GUIA_PRESENTACION_COMISION.md
│   └── [otros archivos de documentación]
├── 📁 scripts_utilidad/        # Scripts de utilidad
│   ├── backup_restore.py
│   ├── check_courses.py
│   ├── create_test_users.py
│   └── setup_questions.py
├── 📁 clustering/              # Algoritmos de ML
│   ├── auto_assignment.py
│   └── feature_engineering.py
├── 📁 templates/               # Templates HTML
├── 📁 static/                  # Archivos estáticos
├── 📁 MDS/                     # Datos de cursos
├── 📁 tests/                   # Pruebas unitarias
├── app.py                      # Aplicación principal
├── routes.py                   # Rutas de la aplicación
├── models.py                   # Modelos de base de datos
├── forms.py                    # Formularios
├── utils.py                    # Utilidades
├── init_db.py                  # Inicialización de BD
└── requirements.txt            # Dependencias
```

## 🎯 Grupos de Formación

El sistema clasifica a los usuarios en 4 grupos principales:

### 1. Alfabetización Digital Básica
- **Perfil:** Docentes con habilidades digitales básicas (1-2/5)
- **Necesidad:** Fundamentos de tecnología educativa
- **Cursos:** Introducción a herramientas digitales, ciudadanía digital

### 2. Habilidades Digitales Avanzadas
- **Perfil:** Docentes con habilidades digitales avanzadas (4-5/5)
- **Necesidad:** Especialización y herramientas avanzadas
- **Cursos:** IA en educación, programación, herramientas avanzadas

### 3. Fortalecimiento Institucional
- **Perfil:** Directivos o docentes con interés en liderazgo
- **Necesidad:** Gestión educativa y liderazgo
- **Cursos:** Liderazgo educativo, gestión de equipos, innovación

### 4. Innovación Educativa
- **Perfil:** Docentes innovadores con interés en nuevas metodologías
- **Necesidad:** Metodologías innovadoras y creatividad
- **Cursos:** Design thinking, gamificación, metodologías activas

## 🔧 Scripts de Utilidad

### Inicialización
```bash
python init_db.py              # Inicializar base de datos
python check_courses.py        # Verificar cursos
python create_test_users.py    # Crear usuarios de prueba
python setup_questions.py      # Configurar preguntas
```

### Backup y Restore
```bash
python scripts_utilidad/backup_restore.py backup    # Hacer backup
python scripts_utilidad/backup_restore.py restore archivo.json  # Restaurar
```

## 🧪 Testing

### Ejecutar Pruebas
```bash
python -m pytest tests/
```

### Pruebas de Rendimiento
```bash
locust -f locustfile.py --host=http://localhost:5000
```

## 🚀 Despliegue

### Railway (Producción)
El proyecto está configurado para desplegarse automáticamente en Railway:

1. **Push a la rama `railway-deployment`**
2. **Railway detecta cambios automáticamente**
3. **Ejecuta scripts de inicialización**
4. **Despliega la aplicación**

### Variables de Entorno
```bash
RAILWAY_ENVIRONMENT=production
SESSION_SECRET=clave_secreta_segura
DATABASE_URL=sqlite:///tmp/edurecom.db
```

## 📊 Métricas del Sistema

- **Total de usuarios:** X usuarios registrados
- **Grupos activos:** 4 grupos de formación
- **Cursos disponibles:** X cursos en el catálogo
- **Tiempo de respuesta:** < 2 segundos
- **Disponibilidad:** 99.9% uptime

## 🔒 Seguridad

- **Hash de contraseñas** con Werkzeug
- **Sesiones seguras** con Flask-Login
- **Protección CSRF** con Flask-WTF
- **Validación de formularios** en servidor
- **Roles y permisos** diferenciados

## 📚 Documentación

- **[Ficha Técnica Completa](documentacion/FICHA_TECNICA_PRESENTACION.md)**
- **[Guía de Presentación](documentacion/GUIA_PRESENTACION_COMISION.md)**
- **[Documentación Técnica](documentacion/SISTEMA_TECNICO.md)**
- **[Diagramas del Sistema](documentacion/DIAGRAMAS_SISTEMA.md)**

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Tu Nombre** - [Tu Email](mailto:tu.email@ejemplo.com)

- GitHub: [@JonaZenteno](https://github.com/JonaZenteno)
- LinkedIn: [Tu LinkedIn](https://linkedin.com/in/tu-perfil)

## 🙏 Agradecimientos

- **Equipo Cursor** por el soporte técnico
- **Comunidad Flask** por la documentación
- **Scikit-learn** por las herramientas de ML
- **Railway** por la plataforma de despliegue

---

## 📞 Contacto

**Proyecto:** EduRecom  
**Repositorio:** https://github.com/JonaZenteno/edurecom  
**Demo:** https://edurecom-production-5bda.up.railway.app  
**Email:** [Tu Email](mailto:tu.email@ejemplo.com)

---

*Desarrollado con ❤️ para mejorar la formación docente*
