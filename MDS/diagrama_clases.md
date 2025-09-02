# Diagrama de Clases - Sistema EduRecom

```mermaid
classDiagram
    %% Clases principales del sistema
    class User {
        +Integer id
        +String username
        +String email
        +String password_hash
        +DateTime created_at
        +UserProfile profile
        +List~CourseView~ course_views
        +is_authenticated()
        +get_id()
    }
    
    class UserProfile {
        +Integer id
        +Integer user_id
        +String role
        +String school_type
        +String dependency
        +String age_range
        +Integer digital_tools_skill
        +Integer advanced_tic_skill
        +Integer digital_citizenship_skill
        +Integer teaching_tech_skill
        +Integer leadership_support
        +Integer resource_support
        +Boolean interest_digital_literacy
        +Boolean interest_educational_innovation
        +Boolean interest_leadership
        +String learning_format
        +String assigned_group
        +DateTime created_at
        +DateTime updated_at
        +User user
        +assign_group()
        +update_profile()
    }
    
    class Course {
        +Integer id
        +String title
        +String description
        +String link
        +String group
        +String duration
        +String format
        +Integer views_count
        +DateTime created_at
        +List~CourseView~ views
        +increment_views()
        +get_view_count()
    }
    
    class CourseView {
        +Integer id
        +Integer course_id
        +Integer user_id
        +DateTime viewed_at
        +Course course
        +User user
        +track_view()
    }
    
    %% Clases del sistema de clustering
    class AutoAssignment {
        +String model_path
        +Object clustering_model
        +Object scaler
        +Object feature_engineer
        +Object cluster_mapping
        +Boolean is_trained
        +train_model()
        +save_model()
        +load_model()
        +assign_group()
        +get_assignment_confidence()
        +prepare_user_profile()
    }
    
    class FeatureEngineer {
        +List~String~ feature_names
        +engineer_features()
        +preprocess_features()
        +normalize_features()
    }
    
    class ClusteringEngine {
        +Object kmeans
        +Object scaler
        +Object feature_engineer
        +Object cluster_mapping
        +train_model()
        +predict_cluster()
        +evaluate_model()
        +save_model()
        +load_model()
    }
    
    %% Clases de utilidades
    class Utils {
        +assign_group()
        +_manual_assign_group()
        +validate_profile()
        +calculate_skills_average()
    }
    
    %% Clases de formularios
    class RegistrationForm {
        +String username
        +String email
        +String password
        +String confirm_password
        +SubmitField submit
        +validate_username()
        +validate_email()
    }
    
    class LoginForm {
        +String username
        +String password
        +Boolean remember_me
        +SubmitField submit
        +validate_credentials()
    }
    
    class ProfileForm {
        +String role
        +String school_type
        +String dependency
        +String age_range
        +Integer digital_tools_skill
        +Integer advanced_tic_skill
        +Integer digital_citizenship_skill
        +Integer teaching_tech_skill
        +Integer leadership_support
        +Integer resource_support
        +Boolean interest_digital_literacy
        +Boolean interest_educational_innovation
        +Boolean interest_leadership
        +String learning_format
        +SubmitField submit
        +validate_profile()
    }
    
    class AdminConfigForm {
        +Integer n_clusters
        +Float confidence_threshold
        +SubmitField submit
        +validate_config()
    }
    
    %% Clases del sistema Flask
    class FlaskApp {
        +String secret_key
        +Object config
        +Object db
        +Object login_manager
        +create_app()
        +configure_database()
        +setup_extensions()
        +register_routes()
    }
    
    class Database {
        +String uri
        +Object engine
        +Object session
        +create_all()
        +drop_all()
        +commit()
        +rollback()
    }
    
    class LoginManager {
        +String login_view
        +String login_message
        +String login_message_category
        +load_user()
        +init_app()
    }
    
    %% Relaciones entre clases
    User ||--|| UserProfile : has
    User ||--o{ CourseView : creates
    Course ||--o{ CourseView : receives
    UserProfile ||--o{ Course : assigned_to
    
    AutoAssignment ||--|| ClusteringEngine : uses
    AutoAssignment ||--|| FeatureEngineer : uses
    ClusteringEngine ||--|| FeatureEngineer : uses
    
    Utils ||--|| AutoAssignment : uses
    Utils ||--|| UserProfile : processes
    
    FlaskApp ||--|| Database : manages
    FlaskApp ||--|| LoginManager : manages
    FlaskApp ||--|| User : authenticates
    
    %% Herencia y mixins
    User ..|> UserMixin : inherits
    UserProfile ..|> db.Model : inherits
    Course ..|> db.Model : inherits
    CourseView ..|> db.Model : inherits
    
    %% Agrupación por paquetes
    classDef modelClass fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef clusteringClass fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef formClass fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef systemClass fill:#e8f5e8,stroke:#388e3c,stroke-width:2px
    
    class User,UserProfile,Course,CourseView modelClass
    class AutoAssignment,FeatureEngineer,ClusteringEngine clusteringClass
    class RegistrationForm,LoginForm,ProfileForm,AdminConfigForm formClass
    class FlaskApp,Database,LoginManager,Utils systemClass
```

## Descripción del Diagrama de Clases

### **1. Clases de Modelo de Datos (Model Classes)**

#### **User**
- **Propósito**: Representa a los usuarios del sistema
- **Atributos principales**: `id`, `username`, `email`, `password_hash`
- **Relaciones**: Tiene un perfil (`UserProfile`) y múltiples visualizaciones de cursos (`CourseView`)
- **Herencia**: Extiende de `UserMixin` para funcionalidades de Flask-Login

#### **UserProfile**
- **Propósito**: Almacena información detallada del perfil del usuario
- **Atributos principales**: Habilidades digitales, contexto educativo, intereses
- **Operaciones**: `assign_group()`, `update_profile()`
- **Relaciones**: Pertenece a un `User` y puede estar asignado a múltiples `Course`

#### **Course**
- **Propósito**: Representa los cursos de formación disponibles
- **Atributos principales**: `title`, `description`, `link`, `group`, `views_count`
- **Operaciones**: `increment_views()`, `get_view_count()`
- **Relaciones**: Recibe múltiples `CourseView` y pertenece a un grupo específico

#### **CourseView**
- **Propósito**: Rastrea las visualizaciones de cursos por usuarios
- **Atributos principales**: `course_id`, `user_id`, `viewed_at`
- **Relaciones**: Conecta `User` y `Course` para tracking

### **2. Clases del Sistema de Clustering**

#### **AutoAssignment**
- **Propósito**: Coordina la asignación automática de grupos usando clustering
- **Atributos principales**: Modelo de clustering, escalador, ingeniero de características
- **Operaciones**: `train_model()`, `assign_group()`, `get_assignment_confidence()`
- **Relaciones**: Usa `ClusteringEngine` y `FeatureEngineer`

#### **FeatureEngineer**
- **Propósito**: Preprocesa y normaliza las características del perfil
- **Atributos principales**: Lista de nombres de características
- **Operaciones**: `engineer_features()`, `preprocess_features()`, `normalize_features()`

#### **ClusteringEngine**
- **Propósito**: Implementa el algoritmo de clustering K-means
- **Atributos principales**: Modelo K-means, escalador, mapeo de clusters
- **Operaciones**: `train_model()`, `predict_cluster()`, `evaluate_model()`

### **3. Clases de Formularios**

#### **RegistrationForm, LoginForm, ProfileForm, AdminConfigForm**
- **Propósito**: Manejan la entrada de datos del usuario
- **Herencia**: Extienden de `FlaskForm`
- **Validación**: Incluyen métodos de validación específicos para cada campo

### **4. Clases del Sistema Flask**

#### **FlaskApp**
- **Propósito**: Aplicación principal de Flask
- **Responsabilidades**: Configuración, inicialización de extensiones, registro de rutas

#### **Database**
- **Propósito**: Maneja la conexión y operaciones de base de datos
- **Operaciones**: `create_all()`, `commit()`, `rollback()`

#### **LoginManager**
- **Propósito**: Gestiona la autenticación de usuarios
- **Funcionalidades**: Carga de usuarios, configuración de login

### **5. Relaciones Principales**

- **Composición (||--||)**: `User` tiene exactamente un `UserProfile`
- **Agregación (||--o{)**: `User` puede crear múltiples `CourseView`
- **Asociación (||--||)**: `AutoAssignment` usa `ClusteringEngine` y `FeatureEngineer`
- **Herencia (..|>)**: Las clases de modelo extienden de `db.Model`

### **6. Patrones de Diseño Identificados**

1. **Model-View-Controller (MVC)**: Separación clara entre modelos, vistas y controladores
2. **Repository Pattern**: Las clases de modelo encapsulan el acceso a datos
3. **Strategy Pattern**: Diferentes estrategias de asignación de grupos
4. **Factory Pattern**: Creación dinámica de formularios basada en configuración
5. **Observer Pattern**: Tracking de visualizaciones de cursos

Este diagrama de clases proporciona una visión completa de la arquitectura del sistema EduRecom, mostrando cómo las diferentes entidades se relacionan entre sí y cómo se organizan las responsabilidades en cada clase.
