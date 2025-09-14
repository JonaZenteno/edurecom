# FICHA TÉCNICA - EduRecom
## Sistema de Recomendación de Formación Docente

---

## 📋 INFORMACIÓN GENERAL

**Nombre del Proyecto:** EduRecom  
**Tipo:** Sistema Web de Recomendación de Formación Docente  
**Tecnología:** Python Flask + Machine Learning  
**Despliegue:** Railway (Producción)  
**Base de Datos:** SQLite (Desarrollo) / PostgreSQL (Producción)  

---

## 🎯 OBJETIVO DEL SISTEMA

EduRecom es un sistema inteligente que recomienda cursos de formación docente personalizados basados en el perfil profesional, habilidades digitales y necesidades específicas de cada educador.

### **Problema que Resuelve:**
- **Falta de personalización** en la oferta de formación docente
- **Desconocimiento de necesidades específicas** de cada educador
- **Falta de orientación** en la selección de cursos relevantes
- **Desperdicio de recursos** en formación no pertinente

---

## 🏗️ ARQUITECTURA DEL SISTEMA

### **Frontend:**
- **HTML5 + CSS3 + Bootstrap 5**
- **JavaScript** para interactividad
- **Responsive Design** para dispositivos móviles
- **Templates Jinja2** para renderizado dinámico

### **Backend:**
- **Python Flask** - Framework web
- **Flask-Login** - Gestión de sesiones
- **Flask-WTF** - Formularios seguros
- **SQLAlchemy** - ORM para base de datos

### **Machine Learning:**
- **Scikit-learn** - Algoritmos de clustering
- **Pandas** - Manipulación de datos
- **NumPy** - Cálculos numéricos
- **Joblib** - Persistencia de modelos

### **Base de Datos:**
- **SQLite** - Desarrollo local
- **PostgreSQL** - Producción (Railway)
- **Migraciones** - Alembic

---

## 🔧 FUNCIONALIDADES PRINCIPALES

### **1. Sistema de Usuarios**
- ✅ **Registro de usuarios** con validación
- ✅ **Autenticación segura** con hash de contraseñas
- ✅ **Gestión de perfiles** completos
- ✅ **Roles diferenciados** (Usuario/Administrador)

### **2. Formulario de Perfil Inteligente**
- ✅ **14 preguntas dinámicas** configurables
- ✅ **Validación en tiempo real**
- ✅ **Campos obligatorios** con valores por defecto
- ✅ **Interfaz intuitiva** y responsive

### **3. Sistema de Recomendación**
- ✅ **Algoritmo de clustering** personalizado
- ✅ **Asignación automática** de grupos de formación
- ✅ **Fallback manual** para casos especiales
- ✅ **Recomendaciones personalizadas** por grupo

### **4. Panel de Administración**
- ✅ **Dashboard con métricas** en tiempo real
- ✅ **Gestión de usuarios** completa
- ✅ **Configuración de preguntas** dinámicas
- ✅ **Gestión de cursos** (CRUD)
- ✅ **Estadísticas de uso** del sistema

### **5. Catálogo de Cursos**
- ✅ **Cursos organizados por grupos** de formación
- ✅ **Información detallada** de cada curso
- ✅ **Enlaces directos** a plataformas
- ✅ **Seguimiento de visualizaciones**

---

## 📊 GRUPOS DE FORMACIÓN

El sistema clasifica a los usuarios en 4 grupos principales:

### **1. Alfabetización Digital Básica**
- **Perfil:** Docentes con habilidades digitales básicas (1-2/5)
- **Necesidad:** Fundamentos de tecnología educativa
- **Cursos:** Introducción a herramientas digitales, ciudadanía digital

### **2. Habilidades Digitales Avanzadas**
- **Perfil:** Docentes con habilidades digitales avanzadas (4-5/5)
- **Necesidad:** Especialización y herramientas avanzadas
- **Cursos:** IA en educación, programación, herramientas avanzadas

### **3. Fortalecimiento Institucional**
- **Perfil:** Directivos o docentes con interés en liderazgo
- **Necesidad:** Gestión educativa y liderazgo
- **Cursos:** Liderazgo educativo, gestión de equipos, innovación

### **4. Innovación Educativa**
- **Perfil:** Docentes innovadores con interés en nuevas metodologías
- **Necesidad:** Metodologías innovadoras y creatividad
- **Cursos:** Design thinking, gamificación, metodologías activas

---

## 🤖 ALGORITMO DE RECOMENDACIÓN

### **Proceso de Clustering:**
1. **Recolección de datos** del perfil del usuario
2. **Preprocesamiento** y normalización
3. **Aplicación de K-Means** clustering
4. **Asignación de grupo** basada en cluster
5. **Recomendación de cursos** específicos

### **Variables de Entrada:**
- Habilidades digitales (4 variables)
- Apoyo institucional (2 variables)
- Intereses específicos (3 variables)
- Características demográficas (4 variables)

### **Fallback Manual:**
Si el algoritmo automático falla, se usa lógica de reglas:
```python
if avg_digital_skills < 3:
    grupo = "Alfabetización Digital Básica"
elif interest_leadership:
    grupo = "Fortalecimiento Institucional"
elif interest_innovation:
    grupo = "Innovación Educativa"
else:
    grupo = "Habilidades Digitales Avanzadas"
```

---

## 🗄️ MODELO DE DATOS

### **Entidades Principales:**

#### **User (Usuario)**
- `id` - Identificador único
- `username` - Nombre de usuario
- `email` - Correo electrónico
- `password_hash` - Hash de contraseña
- `created_at` - Fecha de creación

#### **UserProfile (Perfil de Usuario)**
- `id` - Identificador único
- `user_id` - Referencia al usuario
- `role` - Rol (profesor/director/asistente)
- `school_type` - Tipo de establecimiento
- `dependency` - Dependencia del establecimiento
- `age_range` - Rango de edad
- `digital_tools_skill` - Habilidad con herramientas TI (1-5)
- `advanced_tic_skill` - Habilidad con TIC avanzadas (1-5)
- `digital_citizenship_skill` - Conocimiento de ciudadanía digital (1-5)
- `teaching_tech_skill` - Habilidad para usar tecnología en enseñanza (1-5)
- `leadership_support` - Apoyo del liderazgo (1-5)
- `resource_support` - Recursos disponibles (1-5)
- `interest_digital_literacy` - Interés en alfabetización digital
- `interest_educational_innovation` - Interés en innovación educativa
- `interest_leadership` - Interés en liderazgo
- `learning_format` - Formato de aprendizaje preferido
- `assigned_group` - Grupo de formación asignado

#### **Course (Curso)**
- `id` - Identificador único
- `title` - Título del curso
- `description` - Descripción
- `link` - Enlace al curso
- `group` - Grupo de formación
- `duration` - Duración
- `format` - Formato del curso
- `views_count` - Contador de visualizaciones

#### **CourseView (Visualización de Curso)**
- `id` - Identificador único
- `course_id` - Referencia al curso
- `user_id` - Referencia al usuario
- `viewed_at` - Fecha de visualización

---

## 🚀 DESPLIEGUE Y CONFIGURACIÓN

### **Entorno de Producción (Railway):**
- **URL:** https://edurecom-production-5bda.up.railway.app
- **Rama:** railway-deployment
- **Builder:** Nixpacks
- **Runtime:** Python
- **Base de datos:** SQLite persistente

### **Variables de Entorno:**
```bash
RAILWAY_ENVIRONMENT=production
SESSION_SECRET=clave_secreta_segura
DATABASE_URL=sqlite:///tmp/edurecom.db
```

### **Comando de Inicio:**
```bash
python init_db.py && python check_courses.py && python create_test_users.py && python setup_questions.py && gunicorn --bind 0.0.0.0:$PORT app:app
```

---

## 👥 USUARIOS DE PRUEBA

### **Administrador:**
- **Usuario:** `admin`
- **Contraseña:** `admin123`
- **Acceso:** Panel de administración completo

### **Usuarios de Prueba:**
1. **testuser1** / `test123` → Grupo: Alfabetización Digital Básica
2. **testuser2** / `test123` → Grupo: Habilidades Digitales Avanzadas
3. **testuser3** / `test123` → Grupo: Fortalecimiento Institucional

---

## 📈 MÉTRICAS Y ESTADÍSTICAS

### **Dashboard de Administración:**
- **Total de usuarios** registrados
- **Número de clusters** activos
- **Cursos más visualizados** por grupo
- **Total de visualizaciones** del sistema
- **Top 5 cursos** más populares

### **Seguimiento de Usuarios:**
- **Registro de visualizaciones** de cursos
- **Análisis de comportamiento** por grupo
- **Métricas de engagement** del sistema

---

## 🔒 SEGURIDAD

### **Autenticación:**
- **Hash de contraseñas** con Werkzeug
- **Sesiones seguras** con Flask-Login
- **Protección CSRF** con Flask-WTF
- **Validación de formularios** en servidor

### **Autorización:**
- **Roles diferenciados** (Usuario/Administrador)
- **Protección de rutas** con decoradores
- **Validación de permisos** en cada acción

### **Datos:**
- **Validación de entrada** en todos los formularios
- **Sanitización de datos** antes de guardar
- **Manejo seguro de errores** sin exposición de información

---

## 🧪 TESTING Y CALIDAD

### **Pruebas Implementadas:**
- **Pruebas de autenticación** (`test_auth.py`)
- **Validación de formularios**
- **Pruebas de integración** del sistema
- **Pruebas de rendimiento** con Locust

### **Logging y Monitoreo:**
- **Logs detallados** de todas las operaciones
- **Seguimiento de errores** y excepciones
- **Métricas de rendimiento** del sistema

---

## 📚 RECURSOS Y DOCUMENTACIÓN

### **Archivos de Configuración:**
- `requirements.txt` - Dependencias Python
- `railway.json` - Configuración de Railway
- `questions_admin.json` - Preguntas del formulario
- `MDS/cursos.json` - Catálogo de cursos

### **Scripts de Utilidad:**
- `init_db.py` - Inicialización de base de datos
- `check_courses.py` - Verificación de cursos
- `create_test_users.py` - Creación de usuarios de prueba
- `setup_questions.py` - Configuración de preguntas
- `backup_restore.py` - Backup y restauración

---

## 🎯 PUNTOS CLAVE PARA LA PRESENTACIÓN

### **1. Innovación Tecnológica:**
- **Machine Learning** aplicado a educación
- **Personalización** de recomendaciones
- **Algoritmo de clustering** adaptativo

### **2. Impacto Educativo:**
- **Mejora la pertinencia** de la formación docente
- **Optimiza recursos** educativos
- **Facilita la toma de decisiones** en formación

### **3. Escalabilidad:**
- **Arquitectura modular** y extensible
- **Base de datos** optimizada
- **Despliegue en la nube** con Railway

### **4. Usabilidad:**
- **Interfaz intuitiva** y responsive
- **Proceso simple** de registro y uso
- **Resultados claros** y accionables

---

## 🔮 FUTURAS MEJORAS

### **Corto Plazo:**
- **Integración con APIs** de plataformas educativas
- **Notificaciones** por email
- **Reportes** de progreso personalizados

### **Mediano Plazo:**
- **App móvil** nativa
- **Integración con LMS** existentes
- **Análisis predictivo** avanzado

### **Largo Plazo:**
- **IA conversacional** para recomendaciones
- **Realidad virtual** en formación
- **Blockchain** para certificaciones

---

## 📞 INFORMACIÓN DE CONTACTO

**Desarrollador:** [Tu Nombre]  
**Email:** [Tu Email]  
**GitHub:** [Tu GitHub]  
**LinkedIn:** [Tu LinkedIn]  

**Repositorio:** https://github.com/JonaZenteno/edurecom  
**Demo en Vivo:** https://edurecom-production-5bda.up.railway.app  

---

*Este documento fue generado automáticamente para la presentación del proyecto de titulación EduRecom.*
