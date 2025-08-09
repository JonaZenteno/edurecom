from __init__ import db
from models import Course

def init_courses():
    """Initialize the database with sample courses for each group"""
    
    # Verificar que los cursos se estén cargando
    if Course.query.count() > 0:
        return
    
    courses_data = [
        # Alfabetización Digital Básica
        {
            'title': 'Introducción a la Computación para Educadores',
            'description': 'Aprende los conceptos básicos de computación y herramientas digitales esenciales para el ámbito educativo.',
            'link': 'https://www.edx.org/course/introduccion-computacion-educadores',
            'group': 'Alfabetización Digital Básica',
            'duration': '4 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Microsoft Office para Docentes',
            'description': 'Domina Word, Excel y PowerPoint para crear materiales educativos efectivos y gestionar información académica.',
            'link': 'https://www.coursera.org/learn/microsoft-office-docentes',
            'group': 'Alfabetización Digital Básica',
            'duration': '6 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Navegación Segura en Internet',
            'description': 'Aprende a navegar de forma segura en internet y enseña a tus estudiantes sobre ciudadanía digital.',
            'link': 'https://www.futurelearn.com/courses/internet-seguro-educadores',
            'group': 'Alfabetización Digital Básica',
            'duration': '3 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Herramientas de Google para Educación',
            'description': 'Utiliza Google Classroom, Drive, Docs y otras herramientas de Google para mejorar tu práctica docente.',
            'link': 'https://skillshop.exclaimer.com/google-for-education',
            'group': 'Alfabetización Digital Básica',
            'duration': '5 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Comunicación Digital Efectiva',
            'description': 'Aprende a comunicarte efectivamente usando herramientas digitales con estudiantes, padres y colegas.',
            'link': 'https://www.udemy.com/course/comunicacion-digital-educadores',
            'group': 'Alfabetización Digital Básica',
            'duration': '3 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Gestión de Archivos Digitales',
            'description': 'Organiza y gestiona archivos digitales de manera eficiente para tu trabajo educativo.',
            'link': 'https://www.linkedin.com/learning/gestion-archivos-digitales',
            'group': 'Alfabetización Digital Básica',
            'duration': '2 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Introducción a las Redes Sociales Educativas',
            'description': 'Conoce cómo usar las redes sociales de manera profesional y educativa.',
            'link': 'https://www.canvas.net/browse/redes-sociales-educacion',
            'group': 'Alfabetización Digital Básica',
            'duration': '4 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Fundamentos de Seguridad Digital',
            'description': 'Protege tu información personal y profesional con buenas prácticas de seguridad digital.',
            'link': 'https://www.cybrary.it/course/seguridad-digital-educadores',
            'group': 'Alfabetización Digital Básica',
            'duration': '3 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Videoconferencias para Educadores',
            'description': 'Aprende a usar Zoom, Teams y otras plataformas de videoconferencia para clases virtuales.',
            'link': 'https://www.pluralsight.com/courses/videoconferencias-educacion',
            'group': 'Alfabetización Digital Básica',
            'duration': '2 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Creación de Presentaciones Digitales',
            'description': 'Diseña presentaciones atractivas y efectivas usando herramientas digitales modernas.',
            'link': 'https://www.skillshare.com/classes/presentaciones-digitales-educativas',
            'group': 'Alfabetización Digital Básica',
            'duration': '4 semanas',
            'format': 'Autoaprendizaje'
        },
        
        # Fortalecimiento Institucional
        {
            'title': 'Liderazgo Digital en Instituciones Educativas',
            'description': 'Desarrolla habilidades de liderazgo para implementar tecnología en tu institución educativa.',
            'link': 'https://www.edx.org/course/liderazgo-digital-educativo',
            'group': 'Fortalecimiento Institucional',
            'duration': '6 semanas',
            'format': 'Talleres'
        },
        {
            'title': 'Gestión de Proyectos Educativos TIC',
            'description': 'Planifica, ejecuta y evalúa proyectos de integración tecnológica en instituciones educativas.',
            'link': 'https://www.coursera.org/learn/gestion-proyectos-tic-educacion',
            'group': 'Fortalecimiento Institucional',
            'duration': '8 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Transformación Digital de Centros Educativos',
            'description': 'Guía estrategias de transformación digital integral para instituciones educativas.',
            'link': 'https://www.futurelearn.com/courses/transformacion-digital-educativa',
            'group': 'Fortalecimiento Institucional',
            'duration': '10 semanas',
            'format': 'Talleres'
        },
        {
            'title': 'Desarrollo de Políticas TIC Educativas',
            'description': 'Diseña e implementa políticas institucionales para el uso efectivo de tecnologías educativas.',
            'link': 'https://www.miríadax.net/web/politicas-tic-educativas',
            'group': 'Fortalecimiento Institucional',
            'duration': '7 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Gestión del Cambio en Educación',
            'description': 'Lidera procesos de cambio tecnológico y cultural en instituciones educativas.',
            'link': 'https://www.udemy.com/course/gestion-cambio-educativo',
            'group': 'Fortalecimiento Institucional',
            'duration': '5 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Comunicación Institucional Digital',
            'description': 'Mejora la comunicación interna y externa de tu institución usando herramientas digitales.',
            'link': 'https://www.linkedin.com/learning/comunicacion-institucional-digital',
            'group': 'Fortalecimiento Institucional',
            'duration': '4 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Evaluación de Recursos Tecnológicos',
            'description': 'Evalúa y selecciona recursos tecnológicos apropiados para tu institución educativa.',
            'link': 'https://www.canvas.net/browse/evaluacion-recursos-tecnologicos',
            'group': 'Fortalecimiento Institucional',
            'duration': '6 semanas',
            'format': 'Talleres'
        },
        {
            'title': 'Cultura Digital Institucional',
            'description': 'Promueve una cultura digital positiva y colaborativa en tu centro educativo.',
            'link': 'https://www.kadenze.com/courses/cultura-digital-educativa',
            'group': 'Fortalecimiento Institucional',
            'duration': '5 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Gestión de Recursos Humanos en Era Digital',
            'description': 'Gestiona equipos educativos en el contexto de la transformación digital.',
            'link': 'https://www.pluralsight.com/courses/gestion-rrhh-digital-educacion',
            'group': 'Fortalecimiento Institucional',
            'duration': '6 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Planificación Estratégica con TIC',
            'description': 'Integra las TIC en la planificación estratégica de tu institución educativa.',
            'link': 'https://www.skillshare.com/classes/planificacion-estrategica-tic',
            'group': 'Fortalecimiento Institucional',
            'duration': '8 semanas',
            'format': 'Talleres'
        },
        
        # Innovación Educativa
        {
            'title': 'Metodologías Activas con Tecnología',
            'description': 'Implementa metodologías activas de aprendizaje potenciadas por tecnología digital.',
            'link': 'https://www.edx.org/course/metodologias-activas-tecnologia',
            'group': 'Innovación Educativa',
            'duration': '7 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Gamificación en el Aula Digital',
            'description': 'Diseña experiencias de aprendizaje gamificadas usando herramientas digitales.',
            'link': 'https://www.coursera.org/learn/gamificacion-educativa',
            'group': 'Innovación Educativa',
            'duration': '6 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Realidad Virtual y Aumentada en Educación',
            'description': 'Explora las posibilidades educativas de la realidad virtual y aumentada.',
            'link': 'https://www.futurelearn.com/courses/realidad-virtual-educacion',
            'group': 'Innovación Educativa',
            'duration': '5 semanas',
            'format': 'Talleres'
        },
        {
            'title': 'Inteligencia Artificial para Educadores',
            'description': 'Comprende y aplica herramientas de inteligencia artificial en contextos educativos.',
            'link': 'https://www.miríadax.net/web/ia-para-educadores',
            'group': 'Innovación Educativa',
            'duration': '8 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Aprendizaje Basado en Proyectos Digitales',
            'description': 'Diseña e implementa proyectos de aprendizaje colaborativo usando tecnología.',
            'link': 'https://www.udemy.com/course/abp-digital-educacion',
            'group': 'Innovación Educativa',
            'duration': '6 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Storytelling Digital Educativo',
            'description': 'Crea narrativas digitales interactivas para potenciar el aprendizaje.',
            'link': 'https://www.linkedin.com/learning/storytelling-digital-educativo',
            'group': 'Innovación Educativa',
            'duration': '4 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Maker Education y Fabricación Digital',
            'description': 'Integra la filosofía maker y herramientas de fabricación digital en el currículo.',
            'link': 'https://www.canvas.net/browse/maker-education',
            'group': 'Innovación Educativa',
            'duration': '7 semanas',
            'format': 'Talleres'
        },
        {
            'title': 'Pensamiento Computacional para Todos',
            'description': 'Desarrolla el pensamiento computacional en estudiantes de todas las edades y áreas.',
            'link': 'https://www.kadenze.com/courses/pensamiento-computacional',
            'group': 'Innovación Educativa',
            'duration': '5 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Evaluación Innovadora con TIC',
            'description': 'Diseña sistemas de evaluación innovadores usando herramientas tecnológicas.',
            'link': 'https://www.pluralsight.com/courses/evaluacion-innovadora-tic',
            'group': 'Innovación Educativa',
            'duration': '6 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Espacios de Aprendizaje Flexibles',
            'description': 'Diseña espacios físicos y virtuales flexibles que potencien el aprendizaje innovador.',
            'link': 'https://www.skillshare.com/classes/espacios-aprendizaje-flexibles',
            'group': 'Innovación Educativa',
            'duration': '5 semanas',
            'format': 'Talleres'
        },
        
        # Habilidades Digitales Avanzadas
        {
            'title': 'Programación para Educadores',
            'description': 'Aprende fundamentos de programación para crear recursos educativos y enseñar coding.',
            'link': 'https://www.codecademy.com/learn/programacion-educadores',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '10 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Análisis de Datos Educativos',
            'description': 'Utiliza técnicas de análisis de datos para mejorar los procesos educativos.',
            'link': 'https://www.coursera.org/learn/analisis-datos-educativos',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '8 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Creación de Aplicaciones Educativas',
            'description': 'Desarrolla aplicaciones móviles y web para resolver problemas educativos específicos.',
            'link': 'https://www.udacity.com/course/aplicaciones-educativas',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '12 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Machine Learning en Educación',
            'description': 'Aplica técnicas de aprendizaje automático para personalizar experiencias educativas.',
            'link': 'https://www.edx.org/course/machine-learning-educacion',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '10 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Desarrollo de Contenidos Interactivos',
            'description': 'Crea contenidos educativos interactivos usando tecnologías web avanzadas.',
            'link': 'https://www.futurelearn.com/courses/contenidos-interactivos',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '8 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Administración de Sistemas Educativos',
            'description': 'Gestiona sistemas tecnológicos complejos en instituciones educativas.',
            'link': 'https://www.linux.org/courses/sistemas-educativos',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '9 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Ciberseguridad en Entornos Educativos',
            'description': 'Protege sistemas e información en instituciones educativas contra amenazas digitales.',
            'link': 'https://www.cybrary.it/course/ciberseguridad-educativa',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '7 semanas',
            'format': 'Autoaprendizaje'
        },
        {
            'title': 'Blockchain y Educación',
            'description': 'Explora aplicaciones de blockchain para certificación y gestión educativa.',
            'link': 'https://www.coursera.org/learn/blockchain-educacion',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '6 semanas',
            'format': 'En línea'
        },
        {
            'title': 'Internet de las Cosas (IoT) Educativo',
            'description': 'Implementa soluciones IoT para crear aulas inteligentes y eficientes.',
            'link': 'https://www.udemy.com/course/iot-educativo',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '8 semanas',
            'format': 'Talleres'
        },
        {
            'title': 'Robótica Educativa Avanzada',
            'description': 'Diseña e implementa programas de robótica educativa para diferentes niveles.',
            'link': 'https://www.robotics.org/courses/robotica-educativa-avanzada',
            'group': 'Habilidades Digitales Avanzadas',
            'duration': '10 semanas',
            'format': 'Talleres'
        }
    ]
    
    # Add courses to database
    for course_data in courses_data:
        course = Course(**course_data)
        db.session.add(course)
    
    try:
        db.session.commit()
        print(f"Successfully added {len(courses_data)} courses to the database.")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding courses: {e}")
