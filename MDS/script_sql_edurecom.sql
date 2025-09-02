-- =====================================================
-- SCRIPT SQL - BASE DE DATOS SISTEMA EDURECOM
-- Sistema de Recomendación de Formación para Educadores
-- =====================================================

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS edurecom_db;
USE edurecom_db;

-- =====================================================
-- TABLA: User (Usuarios del sistema)
-- =====================================================
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(64) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- TABLA: UserProfile (Perfiles de usuario)
-- =====================================================
CREATE TABLE IF NOT EXISTS user_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    
    -- Información básica del perfil
    role VARCHAR(50) NOT NULL DEFAULT 'profesor',
    school_type VARCHAR(50) NOT NULL DEFAULT 'urbana',
    dependency VARCHAR(50) NOT NULL DEFAULT 'municipal',
    age_range VARCHAR(20) NOT NULL DEFAULT '31-40',
    
    -- Habilidades digitales (escala 1-5)
    digital_tools_skill INTEGER NOT NULL DEFAULT 3,
    advanced_tic_skill INTEGER NOT NULL DEFAULT 3,
    digital_citizenship_skill INTEGER NOT NULL DEFAULT 3,
    teaching_tech_skill INTEGER NOT NULL DEFAULT 3,
    
    -- Apoyo institucional (escala 1-5)
    leadership_support INTEGER NOT NULL DEFAULT 3,
    resource_support INTEGER NOT NULL DEFAULT 3,
    
    -- Intereses (booleanos)
    interest_digital_literacy BOOLEAN DEFAULT FALSE,
    interest_educational_innovation BOOLEAN DEFAULT FALSE,
    interest_leadership BOOLEAN DEFAULT FALSE,
    
    -- Formato de aprendizaje preferido
    learning_format VARCHAR(50) NOT NULL DEFAULT 'en-linea',
    
    -- Grupo asignado por clustering
    assigned_group VARCHAR(100) NULL,
    
    -- Timestamps
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    -- Clave foránea
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    
    -- Índices para optimización
    INDEX idx_user_profile_user_id (user_id),
    INDEX idx_user_profile_assigned_group (assigned_group),
    INDEX idx_user_profile_role (role)
);

-- =====================================================
-- TABLA: Course (Cursos de formación)
-- =====================================================
CREATE TABLE IF NOT EXISTS course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    link VARCHAR(500) NOT NULL,
    group VARCHAR(100) NOT NULL,
    duration VARCHAR(50) NULL,
    format VARCHAR(50) NULL,
    views_count INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    -- Índices para optimización
    INDEX idx_course_group (group),
    INDEX idx_course_views_count (views_count),
    INDEX idx_course_title (title)
);

-- =====================================================
-- TABLA: CourseView (Visualizaciones de cursos)
-- =====================================================
CREATE TABLE IF NOT EXISTS course_view (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    viewed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    -- Claves foráneas
    FOREIGN KEY (course_id) REFERENCES course(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    
    -- Índices para optimización
    INDEX idx_course_view_course_id (course_id),
    INDEX idx_course_view_user_id (user_id),
    INDEX idx_course_view_viewed_at (viewed_at)
);

-- =====================================================
-- INSERCIÓN DE DATOS DE EJEMPLO
-- =====================================================

-- Insertar usuarios de ejemplo
INSERT INTO user (username, email, password_hash) VALUES
('admin', 'admin@edurecom.cl', 'pbkdf2:sha256:600000$hash_admin'),
('profesor1', 'profesor1@escuela.cl', 'pbkdf2:sha256:600000$hash_prof1'),
('director1', 'director1@escuela.cl', 'pbkdf2:sha256:600000$hash_dir1'),
('asistente1', 'asistente1@escuela.cl', 'pbkdf2:sha256:600000$hash_asi1');

-- Insertar perfiles de ejemplo
INSERT INTO user_profile (
    user_id, role, school_type, dependency, age_range,
    digital_tools_skill, advanced_tic_skill, digital_citizenship_skill, teaching_tech_skill,
    leadership_support, resource_support,
    interest_digital_literacy, interest_educational_innovation, interest_leadership,
    learning_format, assigned_group
) VALUES
(1, 'admin', 'urbana', 'municipal', '31-40', 5, 5, 5, 5, 5, 5, TRUE, TRUE, TRUE, 'en-linea', 'Administradores'),
(2, 'profesor', 'urbana', 'municipal', '31-40', 3, 2, 4, 3, 2, 3, TRUE, FALSE, FALSE, 'en-linea', 'Alfabetización Digital Básica'),
(3, 'director', 'urbana', 'municipal', '41-50', 4, 3, 4, 3, 4, 3, FALSE, TRUE, TRUE, 'talleres', 'Fortalecimiento Institucional'),
(4, 'asistente', 'rural', 'municipal', '20-30', 2, 1, 3, 2, 2, 2, TRUE, FALSE, FALSE, 'autoaprendizaje', 'Alfabetización Digital Básica');

-- Insertar cursos de ejemplo
INSERT INTO course (title, description, link, group, duration, format) VALUES
('Introducción a Herramientas Digitales', 'Curso básico para aprender a usar herramientas digitales en el aula', 'https://ejemplo.com/curso1', 'Alfabetización Digital Básica', '20 horas', 'en-linea'),
('TIC Avanzadas para Educadores', 'Curso intermedio sobre tecnologías avanzadas en educación', 'https://ejemplo.com/curso2', 'Habilidades Digitales Avanzadas', '30 horas', 'en-linea'),
('Liderazgo Educativo Digital', 'Desarrollo de habilidades de liderazgo en entornos digitales', 'https://ejemplo.com/curso3', 'Fortalecimiento Institucional', '25 horas', 'talleres'),
('Innovación en el Aula Digital', 'Estrategias innovadoras para integrar tecnología en la enseñanza', 'https://ejemplo.com/curso4', 'Innovación Educativa', '35 horas', 'en-linea'),
('Herramientas Colaborativas', 'Uso de plataformas colaborativas para el trabajo en equipo', 'https://ejemplo.com/curso5', 'Habilidades Digitales Avanzadas', '15 horas', 'en-linea');

-- Insertar visualizaciones de ejemplo
INSERT INTO course_view (course_id, user_id) VALUES
(1, 2), (1, 4), (2, 2), (3, 3), (4, 2), (5, 2);

-- Actualizar contadores de visualizaciones
UPDATE course SET views_count = (
    SELECT COUNT(*) FROM course_view WHERE course_id = course.id
);

-- =====================================================
-- VISTAS ÚTILES PARA ANÁLISIS
-- =====================================================

-- Vista: Resumen de usuarios por grupo
CREATE VIEW v_user_summary_by_group AS
SELECT 
    up.assigned_group,
    COUNT(*) as total_users,
    AVG(up.digital_tools_skill) as avg_digital_tools,
    AVG(up.advanced_tic_skill) as avg_advanced_tic,
    AVG(up.digital_citizenship_skill) as avg_digital_citizenship,
    AVG(up.teaching_tech_skill) as avg_teaching_tech,
    AVG(up.leadership_support) as avg_leadership_support,
    AVG(up.resource_support) as avg_resource_support
FROM user_profile up
WHERE up.assigned_group IS NOT NULL
GROUP BY up.assigned_group;

-- Vista: Cursos más populares
CREATE VIEW v_popular_courses AS
SELECT 
    c.id,
    c.title,
    c.group,
    c.views_count,
    c.duration,
    c.format
FROM course c
ORDER BY c.views_count DESC;

-- Vista: Actividad de usuarios
CREATE VIEW v_user_activity AS
SELECT 
    u.username,
    u.email,
    up.role,
    up.assigned_group,
    COUNT(cv.id) as courses_viewed,
    MAX(cv.viewed_at) as last_activity
FROM user u
LEFT JOIN user_profile up ON u.id = up.user_id
LEFT JOIN course_view cv ON u.id = cv.user_id
GROUP BY u.id, u.username, u.email, up.role, up.assigned_group;

-- =====================================================
-- PROCEDIMIENTOS ALMACENADOS ÚTILES
-- =====================================================

-- Procedimiento: Actualizar contador de visualizaciones
DELIMITER //
CREATE PROCEDURE UpdateCourseViews(IN course_id_param INT)
BEGIN
    UPDATE course 
    SET views_count = (
        SELECT COUNT(*) 
        FROM course_view 
        WHERE course_id = course_id_param
    )
    WHERE id = course_id_param;
END //
DELIMITER ;

-- Procedimiento: Obtener recomendaciones por usuario
DELIMITER //
CREATE PROCEDURE GetUserRecommendations(IN user_id_param INT)
BEGIN
    SELECT 
        c.id,
        c.title,
        c.description,
        c.link,
        c.duration,
        c.format,
        c.views_count
    FROM course c
    INNER JOIN user_profile up ON up.user_id = user_id_param
    WHERE c.group = up.assigned_group
    ORDER BY c.views_count DESC;
END //
DELIMITER ;

-- =====================================================
-- TRIGGERS PARA MANTENER INTEGRIDAD
-- =====================================================

-- Trigger: Actualizar contador de visualizaciones automáticamente
DELIMITER //
CREATE TRIGGER after_course_view_insert
AFTER INSERT ON course_view
FOR EACH ROW
BEGIN
    UPDATE course 
    SET views_count = views_count + 1
    WHERE id = NEW.course_id;
END //
DELIMITER ;

-- Trigger: Actualizar timestamp de perfil
DELIMITER //
CREATE TRIGGER before_user_profile_update
BEFORE UPDATE ON user_profile
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //
DELIMITER ;

-- =====================================================
-- ÍNDICES ADICIONALES PARA OPTIMIZACIÓN
-- =====================================================

-- Índices compuestos para consultas frecuentes
CREATE INDEX idx_user_profile_skills ON user_profile(digital_tools_skill, advanced_tic_skill, digital_citizenship_skill);
CREATE INDEX idx_course_group_views ON course(group, views_count);
CREATE INDEX idx_course_view_user_course ON course_view(user_id, course_id);

-- =====================================================
-- CONSULTAS DE ANÁLISIS ÚTILES
-- =====================================================

-- Consulta: Distribución de usuarios por grupo
-- SELECT assigned_group, COUNT(*) as total FROM user_profile GROUP BY assigned_group;

-- Consulta: Top 5 cursos más vistos
-- SELECT title, group, views_count FROM course ORDER BY views_count DESC LIMIT 5;

-- Consulta: Usuarios más activos
-- SELECT username, COUNT(cv.id) as views FROM user u JOIN course_view cv ON u.id = cv.user_id GROUP BY u.id ORDER BY views DESC LIMIT 10;

-- Consulta: Habilidades promedio por grupo
-- SELECT assigned_group, AVG(digital_tools_skill) as avg_tools FROM user_profile GROUP BY assigned_group;

-- =====================================================
-- FIN DEL SCRIPT
-- =====================================================

