# EduRecom - Sistema de Recomendación de Cursos Educativos

Sistema inteligente de recomendación de cursos de formación docente basado en competencias digitales y perfil profesional.

## 🚀 Características

- **Recomendaciones personalizadas** basadas en perfil profesional
- **Clasificación automática** de usuarios en grupos de formación
- **Panel de administración** completo para gestión de cursos
- **Seguimiento de visualizaciones** y estadísticas de uso
- **Interfaz moderna** y responsive

## 📋 Requisitos

- Python 3.8+
- Flask
- SQLite
- Bootstrap 5

## 🛠️ Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <repository-url>
   cd EduRecom
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar base de datos**
   ```bash
   python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
   ```

4. **Ejecutar aplicación**
   ```bash
   python app.py
   ```

5. **Acceder a la aplicación**
   - URL: http://localhost:5000
   - Usuario admin por defecto: `admin`

## 📁 Estructura del Proyecto

```
EduRecom/
├── app.py                 # Aplicación principal
├── models.py              # Modelos de base de datos
├── routes.py              # Rutas de la aplicación
├── forms.py               # Formularios WTForms
├── utils.py               # Utilidades del sistema
├── static/                # Archivos estáticos
│   ├── css/
│   └── images/
├── templates/             # Plantillas HTML
├── instance/              # Base de datos SQLite
└── clustering/            # Modelos de clustering
```

## 👥 Usuarios

### Administradores
- Acceso completo al panel de administración
- Gestión de cursos y usuarios
- Estadísticas del sistema

### Usuarios regulares
- Completar perfil profesional
- Recibir recomendaciones personalizadas
- Acceder a cursos recomendados

## 🎯 Grupos de Formación

1. **Alfabetización Digital Básica** - Habilidades digitales fundamentales
2. **Habilidades Digitales Avanzadas** - TIC avanzadas para educadores
3. **Fortalecimiento Institucional** - Liderazgo y gestión educativa
4. **Innovación Educativa** - Estrategias innovadoras en educación
5. **Ciudadanía Digital** - Ética y seguridad digital
6. **Recursos Digitales** - Herramientas y plataformas educativas

## 🔧 Configuración

### Variables de Entorno
```bash
FLASK_ENV=production
SECRET_KEY=your-secret-key
```

### Base de Datos
La aplicación utiliza SQLite por defecto. Para producción, considera migrar a PostgreSQL o MySQL.

## 📊 Estadísticas

El sistema incluye:
- Contador de visualizaciones por curso
- Estadísticas de usuarios por grupo
- Métricas de uso del sistema

## 🚀 Despliegue

### Desarrollo
```bash
python app.py
```

### Producción
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📞 Soporte

Para soporte técnico, contacta al equipo de desarrollo.