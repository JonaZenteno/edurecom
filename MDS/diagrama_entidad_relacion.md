# Diagrama de Entidad-Relación - Sistema EduRecom

```mermaid
erDiagram
    %% Entidad Usuario
    User {
        int id PK "Clave primaria"
        string username UK "Nombre de usuario único"
        string email UK "Email único"
        string password_hash "Hash de contraseña"
        datetime created_at "Fecha de creación"
    }
    
    %% Entidad Perfil de Usuario
    UserProfile {
        int id PK "Clave primaria"
        int user_id FK "Clave foránea a User"
        string role "Rol: profesor, director, asistente"
        string school_type "Tipo de escuela: rural, urbana, etc."
        string dependency "Dependencia: municipal, privada, etc."
        string age_range "Rango de edad: 20-30, 31-40, etc."
        int digital_tools_skill "Habilidad herramientas TI (1-5)"
        int advanced_tic_skill "Habilidad TIC avanzadas (1-5)"
        int digital_citizenship_skill "Ciudadanía digital (1-5)"
        int teaching_tech_skill "Uso de tecnología en enseñanza (1-5)"
        int leadership_support "Apoyo de liderazgo (1-5)"
        int resource_support "Recursos disponibles (1-5)"
        boolean interest_digital_literacy "Interés en alfabetización digital"
        boolean interest_educational_innovation "Interés en innovación educativa"
        boolean interest_leadership "Interés en liderazgo"
        string learning_format "Formato de aprendizaje preferido"
        string assigned_group "Grupo asignado por clustering"
        datetime created_at "Fecha de creación"
        datetime updated_at "Fecha de actualización"
    }
    
    %% Entidad Curso
    Course {
        int id PK "Clave primaria"
        string title "Título del curso"
        text description "Descripción del curso"
        string link "Enlace al curso"
        string group "Grupo al que pertenece"
        string duration "Duración del curso"
        string format "Formato del curso"
        int views_count "Contador de visualizaciones"
        datetime created_at "Fecha de creación"
    }
    
    %% Entidad Visualización de Curso
    CourseView {
        int id PK "Clave primaria"
        int course_id FK "Clave foránea a Course"
        int user_id FK "Clave foránea a User"
        datetime viewed_at "Fecha y hora de visualización"
    }
    
    %% Relaciones
    User ||--|| UserProfile : "tiene un perfil"
    User ||--o{ CourseView : "visualiza cursos"
    Course ||--o{ CourseView : "es visualizado por usuarios"
    UserProfile }o--|| Course : "puede estar asignado a cursos del grupo"
    
    %% Notas explicativas
    %% User -> UserProfile: Relación 1:1 obligatoria
    %% User -> CourseView: Relación 1:N opcional
    %% Course -> CourseView: Relación 1:N opcional
    %% UserProfile -> Course: Relación N:1 opcional (por grupo asignado)
```

## Descripción del Diagrama de Entidad-Relación

### **1. Entidades Principales**

#### **User (Usuario)**
- **Propósito**: Almacena información básica de autenticación de usuarios
- **Clave primaria**: `id` (autoincremental)
- **Claves únicas**: `username`, `email`
- **Atributos**: Información de identificación y autenticación
- **Cardinalidad**: 1 usuario tiene exactamente 1 perfil

#### **UserProfile (Perfil de Usuario)**
- **Propósito**: Almacena información detallada del perfil educativo
- **Clave primaria**: `id` (autoincremental)
- **Clave foránea**: `user_id` → `User.id`
- **Atributos principales**:
  - **Habilidades digitales**: Escala 1-5 para diferentes competencias
  - **Contexto educativo**: Tipo de escuela, dependencia, rol
  - **Intereses**: Booleanos para preferencias de formación
  - **Grupo asignado**: Resultado del algoritmo de clustering
- **Cardinalidad**: 1 perfil pertenece a exactamente 1 usuario

#### **Course (Curso)**
- **Propósito**: Representa los cursos de formación disponibles
- **Clave primaria**: `id` (autoincremental)
- **Atributos principales**:
  - **Contenido**: Título, descripción, enlace
  - **Clasificación**: Grupo, duración, formato
  - **Métricas**: Contador de visualizaciones
- **Cardinalidad**: 1 curso puede ser visualizado por muchos usuarios

#### **CourseView (Visualización de Curso)**
- **Propósito**: Rastrea las interacciones de usuarios con cursos
- **Clave primaria**: `id` (autoincremental)
- **Claves foráneas**: `course_id` → `Course.id`, `user_id` → `User.id`
- **Atributos**: Timestamp de visualización
- **Cardinalidad**: Conecta usuarios y cursos para tracking

### **2. Relaciones entre Entidades**

#### **User ↔ UserProfile (1:1)**
- **Tipo**: Composición obligatoria
- **Descripción**: Cada usuario debe tener exactamente un perfil
- **Restricciones**: No puede existir un usuario sin perfil ni un perfil sin usuario

#### **User ↔ CourseView (1:N)**
- **Tipo**: Agregación opcional
- **Descripción**: Un usuario puede visualizar múltiples cursos
- **Restricciones**: Un usuario puede no haber visualizado ningún curso

#### **Course ↔ CourseView (1:N)**
- **Tipo**: Agregación opcional
- **Descripción**: Un curso puede ser visualizado por múltiples usuarios
- **Restricciones**: Un curso puede no haber sido visualizado por ningún usuario

#### **UserProfile ↔ Course (N:1)**
- **Tipo**: Asociación opcional por grupo
- **Descripción**: Los perfiles pueden estar asignados a cursos según su grupo
- **Restricciones**: La asignación depende del algoritmo de clustering

### **3. Características del Diseño**

#### **Normalización**
- **1NF**: Todos los atributos son atómicos
- **2NF**: No hay dependencias parciales
- **3NF**: No hay dependencias transitivas

#### **Integridad Referencial**
- **Cascade Delete**: Al eliminar un usuario se elimina su perfil
- **Foreign Keys**: Todas las relaciones están correctamente definidas
- **Constraints**: Validaciones a nivel de base de datos

#### **Escalabilidad**
- **Índices**: En claves primarias y foráneas
- **Particionamiento**: Posible por grupos de cursos
- **Cache**: Para consultas frecuentes de recomendaciones

### **4. Ventajas del Diseño**

1. **Separación de Responsabilidades**: Autenticación separada del perfil educativo
2. **Flexibilidad**: Perfiles dinámicos con campos configurables
3. **Tracking**: Seguimiento completo de interacciones de usuarios
4. **Clustering**: Soporte para algoritmos de recomendación
5. **Auditoría**: Timestamps para todas las entidades principales

Este diagrama ERD proporciona una visión clara de la estructura de datos del sistema EduRecom, mostrando cómo se organizan las entidades y sus relaciones para soportar el sistema de recomendación basado en clustering.
