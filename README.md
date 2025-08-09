# EduRecom - Sistema Inteligente de Recomendación de Formación

Sistema de recomendación de formación para educadores chilenos basado en clustering y análisis de perfiles.

## 📁 Estructura del Proyecto

```
EduRecom/
├── app.py                     # Punto de entrada principal de la aplicación
├── __init__.py               # Configuración de Flask y extensiones
├── models.py                 # Modelos de base de datos
├── routes.py                 # Rutas de la aplicación
├── forms.py                  # Formularios de Flask-WTF
├── utils.py                  # Utilidades y lógica de clustering
├── init_data.py              # Inicialización de datos
├── questions_admin.json      # Configuración de preguntas dinámicas
├── pyproject.toml            # Configuración del proyecto y dependencias
├── uv.lock                   # Lock file de dependencias
│
├── clustering/               # Módulo de clustering
│   ├── __init__.py
│   ├── clustering_engine.py  # Motor principal de clustering
│   ├── data_preprocessing.py # Preprocesamiento de datos
│   ├── feature_engineering.py # Ingeniería de características
│   └── auto_assignment.py    # Asignación automática de grupos
│
├── scripts/                  # Scripts de desarrollo y análisis
│   ├── development/          # Scripts de desarrollo
│   │   ├── train_clustering.py
│   │   ├── test_clustering.py
│   │   ├── implement_clustering_improvements.py
│   │   └── improve_clustering_system.py
│   └── analysis/             # Scripts de análisis
│       └── analyze_and_improve_clustering.py
│
├── docs/                     # Documentación
│   ├── results/              # Resultados de análisis
│   │   ├── RESULTADOS_MEJORAS_CLUSTERING.md
│   │   └── RECOMENDACIONES_MEJORA_CLUSTERING.md
│   └── assets/               # Assets de documentación
│       └── attached_assets/
│
├── data/                     # Datos del proyecto
│   ├── Asistentes.csv
│   ├── Directores.csv
│   ├── RespuestasDocentes.csv
│   └── RespuesDocentesYDirectores.csv
│
├── templates/                # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── profile_form.html
│   ├── recommendations.html
│   ├── admin_dashboard.html
│   ├── admin_users.html
│   ├── admin_config.html
│   └── admin_questions.html
│
├── static/                   # Archivos estáticos
│   └── css/
│       └── style.css
│
└── instance/                 # Archivos de instancia (DB, etc.)
    └── education_recommender.db
```

## 🚀 Instalación y Uso

### Requisitos
- Python 3.11+
- Dependencias listadas en `pyproject.toml`

### Instalación
```bash
# Instalar dependencias
pip install -e .

# O usando uv (recomendado)
uv sync
```

### Ejecución
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 🔧 Funcionalidades

### Para Usuarios
- **Registro e Inicio de Sesión**: Sistema de autenticación completo
- **Perfil de Usuario**: Formulario dinámico para recopilar información
- **Recomendaciones**: Sistema de recomendación basado en clustering
- **Asignación de Grupos**: Automática con fallback manual

### Para Administradores
- **Dashboard**: Métricas y estadísticas del sistema
- **Gestión de Usuarios**: Ver y gestionar usuarios registrados
- **Configuración**: Ajustar parámetros del sistema
- **Gestión de Preguntas**: Configurar formularios dinámicos

## 🤖 Sistema de Clustering

El sistema utiliza un motor de clustering híbrido:
- **Asignación Automática**: Basada en modelos de machine learning
- **Fallback Manual**: Algoritmo de reglas cuando la confianza es baja
- **Modelos Guardados**: `clustering_model.pkl` y `improved_clustering_model.pkl`

## 📊 Datos

Los datos se almacenan en:
- **Base de Datos**: SQLite (`instance/education_recommender.db`)
- **Archivos CSV**: Datos de entrada en `data/`
- **Modelos**: Archivos `.pkl` en el directorio raíz

## 🛠️ Desarrollo

### Scripts de Desarrollo
- `scripts/development/train_clustering.py`: Entrenar modelos de clustering
- `scripts/development/test_clustering.py`: Probar el sistema de clustering
- `scripts/development/implement_clustering_improvements.py`: Implementar mejoras
- `scripts/development/improve_clustering_system.py`: Mejorar el sistema

### Scripts de Análisis
- `scripts/analysis/analyze_and_improve_clustering.py`: Análisis y mejora de clustering

## 📝 Documentación

- `docs/results/`: Resultados de análisis y mejoras
- `docs/assets/`: Documentos y assets relacionados

## 🔒 Seguridad

- Autenticación con Flask-Login
- Hashing de contraseñas con Werkzeug
- Validación de formularios con WTForms
- Control de acceso basado en roles

## 📈 Monitoreo

El sistema incluye:
- Logging configurado
- Métricas de clustering
- Estadísticas de usuarios
- Monitoreo de rendimiento

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es parte de un trabajo de título académico.
