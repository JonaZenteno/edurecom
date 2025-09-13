import json
from __init__ import create_app, db
from models import Course

def load_courses_from_json():
    """Carga los cursos desde un archivo JSON a la base de datos."""
    app = create_app()
    with app.app_context():
        try:
            with open('MDS/cursos.json', 'r', encoding='utf-8') as f:
                courses_data = json.load(f)
            
            for course_info in courses_data:
                # Mapeo flexible de claves JSON a los atributos del modelo Course
                title = course_info.get('titulo', course_info.get('title'))
                description = course_info.get('descripcion', course_info.get('description'))
                link = course_info.get('enlace', course_info.get('link'))
                group = course_info.get('grupo_formacion', course_info.get('group'))
                duration = course_info.get('duration')
                course_format = course_info.get('format')

                # Validar que los campos esenciales no sean nulos
                if not all([title, description, link, group]):
                    print(f"Omitiendo curso por falta de datos esenciales: {course_info}")
                    continue

                # Crear instancia del curso si no existe
                if not Course.query.filter_by(title=title).first():
                    new_course = Course(
                        title=title,
                        description=description,
                        link=link,
                        group=group,
                        duration=duration,
                        format=course_format
                    )
                    db.session.add(new_course)
            
            db.session.commit()
            print("Cursos cargados exitosamente.")

        except Exception as e:
            db.session.rollback()
            print(f"Error al cargar los cursos: {e}")

if __name__ == '__main__':
    load_courses_from_json()
