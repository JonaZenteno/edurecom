from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, RadioField, BooleanField, SubmitField, IntegerField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, URL, Optional

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[
        DataRequired(message='El nombre de usuario es obligatorio'),
        Length(min=4, max=20, message='El nombre de usuario debe tener entre 4 y 20 caracteres')
    ])
    email = StringField('Correo electrónico', validators=[
        DataRequired(message='El correo electrónico es obligatorio'),
        Email(message='Ingresa un correo electrónico válido')
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='La contraseña es obligatoria'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    password2 = PasswordField('Confirmar contraseña', validators=[
        DataRequired(message='Confirma tu contraseña'),
        EqualTo('password', message='Las contraseñas deben coincidir')
    ])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[
        DataRequired(message='El nombre de usuario es obligatorio')
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='La contraseña es obligatoria')
    ])
    submit = SubmitField('Iniciar sesión')

class ProfileForm(FlaskForm):
    role = SelectField('¿Cuál es tu rol en el establecimiento educativo?', validators=[DataRequired()], choices=[
        ('', 'Selecciona una opción'),
        ('profesor', 'Profesor/a'),
        ('director', 'Director/a'),
        ('asistente', 'Asistente de la educación')
    ])
    
    school_type = SelectField('¿En qué tipo de establecimiento educativo es?', validators=[DataRequired()], choices=[
        ('', 'Selecciona una opción'),
        ('rural', 'Escuela rural'),
        ('urbana', 'Escuela urbana'),
        ('cientifico-humanista', 'Liceo científico-humanista'),
        ('tecnico-profesional', 'Liceo técnico-profesional')
    ])
    
    dependency = SelectField('¿Cuál es la dependencia del establecimiento?', validators=[DataRequired()], choices=[
        ('', 'Selecciona una opción'),
        ('municipal', 'Municipal'),
        ('privada-subvencionada', 'Particular subvencionada'),
        ('privada-pagada', 'Particular pagada')
    ])
    
    age_range = SelectField('¿En qué rango de edad te encuentras?', validators=[DataRequired()], choices=[
        ('', 'Selecciona una opción'),
        ('20-30', '20-30 años'),
        ('31-40', '31-40 años'),
        ('41-50', '41-50 años'),
        ('51+', '51+ años')
    ])
    
    # Digital skills (1-5 scale)
    digital_tools_skill = SelectField('Herramientas TI básicas (procesadores de texto, hojas de cálculo)', 
        validators=[DataRequired()], choices=[
        ('', 'Selecciona tu nivel'),
        ('1', '1 - Principiante'),
        ('2', '2 - Básico'),
        ('3', '3 - Intermedio'),
        ('4', '4 - Avanzado'),
        ('5', '5 - Experto')
    ])
    
    advanced_tic_skill = SelectField('TIC avanzadas (plataformas educativas, herramientas multimedia)', 
        validators=[DataRequired()], choices=[
        ('', 'Selecciona tu nivel'),
        ('1', '1 - Principiante'),
        ('2', '2 - Básico'),
        ('3', '3 - Intermedio'),
        ('4', '4 - Avanzado'),
        ('5', '5 - Experto')
    ])
    
    digital_citizenship_skill = SelectField('Ciudadanía digital (seguridad online, ética digital)', 
        validators=[DataRequired()], choices=[
        ('', 'Selecciona tu nivel'),
        ('1', '1 - Principiante'),
        ('2', '2 - Básico'),
        ('3', '3 - Intermedio'),
        ('4', '4 - Avanzado'),
        ('5', '5 - Experto')
    ])
    
    teaching_tech_skill = SelectField('Uso de tecnología en la enseñanza', 
        validators=[DataRequired()], choices=[
        ('', 'Selecciona tu nivel'),
        ('1', '1 - Principiante'),
        ('2', '2 - Básico'),
        ('3', '3 - Intermedio'),
        ('4', '4 - Avanzado'),
        ('5', '5 - Experto')
    ])
    
    # Soporte institucional(1-5 escala)
    leadership_support = SelectField('Liderazgo institucional para el uso de TIC', 
        validators=[DataRequired()], choices=[
        ('', 'Selecciona el nivel'),
        ('1', '1 - Muy bajo'),
        ('2', '2 - Bajo'),
        ('3', '3 - Medio'),
        ('4', '4 - Alto'),
        ('5', '5 - Muy alto')
    ])
    
    resource_support = SelectField('Recursos tecnológicos disponibles en tu establecimiento', 
        validators=[DataRequired()], choices=[
        ('', 'Selecciona el nivel'),
        ('1', '1 - Muy escasos'),
        ('2', '2 - Escasos'),
        ('3', '3 - Suficientes'),
        ('4', '4 - Buenos'),
        ('5', '5 - Excelentes')
    ])
    
    # Intereses
    interest_digital_literacy = BooleanField('Alfabetización digital')
    interest_educational_innovation = BooleanField('Innovación educativa')
    interest_leadership = BooleanField('Liderazgo educativo')
    
    learning_format = SelectField('¿Cuál es tu formato de aprendizaje preferido?', 
        validators=[DataRequired()], choices=[
        ('', 'Selecciona una opción'),
        ('en-linea', 'En línea'),
        ('talleres', 'Talleres presenciales'),
        ('autoaprendizaje', 'Autoaprendizaje')
    ])
    
    submit = SubmitField('Obtener recomendaciones')

class AdminConfigForm(FlaskForm):
    n_clusters = IntegerField('Número de clusters (K-Means)', validators=[DataRequired()])
    confidence_threshold = FloatField('Umbral de confianza para asignación automática (0-1)', validators=[DataRequired()])
    submit = SubmitField('Guardar configuración')

class CourseForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    link = StringField('Enlace', validators=[DataRequired(), URL(message='Debe ser una URL válida')])
    group = SelectField('Grupo de Formación', validators=[DataRequired()], choices=[
        ('', 'Selecciona un grupo'),
        ('Alfabetización Digital Básica', 'Alfabetización Digital Básica - Habilidades digitales fundamentales'),
        ('Habilidades Digitales Avanzadas', 'Habilidades Digitales Avanzadas - TIC avanzadas para educadores'),
        ('Fortalecimiento Institucional', 'Fortalecimiento Institucional - Liderazgo y gestión educativa'),
        ('Innovación Educativa', 'Innovación Educativa - Estrategias innovadoras en educación'),
        ('Ciudadanía Digital', 'Ciudadanía Digital - Ética y seguridad digital'),
        ('Recursos Digitales', 'Recursos Digitales - Herramientas y plataformas educativas')
    ])
    duration = StringField('Duración', validators=[Optional(), Length(max=50)], 
                          render_kw={'placeholder': 'Ej: 20 horas, 3 semanas, 1 mes'})
    format = SelectField('Formato', validators=[Optional()], choices=[
        ('', 'Selecciona un formato'),
        ('en-linea', 'En línea - Curso virtual'),
        ('talleres', 'Talleres presenciales - Sesiones presenciales'),
        ('autoaprendizaje', 'Autoaprendizaje - Materiales para estudio independiente'),
        ('hibrido', 'Híbrido - Combinación presencial y virtual'),
        ('webinar', 'Webinar - Sesiones en vivo online'),
        ('microlearning', 'Microlearning - Contenido en pequeñas dosis')
    ])
    submit = SubmitField('Guardar curso')