# Evidencia 2: Análisis y Diseño del Sistema "EduRecom"

## 3. Factibilidad del Proyecto

### 3.1. Factibilidad Técnica

#### Descripción General
El proyecto consiste en el desarrollo de una aplicación web denominada "EduRecom", cuyo objetivo es proporcionar recomendaciones de formación a educadores. Técnicamente, el sistema se fundamenta en tecnologías de código abierto, robustas y ampliamente utilizadas en la industria del software. La arquitectura se compone de:

*   **Backend:** Una aplicación web desarrollada en **Python** utilizando el micro-framework **Flask**. Se encarga de la lógica de negocio, la gestión de usuarios, el procesamiento de datos y la comunicación con la base de datos.
*   **Base de Datos:** Se utiliza **SQLAlchemy** como ORM (Object-Relational Mapper), lo que permite interactuar con bases de datos SQL de manera flexible. La presencia de `psycopg2-binary` indica compatibilidad y preparación para un motor como PostgreSQL en producción.
*   **Machine Learning:** El núcleo del sistema de recomendación se basa en técnicas de clustering, implementadas con la librería **Scikit-learn**. Se utilizan **Pandas** y **NumPy** para la manipulación y el procesamiento de los datos que alimentan los modelos.
*   **Frontend:** Plantillas HTML renderizadas por el servidor a través de Flask, permitiendo la interacción del usuario con el sistema.

Se cuenta con el conocimiento y las habilidades necesarias, como lo demuestra el código fuente ya desarrollado. Las herramientas y equipos son estándar para el desarrollo de software moderno.

#### Respuestas a Preguntas Clave

*   **¿Es práctica la tecnología o solución propuesta, considerando su madurez?**
    Sí. Las tecnologías seleccionadas (Python, Flask, Scikit-learn, Pandas, SQLAlchemy) son líderes en sus respectivos dominios. Son soluciones maduras, estables, con una vasta cantidad de documentación, tutoriales y comunidades de soporte activas. Esto minimiza los riesgos asociados a la implementación y asegura la sostenibilidad del proyecto a largo plazo.

*   **¿Se cuenta actualmente con la tecnología necesaria o se puede adquirir?**
    Sí. Toda la tecnología de software requerida es de **código abierto (Open Source)** y está disponible de forma gratuita. Las librerías se gestionan a través de `pip` y se especifican en el archivo `pyproject.toml`, lo que facilita su instalación y la replicación del entorno de desarrollo en cualquier máquina, sin costos de licenciamiento.

*   **¿Se tiene la experiencia técnica requerida para aplicar la tecnología correctamente?**
    Sí. La estructura del proyecto y el código existente demuestran que se posee la experiencia técnica fundamental en desarrollo web con Flask, gestión de bases de datos con SQLAlchemy y la aplicación de modelos de machine learning con Scikit-learn. Estas habilidades son comunes en el mercado de TI, lo que facilita encontrar personal para el mantenimiento o futuro desarrollo del sistema.

#### Configuración de Recursos Técnicos

A continuación, se detalla la configuración mínima y óptima para la implementación y operación del proyecto.

**Configuración Mínima (Para Desarrollo y Pruebas a Pequeña Escala)**

*   **Hardware:**
    *   **CPU:** 2 núcleos
    *   **RAM:** 4 GB
    *   **Almacenamiento:** 10 GB de espacio en disco
    *   **Descripción:** Un computador personal estándar o una máquina virtual de nivel básico es suficiente.
*   **Software:**
    *   **Sistema Operativo:** Windows, macOS o Linux.
    *   **Entorno de Ejecución:** Python 3.11 o superior.
    *   **Base de Datos:** SQLite (integrada en Python, ideal para desarrollo por su simplicidad).
    *   **Servidor de Aplicaciones:** Servidor de desarrollo de Werkzeug (incluido con Flask).

**Configuración Óptima (Para Producción y Operación Real)**

*   **Hardware:**
    *   **CPU:** 4+ núcleos
    *   **RAM:** 8 GB o más (dependiendo del número de usuarios concurrentes y la complejidad de los cálculos del modelo).
    *   **Almacenamiento:** 50 GB+ de almacenamiento SSD (para un acceso más rápido a la base de datos y los archivos).
    *   **Descripción:** Un Servidor Privado Virtual (VPS) o una instancia en un proveedor de nube (como AWS, Google Cloud o Azure).
*   **Software:**
    *   **Sistema Operativo:** Linux (Debian, Ubuntu, etc.) por su estabilidad y rendimiento para servidores.
    *   **Base de Datos:** PostgreSQL o MySQL, para mayor escalabilidad, concurrencia y robustez.
    *   **Servidor de Aplicaciones WSGI:** Gunicorn (ya incluido en las dependencias) o uWSGI, para gestionar múltiples procesos de la aplicación de forma eficiente.
    *   **Servidor Web (Proxy Inverso):** Nginx o Apache, para gestionar las peticiones HTTP, servir archivos estáticos y mejorar la seguridad.
    *   **Adicional:** Sistema de copias de seguridad automáticas para la base de datos y monitoreo del rendimiento del servidor.

### 3.2. Factibilidad Económica

**Nota Importante:** Los valores presentados a continuación son **ejemplos ilustrativos** para demostrar la metodología. Un análisis real requeriría una investigación de mercado detallada para estimar costos e ingresos con mayor precisión. Las cifras se expresan en unidades monetarias (u.m.).

---

#### Análisis de Costo-Beneficio

Primero, se detallan los costos de inversión y operativos, y se proyectan los posibles beneficios.

**Tabla 1: Costos de Inversión (Año 0)**
| Concepto | Valor (u.m.) |
| :--- | :--- |
| Desarrollo de Software (horas de ingeniería) | $5,000,000 |
| Configuración Inicial de Servidores y BD | $700,000 |
| Gastos Legales y Administrativos | $500,000 |
| **Total Inversión Inicial (I₀)** | **$6,200,000** |

**Tabla 2: Costos Operativos Anuales Proyectados**
| Concepto | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Costo de Servidor/Hosting | $1,200,000 | $1,250,000 | $1,300,000 | $1,350,000 | $1,400,000 |
| Mantenimiento y Soporte | $500,000 | $550,000 | $600,000 | $650,000 | $700,000 |
| Marketing y Ventas | $100,000 | $100,000 | $150,000 | $200,000 | $250,000 |
| Dominio y Licencias | $50,000 | $50,000 | $50,000 | $50,000 | $50,000 |
| **Total Costos Operativos** | **$1,850,000** | **$1,950,000** | **$2,100,000** | **$2,250,000** | **$2,400,000**|

**Tabla 3: Proyección de Beneficios (Ingresos Anuales)**
| Concepto | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Ingresos por Suscripciones | $2,000,000 | $4,000,000 | $6,250,000 | $8,800,000 | $11,550,000|
| **Total Ingresos** | **$2,000,000** | **$4,000,000** | **$6,250,000** | **$8,800,000** | **$11,550,000**|

---

#### Indicadores Financieros

Se asume una **tasa de descuento (r) del 12%** para este proyecto tecnológico.

##### 1. Flujo de Caja (FC)
El Flujo de Caja detalla las entradas y salidas de dinero en un período determinado. Es la base para calcular el VAN y la TIR, y permite determinar las necesidades de efectivo del proyecto. Se calcula restando los egresos (costos) de los ingresos en cada período.

**Tabla 4: Flujo de Caja Neto Proyectado**
| Concepto | Año 0 | Año 1 | Año 2 | Año 3 | Año 4 | Año 5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Total Ingresos | $0 | $2,000,000 | $4,000,000 | $6,250,000 | $8,800,000 | $11,550,000|
| Total Costos Operativos | $0 | ($1,850,000)| ($1,950,000)| ($2,100,000)| ($2,250,000)| ($2,400,000)|
| Inversión Inicial | ($6,200,000)| $0 | $0 | $0 | $0 | $0 |
| **Flujo de Caja Neto (FC)**| **($6,200,000)**| **$150,000** | **$2,050,000**| **$4,150,000**| **$6,550,000**| **$9,150,000**|

##### 2. Valor Actual Neto (VAN)
El VAN mide el beneficio económico del proyecto, trayendo todos los flujos de caja futuros al presente y restando la inversión inicial. Un VAN positivo indica que el proyecto genera valor.

*   **Fórmula:**
    > VAN = -I₀ + Σ [ FCt / (1 + r)ᵗ ]
    > Donde:
    > *   **I₀**: Inversión Inicial
    > *   **FCt**: Flujo de Caja en el período *t*
    > *   **r**: Tasa de descuento
    > *   **t**: Período de tiempo

*   **Cálculo:**
    VAN = -6,200,000 + [150,000 / (1.12)¹] + [2,050,000 / (1.12)²] + [4,150,000 / (1.12)³] + [6,550,000 / (1.12)⁴] + [9,150,000 / (1.12)⁵]
    VAN = -6,200,000 + 133,929 + 1,634,439 + 2,954,158 + 4,162,881 + 5,192,441
    **VAN = $8,077,848**

*   **Conclusión:** Dado que el VAN es significativamente positivo, el proyecto es económicamente atractivo y factible.

##### 3. Tasa Interna de Retorno (TIR)
La TIR es la tasa de descuento que hace que el VAN sea igual a cero. Representa la rentabilidad intrínseca del proyecto.

*   **Criterio de Decisión:**
    *   Si **TIR > r**: El proyecto es rentable y se acepta.
    *   Si **TIR < r**: El proyecto no es rentable y se rechaza.
    *   Si **TIR = r**: El proyecto es indiferente.

*   **Cálculo:**
    La TIR se calcula mediante iteración (generalmente con software). Para los flujos de caja de este proyecto, la **TIR es aproximadamente 55.2%**.

*   **Conclusión:** Puesto que **TIR (55.2%) > r (12%)**, se confirma la viabilidad del proyecto. La rentabilidad generada es muy superior al costo de oportunidad del capital.

##### 4. Periodo de Recuperación (PR)
Indica el tiempo necesario para que los flujos de caja acumulados igualen la inversión inicial.

*   **Fórmula:**
    > PR = A + (B / C)
    > Donde:
    > *   **A**: Año inmediatamente anterior a la recuperación.
    > *   **B**: Inversión que falta por recuperar al inicio del año A+1.
    > *   **C**: Flujo de caja generado durante el año A+1.

*   **Cálculo:**
    **Tabla 5: Flujo de Caja Acumulado**
    | Año | Flujo de Caja Neto | Flujo de Caja Acumulado |
    | :-- | :--- | :--- |
    | 0 | ($6,200,000) | ($6,200,000) |
    | 1 | $150,000 | ($6,050,000) |
    | 2 | $2,050,000 | ($4,000,000) |
    | 3 | $4,150,000 | $150,000 |

    La recuperación ocurre durante el Año 3.
    *   A = 2 años
    *   B = 4,000,000 (el monto que faltaba al final del año 2)
    *   C = 4,150,000 (el flujo generado en el año 3)

    PR = 2 + (4,000,000 / 4,150,000) = 2 + 0.96
    **PR ≈ 2.96 años**

*   **Conclusión:** La inversión inicial se recuperará en aproximadamente 2 años y 11.5 meses.

### 3.3. Factibilidad Operacional

Este análisis evalúa si el proyecto puede ser implementado y mantenido de manera efectiva dentro de la organización, considerando los recursos humanos, los procesos y la aceptación por parte de los usuarios.

#### Recursos y Procesos

El proyecto "EduRecom" requiere de roles y procesos específicos para su correcta operación y mantenimiento a lo largo del tiempo.

**Tabla 6: Recursos Humanos Requeridos para la Operación**
| Rol | Responsabilidades Clave | Disponibilidad / Capacitación |
| :--- | :--- | :--- |
| **Administrador del Sistema** | - Monitorear el rendimiento del servidor y la base de datos.<br>- Realizar copias de seguridad.<br>- Gestionar la seguridad y aplicar parches. | Se requiere personal con conocimientos en administración de sistemas Linux, servidores web (Nginx) y bases de datos (PostgreSQL). Puede ser un rol a tiempo parcial o un servicio contratado. |
| **Desarrollador/Mantenedor** | - Corregir bugs y errores.<br>- Desarrollar nuevas funcionalidades.<br>- Actualizar las librerías y dependencias.<br>- Mejorar y reentrenar los modelos de ML. | El equipo inicial posee las capacidades. A futuro, se pueden contratar desarrolladores con experiencia en Python/Flask y Scikit-learn, perfiles comunes en el mercado. |
| **Soporte al Usuario** | - Atender consultas y problemas de los usuarios.<br>- Recopilar feedback para futuras mejoras.<br>- Gestionar las cuentas de usuario. | Puede ser asumido inicialmente por el equipo de desarrollo. A medida que la base de usuarios crezca, se podría requerir una persona dedicada. |

#### Aceptación e Integración

*   **Urgencia y Procesos:** El proyecto se centra en el proceso clave de **desarrollo profesional docente**. Automatiza y personaliza la recomendación de cursos y formaciones, un proceso que actualmente puede ser manual, genérico o ineficiente. La urgencia de su implementación radica en la necesidad de ofrecer a los educadores herramientas ágiles y pertinentes que apoyen su formación continua, mejorando la calidad educativa.

*   **Aceptación del Personal Interno:** El personal técnico (desarrolladores, administradores) encontrará una alta aceptación, ya que el sistema utiliza tecnologías modernas, bien documentadas y estándar en la industria, lo que facilita su mantenimiento y escalabilidad.

*   **Aceptación de Usuarios Finales:** Se determina que los usuarios finales (educadores) estarán dispuestos a emplear el servicio por las siguientes razones:
    *   **Propuesta de Valor Clara:** Ahorra tiempo en la búsqueda de formación relevante.
    *   **Personalización:** Ofrece recomendaciones ajustadas a sus perfiles y necesidades, a diferencia de los catálogos de cursos genéricos.
    *   **Facilidad de Uso:** La interfaz web (como se ve en los archivos de `templates`) está diseñada para ser intuitiva (registro, login, perfil, recomendaciones).

La existencia de un formulario de perfil (`profile_form.html`) y un sistema de registro (`register.html`) indica que el sistema está diseñado desde su núcleo para ser interactivo y centrado en el usuario, lo que aumenta la probabilidad de una buena adopción.

---

### 3.4. Factibilidad Legal

Este análisis confirma que el proyecto cumple con el marco normativo y las obligaciones contractuales pertinentes.

#### Cumplimiento Normativo y Legal

*   **Leyes de Protección de Datos:** El proyecto manejará datos personales de los educadores (nombre, correo, perfiles profesionales, etc.). Por lo tanto, es **mandatorio** cumplir con la legislación de protección de datos vigente en Chile (Ley N° 19.628 sobre Protección de la Vida Privada). Esto implica:
    *   **Consentimiento Informado:** Los usuarios deben aceptar explícitamente los términos de servicio y la política de privacidad antes de registrarse.
    *   **Finalidad del Dato:** Los datos solo pueden ser usados para los fines informados (la recomendación de cursos).
    *   **Derechos ARCO:** Se debe garantizar a los usuarios el derecho de Acceso, Rectificación, Cancelación y Oposición sobre sus datos.
    *   **Seguridad:** Se deben implementar medidas técnicas para proteger la integridad y confidencialidad de los datos.

*   **Propiedad Intelectual:** El nombre "EduRecom" y el logo deberían ser registrados como marca comercial para proteger la identidad del proyecto.

#### Obligaciones Contractuales y de Licencia

*   **Propiedad del Código Fuente:** El código fuente desarrollado específicamente para el proyecto es propiedad de sus creadores o de la entidad que lo financió. Esto debe quedar claramente establecido.

*   **Licenciamiento de Software de Terceros:** El proyecto se basa en software de código abierto. Es fundamental adherirse a los términos de sus licencias.

**Tabla 7: Análisis de Licencias de Dependencias Clave**
| Software / Librería | Licencia Común | Implicaciones y Obligaciones |
| :--- | :--- | :--- |
| Python | Python Software Foundation License | Permisiva, permite uso comercial sin restricciones. |
| Flask, Werkzeug | BSD 3-Clause | Permisiva, requiere mantener el aviso de copyright original. |
| Scikit-learn, Pandas, NumPy | BSD 3-Clause | Permisivas, compatibles con el desarrollo de un producto comercial. |
| SQLAlchemy, WTForms | MIT License | Muy permisiva, requiere mantener el aviso de copyright y licencia. |
| **Conclusión General** | | Las licencias de las tecnologías utilizadas son de tipo **permisivo**, lo que **confirma la viabilidad legal** para desarrollar un producto comercial derivado. No obligan a que el código fuente propio del proyecto sea abierto (a diferencia de licencias como la GPL). |

*   **Acuerdos de Confidencialidad (NDA):** Si se trabaja con instituciones o socios externos, se deben firmar acuerdos de confidencialidad para proteger la información estratégica y los datos compartidos.

## 4. Diseño de Diagramas del Sistema

### 4.1. Diagrama de Casos de Uso con Escenarios

Este diagrama describe las funcionalidades principales del sistema "EduRecom" y la interacción de los usuarios (actores) con dichas funcionalidades.

#### Actores Identificados

1.  **Educador (Actor Principal):** Es el usuario primario del sistema. Busca registrarse, gestionar su perfil y recibir recomendaciones de formación personalizadas.
2.  **Administrador (Actor de Soporte):** Es el usuario responsable de mantener el sistema. Gestiona las cuentas de usuario, las preguntas de los perfiles y la configuración general de la plataforma.

#### Diagrama de Casos de Uso (Mermaid)

```mermaid
usecaseDiagram
    title Sistema de Recomendación "EduRecom"

    actor Educador
    actor Administrador

    rectangle EduRecom {
        usecase "Registrarse en el Sistema" as UC1
        usecase "Iniciar Sesión" as UC2
        usecase "Gestionar Perfil Profesional" as UC3
        usecase "Recibir Recomendaciones" as UC4
        usecase "Recuperar Contraseña" as UC5

        usecase "Gestionar Usuarios" as UC6
        usecase "Gestionar Preguntas del Perfil" as UC7
        usecase "Administrar Configuración" as UC8
    }

    ' Casos de Uso del Educador
    Educador -- UC1
    Educador -- UC2
    Educador -- UC3
    Educador -- UC4

    ' Casos de Uso del Administrador
    Administrador -- UC6
    Administrador -- UC7
    Administrador -- UC8
    Administrador -- UC2 ' El admin también inicia sesión

    ' Relaciones entre Casos de Uso
    UC3 ..> UC2 : <<include>>
    UC4 ..> UC2 : <<include>>
    UC2 <.. UC5 : <<extend>>

    UC6 ..> UC2 : <<include>>
    UC7 ..> UC2 : <<include>>
    UC8 ..> UC2 : <<include>>

```

#### Descripción de Relaciones

*   **Comunicación:** Las líneas continuas entre un actor y un caso de uso indican que el actor participa en ese caso de uso (ej. `Educador` -> `Registrarse en el Sistema`).
*   **Inclusión (`<<include>>`):** La línea punteada con la flecha y la etiqueta `<<include>>` indica que un caso de uso depende de otro. Por ejemplo, para `Gestionar Perfil Profesional` es obligatorio `Iniciar Sesión` primero.
*   **Extensión (`<<extend>>`):** La línea punteada con la etiqueta `<<extend>>` indica una funcionalidad opcional que puede surgir desde un caso de uso base. Por ejemplo, durante el `Iniciar Sesión`, un usuario podría necesitar `Recuperar Contraseña`.

---

#### Escenarios para el Caso de Uso Clave: "Recibir Recomendaciones"

A continuación, se describen tres escenarios para el caso de uso más importante del sistema.

**Caso de Uso Clave:** Recibir Recomendaciones
**Actor Principal:** Educador
**Objetivo:** Obtener una lista de cursos y formaciones personalizadas basadas en el perfil profesional del educador.

---

**Escenario 1: Flujo Básico (Camino Feliz)**

*   **Nombre:** Obtención exitosa de recomendaciones con perfil completo.
*   **Precondiciones:**
    1.  El Educador ha iniciado sesión en el sistema.
    2.  El Educador ha completado todos los campos requeridos de su perfil profesional.
*   **Secuencia de Acciones:**
    1.  El Educador hace clic en la opción "Ver mis Recomendaciones" en el menú de navegación.
    2.  El sistema recupera los datos del perfil del Educador desde la base de datos.
    3.  El sistema procesa estos datos y los envía al motor de clustering (modelo de Machine Learning).
    4.  El motor de clustering asigna al educador a un grupo (clúster) específico junto a otros perfiles similares.
    5.  El sistema consulta qué rutas de formación o cursos están asociados a ese clúster.
    6.  El sistema presenta al Educador una página con la lista de cursos recomendados, ordenados por relevancia.
*   **Postcondición:** El Educador visualiza su lista de recomendaciones personalizadas.

---

**Escenario 2: Flujo Alternativo**

*   **Nombre:** Intento de obtener recomendaciones con un perfil incompleto.
*   **Precondiciones:**
    1.  El Educador ha iniciado sesión en el sistema.
    2.  El Educador **no** ha completado campos esenciales de su perfil (ej. áreas de interés, años de experiencia).
*   **Secuencia de Acciones:**
    1.  El Educador hace clic en la opción "Ver mis Recomendaciones".
    2.  El sistema intenta validar el perfil del Educador antes de llamar al motor de recomendación.
    3.  El sistema detecta que el perfil está incompleto.
    4.  El sistema **no** ejecuta el proceso de recomendación.
    5.  El sistema redirige al Educador a la página de "Gestionar Perfil Profesional".
    6.  El sistema muestra un mensaje informativo en la parte superior de la página, como: "Para poder generar tus recomendaciones, por favor completa los campos marcados en tu perfil".
*   **Postcondición:** El Educador se encuentra en la página de edición de su perfil para poder completarlo.

---

**Escenario 3: Flujo de Excepción**

*   **Nombre:** Falla del servicio de recomendación.
*   **Precondiciones:**
    1.  El Educador ha iniciado sesión y tiene un perfil completo.
*   **Secuencia de Acciones:**
    1.  El Educador hace clic en la opción "Ver mis Recomendaciones".
    2.  El sistema intenta procesar la solicitud.
    3.  Se produce un error inesperado en el servidor (ej. el modelo de Machine Learning no se carga correctamente, hay un problema de conexión con la base de datos).
    4.  El sistema captura la excepción internamente para evitar que la aplicación se bloquee.
    5.  El sistema registra los detalles del error en el archivo de logs (`logs/app.log`) para que el Administrador pueda investigarlo.
    6.  El sistema muestra al Educador una página de error amigable con un mensaje como: "Lo sentimos, ha ocurrido un problema al generar tus recomendaciones. Por favor, inténtalo de nuevo más tarde."
*   **Postcondición:** El Educador es informado del problema de forma controlada y el error queda registrado para su posterior análisis.

### 4.2. Diagrama de Clases

Este diagrama representa la estructura estática del sistema "EduRecom", mostrando las clases principales, sus atributos, métodos y las relaciones que existen entre ellas.

#### Diagrama de Clases (Mermaid)

```mermaid
classDiagram
    direction LR

    class User {
        -id: int
        -email: str
        -username: str
        -password_hash: str
        -is_admin: bool
        +set_password(password: str): void
        +check_password(password: str): bool
        +get_id(): int
    }

    class Profile {
        -id: int
        -full_name: str
        -years_experience: int
        -educational_level: str
        -interests: list
        +update_details(data: dict): void
        +get_profile_vector(): list
    }

    class Cluster {
        -id: int
        -name: str
        -description: str
        +get_courses(): list~Course~
    }

    class Course {
        -id: int
        -name: str
        -description: str
        -url: str
        -provider: str
        +get_details(): dict
    }

    class RecommendationEngine {
        +assign_cluster(profile: Profile): Cluster
        +get_recommendations(cluster: Cluster): list~Course~
    }

    %% --- Relaciones ---

    ' Composición: Un User tiene un Profile, y el Profile no existe sin el User.
    User "1" *-- "1" Profile : has

    ' Asociación: Un User es asignado a un Cluster.
    User "1" -- "0..1" Cluster : is assigned to

    ' Asociación: Un Cluster tiene muchas recomendaciones de Cursos.
    Cluster "1" -- "*" Course : recommends

    ' Dependencia: El motor de recomendaciones USA perfiles, clusters y cursos para funcionar.
    RecommendationEngine ..> Profile : uses
    RecommendationEngine ..> Cluster : uses
    RecommendationEngine ..> Course : uses

```

---

#### Descripción de Clases, Atributos y Operaciones

*   **Visibilidad:** `+` (Público), `-` (Privado).

1.  **User:** Representa a una persona registrada en el sistema, que puede ser un educador o un administrador.
    *   **Atributos:** `id`, `email`, `username` para la identificación y `password_hash` para la seguridad. El booleano `is_admin` distingue su rol.
    *   **Operaciones:** Métodos para gestionar la contraseña de forma segura (`set_password`, `check_password`).

2.  **Profile:** Contiene la información profesional y académica del educador, que es la base para las recomendaciones.
    *   **Atributos:** Datos como `full_name`, `years_experience`, `educational_level` e `interests`.
    *   **Operaciones:** `update_details` para modificar el perfil y `get_profile_vector` para convertir los datos del perfil en un formato numérico que el modelo de Machine Learning pueda procesar.

3.  **Course (Curso/Formación):** Representa una oferta académica que puede ser recomendada.
    *   **Atributos:** `id`, `name`, `description`, `url` para acceder al curso y `provider` (proveedor).
    *   **Operaciones:** `get_details` para obtener la información completa de un curso.

4.  **Cluster:** Representa un grupo de perfiles de usuario con características similares, según el algoritmo de Machine Learning.
    *   **Atributos:** `id`, `name` y `description` para identificar al grupo.
    *   **Operaciones:** `get_courses` para obtener la lista de cursos recomendados para ese grupo específico.

5.  **RecommendationEngine:** Es una clase de tipo "servicio" o "controlador" que orquesta la lógica de negocio principal. No representa una entidad de negocio, sino una funcionalidad.
    *   **Operaciones:** `assign_cluster` toma un perfil y determina a qué clúster pertenece. `get_recommendations` devuelve la lista de cursos para un clúster dado.

#### Descripción de Relaciones y Multiplicidad

*   **Composición (User `1`--`1` Profile):**
    *   **Descripción:** Un `User` tiene exactamente un `Profile`, y un `Profile` pertenece a un solo `User`. Es una relación fuerte de "parte-de": el `Profile` no puede existir si el `User` es eliminado.
    *   **Multiplicidad:** `1` a `1`.

*   **Asociación (User `1`--`0..1` Cluster):**
    *   **Descripción:** Un `User` puede ser asignado a un `Cluster`. Es una relación semántica donde un usuario "pertenece a" un grupo.
    *   **Multiplicidad:** `1` a `0..1` (cero o uno), lo que indica que un usuario podría no tener un clúster asignado todavía (por ejemplo, si es nuevo o su perfil está incompleto).

*   **Asociación (Cluster `1`--`*` Course):**
    *   **Descripción:** Un `Cluster` está asociado con múltiples `Course`s. Esta relación define qué cursos son apropiados para cada grupo de usuarios.
    *   **Multiplicidad:** `1` a `*` (muchos), lo que significa que un clúster puede tener varias recomendaciones de cursos.

*   **Dependencia (RecommendationEngine ...> Profile, Cluster, Course):**
    *   **Descripción:** La clase `RecommendationEngine` depende de las clases `Profile`, `Cluster` y `Course` para realizar sus operaciones. No las contiene ni las almacena permanentemente, sino que las utiliza como parámetros o resultados en sus métodos.

### 4.3. Diagrama Entidad-Relación (E-R)

Este diagrama modela la estructura lógica de la base de datos que daría soporte al sistema. Representa las tablas principales, sus columnas y cómo se conectan entre sí.

**Nota sobre la Notación:** El siguiente diagrama utiliza la notación de "Pata de Cuervo" (Crow's Foot), que es una forma estándar y moderna de representar diagramas E-R, comúnmente usada en herramientas de modelado. Los conceptos son equivalentes a la notación clásica:
*   **Entidades:** Son los recuadros con el nombre de la tabla.
*   **Atributos:** Son las filas dentro de cada recuadro. La **Clave Primaria (PK)** está marcada. Las **Claves Foráneas (FK)** también se indican.
*   **Relaciones y Cardinalidad:** Se representan mediante las líneas que conectan las entidades, y los símbolos en sus extremos definen la cardinalidad.

#### Diagrama E-R (Mermaid)

```mermaid
erDiagram
    USER {
        int user_id PK
        string username
        string email
        string password_hash
        bool is_admin
    }

    PROFILE {
        int profile_id PK
        string full_name
        int years_experience
        string educational_level
        int user_id FK
    }

    CLUSTER {
        int cluster_id PK
        string name
        string description
    }

    COURSE {
        int course_id PK
        string name
        string description
        string url
    }

    CLUSTER_COURSE_ASSOCIATION {
        int cluster_id FK
        int course_id FK
    }

    %% --- Relaciones ---

    ' Relación 1:1 entre USER y PROFILE
    USER ||--|| PROFILE : "has"

    ' Relación 1:N entre CLUSTER y USER
    ' Un usuario puede pertenecer a 0 o 1 clúster. Un clúster puede tener 0 o muchos usuarios.
    USER |o--o{ CLUSTER : "is_assigned_to"

    ' Relación N:M entre CLUSTER y COURSE, resuelta con la tabla de asociación
    CLUSTER }|--|{ CLUSTER_COURSE_ASSOCIATION : "recommends"
    COURSE }|--|{ CLUSTER_COURSE_ASSOCIATION : "is_recommended_in"

```

---

#### Descripción de Entidades y Atributos

1.  **USER (Usuario)**
    *   **Descripción:** Almacena la información de inicio de sesión y credenciales de cada persona registrada en el sistema.
    *   **Atributos:**
        *   `user_id` (PK): Identificador numérico único para cada usuario.
        *   `username`, `email`, `password_hash`: Datos para la autenticación.
        *   `is_admin`: Campo booleano para diferenciar roles.

2.  **PROFILE (Perfil)**
    *   **Descripción:** Guarda los datos profesionales y académicos del educador, que son la entrada para el sistema de recomendación.
    *   **Atributos:**
        *   `profile_id` (PK): Identificador único para cada perfil.
        *   `full_name`, `years_experience`, `educational_level`: Ejemplos de atributos del perfil.
        *   `user_id` (FK): Clave foránea que lo vincula a la tabla `USER`.

3.  **CLUSTER (Clúster/Grupo)**
    *   **Descripción:** Representa los grupos de perfiles similares identificados por el algoritmo de Machine Learning.
    *   **Atributos:**
        *   `cluster_id` (PK): Identificador único para cada clúster.
        *   `name`, `description`: Para dar un nombre y contexto a cada grupo (ej. "Docentes de media con interés en TIC").

4.  **COURSE (Curso)**
    *   **Descripción:** Almacena la información de toda la oferta de cursos, formaciones y especializaciones disponibles para ser recomendadas.
    *   **Atributos:**
        *   `course_id` (PK): Identificador único para cada curso.
        *   `name`, `description`, `url`: Información detallada del curso.

#### Descripción de Relaciones y Cardinalidad

*   **USER `has` PROFILE (Relación 1 a 1)**
    *   **Descripción:** Cada `USER` tiene exactamente un `PROFILE` y cada `PROFILE` pertenece a un único `USER`. Es una relación obligatoria y única en ambos sentidos.
    *   **Cardinalidad:** `||--||` (Uno y solo uno).

*   **USER `is_assigned_to` CLUSTER (Relación 1 a N)**
    *   **Descripción:** Un `CLUSTER` puede agrupar a muchos usuarios, pero un `USER` pertenece a un solo `CLUSTER`.
    *   **Cardinalidad:** El símbolo `|o--o{` indica que un `CLUSTER` puede tener cero o muchos (`o{`) `USER`s, y un `USER` puede pertenecer a cero o un (`|o`) `CLUSTER`. Esto permite que un usuario recién registrado aún no tenga un clúster asignado.

*   **CLUSTER `recommends` COURSE (Relación N a M)**
    *   **Descripción:** Esta es una relación de **varios a varios**: un `CLUSTER` puede recomendar muchos `COURSE`s, y un mismo `COURSE` puede ser recomendado para varios `CLUSTER`s.
    *   **Implementación:** Para implementar esta relación en una base de datos relacional, se crea una **tabla intermedia** llamada `CLUSTER_COURSE_ASSOCIATION`. Esta tabla contiene dos claves foráneas: `cluster_id` y `course_id`. Cada fila en esta tabla crea una asociación única entre un clúster y un curso.

## 5. Modelo de Datos de la Base de Datos

### 5.1. Base de Datos Normalizada (1FN, 2FN, 3FN)

El siguiente diseño de base de datos ha sido estructurado aplicando las reglas de normalización para reducir la redundancia, evitar anomalías de datos (inserción, actualización y borrado) y garantizar la integridad de la información.

#### Esquema de la Base de Datos Propuesto

**Tabla: `USERS`**
| Columna | Tipo de Dato | Restricciones |
| :--- | :--- | :--- |
| user_id | INTEGER | PK (Primary Key) |
| username | VARCHAR(80) | UNIQUE, NOT NULL |
| email | VARCHAR(120) | UNIQUE, NOT NULL |
| password_hash | VARCHAR(256) | NOT NULL |
| is_admin | BOOLEAN | NOT NULL, DEFAULT FALSE |

**Tabla: `PROFILES`**
| Columna | Tipo de Dato | Restricciones |
| :--- | :--- | :--- |
| profile_id | INTEGER | PK |
| user_id | INTEGER | FK (USERS.user_id) |
| full_name | VARCHAR(120) | |
| years_experience | INTEGER | |
| educational_level | VARCHAR(100) | |
| cluster_id | INTEGER | FK (CLUSTERS.cluster_id), NULLABLE |

**Tabla: `CLUSTERS`**
| Columna | Tipo de Dato | Restricciones |
| :--- | :--- | :--- |
| cluster_id | INTEGER | PK |
| name | VARCHAR(100) | NOT NULL |
| description | TEXT | |

**Tabla: `COURSES`**
| Columna | Tipo de Dato | Restricciones |
| :--- | :--- | :--- |
| course_id | INTEGER | PK |
| name | VARCHAR(200) | NOT NULL |
| description | TEXT | |
| url | VARCHAR(255) | |

**Tabla: `CLUSTER_COURSE_MAP` (Tabla de Asociación)**
| Columna | Tipo de Dato | Restricciones |
| :--- | :--- | :--- |
| cluster_id | INTEGER | PK, FK (CLUSTERS.cluster_id) |
| course_id | INTEGER | PK, FK (COURSES.course_id) |

---
#### Análisis de Formas Normales

**Primera Forma Normal (1FN): Atomicidad de los Atributos**

*   **Regla:** Cada celda de una tabla debe contener un único valor (atómico), y no puede haber grupos de repetición.
*   **Demostración:**
    *   En todas las tablas presentadas (`USERS`, `PROFILES`, `CLUSTERS`, `COURSES`), cada columna está diseñada para almacenar un solo dato: un número, una cadena de texto, un booleano.
    *   Un ejemplo clave de esta decisión es cómo se manejarían los "intereses" de un perfil. En lugar de almacenar una lista como `"TIC, Liderazgo, Inclusión"` en una sola celda de la tabla `PROFILES` (lo cual violaría la 1FN), el diseño correcto (no mostrado arriba por simplicidad, pero implícito en la metodología) sería crear tablas adicionales: `INTERESTS(interest_id, name)` y `PROFILE_INTERESTS_MAP(profile_id, interest_id)`.
    *   **Conclusión:** El esquema cumple con la 1FN.

**Segunda Forma Normal (2FN): Eliminación de Dependencias Parciales**

*   **Regla:** La tabla debe estar en 1FN y todos los atributos que no forman parte de la clave primaria deben depender funcionalmente de la **totalidad** de la clave primaria.
*   **Demostración:**
    *   Las tablas `USERS`, `PROFILES`, `CLUSTERS` y `COURSES` tienen una clave primaria de una sola columna (`user_id`, `profile_id`, etc.). Por definición, no pueden existir dependencias parciales en ellas, por lo que cumplen automáticamente con la 2FN.
    *   La única tabla con una clave primaria compuesta es `CLUSTER_COURSE_MAP`. Su clave primaria es `(cluster_id, course_id)`. Esta tabla no tiene ningún otro atributo, por lo que no hay atributos no clave que puedan depender parcialmente de la clave.
    *   **Conclusión:** El esquema cumple con la 2FN.

**Tercera Forma Normal (3FN): Eliminación de Dependencias Transitivas**

*   **Regla:** La tabla debe estar en 2FN y no deben existir dependencias transitivas, es decir, un atributo no clave no puede depender de otro atributo no clave.
*   **Demostración:**
    *   Analicemos la tabla `PROFILES`. Los atributos `full_name`, `years_experience` y `educational_level` dependen directamente de `profile_id`, no entre sí. El `cluster_id` también depende directamente del perfil al que se le asigna. No hay dependencias transitivas.
    *   Consideremos un caso hipotético: si en la tabla `COURSES` tuviéramos los campos `provider_name` y `provider_address`. En este caso, `provider_address` dependería de `provider_name` (que no es clave), y `provider_name` dependería de `course_id` (la clave). Esto sería una **dependencia transitiva** (`course_id` → `provider_name` → `provider_address`).
    *   El diseño actual evita esto. Si se necesitara más información del proveedor, se crearía una tabla `PROVIDERS(provider_id, name, address)` y en la tabla `COURSES` solo se almacenaría un `provider_id` (FK).
    *   **Conclusión:** El esquema actual no presenta dependencias transitivas y cumple con la 3FN.

---
#### Dependencias Funcionales y Mitigación de Redundancia

*   **Dependencias Funcionales:** Son la base de la normalización. Una dependencia funcional `X → Y` significa que el valor de X determina un único valor de Y.
    *   **Determinantes:** Son los atributos del lado izquierdo (X). En nuestro modelo, las claves primarias son los determinantes principales.
    *   **Ejemplos en el modelo:**
        *   En `USERS`: `{user_id} → {username, email, password_hash, is_admin}`.
        *   En `PROFILES`: `{profile_id} → {user_id, full_name, years_experience, ...}`.
        *   En `CLUSTER_COURSE_MAP`: `{cluster_id, course_id} → {}` (no hay más atributos que determinar).

*   **Dependencias Transitivas:** Como se explicó en la 3FN, una dependencia transitiva `A → B → C` (donde A es la clave primaria) se resuelve creando una nueva tabla para la relación `B → C`, donde B se convierte en la clave primaria. Nuestro diseño ya está estructurado para prevenir esto.

*   **Mitigación de la Redundancia de Datos:**
    *   La normalización reduce la redundancia al asegurar que cada pieza de información se almacene una sola vez.
    *   **Ejemplo 1:** El nombre de un `COURSE` se almacena una única vez en la tabla `COURSES`. Si 1000 usuarios reciben la misma recomendación, no se repite el nombre del curso 1000 veces. En su lugar, se crea una relación a través de sus respectivos clústeres en la tabla `CLUSTER_COURSE_MAP`, usando únicamente los `id` numéricos, que son mucho más eficientes.
    *   **Ejemplo 2:** Los datos de un `USER` (email, pass) están en una tabla y los de su `PROFILE` (experiencia, etc.) en otra. Esto permite que la lógica de autenticación trabaje solo con la tabla `USERS`, que es más pequeña y rápida, sin necesidad de cargar toda la información del perfil.
    *   Este enfoque no solo ahorra espacio, sino que previene **anomalías de actualización**. Si el nombre de un curso cambia, solo se debe modificar en un único registro en la tabla `COURSES`, y el cambio se reflejará automáticamente para todos los usuarios a quienes se les recomienda.

### 5.2. Diccionario de Datos

El Diccionario de Datos para "EduRecom" es un repositorio centralizado de metadatos que define y describe todos los elementos de datos utilizados en el sistema. Sirve como una guía esencial para desarrolladores, administradores de bases de datos y analistas.

#### 1. Flujos de Datos

Describen el movimiento de la información entre los procesos, los usuarios y los almacenes de datos.

*   **Flujo de Entrada: `Registro_de_Usuario`**
    *   **Descripción:** Información proporcionada por un nuevo educador a través del formulario de registro.
    *   **Fuente:** Actor `Educador`.
    *   **Destino:** Proceso "Crear Cuenta".

*   **Flujo de Entrada: `Datos_de_Perfil`**
    *   **Descripción:** Información profesional y académica que el educador proporciona para completar su perfil.
    *   **Fuente:** Actor `Educador`.
    *   **Destino:** Proceso "Actualizar Perfil".

*   **Flujo Intermedio: `Vector_de_Perfil`**
    *   **Descripción:** Representación numérica de los `Datos_de_Perfil` para ser procesada por el modelo de Machine Learning.
    *   **Fuente:** Proceso "Generar Recomendación".
    *   **Destino:** Proceso "Asignar Clúster".

*   **Flujo de Salida: `Lista_de_Recomendaciones`**
    *   **Descripción:** Conjunto de cursos y formaciones personalizadas que se muestran al usuario.
    *   **Fuente:** Proceso "Generar Recomendación".
    *   **Destino:** Actor `Educador`.

*   **Flujo de Almacenamiento: `Nuevo_Usuario`**
    *   **Descripción:** Datos de un usuario recién registrado que se persisten en la base de datos.
    *   **Fuente:** Proceso "Crear Cuenta".
    *   **Destino:** Almacén de datos `USERS`.

#### 2. Estructuras de Datos (Notación Algebraica)

Definen la composición de los flujos de datos.
*   `=` se lee como "está compuesto por".
*   `+` indica la concatenación de elementos.
*   `{}` indica la repetición de un elemento o estructura (una lista).

```
Registro_de_Usuario       = Nombre_de_Usuario + Email + Contraseña
Datos_de_Perfil           = Nombre_Completo + Años_de_Experiencia + Nivel_Educacional
Lista_de_Recomendaciones  = {Recomendacion}
Recomendacion             = Nombre_Curso + Descripcion_Curso + URL_Curso
Nuevo_Usuario             = ID_Usuario + Nombre_de_Usuario + Email + Hash_Contraseña + Es_Admin
```

#### 3. Elementos de Datos

Esta es la definición detallada de cada campo en la base de datos.

| Elemento (Campo) | Tipo de Dato | Longitud | Descripción | Clave (PK/FK) | Tabla |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **user_id** | INTEGER | N/A | Identificador único y secuencial para cada usuario. | **PK** | USERS |
| username | VARCHAR | 80 | Nombre de usuario único para el inicio de sesión. | | USERS |
| email | VARCHAR | 120 | Correo electrónico único del usuario. | | USERS |
| password_hash | VARCHAR | 256 | Hash de la contraseña del usuario para almacenamiento seguro. | | USERS |
| is_admin | BOOLEAN | N/A | Indica si el usuario tiene privilegios de administrador. | | USERS |
| **profile_id** | INTEGER | N/A | Identificador único para el perfil de un usuario. | **PK** | PROFILES |
| user_id | INTEGER | N/A | Clave foránea que vincula el perfil con el usuario. | **FK** (USERS.user_id) | PROFILES |
| full_name | VARCHAR | 120 | Nombre completo del educador. | | PROFILES |
| years_experience | INTEGER | N/A | Años de experiencia profesional del educador. | | PROFILES |
| educational_level | VARCHAR | 100 | Último nivel educativo alcanzado por el educador. | | PROFILES |
| cluster_id | INTEGER | N/A | Clave foránea que indica el clúster asignado al perfil. | **FK** (CLUSTERS.cluster_id) | PROFILES |
| **cluster_id** | INTEGER | N/A | Identificador único para cada clúster o grupo. | **PK** | CLUSTERS |
| name | VARCHAR | 100 | Nombre descriptivo del clúster (ej. "Expertos en TIC"). | | CLUSTERS |
| description | TEXT | N/A | Explicación detallada de las características del clúster. | | CLUSTERS |
| **course_id** | INTEGER | N/A | Identificador único para cada curso o formación. | **PK** | COURSES |
| name | VARCHAR | 200 | Nombre oficial del curso. | | COURSES |
| description | TEXT | N/A | Descripción detallada del contenido y objetivos del curso. | | COURSES |
| url | VARCHAR | 255 | Enlace web para acceder a la información del curso. | | COURSES |
| cluster_id | INTEGER | N/A | Clave foránea que vincula la recomendación al clúster. | **PK, FK** (CLUSTERS.cluster_id) | CLUSTER_COURSE_MAP |
| course_id | INTEGER | N/A | Clave foránea que vincula la recomendación al curso. | **PK, FK** (COURSES.course_id) | CLUSTER_COURSE_MAP |

#### 4. Almacenes de Datos

Descripción del propósito de cada tabla en la base de datos.

*   **`USERS`:** Almacena las credenciales y datos de acceso de todos los usuarios que pueden interactuar con el sistema. Es fundamental para la autenticación y la gestión de roles.
*   **`PROFILES`:** Contiene la información profesional detallada de los educadores. Estos datos son la entrada principal para el motor de recomendaciones.
*   **`CLUSTERS`:** Guarda la definición de los grupos de perfiles similares que genera el modelo de Machine Learning. Actúa como un puente entre los perfiles y los cursos recomendados.
*   **`COURSES`:** Funciona como el catálogo central de todas las ofertas de formación que el sistema puede recomendar.
*   **`CLUSTER_COURSE_MAP`:** Es una tabla de enlace que implementa la relación "varios a varios" entre los clústeres y los cursos, definiendo qué cursos son apropiados para cada grupo de usuarios.

#### 5. Ventajas del Diccionario de Datos

La creación y mantenimiento de este diccionario de datos aporta beneficios significativos al proyecto:

1.  **Comprensión Unificada:** Proporciona una fuente única y fiable de verdad para todos los stakeholders (desarrolladores, analistas, administradores), asegurando que todos tengan el mismo entendimiento sobre los datos.
2.  **Consistencia en el Desarrollo:** Garantiza que se utilicen los mismos nombres de campo, tipos de datos y longitudes en todo el sistema, desde la base de datos hasta la interfaz de usuario, reduciendo errores de integración.
3.  **Facilita el Análisis de Impacto:** Si se necesita cambiar un elemento de dato (ej. extender la longitud de un campo), el diccionario permite identificar rápidamente todas las partes del sistema que se verán afectadas.
4.  **Documentación Esencial:** Sirve como una pieza clave de la documentación técnica, crucial para el mantenimiento a largo plazo y la incorporación de nuevos miembros al equipo.
5.  **Acelera el Desarrollo:** Actúa como un plano para los desarrolladores, permitiéndoles escribir código que interactúa con la base de datos de manera más rápida y con menos errores.

### 5.3. Modelo Relacional

El modelo relacional es la implementación física del diseño lógico de la base de datos. A continuación, se presentan los comandos SQL (en un dialecto estándar, similar a PostgreSQL) para crear y manipular las tablas del sistema "EduRecom".

#### 1. Definición de Datos (DDL - Data Definition Language)

Estos comandos `CREATE TABLE` definen la estructura de cada tabla, sus columnas, tipos de datos y las restricciones que garantizan la integridad referencial (claves primarias y foráneas).

```sql
-- Tabla para almacenar los usuarios del sistema
CREATE TABLE USERS (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabla para almacenar los clústeres o grupos de perfiles
CREATE TABLE CLUSTERS (
    cluster_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Tabla para los perfiles profesionales de los usuarios
CREATE TABLE PROFILES (
    profile_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,
    full_name VARCHAR(120),
    years_experience INTEGER,
    educational_level VARCHAR(100),
    cluster_id INTEGER,

    CONSTRAINT fk_user
        FOREIGN KEY(user_id) 
        REFERENCES USERS(user_id)
        ON DELETE CASCADE, -- Si se borra un usuario, se borra su perfil

    CONSTRAINT fk_cluster
        FOREIGN KEY(cluster_id)
        REFERENCES CLUSTERS(cluster_id)
        ON DELETE SET NULL -- Si se borra un clúster, el perfil queda sin asignar
);

-- Tabla para el catálogo de cursos
CREATE TABLE COURSES (
    course_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    url VARCHAR(255)
);

-- Tabla de asociación para la relación N:M entre Clústeres y Cursos
CREATE TABLE CLUSTER_COURSE_MAP (
    cluster_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,

    PRIMARY KEY (cluster_id, course_id), -- Clave primaria compuesta

    CONSTRAINT fk_cluster_map
        FOREIGN KEY(cluster_id)
        REFERENCES CLUSTERS(cluster_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_course_map
        FOREIGN KEY(course_id)
        REFERENCES COURSES(course_id)
        ON DELETE CASCADE
);
```

---
#### 2. Manipulación de Datos (DML - Data Manipulation Language)

Estos comandos se utilizan para interactuar con los datos almacenados en las tablas.

*   **`INSERT` (Insertar datos)**
    ```sql
    -- Insertar un nuevo usuario educador
    INSERT INTO USERS (username, email, password_hash) 
    VALUES ('j.perez', 'juan.perez@email.com', 'hash_muy_seguro_de_su_password');

    -- Insertar un nuevo curso
    INSERT INTO COURSES (name, description, url) 
    VALUES ('Introducción a la Gamificación en el Aula', 'Curso para aprender a aplicar técnicas de juego en entornos educativos.', 'http://example.com/gamificacion');
    ```

*   **`SELECT` (Consultar datos)**
    ```sql
    -- Seleccionar todos los usuarios administradores
    SELECT user_id, username, email FROM USERS WHERE is_admin = TRUE;

    -- Seleccionar el perfil de un usuario específico usando un JOIN
    SELECT u.username, p.full_name, p.years_experience
    FROM USERS u
    JOIN PROFILES p ON u.user_id = p.user_id
    WHERE u.username = 'j.perez';
    ```

*   **`UPDATE` (Actualizar datos)**
    ```sql
    -- Asignar un clúster a un perfil de usuario
    UPDATE PROFILES
    SET cluster_id = 2
    WHERE user_id = (SELECT user_id FROM USERS WHERE email = 'juan.perez@email.com');
    ```

*   **`DELETE` (Eliminar datos)**
    ```sql
    -- Eliminar un curso del catálogo
    DELETE FROM COURSES WHERE course_id = 10; 
    -- Nota: Gracias a "ON DELETE CASCADE", todas las entradas en CLUSTER_COURSE_MAP que referencian este curso también se eliminarán.
    ```

---
#### 3. Consultas de Agrupamiento y Ordenamiento

Ejemplos de cómo analizar los datos utilizando funciones de agregación.

*   **`COUNT` y `GROUP BY`**
    ```sql
    -- Contar cuántos usuarios hay en cada clúster
    SELECT c.name, COUNT(p.profile_id) AS numero_de_usuarios
    FROM CLUSTERS c
    LEFT JOIN PROFILES p ON c.cluster_id = p.cluster_id
    GROUP BY c.name
    ORDER BY numero_de_usuarios DESC;
    ```

*   **`AVG`, `MAX`, `MIN`**
    ```sql
    -- Calcular el promedio, máximo y mínimo de años de experiencia de los educadores registrados
    SELECT 
        AVG(years_experience) AS promedio_experiencia,
        MAX(years_experience) AS maxima_experiencia,
        MIN(years_experience) AS minima_experiencia
    FROM PROFILES;
    ```

*   **`DISTINCT`**
    ```sql
    -- Contar cuántos cursos únicos han sido recomendados (están en el mapa)
    SELECT COUNT(DISTINCT course_id) AS cursos_recomendados FROM CLUSTER_COURSE_MAP;
    ```

*   **`ORDER BY`**
    ```sql
    -- Listar los 10 usuarios más recientes del sistema
    SELECT username, created_at
    FROM USERS
    ORDER BY created_at DESC
    LIMIT 10;
    ```
