# Diagrama de Casos de Uso - Sistema EduRecom

```mermaid
graph TB
    %% Definición de actores
    Usuario[👤 Usuario]
    Admin[👨‍💼 Administrador]
    Sistema[🤖 Sistema]
    
    %% Casos de uso principales
    UC1[📝 Registro de Usuario]
    UC2[🔐 Inicio de Sesión]
    UC3[👤 Completar Perfil]
    UC4[📚 Generar Recomendaciones]
    UC5[👁️ Visualizar Curso]
    UC6[👥 Gestión de Usuarios]
    UC7[⚙️ Configuración del Sistema]
    UC8[❓ Gestión de Preguntas]
    UC9[📊 Dashboard Administrativo]
    UC10[🎯 Asignación Automática de Grupos]
    
    %% Casos de uso incluidos
    UC11[✅ Validar Credenciales]
    UC12[🔍 Verificar Usuario Existente]
    UC13[📊 Procesar Perfil]
    UC14[🎯 Aplicar Modelo Clustering]
    UC15[📈 Calcular Métricas]
    UC16[💾 Guardar Configuración]
    
    %% Casos de uso extendidos
    UC17[❌ Manejo de Errores]
    UC18[🔒 Verificación de Permisos]
    UC19[📝 Log de Actividades]
    
    %% Relaciones de actores con casos de uso
    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
    Usuario --> UC4
    Usuario --> UC5
    
    Admin --> UC6
    Admin --> UC7
    Admin --> UC8
    Admin --> UC9
    
    Sistema --> UC10
    
    %% Relaciones include (<<include>>)
    UC2 -.->|<<include>> UC11
    UC1 -.->|<<include>> UC12
    UC3 -.->|<<include>> UC13
    UC10 -.->|<<include>> UC14
    UC9 -.->|<<include>> UC15
    UC7 -.->|<<include>> UC16
    
    %% Relaciones extend (<<extend>>)
    UC1 -.->|<<extend>> UC17
    UC2 -.->|<<extend>> UC17
    UC3 -.->|<<extend>> UC17
    UC4 -.->|<<extend>> UC17
    UC5 -.->|<<extend>> UC17
    
    UC6 -.->|<<extend>> UC18
    UC7 -.->|<<extend>> UC18
    UC8 -.->|<<extend>> UC18
    UC9 -.->|<<extend>> UC18
    
    UC10 -.->|<<extend>> UC19
    
    %% Agrupación de casos de uso por paquete
    subgraph "Gestión de Usuarios"
        UC1
        UC2
        UC3
        UC6
    end
    
    subgraph "Sistema de Recomendaciones"
        UC4
        UC5
        UC10
    end
    
    subgraph "Administración del Sistema"
        UC7
        UC8
        UC9
    end
    
    subgraph "Funcionalidades del Sistema"
        UC11
        UC12
        UC13
        UC14
        UC15
        UC16
        UC17
        UC18
        UC19
    end
    
    %% Estilos
    classDef actor fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef useCase fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef includeCase fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef extendCase fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    
    class Usuario,Admin,Sistema actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10 useCase
    class UC11,UC12,UC13,UC14,UC15,UC16 includeCase
    class UC17,UC18,UC19 extendCase
```

## Descripción de las Relaciones

### Relaciones <<include>>
- **UC2 <<include>> UC11**: El inicio de sesión incluye la validación de credenciales
- **UC1 <<include>> UC12**: El registro incluye la verificación de usuario existente
- **UC3 <<include>> UC13**: Completar perfil incluye el procesamiento del perfil
- **UC10 <<include>> UC14**: La asignación automática incluye aplicar el modelo de clustering
- **UC9 <<include>> UC15**: El dashboard incluye el cálculo de métricas
- **UC7 <<include>> UC16**: La configuración incluye guardar la configuración

### Relaciones <<extend>>
- **UC1, UC2, UC3, UC4, UC5 <<extend>> UC17**: Todos los casos de uso principales pueden extenderse con manejo de errores
- **UC6, UC7, UC8, UC9 <<extend>> UC18**: Los casos de administración pueden extenderse con verificación de permisos
- **UC10 <<extend>> UC19**: La asignación automática puede extenderse con logging de actividades

### Paquetes de Casos de Uso
1. **Gestión de Usuarios**: Funcionalidades básicas de autenticación y perfiles
2. **Sistema de Recomendaciones**: Core del sistema de recomendación y clustering
3. **Administración del Sistema**: Funcionalidades exclusivas para administradores
4. **Funcionalidades del Sistema**: Casos de uso de soporte y utilidades
